import { axiosClient } from "../../../api";

const DEFAULT_PATH = "/model/performance";

export async function getModelStatistics(name) {
     const accepted_statistics = ["accuracy", "f1_score", "precision", "recall"];
     if (!accepted_statistics.includes(name)) {
          throw new Error("Invalid statistics name");
     }

     return axiosClient.get(DEFAULT_PATH + "?metric=" + name);
}