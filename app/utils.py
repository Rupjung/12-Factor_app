# app/utils.py


def compute_engineered_features(data):
    """
    Given raw wine input, compute additional engineered features.
    """
    fixed_acidity = data.fixed_acidity
    volatile_acidity = data.volatile_acidity
    residual_sugar = data.residual_sugar
    alcohol = data.alcohol
    free_SO2 = data.free_sulfur_dioxide
    total_SO2 = data.total_sulfur_dioxide

    # Engineered features
    acidity_sum = fixed_acidity + volatile_acidity + 0.01
    alcohol_to_acidity_ratio = alcohol / acidity_sum
    sugar_to_acidity_ratio = residual_sugar / acidity_sum
    total_acidity = fixed_acidity + volatile_acidity
    total_SO2_combined = free_SO2 + total_SO2

    return [alcohol_to_acidity_ratio, sugar_to_acidity_ratio, total_acidity, total_SO2_combined]
