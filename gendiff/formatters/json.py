#!/usr/bin/env python3
import json


def json_formatter(diff):
    return json.dumps(diff, indent=4, separators=(',', ': '))
