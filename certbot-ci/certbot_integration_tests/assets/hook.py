#!/usr/bin/env python
import sys
import os

hook_script_type = os.path.basename(os.path.dirname(sys.argv[1]))
sys.stderr.write(str(os.environ))
if hook_script_type == 'deploy' and ('RENEWED_DOMAINS' not in os.environ or 'RENEWED_LINEAGE' not in os.environ):
    sys.stderr.write('Environment variables not properly set!\n')
    sys.exit(1)

with open(sys.argv[2], 'a') as file_h:
    file_h.write(hook_script_type + '\n')