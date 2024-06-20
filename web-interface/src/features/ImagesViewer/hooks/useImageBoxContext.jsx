import { useContext } from 'react';
import { ImageBoxContext } from '../contexts';

export default function useImageBoxContext() {
     return useContext(ImageBoxContext);
}