import { Box, Heading, Text } from "@chakra-ui/react";
export default function Note() {
     return (
          <Box bg="blue.600" rounded="md" w="40%">
               <Heading as="h4" size="md" color="blue.300" pl={4} pt={4}>
                    *Note:
               </Heading>
               <Text color="gray.300" my={4} mx={2} pl={4}>
                    This images are the modified versions.
               </Text>
          </Box>
     );
}