"""Run and manage Swarm containers

Usage:
    dcos swarm --help
    dcos swarm --info
    dcos swarm --version
    dcos swarm --config-schema

Options:
    --help                  Show this screen
    --info                  Show info
    --version               Show version
"""
from __future__ import print_function
import docopt
from dcos_spark import constants, discovery, spark_submit


def swarm_daemon():
    return discovery.get_swarm_daemon()

def proxy_docker(args):
    return docker_client.proxy(swarm_daemon(), args)

def print_schema():
    print("{}")

def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-spark version {}'.format(constants.version), help=False)

    if args['--info']:
        print(__doc__.split('\n')[0])
    elif args['--config-schema']:
        print_schema()
    else:
        print(__doc__)
        return 1

    return 0
