# written by Michael Mumford
import sublime_plugin
import subprocess

from focusbase import FocusFile


class FormatCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)

    def run(self, edit):
        filename = '"' + self.view.file_name() + '"'
        cmd = str(self.cmdprefix + " FORMAT " + filename)
        subprocess.Popen(cmd)
