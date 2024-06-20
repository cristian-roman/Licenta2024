import { useContext } from "react";

import { MobileContext } from "../contexts";

export default function useMobileContext() {
     return useContext(MobileContext);
}