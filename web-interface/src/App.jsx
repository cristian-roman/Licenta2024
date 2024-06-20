import { Route, createBrowserRouter, createRoutesFromElements, RouterProvider } from 'react-router-dom';

import { MobileProvider } from './contexts';
import { RootLayout } from './layouts';
import { Landing, Dataset, Model, NotFound } from './pages';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route index element={<Landing />} />
      <Route path="dataset" element={<Dataset />} />
      <Route path="model" element={<Model />} />
      <Route path="*" element={<NotFound />} />
    </Route>
  )
);


function App() {
  return (
    <MobileProvider>
      <RouterProvider router={router} />
    </MobileProvider>
  );
}

export default App
