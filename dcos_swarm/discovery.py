from __future__ import print_function

import os
import sys

import requests
import toml

from dcos import marathon

def get_swarm_tasks():
    client = marathon.create_client()
    return client.get_tasks("swarm")

def get_swarm_dispatcher():
    dcos_swarm_url = os.getenv("DCOS_SWARM_URL")
    if dcos_swarm_url is not None:
        return dcos_swarm_url

    tasks = get_swarm_tasks()

    if len(tasks) == 0:
        print("Swarm daemon task is not running yet.")
        sys.exit(1)

    return tasks[0]["host"] + ":" + str(tasks[0]["ports"][0])
