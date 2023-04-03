import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import t


chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    # Calculate sample mean and sample variance of measurements
    X_bar = np.mean(x)
    s_squared = np.var(x, ddof=1)
    
    # Calculate sample mean and sample variance of time squared
    t_squared = 59 ** 2
    
    # Calculate acceleration coefficient and its standard error
    A_bar = X_bar / t_squared
    s_A = np.sqrt(s_squared / t_squared**2)
    
    # Calculate degrees of freedom
    n = len(x)
    df = n - 1
    
    # Calculate t-value for given trust level and degrees of freedom
    t_value = t.ppf(1 - alpha / 2, df)
    
    # Calculate margin of error
    margin_error = t_value * s_A / np.sqrt(n)
    
    # Calculate confidence interval
    lower_bound = A_bar - margin_error
    upper_bound = A_bar + margin_error
    
    return (lower_bound, upper_bound)
