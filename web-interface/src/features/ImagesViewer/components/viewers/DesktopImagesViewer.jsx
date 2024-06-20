import PropTypes from 'prop-types';
import { HStack, Flex } from "@chakra-ui/react";

import { PageSwitcher } from '../pageSwitcher';
import { Note } from '../ui/note';
import { Filters } from "../filter";

export default function DesktopImagesViewer({ children }) {
     return (
          <>
               <HStack spacing={10} mx={4} px={4} justify={"space-between"} w="100%">
                    {children}
               </HStack >
               <PageSwitcher />
               <Flex w="100%" justify={"space-between"} mt={10} mx={4} px={8}>
                    <Filters />
                    <Note />
               </Flex >
          </>
     );
}

DesktopImagesViewer.propTypes = {
     children: PropTypes.node
};