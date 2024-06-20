import { Button, HStack, Input, Text } from "@chakra-ui/react";
import { useState, useEffect } from "react";

import { usePageFilterContext } from "../../hooks";

import { validateIndex, getPrevIndex, getNextIndex } from "../../../../utils";

const buttonStyle = {
     bg: "blue.100",
     color: "blue.700",
     _hover: {
          bg: "blue.200",
          color: "blue.700"
     }
};

const inputStyle = {
     size: "md",
     variant: "outline",
     w: "70px",
     textAlign: "center"
};

export default function PageSwitcher() {
     const pageFilterContext = usePageFilterContext();

     const [uiImageIndex, setUiImageIndex] = useState(pageFilterContext.index);

     useEffect(() => {
          setUiImageIndex(pageFilterContext.index);
     }, [pageFilterContext.index]);

     const handleImageChange = (e) => {
          const { value } = e.target;
          const new_value = validateIndex(value, pageFilterContext.pages);
          setUiImageIndex(new_value);
          if (new_value !== "") {
               pageFilterContext.setIndex(new_value);
          }
     }

     const handlePrevButtonClick = () => {
          const new_index = getPrevIndex(pageFilterContext.index, pageFilterContext.pages);
          pageFilterContext.setIndex(new_index);
     }

     const handleNextButtonClick = () => {
          const new_index = getNextIndex(pageFilterContext.index, pageFilterContext.pages);
          pageFilterContext.setIndex(new_index);
     }

     return (
          <HStack mt={4}>
               <Button {...buttonStyle} onClick={handlePrevButtonClick}>
                    &lt;
               </Button>
               <Input
                    {...inputStyle}
                    value={uiImageIndex}
                    onChange={handleImageChange}
               />
               <Text>
                    of {pageFilterContext.pages}
               </Text>
               <Button {...buttonStyle} onClick={handleNextButtonClick}>
                    &gt;
               </Button>
          </HStack >
     );
}
