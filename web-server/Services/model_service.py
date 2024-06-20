from Repository import model_stats_repository


def get_performance(metric):
    model_stats = model_stats_repository.get_entry()
    return {"value": model_stats.get(metric)}
