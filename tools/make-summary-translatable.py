#!/usr/bin/env python3

import glob
import os
import re
import yaml

os.chdir(os.path.dirname(__file__) + '/../')

for f in glob.glob('metadata/*.yml'):
    with open(f) as fp:
        raw = fp.read()
        data = yaml.load(raw)
    archive_policy = data.get('ArchivePolicy')
    if 'Disabled' not in data and 'Summary' in data \
       and (archive_policy is None or not archive_policy.startswith('0 ')):
        en_US_dir = f[:-4] + '/en-US/'
        os.makedirs(en_US_dir, exist_ok=True)
        with open(en_US_dir + '/summary.txt', 'w') as fp:
            fp.write(data['Summary'].strip().rstrip() + '\n')
        with open(f, 'w') as out:
            out.write(re.sub(r'Summary:[^\n]+\n', r'', raw))
