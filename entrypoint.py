#!/usr/bin/python3

import os
import sys

import validate_theme


def main(schema_path, theme_dir):
    themes = [os.path.join(theme_dir, theme) for theme in os.listdir(theme_dir)
              if theme.endswith('.json')]
    validate_theme.main(schema_path, themes)
    # FIXME: provide informative outputs


if __name__ == '__main__':
    if 'GITHUB_WORKSPACE' not in os.environ:
        sys.stderr.write('GITHUB_WORKSPACE not set\n')
        sys.exit(1)

    path = os.environ['GITHUB_WORKSPACE']
    schema_path = os.path.join(path, 'theme.schema.json')
    themes_dir = os.path.join(path, 'themes')
    main(schema_path, themes_dir)
