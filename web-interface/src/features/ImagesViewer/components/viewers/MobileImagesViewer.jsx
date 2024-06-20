import PropTypes from "prop-types";
import { Flex } from "@chakra-ui/react";
import PageSwitcher from "../pageSwitcher/PageSwitcher";
import { Note } from "../ui/note";
import { Filters } from "../filter";

export default function MobileImagesViewer({ children }) {
     return (
          <>
               {children}

               <PageSwitcher />

               <Flex w="100%" justify={"space-between"} mt={10} mx={4} px={8}>
                    <Filters />
                    <Note />
               </Flex >
          </>
     );
}

MobileImagesViewer.propTypes = {
     children: PropTypes.node,
};