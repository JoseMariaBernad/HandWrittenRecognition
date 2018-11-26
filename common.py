from fastai import Path
from fastai import Config
import json
#path = Path(Config.get_key('data_path')).expanduser()/'handwritten'
# /mnt/handwritten is a path specific to azure datascience machine. If it does not work, uncomment the line above
# and comment line below
ramdisk_path = Path('/tmp/ramdisk')
path = Path(ramdisk_path/'handwritten')
permanent_path = Path(Config.get_key('data_path')).expanduser()/'handwritten'

def save_classes(file, classes, path=Path('.')):
    path = path/'models'
    file = path/file
    filestr = str(file)
    with open(filestr + '.classes', 'w') as f:
        f.write(json.dumps(classes))

def load_classes(file, path=Path('.')):
    path = path/'models'
    file = path/file
    filestr = str(file)
    with open(filestr + '.classes', 'r') as f:
        return json.loads(f.read())