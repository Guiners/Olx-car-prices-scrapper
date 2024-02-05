import pytest
import sys

sys.path.append("F:\Coding\Projects\source_code")
from format_data import Format_data


def test_remove_outliers1():
    formatter = Format_data
    data = [30, 50, 90, 100, 30, 95, 55, 20, 2, 1000, 67, 84, 66]
    output = formatter.remove_outliers(data)
    assert output == [30, 50, 90, 100, 30, 95, 55, 20, 2, 67, 84, 66]


def test_remove_outliers2():
    formatter = Format_data
    data = [30, 50, 90, 30, 95, 55, 20, 2, 67, 84, 66]
    output = formatter.remove_outliers(data)
    assert output == [30, 50, 90, 30, 95, 55, 20, 2, 67, 84, 66]


def test_format_price():
    formatter = Format_data
    data = "23 000 zł"
    assert formatter.format_price(data) != "23 000 zł"
    assert formatter.format_price(data) == 23000


def test_format_number():
    formatter = Format_data
    data = "\n 23344 \n"
    assert formatter.format_price(data) == 23344
