import pandas as pd
import numpy as np

from scipy.stats import t

chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    t_value = t.ppf((1 + p) / 2, n-1)  
    t_squared = 59**2
    
    # Calculate acceleration coefficients
    accel_coefficients = 2 * (x + 0.5) / t_squared

    # Calculate sample mean and standard deviation
    sample_mean = np.mean(accel_coefficients)
    sample_std = np.std(accel_coefficients, ddof=1)

    # Calculate standard error and margin of error
    standard_error = sample_std / np.sqrt(n)
    margin_of_error = t_value * standard_error

    # Calculate confidence interval bounds
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    
    return lower_bound, upper_bound
