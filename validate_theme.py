#!/usr/bin/env python3
#
# Script for validating pekwm theme registry files
#

import json
import jsonschema
import os
import sys


def main(schema_path, themes):
    print('loading schema...')
    with open(schema_path) as fp:
        theme_schema = json.load(fp)

    for path in themes:
        print('validating {}'.format(path))
        with open(path) as fp:
            theme = json.load(fp)
        jsonschema.validate(instance=theme, schema=theme_schema)


if __name__ == '__main__':
    main(sys.argv[1:])
