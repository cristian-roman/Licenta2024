import { Heading, Divider, Box, Flex } from "@chakra-ui/react"

import { Background } from '../components';
import { growAnimation } from '../styles/animations';
import { Statistics, ImagesViewer } from '../features'
import { ImageBoxProvider } from "../features/ImagesViewer/contexts";

const titleProps = {
     color: "white",
     size: "2xl",
     mt: 10,
     css: growAnimation(),
     align: "center"
};

const subTitleProps = {
     color: "white",
     css: growAnimation(1, 1.5)
};
export default function Dataset() {
     return (
          <Background
               justify="top"
          >
               <Heading {...titleProps}>
                    Training dataset
               </Heading>

               <Divider borderWidth={2} borderColor="white" w="50%" my={5} />

               <Box bg="blue.700" p={4} rounded="md" my={3}>
                    <Heading {...subTitleProps}>
                         Statistics
                    </Heading>
               </Box>

               <Flex direction="column" align="center" justify="center" w="100%" maxW={"1000"}>
                    <Statistics />

                    <Box bg="blue.700" p={4} rounded="md" my={3}>
                         <Heading color="white" fontSize={"1.5rem"}>
                              Images viewer
                         </Heading>
                    </Box>
                    <ImagesViewer>
                         <ImageBoxProvider title="Ultrasound image" searching_word="image" />
                         <ImageBoxProvider title="Ground truth" searching_word="mask" />
                         <ImageBoxProvider title="Averaged truth" searching_word="averaged_mask" />
                    </ImagesViewer>
               </Flex>
          </Background >
     )
}
