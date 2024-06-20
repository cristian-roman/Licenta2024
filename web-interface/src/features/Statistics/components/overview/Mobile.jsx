import { Flex } from '@chakra-ui/react'

import { SectionCard, InfoCard } from '../ui'
import { useOverviewContext } from '../../hooks'
import { ErrorScreen, LoadingScreen } from '../../../../components'

export default function Mobile() {
     const overviewData = useOverviewContext();
     return (
          overviewData.fetching ? (
               <LoadingScreen />
          ) : overviewData.error ? (
               <ErrorScreen message={overviewData.error} />
          ) : (
               <Flex
                    direction="column"
                    w="100%"
                    align="center"
                    justify="center"
               >
                    <SectionCard title="Overview" />
                    <InfoCard
                         title="Pairs"
                         value={overviewData.pairs}
                    />
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

                    <SectionCard title="Disease Distribution" />
                    <InfoCard
                         title="Healthy"
                         value={overviewData.healthy_slices}
                    />
                    <InfoCard
                         title="Diseased"
                         value={overviewData.diseased_slices}
                    />
               </Flex>
          )
     );
}