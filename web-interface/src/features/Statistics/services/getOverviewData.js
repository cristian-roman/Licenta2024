import { axiosClient } from "../../../api";

const DEFALT_PATH = '/dataset/statistics/overview';

export async function getOverviewData() {
     try {
          const response = await axiosClient.get(DEFALT_PATH);
          return response.data;
     } catch (error) {
          console.error('Error fetching overview data:', error);
          return null;
     }
}