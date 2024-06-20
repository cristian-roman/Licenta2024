import { Link as ReactRouterLink } from 'react-router-dom';
import { Link as ChakraLink } from '@chakra-ui/react';
import PropTypes from 'prop-types';

export default function NavItem({ name }) {

     let link = `/${name.toLowerCase()}`;
     if (link === '/home') {
          link = '/';
     }

     return (
          <ChakraLink
               as={ReactRouterLink} to={link}
               px={2}
               py={1}
               rounded="md"
               _hover={
                    {
                         textDecoration: 'none',
                         bg: 'blue.600'
                    }
               }
               color="white" >
               {name}
          </ChakraLink>
     );
}

NavItem.propTypes = {
     name: PropTypes.string
};