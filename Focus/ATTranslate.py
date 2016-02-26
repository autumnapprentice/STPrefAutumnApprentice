# written by Michael Mumford
# import sublime
import sublime_plugin
import subprocess

from focusbase import FocusFile


class ATTranslateCommand(sublime_plugin.TextCommand):

    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)
        self.params = self.systempath + "magic.mas"

    def run(self, edit):
        file = str('"' + self.view.file_name() + '"')
        cmd = str(self.magicpath + ' ' + self.params + file)
        subprocess.call(cmd, shell=False)
