import { useContext } from "react";
import { OverviewContext } from "../contexts";

export default function useOverviewContext() {
     return useContext(OverviewContext);
}