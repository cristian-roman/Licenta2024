import { useNavigate } from "react-router-dom";
import { Heading, Text, Button } from "@chakra-ui/react";


import { Background, MainContainer } from '../components';


export default function LandingPage() {
     const navigate = useNavigate();
     return (
          <Background>
               <MainContainer maxW={650}>
                    <Heading size="2xl" mb={4}>
                         Welcome to MedAI
                    </Heading>

                    <Text fontSize="xl" align={"center"}>
                         MedAI is a web portal that allows visualizing the training dataset, see statistics about it, and check the model&apos;s performance and outputs.
                    </Text>

                    <Button colorScheme="blue" mt={4} onClick={() => navigate('/dataset')} w="30%" boxShadow="2xl">
                         Get Started
                    </Button>

               </MainContainer>
          </Background >
     )
}
