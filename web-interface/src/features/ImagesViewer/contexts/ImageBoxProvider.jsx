import PropTypes from 'prop-types';
import { createContext, useState, useEffect } from 'react';
import { usePageFilterContext } from '../hooks';
import { getImage } from '../services';
import ImageBox from '../components/ui/imageBox/ImageBox';

export const ImageBoxContext = createContext();

export default function ImageBoxProvider({ title, searching_word: type }) {
     const pageFilterContext = usePageFilterContext();

     const [image_src, setImageSrc] = useState(null);

     useEffect(() => {
          async function fetchImage() {
               let src = await getImage(
                    pageFilterContext.index,
                    type,
                    pageFilterContext.provenience_filter,
                    pageFilterContext.health_state_filter);
               setImageSrc(src);
          }
          fetchImage();
     }, [pageFilterContext.index, type, pageFilterContext.provenience_filter, pageFilterContext.health_state_filter]);

     const imageBoxContextObject = {
          title,
          image_src,
     };

     return (
          <ImageBoxContext.Provider value={imageBoxContextObject}>
               <ImageBox />
          </ImageBoxContext.Provider>
     );
}

ImageBoxProvider.propTypes = {
     title: PropTypes.string.isRequired,
     searching_word: PropTypes.string.isRequired
};
