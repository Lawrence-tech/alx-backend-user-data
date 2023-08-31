#!/usr/bin/env python3
"""
Module filter_datum that returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    function to return the log message with arguments. uses regex
    """
    return re.sub(r'(?<=(' + re.escape(separator) + '|^)' + '|'.join(fields)
                  + r'=)[^' + re.escape(separator) + r']+', redaction, message)
