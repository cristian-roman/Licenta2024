import { Flex } from "@chakra-ui/react";
import PropTypes from "prop-types";

export default function Background({ children, ...props }) {
     return (
          <Flex
               direction={"column"}
               align={"center"}
               justify={"center"}
               minH="100vh"
               bgGradient="linear(to-r, blue.200, blue.400)"
               {...props}
          >
               {children}
          </Flex>
     );
}


Background.propTypes = {
     children: PropTypes.node,
};
