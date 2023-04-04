import pandas as pd
import numpy as np

from scipy.stats import expon

chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    t_squared = 59**2 
    # Calculate acceleration coefficients
    accel_coefficients = 2 * (x + 0.5) / t_squared
    alpha = 1 - p

    return accel_coefficients.mean() - np.sqrt(np.var(accel_coefficients)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)), \
           accel_coefficients.mean() - np.sqrt(np.var(accel_coefficients)) * norm.ppf(alpha / 2) / np.sqrt(len(x))
