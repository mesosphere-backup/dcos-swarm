from __future__ import print_function

import os
import sys

import requests
import toml

from dcos import marathon, util

def get_swarm_daemon():
    base_url = util.get_config().get('core.dcos_url')
    return base_url + '/service/swarm/'
