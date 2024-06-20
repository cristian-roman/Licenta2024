import { Box, HStack, Link as ChakraLink, Heading, Spacer } from "@chakra-ui/react";
import { Outlet, Link as ReactRouterLink } from "react-router-dom";
import PropTypes from "prop-types";

import { Logo } from '../components';

export default function NavContainer({ children }) {
     return (
          <>
               <Box
                    bg="blue.500"
                    px={4}
               >
                    <HStack
                         h={16}
                         alignItems="center"
                         justifyContent="space-between"
                    >
                         <ChakraLink
                              as={ReactRouterLink} to="/"
                              _hover={{ textDecoration: 'none' }}
                         >
                              <HStack
                                   spacing={8}
                                   alignItems="center"
                              >
                                   <Logo />
                                   <Heading
                                        size="md"
                                        color="white"
                                   >
                                        MedAI
                                   </Heading>
                              </HStack>
                         </ChakraLink>
                         <Spacer />
                         {children}
                    </HStack>
               </Box>
               <Outlet />
          </>
     );
}


NavContainer.propTypes = {
     children: PropTypes.node,
};