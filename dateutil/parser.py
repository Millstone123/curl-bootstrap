"""Minimal date parsing used by the report renderer."""

from datetime import datetime

def parse(value):
    return datetime.fromisoformat(value)
