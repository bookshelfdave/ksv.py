# -*- coding: utf-8 -*-

"""Console script for ksv."""

import click
from ksv.ksv import show_yaml


@click.command()
@click.option('--encode', is_flag=True, help='Encode secret values')
def main(encode):
    """Decodes (or encodes with --encode) Kubernetes secrets yaml via stdin."""
    from sys import stdin
    show_yaml(stdin, encode)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
