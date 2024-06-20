import { useState, useEffect, createContext } from "react";
import PropTypes from "prop-types";

import { ItemDetails } from "../components";
import { axiosClient } from "../../../api";

const DEFAULT_PATH = "/dataset/statistics"

export const ItemDetailsContext = createContext();

export function ItemDetailsProvider({ children }) {

     const [title, setTitle] = useState("");
     const [details_path, setDetailsPath] = useState("");

     const [isOpen, setIsOpen] = useState(false);
     const [content, setContent] = useState([]);

     useEffect(() => {
          const fetchContent = async (path) => {
               const response = await axiosClient.get(DEFAULT_PATH + path);
               return response.data;
          }

          if (isOpen) {
               fetchContent(details_path).then((data) => {
                    setContent(data);
               }).catch((error) => {
                    console.error("Error fetching content: ", error);
               });
          }
          else {
               setContent([]);
          }

     }, [details_path, isOpen]);

     const modalContextObject = {
          title,
          setTitle,
          details_path,
          setDetailsPath,
          isOpen,
          setIsOpen,
          content

     };

     return (
          <ItemDetailsContext.Provider value={modalContextObject}>
               <ItemDetails />
               {children}
          </ItemDetailsContext.Provider>
     );
}

ItemDetailsProvider.propTypes = {
     children: PropTypes.node
};