import { useState, createContext, useEffect } from 'react';
import PropTypes from 'prop-types';
import BarStatistics from '../components/BarStatistics';
import { getModelStatistics } from '../services/getModelStatistics';

export const BarStatisticsContext = createContext();

export function BarStatisticsProvider({ title, search_key_word }) {
     const [value, setValue] = useState(0);

     useEffect(() => {
          const fetchBarData = async () => {
               const response = await getModelStatistics(search_key_word);
               return response.data.value;
          }
          fetchBarData().then((data) => setValue(data));
     }, [search_key_word]);

     return (
          <BarStatisticsContext.Provider value={{ value, title }}>
               <BarStatistics />
          </BarStatisticsContext.Provider>
     );
}

BarStatisticsProvider.propTypes = {
     title: PropTypes.string.isRequired,
     search_key_word: PropTypes.string.isRequired
};