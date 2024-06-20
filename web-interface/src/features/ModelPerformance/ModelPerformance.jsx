import { MainContainer } from "../../components"
import { BarStatisticsProvider } from "./contexts";

export default function ModelPerformance() {
     return (
          <MainContainer w="100%" animation="none" p={4}>
               <BarStatisticsProvider title="Accuracy" search_key_word="accuracy" />
               <BarStatisticsProvider title="Precision" search_key_word="precision" />
               <BarStatisticsProvider title="Recall" search_key_word="recall" />
               <BarStatisticsProvider title="F1 Score" search_key_word="f1_score" />
          </MainContainer>
     );
}