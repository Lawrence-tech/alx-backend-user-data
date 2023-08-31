#!/usr/bin/env python3
"""
Module to obfuscate log fields using regular expressions.
"""


import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        The itself funtion defination
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        The format logging record function
        """
        log_message = super().format(record)
        for field in self.fields:
            log_message = re.sub(rf'{field}=([^;]+)',
                                 f'{field}={self.REDACTION}', log_message)
        return log_message
