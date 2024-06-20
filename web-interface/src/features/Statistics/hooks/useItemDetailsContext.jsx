import { useContext } from "react";
import { ItemDetailsContext } from "../contexts";

export default function useItemDetailsContext() {
     return useContext(ItemDetailsContext);
}