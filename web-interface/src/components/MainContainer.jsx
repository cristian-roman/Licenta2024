import { Flex } from "@chakra-ui/react";
import PropTypes from "prop-types";

import { fadeIn } from '../styles/animations';

export default function MainContainer({ children, ...props }) {
     return (
          <Flex
               direction={"column"}
               align={"center"}
               justify={"center"}
               bg="white"
               rounded="md"
               boxShadow="inside"
               animation={fadeIn()}
               {...props}
               p={8}
          >
               {children}
          </Flex >
     )
}

MainContainer.propTypes = {
     props: PropTypes.object,
     children: PropTypes.node
}