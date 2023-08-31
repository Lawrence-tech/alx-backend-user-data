#!/usr/bin/env python3
"""
Module to obfuscate log fields using regular expressions.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator:
                 str) -> str:
    """
    Replace occurrences of certain field values with the redaction string.

    Args:
        fields (List[str]): List of strings representing fields to obfuscate.
        redaction (str): String to replace the field values.
        message (str): Log line containing field-value pairs.
        separator (str): Character separating fields in the log line.

    Returns:
        str: Log message with specified fields obfuscated.
    """

    return re.sub(r'(?<=(' + re.escape(separator) + '|^)' + '|'.join(fields)
                  + r'=)[^' + re.escape(separator) + r']+', redaction, message)
