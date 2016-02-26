# written by Michael Mumford
import sublime_plugin
import subprocess

from focusbase import FocusFile


class TranslateCommand(sublime_plugin.TextCommand):

    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)

    def run(self, edit):
        filepath = '"' + self.view.file_name() + '"'
        cmd = str(self.cmdprefix + " TRANSLATE " + filepath)
        subprocess.Popen(cmd)
