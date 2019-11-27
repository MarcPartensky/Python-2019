import subprocess
import sys


command = "open -a Terminal -n\n echo test"

ssh = subprocess.Popen(["ssh", "%s" % host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()

if result == []:
    error = ssh.stderr.readlines()
    print("ERROR: %s" % error )
else:
    print( result )
