# written by Michael Mumford
# import sublime
import sublime_plugin
import subprocess
import re


class CsNprTranslateCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

        self.work = re.split('Dpms', str(self.view.file_name()))
        self.workspacepath = str(self.work[0])[:-1]

        start = '"C:\\Program Files (x86)\\MEDITECH'
        self.unvtranspath = start + '\\UniversalTranslate\\'
        # tags = '"-unv MTUNV -ring S6.1N -app HR"'
        # parse from filepath the project : D6.15N HR for example
        # proj = '"C:\\Users\\Michael\\workspace\\D6.15N HR"'
        settingpath = '\\.settings\\com.meditech.ide.npr.prefs'
        self.settings = self.workspacepath + settingpath

    def run(self, view):
        nprsettings = open(self.settings)
        line = nprsettings.readline()
        while line:
            name = re.split('npr_project_', line)
            get = name.pop()
            get = get.strip('\n')
            if get[:5] == "ring=":
                self.ring = get[5:]
            elif get[:4] == "unv=":
                self.unv = get[4:]
            line = nprsettings.readline()
        nprsettings.close()

        filename = ' -file ' + '"' + self.view.file_name() + '"'
        proj = ' -proj ' + '"' + self.workspacepath + '"'
        unv = ' -unv ' + self.unv
        ring = ' -ring ' + self.ring
        tag = unv + ring + proj + ' -obj NO'
        magicpath = self.unvtranspath + 'Magic.exe"'
        toolspath = self.unvtranspath + 'DispatchTranslate.mps"'
        cmdprefix = magicpath + ' ' + toolspath + ' -tool Xlate'
        cmd = cmdprefix + filename + tag
        print(cmd)
        subprocess.call(cmd, shell=False)
        "end"
