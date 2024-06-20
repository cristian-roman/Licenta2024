import { useNavigate } from "react-router-dom";
import { Heading, Text, Button } from "@chakra-ui/react";

import { Background, MainContainer } from '../components'

export default function NotFoundPage() {
     const navigate = useNavigate();


     return (
          <Background bgGradient="linear(to-r, red.400, red.600)">
               <MainContainer maxW={450}>
                    <Heading size="lg" mb={4}>
                         404 - Not Found
                    </Heading>
                    <Text>
                         Oops! The page you are looking for does not exist.
                    </Text>

                    <Button colorScheme="red" mt={4} onClick={() => navigate('/')}>
                         Go Home
                    </Button>
               </MainContainer>
          </Background>
     )
}
