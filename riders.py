#!/usr/bin/env python

import sys
import os
import time
import subprocess

def open_display(display_number):
    os.system('export DISPLAY=:'+str(display_number))
    os.environ["DISPLAY"] = ':'+str(display_number)
    subprocess.call('./Open_Display.sh', shell=True, cwd='/workspace/src')
