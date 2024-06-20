import { createContext, useState, useEffect } from 'react';
import PropTypes from 'prop-types';

import { getImagesStats } from '../services';

export const ImagesStatsContext = createContext();

export function ImagesStatsProvider({ type, modified, children }) {
     const [fetching, setFetching] = useState(true);
     const [error, setError] = useState(null);

     const [max_np_value, setMaxNpValue] = useState(0);
     const [min_np_value, setMinNpValue] = useState(0);
     const [unique_sizes_count, setUniqueSizes] = useState(0);
     const [unique_np_values_count, setUniqueNpValues] = useState(0);

     useEffect(() => {
          async function fetchImagesStats() {
               setFetching(true);

               const data = await getImagesStats(type, modified);


               if (data == null)
                    setError('Error fetching images stats for ' + type + ' version: modified=' + modified);
               else {

                    setMaxNpValue(data.max_np_value);
                    setMinNpValue(data.min_np_value);
                    setUniqueSizes(data.unique_sizes_count);
                    setUniqueNpValues(data.unique_np_values_count);
               }
               setFetching(false);
          }

          fetchImagesStats();
     }, [type, modified, max_np_value]);

     const providerObject = {
          fetching,
          error,
          type,
          modified,
          max_np_value,
          min_np_value,
          unique_sizes_count,
          unique_np_values_count
     };

     return (
          <ImagesStatsContext.Provider value={providerObject}>
               {children}
          </ImagesStatsContext.Provider>
     );

}

ImagesStatsProvider.propTypes = {
     modified: PropTypes.bool.isRequired,
     type: PropTypes.string.isRequired,
     children: PropTypes.node.isRequired
}