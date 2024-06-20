import { createContext } from 'react';
import { useBreakpointValue } from '@chakra-ui/react';
import PropTypes from 'prop-types';

export const MobileContext = createContext();

export function MobileProvider({ children }) {

     const mobileBreakPoint = useBreakpointValue(
          {
               base: true,
               xs: true,
               sm: true,
               md: false,
               lg: false,
               xl: false
          })

     return (
          <MobileContext.Provider value={mobileBreakPoint}>
               {children}
          </MobileContext.Provider>
     )
}

MobileProvider.propTypes = {
     children: PropTypes.node
};