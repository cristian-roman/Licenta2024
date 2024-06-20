import { axiosClient } from "../../../api";

const DEFAULT_PATH = '/dataset/statistics';

export async function getImagesStats(type, modified) {
     const path = DEFAULT_PATH + ('/' + type) + '?modified=' + modified;

     try {
          const response = await axiosClient.get(path);
          return response.data;
     } catch (error) {
          console.error(error);
          return null;
     }
}