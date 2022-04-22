"""Decimal Util"""
import ast
from decimal import Decimal


def str_to_float(number_str: str) -> float:
    """Cast str to float

    Args:
        number_str (str): unsafe number str from external sources

    Returns:
        float: converted number_str
    """
    return ast.literal_eval(number_str)


def str_to_decimal(number_str: str) -> Decimal:
    """Cast str to Decimal

    Args:
        number_str (str): unsafe number str from external sources

    Returns:
        Decimal: converted number_str
    """

    return Decimal(number_str)
