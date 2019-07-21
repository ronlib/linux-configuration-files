#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Use in i3wm with:
Save as screeshot.py somewhere into your PATH
bindsym --release Print exec --no-startup-id screenshot.py
"""


import os
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile

SCREENSHOT_UTILITY = '/usr/bin/scrot ~/Pictures/screenshot_%Y_%m-%d_%H-%M.png' # /usr/bin/import

def feed_xclipboard(str):
    pipe = Popen("xclip -sel clip", shell=True, stdin=PIPE).stdin
    pipe.write(str)
    pipe.close()

def import_screenshot():
    # filename = NamedTemporaryFile(
    #     suffix='.png',
    #     prefix='screenshot_',
    #     dir = os.path.expanduser('~/Pictures'),
    #     delete=False).name
    p = Popen(SCREENSHOT_UTILITY, shell=True)
    os.waitpid(p.pid, 0)[1]
    # return filename


if __name__ == '__main__':
    import_screenshot()
    # feed_xclipboard(screenshot)