import PropTypes from 'prop-types';
import { Flex, Heading } from '@chakra-ui/react';

export default function SectionCard({ title }) {
     return (
          <Flex
               direction={"column"}
               alignItems={"center"}
               justifyContent={"center"}
               minW={110}
               mx={2}
          >
               <Heading size="lg" color="blue.600" align="center">
                    {title}
               </Heading>
          </Flex>
     )
}

SectionCard.propTypes = {
     title: PropTypes.string.isRequired
}
