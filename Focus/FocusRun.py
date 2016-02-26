# written by Michael Mumford
import sublime_plugin
import subprocess

from focusbase import FocusFile


class FocusRunCommand(sublime_plugin.TextCommand):

    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)
        self.startup = str(self.magicpath + ' ' + self.textpadpath + " RUN ")

    def run(self, edit):
        cmd = str(self.startup + ' ' + '"' + self.view.file_name() + '"')
        print(cmd)
        subprocess.call(cmd, shell=False)
