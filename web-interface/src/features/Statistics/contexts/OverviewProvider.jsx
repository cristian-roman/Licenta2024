import { useState, useEffect, createContext } from 'react';
import PropTypes from 'prop-types'

import { getOverviewData } from '../services';

export const OverviewContext = createContext();

export function OverviewProvider({ children }) {

     const [fetching, setFetching] = useState(true);
     const [error, setError] = useState(null);

     const [pairs, setPairs] = useState(0);
     const [hearts, setHearts] = useState(0);
     const [prostates, setProstates] = useState(0);
     const [endometriosis, setEndometriosis] = useState(0);
     const [diseased_slices, setDiseasedSlices] = useState(0);
     const [healthy_slices, setHealthySlices] = useState(0);

     useEffect(() => {
          async function fetchData() {
               const fetchedData = await getOverviewData();
               setFetching(false);
               if (fetchedData == null) {
                    setError('Server could not provide the overview data');
               }
               else {
                    setPairs(fetchedData.pairs);
                    setHearts(fetchedData.hearts);
                    setProstates(fetchedData.prostates);
                    setEndometriosis(fetchedData.endometriosis);
                    setDiseasedSlices(fetchedData.diseased_slices);
                    setHealthySlices(fetchedData.healthy_slices);
               }
          }
          fetchData();
     }, []);

     const contextObject = {
          fetching,
          error,
          pairs,
          hearts,
          prostates,
          endometriosis,
          diseased_slices,
          healthy_slices
     };

     return (
          <OverviewContext.Provider value={contextObject}>
               {children}
          </OverviewContext.Provider>
     );
}

OverviewProvider.propTypes = {
     children: PropTypes.node.isRequired
};