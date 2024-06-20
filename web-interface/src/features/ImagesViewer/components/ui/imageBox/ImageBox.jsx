import { Box, Heading, Image, VStack } from '@chakra-ui/react';

import { useImageBoxContext } from '../../../hooks';

export default function ImageBox() {
     const imageBoxContext = useImageBoxContext();
     return (
          <VStack>
               <Box bg="blue.700" p={4} rounded="md" mt={8} mb={4}>
                    <Heading color="blue.300" align="center">
                         {imageBoxContext.title}
                    </Heading>
               </Box>
               <Image src={imageBoxContext.image_src} p={4} />
          </VStack>

     );
}