import subprocess

subprocess.call(['rm','-f', './deploy/getBandsintownEvents.zip'])
subprocess.call(['zip', '-r', '../deploy/getBandsintownEvents.zip', 'getBandsintownEvents.py', 'requests', 'requests-2.12.0.dist-info'], cwd='app')
subprocess.call(['aws', 'lambda', 'update-function-code', '--function-name', 'getBandsintownEvents', '--zip-file', 'fileb://./deploy/getBandsintownEvents.zip'])
