# written by Michael Mumford
# import sublime
# import sublime_plugin

# import subprocess
import os
import os.path
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))


class FocusFile():

    def __init__(self, view):
        self.view = view
        #  assume file_name starts with 'C:\ProgramData\MEDITECH',
        # strip first 23 characters...
        head = str(self.view.file_name())[23:]
        # assume '!AllUsers\Sys\PgmCache\...' is after
        # the '\universe\ring\' = stop at the first '!'
        self.unvring = re.split('[\!]', head)

        start = '"C:\Program Files (x86)\MEDITECH'
        textpadtools = 'System\PgmObject\FocZ.TextPadTools.P.mps"'
        sublimeprog = 'System\PgmObject\TestMmmAlpha.SublimeText.P.mps"'

        self.magicpath = start + str(self.unvring[0]) + 'System\magic.exe"'
        self.systempath = start + str(self.unvring[0]) + 'System\"'
        self.textpadpath = start + str(self.unvring[0]) + textpadtools
        self.sublimetextpath = start + str(self.unvring[0]) + sublimeprog
        self.cmdprefix = str(self.magicpath + ' ' + self.textpadpath)

    def focus_file_setup(self, view):
        pass
