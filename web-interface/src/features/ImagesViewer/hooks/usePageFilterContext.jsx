import { useContext } from "react";
import { PageFilterContext } from "../contexts"

export default function usePageFilterContext() {
     return useContext(PageFilterContext);
}