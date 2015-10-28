"""Run and manage Swarm containers

Usage:
    dcos swarm --help
    dcos swarm --info
    dcos swarm --version
    dcos swarm --config-schema
    dcos swarm env

Options:
    --help                  Show this screen
    --info                  Show info
    --version               Show version
"""
from __future__ import print_function
import docopt
import os
from dcos_swarm import constants, discovery
from dcos import marathon, util


def swarm_daemon():
    return discovery.get_swarm_daemon()

def print_schema():
    print("{}")

def print_env():
    url = util.get_config().get('core.dcos_url')
    if url.startswith("http://"):
       url = url[7:]
    else:
       return 1;

    if url.endswith("/"):
        url = url[:-1]

    print("export DOCKER_HOST=" + url + ":80/service/swarm")
    return 0;

def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-swarm version {}'.format(constants.version), help=False)

    if args['--info']:
        print(__doc__.split('\n')[0])
    elif args['--config-schema']:
        print_schema()
    elif args['env']:
        return print_env()
    else:
        print(__doc__)
        return 1

    return 0
