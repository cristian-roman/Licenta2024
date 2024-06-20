import { Flex, Spinner, Text } from '@chakra-ui/react'

export default function LoadingScreen() {
     return (
          <Flex
               direction="column"
               w="100%"
               align="center"
               justify="center"
          >
               <Spinner
                    thickness="4px"
                    speed="0.65s"
                    emptyColor="gray.200"
                    color="blue.500"
                    size="xl"
               />
               <Text mt={4}>Loading...</Text>
          </Flex>
     )
}