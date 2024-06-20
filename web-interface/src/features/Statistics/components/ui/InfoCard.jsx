import { Flex, Heading } from '@chakra-ui/react';
import PropTypes from 'prop-types';
import { useItemDetailsContext } from '../../hooks';

const defaultStyles = {
     direction: "column",
     align: "center",
     justify: "center",
     backgroundColor: "blue.100",
     rounded: "md",
     w: "100%",
     margin: "2",
};

const interaction = {
     cursor: "pointer",
     _hover: {
          backgroundColor: "blue.200"
     }
};

export default function InfoCard({ title, value, details_path }) {
     const itemDetailsContext = useItemDetailsContext();

     //if type of value is float fixed it 2 decimal places
     if (typeof value === 'number') {
          if (Number.isInteger(value)) {
               value = value.toFixed(0);
          }
          else {
               value = value.toFixed(2);
          }
     }

     let onClick = null;
     if (details_path) {
          onClick = () => {
               itemDetailsContext.setTitle(title);
               itemDetailsContext.setDetailsPath(details_path);
               itemDetailsContext.setIsOpen(true);
          }
     }
     return (
          <Flex
               {...defaultStyles}
               {...(onClick && interaction)}
               onClick={onClick}
          >
               <Heading size="md" color="blue.700" align="center">
                    {title}
               </Heading>
               <Heading
                    size="lg"
                    color="blue.400"
                    textAlign={"center"}
               >
                    {value}
               </Heading>
          </Flex >
     );
}

InfoCard.propTypes = {
     title: PropTypes.string.isRequired,
     value: PropTypes.number.isRequired,
     details_path: PropTypes.string
};
