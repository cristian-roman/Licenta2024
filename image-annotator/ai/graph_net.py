import torch
from torch_geometric.nn import GCNConv
from utils.injector import Injector


class GraphNet(torch.nn.Module):

    @staticmethod
    def __connect_index_to_sized_square(i, j, size, square_size, edges):
        square_size = min(square_size, size)
        current_index = i * size + j
        i_start = max(i - square_size // 2, 0)
        i_end = min(i + square_size // 2, size - 1)
        j_start = max(j - square_size // 2, 0)
        j_end = min(j + square_size // 2, size - 1)

        for i in range(i_start, i_end + 1):
            for j in range(j_start, j_end + 1):
                pair_index = (current_index, i * size + j)
                if pair_index not in edges:
                    edges.add(pair_index)

    @staticmethod
    def __create_grid_edges(size):
        mid_index = size // 2
        edges = set()
        for i in range(size):
            for j in range(size):
                index = i * size + j
                if i > 0:  # Connect to the node above
                    edges.add((index, index - size))
                if i < size - 1:  # Connect to the node below
                    edges.add((index, index + size))
                if j > 0:  # Connect to the node on the left
                    edges.add((index, index - 1))
                if j < size - 1:  # Connect to the node on the right
                    edges.add((index, index + 1))

                if i > 0:
                    if j > 0:
                        edges.add((index, index - size - 1))
                    if j < size - 1:
                        edges.add((index, index - size + 1))

                if i < size - 1:
                    if j > 0:
                        edges.add((index, index + size - 1))
                    if j < size - 1:
                        edges.add((index, index + size + 1))

                max_kernel = 8
                min_kernel = 3
                if min_kernel <= abs(i - mid_index) <= max_kernel and min_kernel <= abs(j - mid_index) <= max_kernel:
                    square_size = max_kernel - abs(i - mid_index) + max_kernel - abs(j - mid_index)
                    GraphNet.__connect_index_to_sized_square(i, j, size, square_size, edges)

        edges = list(edges)
        return edges

    def __init__(self, size, in_channels, out_channels):
        super(GraphNet, self).__init__()
        self.size = size
        self.in_channels = in_channels
        self.out_channels = out_channels
        if Injector.get_instance(f"{in_channels}_{out_channels}") is None:
            Injector.register_instance(f"{in_channels}_{out_channels}", self.__create_grid_edges(size))
        edges = Injector.get_instance(f"{in_channels}_{out_channels}")
        self.edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
        self.conv1 = GCNConv(in_channels, 2 * out_channels)
        self.conv4 = GCNConv(2 * out_channels, out_channels)

    def forward(self, x):
        self.edge_index = self.edge_index.to(x.device)
        x = x.reshape(self.size * self.size, self.in_channels)
        x = self.conv1(x, self.edge_index)
        x = self.conv4(x, self.edge_index)
        x = x.reshape(self.out_channels, self.size, self.size)
        return x
