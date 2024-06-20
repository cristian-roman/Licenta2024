import { useContext } from "react";
import { BarStatisticsContext } from "../contexts";

export default function useBarStatisticsContext() {
     return useContext(BarStatisticsContext);
}