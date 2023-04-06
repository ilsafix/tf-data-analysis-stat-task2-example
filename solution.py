import pandas as pd
import numpy as np

from scipy.stats import norm, erlang

chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    t_squared = 59**2 
    # Calculate acceleration coefficients
    accel_coefficients = 2 * x / t_squared
    alpha = 1 - p
    s = np.sqrt(np.var(accel_coefficients)) / np.sqrt(len(x))
    return accel_coefficients.mean() - s * (norm.ppf(1 - alpha / 2) + erlang(a=len(x), loc=0.5, scale=1/len(x)).ppf(p)), \
           accel_coefficients.mean() - s * (norm.ppf(alpha / 2) - erlang(a=len(x), loc=0.5, scale=1/len(x)).ppf(p))
