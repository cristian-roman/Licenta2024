import { HStack } from "@chakra-ui/react";

import { SectionCard, InfoCard } from "../ui";
import { useImagesStatsContext } from "../../hooks";
import { LoadingScreen, ErrorScreen } from "../../../../components";

export default function Desktop() {

     const imagesStats = useImagesStatsContext();

     return (
          (imagesStats.fetching) ?
               <LoadingScreen />
               :
               (imagesStats.error) ?
                    <ErrorScreen message={imagesStats.error} />
                    :
                    <HStack
                         align={"stretch"}
                         justify={"start"}
                    >
                         <SectionCard title={imagesStats.type} />
                         <HStack
                              align={"stretch"}
                              justify={"start"}
                              flex={1}
                         >
                              <InfoCard
                                   title="Unique sizes"
                                   value={imagesStats.unique_sizes_count}
                                   details_path={'/' + imagesStats.type + '/unique_sizes' + '?modified=' + imagesStats.modified}
                              />
                              <InfoCard
                                   title="Unique np values"
                                   value={imagesStats.unique_np_values_count}
                                   details_path={'/' + imagesStats.type + '/weighted_average_np_value' + '?modified=' + imagesStats.modified}
                              />
                              <InfoCard
                                   title="Min np value"
                                   value={imagesStats.min_np_value}
                              />
                              <InfoCard
                                   title="Max np value"
                                   value={imagesStats.max_np_value}
                              />
                         </HStack>
                    </HStack>
     );
}
