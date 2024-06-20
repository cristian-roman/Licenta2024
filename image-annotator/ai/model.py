import torch
import torch.nn as nn

from ai.graph_net import GraphNet


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.encoder_1 = nn.ModuleList([self.get_encode_block(1, 4, 8) for _ in range(5)])
        self.encoder_2 = nn.ModuleList([self.get_encode_block(8, 32, 64) for _ in range(3)])
        self.encoder_3 = nn.ModuleList([self.get_encode_block(64, 256, 512) for _ in range(1)])

        self.encoder_4 = nn.Sequential(
            nn.Conv2d(512, 1024, 3),
            nn.MaxPool2d(2)
        )

        self.linear = nn.Sequential(
            nn.Linear(17 * 17, 17 * 17),
            nn.LeakyReLU()
        )

        self.graph_net = nn.Sequential(
            GraphNet(17, 1024, 1024),
            nn.LeakyReLU()
        )

        self.bias = nn.Linear(17 * 17, 1)

        self.decode_from_4_to_3 = nn.Sequential(
            nn.ConvTranspose2d(1024, 512, 2, stride=2),
            nn.ConvTranspose2d(512, 512, 3),
            nn.LeakyReLU(0.2)
        )

        self.decode_from_3_to_2 = nn.Sequential(
            nn.ConvTranspose2d(512, 256, 2, stride=2),
            nn.ConvTranspose2d(256, 128, 3),
            nn.ConvTranspose2d(128, 64, 3),
            nn.ConvTranspose2d(64, 64, 2),
            nn.ReLU()
        )

        self.decode_from_2_to_1 = nn.Sequential(
            nn.ConvTranspose2d(64, 32, 2, stride=2),
            nn.ConvTranspose2d(32, 16, 3),
            nn.ConvTranspose2d(16, 8, 3),
        )

        self.decode_from_1_to_0 = nn.Sequential(
            nn.ConvTranspose2d(8, 4, 2, stride=2),
            nn.ConvTranspose2d(4, 2, 3),
            nn.ConvTranspose2d(2, 1, 3),
        )

    @staticmethod
    def get_encode_block(start, second, third):
        return nn.Sequential(
            nn.Conv2d(start, second, 3),
            nn.Conv2d(second, third, 3),
            nn.MaxPool2d(2)
        )

    def forward(self, x):
        enc_1_output = self.encoder_1[0](x)
        for i in range(1, len(self.encoder_1)):
            enc_1_output += self.encoder_1[i](x)

        enc_2_output = self.encoder_2[0](enc_1_output)
        for i in range(1, len(self.encoder_2)):
            enc_2_output += self.encoder_2[i](enc_1_output)

        enc_3_output = self.encoder_3[0](enc_2_output)
        for i in range(1, len(self.encoder_3)):
            enc_3_output += self.encoder_3[i](enc_2_output)

        enc_4_output = self.encoder_4(enc_3_output)

        linear_output = self.__pass_through_linear(enc_4_output, self.linear)
        graph_net_output = self.graph_net(enc_4_output) * 0.0001
        bias = self.__get_bias(enc_4_output)

        summed = linear_output + graph_net_output

        enc_end = summed

        dec_from_4_to_3 = self.decode_from_4_to_3(enc_end)

        summed = dec_from_4_to_3 + enc_3_output

        dec_from_3_to_2 = self.decode_from_3_to_2(summed)

        summed = dec_from_3_to_2 + enc_2_output

        dec_from_2_to_1 = self.decode_from_2_to_1(summed)

        summed = dec_from_2_to_1 + enc_1_output

        dec_from_1_to_0 = self.decode_from_1_to_0(summed)

        return dec_from_1_to_0.squeeze() * bias

    @staticmethod
    def __pass_through_linear(x, linear):
        ans = torch.zeros_like(x)
        for i in range(x.size(0)):
            ans[i] = linear(x[i].flatten()).reshape(17, 17)

        return ans

    def __get_bias(self, x):
        ans = 0
        for i in range(x.size(0)):
            ans += self.bias(x[i].flatten())

        return ans / x.size(0)
