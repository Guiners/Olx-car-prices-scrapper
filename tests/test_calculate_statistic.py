import pytest
import sys

sys.path.append("F:\Coding\Projects\source_code")
from calculate_statistic import Calculate_statistic


def test_count_average():
    data = [30, 50, 90, 100, 30, 95, 55]
    calculator = Calculate_statistic
    assert calculator.count_average(data) == 64.29


def test_count_min():
    data = [20, 506, 34, 77, 1000, 5, 345, 6, 775, 8]
    calculator = Calculate_statistic
    assert calculator.count_min(data) == 5


def test_count_max():
    data = [20, 506, 34, 77, 1000, 5, 345, 6, 775, 8]
    calculator = Calculate_statistic
    assert calculator.count_max(data) == 1000
