# written by Michael Mumford
import os
from os import path
import sublime_plugin
import subprocess

from focusbase import FocusFile


class FocusTransFolderCommand(sublime_plugin.TextCommand):

    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)

    def run(self, edit):
        folderpath = os.path.dirname(self.view.file_name())
        filelist = [x for x in os.listdir(folderpath)
                    if path.isfile(folderpath + os.sep + x)]
        for y in filelist:
            filepath = folderpath + "\\" + y
            self.translateone(filepath)

    def translateone(self, edit):
        cmd = str(self.cmdprefix + " TRANSLATE " + edit)
        subprocess.Popen(cmd)
