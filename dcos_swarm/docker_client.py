from __future__ import print_function
import json
import os
import os.path
import subprocess

import pkg_resources

def proxy(master, args):
    response = run(master, args)
    if response[0] is not None:
        print("Run job succeeded. Submission id: " +
              response[0]['submissionId'])
    return response[1]

def which(program):
    """Returns the path to the named executable program.

    :param program: The program to locate:
    :type program: str
    :rtype: str
    """

    def is_exe(file_path):
        return os.path.isfile(file_path) and os.access(file_path, os.X_OK)

    file_path, filename = os.path.split(program)
    if file_path:
        if is_exe(program):
            return program
    elif constants.PATH_ENV in os.environ:
        for path in os.environ[constants.PATH_ENV].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def check_docker():
    # Check if JAVA is in the PATH
    return which('docker') is not None

def run(master, args, props = []):
    """
    This method runs spark_submit with the passed in parameters.
    ie: ./bin/spark-submit --deploy-mode cluster --class
    org.apache.spark.examples.SparkPi --master mesos://10.127.131.174:8077
    --executor-memory 1G --total-executor-cores 100 --driver-memory 1G
    http://10.127.131.174:8000/spark-examples_2.10-1.3.0-SNAPSHOT.jar 30
    """
    if not check_docker():
        print("DCOS Spark requires Docker client to be installed. Please install Docker client.")
        return (None, 1)

    command = ["docker", "-H", master] + args

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Swarm failed:")
        print(stderr)
        return (None, process.returncode)
    else:
        response = json.loads(stderr[stderr.index('{')::])
        return (response, process.returncode)
