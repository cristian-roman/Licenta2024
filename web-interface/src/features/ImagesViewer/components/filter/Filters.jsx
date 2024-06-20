import { Button, Heading, HStack, Icon, Menu, MenuButton, MenuList, VStack, Stack } from "@chakra-ui/react";
import { FiFilter } from "react-icons/fi";
import { useMobileContext } from "../../../../hooks";
import { usePageFilterContext } from "../../hooks";

export default function Filters() {
     const isMobile = useMobileContext();
     const pageFilterContext = usePageFilterContext();

     const onClickProvenience = (provenience) => {
          pageFilterContext.setIndex(1);
          pageFilterContext.setProvenienceFilter(provenience);
     }

     const onClickHealthState = (health_state) => {
          pageFilterContext.setIndex(1);
          pageFilterContext.setHealthStateFilter(health_state);
     }

     const ContainerType = isMobile ? VStack : HStack;
     return (
          <ContainerType>
               <HStack>
                    <Icon as={FiFilter} boxSize={6} />
                    <Heading as="h4" size="md" color="blue.300">
                         Filters
                    </Heading>
               </HStack>
               <Menu>
                    <MenuButton
                         minW={"100px"}
                         as={Button}
                         colorScheme="blue"
                         variant="outline"
                    >
                         Provenience
                    </MenuButton>
                    <MenuList>
                         <Stack spacing={2}>
                              <Button
                                   onClick={() => onClickProvenience('all')}
                              >All</Button>
                              <Button
                                   onClick={() => onClickProvenience('heart')}
                              >Heart</Button>
                              <Button
                                   onClick={() => onClickProvenience('prostate')}
                              >
                                   Prostate</Button>
                              <Button
                                   onClick={() => onClickProvenience('endometriosis')}
                              >Endometriosis</Button>
                         </Stack>
                    </MenuList>
               </Menu>
               <Menu>
                    <MenuButton
                         as={Button}
                         colorScheme="blue"
                         variant="outline"
                    >
                         Health state
                    </MenuButton>
                    <MenuList>
                         <Stack spacing={2}>
                              <Button
                                   onClick={() => onClickHealthState('all')}
                              >All</Button>
                              <Button
                                   onClick={() => onClickHealthState('healthy')}
                              >Healthy</Button>
                              <Button
                                   onClick={() => onClickHealthState('diseased')}
                              >Diseased</Button>
                         </Stack>
                    </MenuList>
               </Menu>
          </ContainerType >
     );
}
