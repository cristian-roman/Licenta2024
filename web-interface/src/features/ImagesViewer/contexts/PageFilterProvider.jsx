import { useState, createContext, useEffect } from "react";
import PropTypes from "prop-types";
import { getPages } from "../services";

export const PageFilterContext = createContext();

export default function PageFilterProvider({ children }) {
  const [index, setIndex] = useState(1);
  const [pages, setPages] = useState(0);
  const [provenience_filter, setProvenienceFilter] = useState('all');
  const [health_state_filter, setHealthStateFilter] = useState('all');

  useEffect(() => {
    async function fetchPages() {
      const counter = await getPages(provenience_filter, health_state_filter);
      setPages(counter);
    }
    fetchPages();
    setIndex(1);
  }, [provenience_filter, health_state_filter])

  const imagePairContextObject = {
    index,
    setIndex,
    pages,
    provenience_filter,
    setProvenienceFilter,
    health_state_filter,
    setHealthStateFilter
  };

  return (
    <PageFilterContext.Provider value={imagePairContextObject}>
      {children}
    </PageFilterContext.Provider>
  );
}

PageFilterProvider.propTypes = {
  children: PropTypes.node
}; 