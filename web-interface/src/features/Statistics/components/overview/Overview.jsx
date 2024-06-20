import { useMobileContext } from '../../../../hooks'
import { OverviewProvider } from '../../contexts'
import Mobile from './Mobile'
import Desktop from './Desktop'

export default function Overview() {
     const isMobile = useMobileContext();
     return (
          <OverviewProvider>
               {isMobile ? <Mobile /> : <Desktop />}
          </OverviewProvider>
     );
}