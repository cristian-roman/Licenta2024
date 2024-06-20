import { Heading, Box, Flex, Divider } from "@chakra-ui/react";

import { Background } from "../components";
import { growAnimation } from "../styles/animations";
import { ImagesViewer } from "../features";
import { ImageBoxProvider } from "../features/ImagesViewer/contexts";
import { ModelPerformance } from "../features"

const titleProps = {
     color: "white",
     size: "2xl",
     mt: 10,
     align: "center",
     css: growAnimation()
};

const subTitleProps = {
     color: "white",
     css: growAnimation(1, 1.5)
};

export default function Model() {
     return (
          <Background justify="top">
               <Heading {...titleProps}>
                    Model
               </Heading>
               <Divider borderWidth={2} borderColor="white" w="50%" my={5} />

               <Box bg="blue.700" p={4} rounded="md" m={4}>
                    <Heading {...subTitleProps}>
                         Performance
                    </Heading>
               </Box>


               <Flex direction="column" align="center" justify="center" w="100%" maxW={"1000"}>
                    <ModelPerformance />
                    <Box bg="blue.700" p={4} rounded="md" mt={10} mb={2}>
                         <Heading color="white" fontSize={"1.5rem"}>
                              Model outputs
                         </Heading>
                    </Box>
                    <ImagesViewer>
                         <ImageBoxProvider title="Ultrasound image" searching_word="image" />
                         <ImageBoxProvider title="Averaged turth" searching_word="averaged_mask" />
                         <ImageBoxProvider title="Model output" searching_word="ai" />
                    </ImagesViewer>
               </Flex>
          </Background>


     );
}