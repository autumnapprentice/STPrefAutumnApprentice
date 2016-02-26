# written by Michael Mumford
# Call the Class Dictionary function
import sublime_plugin
import subprocess
from focusbase import FocusFile


class FocusClassDictCommand(sublime_plugin.TextCommand):

    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)
        self.classdict = "FocObj.Mgmt.S.focus"

    def run(self, edit):
        cmd = str(self.startup + self.classdict)
        print(cmd)
        subprocess.call(cmd, shell=False)
