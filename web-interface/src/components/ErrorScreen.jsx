import { Heading } from '@chakra-ui/react';
import PropTypes from 'prop-types';

export default function ErrorScreen({ message }) {
     return (

          <Heading
               w="100%"
               h="100%"
               size="lg"
               p={4}
               bg="red.500"
               rounded="full"
               align="center"
               color="gray.200"
          >
               {message}
          </Heading>
     )
}

ErrorScreen.propTypes = {
     message: PropTypes.string
};