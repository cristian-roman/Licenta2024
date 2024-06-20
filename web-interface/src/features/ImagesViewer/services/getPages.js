import { axiosClient } from "../../../api";

const DEFAULT_PATH = '/images/count';

export async function getPages(provenience_filter, health_state_filter) {
     const accepted_provenience = ['all', 'heart', 'prostate', 'endometriosis'];
     const accepted_health_state = ['all', 'healthy', 'diseased'];

     if ((provenience_filter === null || provenience_filter === undefined || !accepted_provenience.includes(provenience_filter))) {
          console.error('Invalid provenience filter:', provenience_filter);
          return null;
     }
     if ((health_state_filter === null || health_state_filter === undefined || !accepted_health_state.includes(health_state_filter))) {
          console.error('Invalid health state filter:', health_state_filter);
          return null;
     }

     const raw_json_post_body = {
          "provenience": provenience_filter,
          "health_state": health_state_filter
     }

     try {
          const response = await axiosClient.post(DEFAULT_PATH, raw_json_post_body, {
               responseType: 'json'
          });
          return response.data.pages;
     } catch (error) {
          console.error('Error fetching entry data:', error);
          return null;
     }
}