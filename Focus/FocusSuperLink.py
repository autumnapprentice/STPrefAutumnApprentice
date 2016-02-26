# written by Michael Mumford
# import sublime
import sublime_plugin
import subprocess

from focusbase import FocusFile


class SuperLinkCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        FocusFile.__init__(self, view)

    def run(self, edit):
        line, col = self.view.rowcol(self.view.sel()[0].begin())
        line = str(line + 1)
        col = str(col + 1)
        filename = str('"' + self.view.file_name() + '"')
        sel = self.view.substr(self.view.sel()[0])
        pgmsourcepath = '\\\FOCDEV3\E1\MTUNV.Universe\S61F.Ring\PgmSource'
        cmd = self.cmdprefix + " RUNRINGTOOL " + '"' + pgmsourcepath + '\Test\TestHawSources.TextPad.ViewSource.P.focus" ' + filename + ' ' + line + ' ' + col
        subprocess.call(cmd, shell=False)
