import PropTypes from 'prop-types';

import { useMobileContext } from '../../hooks';
import { MainContainer } from "../../components";
import { MobileImagesViewer, DesktopImagesViewer } from "./components/";
import { PageFilterProvider } from "./contexts";

export default function ImagesViewer({ children }) {
     const isMobile = useMobileContext();
     return (
          <MainContainer w="100%" my={3}>
               <PageFilterProvider>
                    {isMobile ?
                         <MobileImagesViewer>
                              {children}
                         </MobileImagesViewer>
                         :
                         <DesktopImagesViewer>
                              {children}
                         </DesktopImagesViewer>
                    }
               </PageFilterProvider>
          </MainContainer>
     )
}

ImagesViewer.propTypes = {
     children: PropTypes.node,
};