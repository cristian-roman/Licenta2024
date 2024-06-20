import { useContext } from "react";
import { ImagesStatsContext } from "../contexts"
export default function useImagesStatsContext() {
     return useContext(ImagesStatsContext);
}