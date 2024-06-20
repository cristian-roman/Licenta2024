import { axiosClient } from './../../../api';

const DEFAULT_PATH = '/images';

export async function getImage(index, type, provenience_filter, health_state_filter) {
     if (index === null || index === undefined || typeof index !== 'number') {
          console.error('Error fetching image: index is mandatory and must be a number');
          return null;
     }

     const types = ['image', 'mask', 'averaged_mask', 'ai'];
     if (!types.includes(type)) {
          console.error('Error fetching image: type must be either image or mask');
          return null;
     }

     let path = `${DEFAULT_PATH}/${index}?type=${type}`;

     const accpeted_proveniences = ['all', 'heart', 'prostate', 'endometriosis'];
     const accepted_health_states = ['all', 'healthy', 'diseased'];

     if ((provenience_filter === null || provenience_filter === undefined || !accpeted_proveniences.includes(provenience_filter))) {
          console.error('Error fetching image: organ_filter must be either all, heart, prostate or endometriosis');
          return null;
     }

     if ((health_state_filter === null || health_state_filter === undefined || !accepted_health_states.includes(health_state_filter))) {
          console.error('Error fetching image: diseased_filter must be either all, true or false');
          return null;
     }

     const raw_json_post_body = {
          "provenience": provenience_filter,
          "health_state": health_state_filter
     }

     try {
          const response = await axiosClient.post(path, raw_json_post_body, { responseType: 'arraybuffer' });
          const base64 = btoa(
               new Uint8Array(response.data).reduce((data, byte) => data + String.fromCharCode(byte), '')
          );
          const mimeType = response.headers['content-type'];
          return `data:${mimeType};base64,${base64}`;
     } catch (error) {
          console.error('Error fetching image:', error);
          return null;
     }
}