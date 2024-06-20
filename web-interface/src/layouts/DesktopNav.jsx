import { HStack } from "@chakra-ui/react";

import NavItem from "./NavItem";

export default function DesktopNav() {
     return (
          <HStack spacing={8} alignItems="center">
               <NavItem name="Home" />
               <NavItem name="Dataset" />
               <NavItem name="Model" />
          </HStack>
     );
}