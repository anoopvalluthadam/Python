import os
path = '/home/gabriel/bin'
listDir = os.listdir(path)
shell_script = filter(lambda x: x.endswith('*.sh'),listDir)
for files in shell_script:
    print files
