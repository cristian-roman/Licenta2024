import { Menu, MenuButton, IconButton, MenuList, MenuItem } from "@chakra-ui/react";
import { HamburgerIcon } from "@chakra-ui/icons";
import { Link as ReactRouterLink } from "react-router-dom";

export default function MobileNav() {
     return (
          <Menu>
               <MenuButton
                    as={IconButton}
                    icon={<HamburgerIcon />}
                    variant="outline"
                    aria-label="Options"
               />
               <MenuList>
                    <MenuItem as={ReactRouterLink} to="/">Home</MenuItem>
                    <MenuItem as={ReactRouterLink} to="/dataset">Dataset</MenuItem>
                    <MenuItem as={ReactRouterLink} to="/model">Model</MenuItem>
               </MenuList>
          </Menu>
     );
}