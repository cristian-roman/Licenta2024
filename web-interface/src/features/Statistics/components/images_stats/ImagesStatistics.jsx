import PropTypes from "prop-types";

import { useMobileContext } from "../../../../hooks";

import Mobile from "./Mobile";
import Desktop from "./Desktop";

import { ImagesStatsProvider } from "../../contexts";

export default function ImagesStatistics({ type, modified }) {
     const isMobile = useMobileContext();

     return (
          <ImagesStatsProvider type={type} modified={modified}>
               {isMobile ? <Mobile /> : <Desktop />}
          </ImagesStatsProvider>
     )
}

ImagesStatistics.propTypes = {
     type: PropTypes.string.isRequired,
     modified: PropTypes.bool.isRequired
}