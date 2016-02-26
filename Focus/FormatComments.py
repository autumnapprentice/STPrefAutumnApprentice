# written by Michael Mumford
# import re
# import sublime
import sublime_plugin
# import subprocess

from focusbase import FocusFile


class FocusFormatCommentsCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)

    def run(self, edit):
        print(self.unvring)
