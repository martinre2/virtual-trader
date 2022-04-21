"""Decimal Util"""
import ast


def str_to_float(number_str: str) -> float:
    """Cast str to float

    Args:
        number_str (str): unsafe number str from external sources

    Returns:
        float: converted number_str
    """
    return ast.literal_eval(number_str)
