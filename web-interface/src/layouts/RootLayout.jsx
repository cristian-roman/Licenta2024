import { useMobileContext } from '../hooks';
import NavContainer from './NavContainer';
import MobileNav from './MobileNav';
import DesktopNav from './DesktopNav';

export default function RootLayout() {
     const isMobile = useMobileContext();

     return (
          <NavContainer>
               {isMobile ? <MobileNav /> : <DesktopNav />}
          </NavContainer>
     );
}
