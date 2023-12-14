import subprocess
import os

# os.chmod('./demo.sh', 0o755)
with open('./demo1.sh', 'rb') as file:
    script = file.read()
rc = subprocess.call(script, shell=True)

# rc = subprocess.call("./demo.sh")