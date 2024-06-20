import { HStack, VStack, Spacer, Flex } from "@chakra-ui/react";

import { SectionCard, InfoCard } from "../ui";
import { useOverviewContext } from "../../hooks";

import { ErrorScreen, LoadingScreen } from "../../../../components";

export default function Desktop() {
     const overviewData = useOverviewContext();
     return (
          <>
               {overviewData.fetching ? (
                    <LoadingScreen />
               ) : overviewData.error ? (
                    <ErrorScreen message={overviewData.error} />
               ) : (
                    <Flex
                         justify={"start"}
                         w="100%"
                    >
                         <SectionCard title="Overview" />
                         <HStack
                              align={"stretch"}
                              justify={"space-between"}
                              w="100%"
                              flex={1}
                              mx={2}
                         >
                              <InfoCard
                                   title="Pairs"
                                   value={overviewData.pairs}
                                   flex={1}
                              />
                              <VStack
                                   align={"stretch"}
                                   justify={"space-around"}
                              >
                                   <InfoCard
                                        title="Heart"
                                        value={overviewData.hearts}
                                        details_path={'/provenience?organ=heart'}
                                   />
                                   <InfoCard
                                        title="Prostate"
                                        value={overviewData.prostates}
                                        details_path={'/provenience?organ=prostate'}
                                   />
                                   <InfoCard
                                        title="Endometriosis"
                                        value={overviewData.endometriosis}
                                        details_path={'/provenience?organ=endometriosis'}
                                   />
                              </VStack>
                              <VStack
                                   alignItems={"stretch"}
                                   justifyContent={"end"}
                                   h="100%"
                                   flex={2}
                                   px={2}
                              >
                                   <Spacer />
                                   <SectionCard title="Disease Distribution" />
                                   <Spacer />
                                   <InfoCard
                                        title="Healthy"
                                        value={overviewData.healthy_slices}
                                   />
                                   <InfoCard
                                        title="Diseased"
                                        value={overviewData.diseased_slices}
                                   />
                              </VStack>
                         </HStack>
                    </Flex>
               )}
          </>
     );
}