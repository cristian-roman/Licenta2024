import { Flex } from "@chakra-ui/react";

import { SectionCard, InfoCard } from "../ui";
import { useImagesStatsContext } from "../../hooks";
import { LoadingScreen, ErrorScreen } from "../../../../components";

export default function Mobile() {
     const imagesStats = useImagesStatsContext();

     return (
          (imagesStats.fetching) ?
               <LoadingScreen />
               :
               (imagesStats.error) ?
                    <ErrorScreen
                         message={imagesStats.error}
                    />
                    :
                    <Flex
                         direction="column"
                         my={4}
                         w="100%"
                    >
                         <SectionCard title={imagesStats.type} />
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
                    </Flex>
     );
}