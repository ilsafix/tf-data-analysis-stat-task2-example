import pandas as pd
import numpy as np

from scipy.stats import expon

chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return expon(scale=1).ppf(alpha / 2) / (len(x)*np.min(x)), \
           expon(scale=1).ppf(1 - alpha / 2) / (len(x)*np.min(x))
