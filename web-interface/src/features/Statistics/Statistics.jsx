import { Divider, Box } from "@chakra-ui/react";
import { MainContainer } from "../../components";
import { ImagesStatistics, Overview } from "./components";
import { ItemDetailsProvider } from "./contexts";
import { SectionCard } from "./components";

export default function Statistics() {
     return (
          <ItemDetailsProvider>
               <MainContainer w="100%" my={5}>

                    <Box w="85%" rounded="md" p={4} m={4} boxShadow={"dark-lg"}>
                         <Overview />
                    </Box>

                    <MainContainer mt={10} mb={2} bg="blue.100">
                         <Divider borderWidth="2px" borderColor="gray.500" />
                         <SectionCard title="Unmodified images" />
                         <Divider borderWidth="2px" borderColor="gray.500" />
                    </MainContainer>

                    <Box w="85%" rounded="md" p={4} m={2} boxShadow={"dark-lg"}>
                         <ImagesStatistics type="images" modified={false} />
                         <ImagesStatistics type="masks" modified={false} />
                    </Box>

                    <MainContainer mt={10} mb={2} bg="blue.100">
                         <Divider borderWidth="2px" borderColor="gray.500" />
                         <SectionCard title="Modified images" />
                         <Divider borderWidth="2px" borderColor="gray.500" />
                    </MainContainer>

                    <Box w="85%" rounded="md" p={4} m={2} boxShadow={"dark-lg"}>
                         <ImagesStatistics type="images" modified={true} />
                         <ImagesStatistics type="masks" modified={true} />
                    </Box>
               </MainContainer>
          </ItemDetailsProvider>
     );
}