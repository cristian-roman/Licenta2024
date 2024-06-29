import { Box, Text, Flex, Heading } from '@chakra-ui/react';
import { useState, useEffect } from 'react';

import { useBarStatisticsContext } from '../hooks';

const growing_width_animation = (percentage) => {
     return {
          width: `${percentage}%`,
          transition: "width 2s",
     };
};

export default function BarStatistics() {

     const barData = useBarStatisticsContext();

     const [width, setWidth] = useState(0);

     useEffect(() => {
          setWidth(barData.value * 100);
     }, [barData.value]);

     return (
          <Flex align="stretch" w="100%" rounded="md" justify="space-around" my={2}>
               < Box background="white" p={1} borderRadius="md" boxShadow="md" bg="gray.700" w="80%" >
                    <Box
                         h="100%"
                         minW={"10"}
                         background="green.500"
                         borderRadius="md"
                         p={2}
                         color="white"
                         fontWeight="bold"
                         position="relative"
                         overflow="hidden"
                         css={growing_width_animation(width)}
                    >
                         <Text position="absolute" left="50%" top="50%" transform="translate(-50%, -50%)">
                              {Math.round(barData.value * 100)}%
                         </Text>
                    </Box>
               </Box >
               <Heading color={"gray.700"} p={2} textAlign="center" fontSize={"1.5rem"} minW="200px">
                    {barData.title}
               </Heading>
          </Flex >
     );
}