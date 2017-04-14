import subprocess

subprocess.call(['cp','-f', './views/js/bit.js', './deploy/bit.js'])
subprocess.call(['cp','-f', './views/css/bit.css', './deploy/bit.css'])
subprocess.call(['aws','s3', 'sync', './deploy', 's3://bandsintown-calendar-assets', '--acl', 'public-read'])
