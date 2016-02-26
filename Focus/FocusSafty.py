# written by Michael Mumford
# import sublime
import sublime_plugin
# import subprocess

from focusbase import FocusFile
from FocusFormat import FormatCommand
from FocusTranslate import TranslateCommand


class SaftyCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)

    def run(self, edit):
        self.edit = edit
        FormatCommand.run(self, edit)
        TranslateCommand.run(self, edit)
