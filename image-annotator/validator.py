import numpy as np

from Data.data_provider import DataProvider
from Data.db_connection import DbConnection
from ModelState.trainer_model_state import TrainerModelState
from utils.injector import Injector

__tp_total = 0
__tn_total = 0
__fp_total = 0
__fn_total = 0


def run_validation_phase(model_state: TrainerModelState, data_provider: DataProvider):
    global __tp_total, \
        __tn_total, \
        __fp_total, \
        __fn_total

    logger = Injector.get_instance("logger")
    logger.log_info("Validation phase started")

    for (img_np, mask_np, index) in data_provider.validation_data_iterator():
        print(f"Validating input {index} / {data_provider.count_validation_indices}")
        annotated_mask_np = model_state.annotate_image(img_np)
        tp, tn, fp, fn = __compute_entry_metrics(annotated_mask_np, mask_np)
        __add_to_global_metrics(tp, tn, fp, fn)

    accuracy = (__tp_total + __tn_total) / (__tp_total + __tn_total + __fp_total + __fn_total)
    recall = __tp_total / (__tp_total + __fn_total)
    precision = __tp_total / (__tp_total + __fp_total)
    f1_score = 2 * (precision * recall) / (precision + recall)

    logger.log_info(f"Tp: {__tp_total}")
    logger.log_info(f"Tn: {__tn_total}")
    logger.log_info(f"Fp: {__fp_total}")
    logger.log_info(f"Fn: {__fn_total}")

    logger.log_info(f"Accuracy: {accuracy}")
    logger.log_info(f"Recall: {recall}")
    logger.log_info(f"Precision: {precision}")
    logger.log_info(f"F1 Score: {f1_score}")

    __save_metrics_to_db(accuracy, recall, precision, f1_score)

    logger.log_info("Validation phase completed. Models stats saved to database.")


def __compute_entry_metrics(annotated_mask_np, mask_np):
    mask_np = (mask_np >= 0.58).astype(int)
    tp = np.sum(np.logical_and(mask_np == 1, annotated_mask_np == 1))
    tn = np.sum(np.logical_and(mask_np == 0, annotated_mask_np == 0))
    fp = np.sum(np.logical_and(mask_np == 0, annotated_mask_np == 1))
    fn = np.sum(np.logical_and(mask_np == 1, annotated_mask_np == 0))

    return tp, tn, fp, fn


def __add_to_global_metrics(tp, tn, fp, fn):
    global __tp_total, \
        __tn_total, \
        __fp_total, \
        __fn_total

    __tp_total += tp
    __tn_total += tn
    __fp_total += fp
    __fn_total += fn


def __save_metrics_to_db(accuracy, recall, precision, f1_score):
    global __tp_total, \
        __tn_total, \
        __fp_total, \
        __fn_total

    with DbConnection() as (db, _):
        metrics = {
            "tp": int(__tp_total),
            "tn": int(__tn_total),
            "fp": int(__fp_total),
            "fn": int(__fn_total),
            "accuracy": float(accuracy),
            "recall": float(recall),
            "precision": float(precision),
            "f1_score": float(f1_score)
        }

        model_stats_id = get_model_stats_id()
        if model_stats_id:
            db.model_stats.update_one({"_id": model_stats_id}, {"$set": metrics})
        else:
            db.model_stats.insert_one(metrics)


def get_model_stats_id():
    with DbConnection() as (db, _):
        try:
            return db.model_stats.find_one(sort=[("date", -1)])['_id']
        except Exception:
            return None