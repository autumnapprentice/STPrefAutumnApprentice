# written by Michael Mumford
import os
import os.path
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))
# https://sites.google.com/a/meditech.com/versioncontrol/npr/npr-eclipse-tools-instructions-64bit-os-x86
# ObjectEE, MultiEE, FE, ProcEE, Run, Lookup, App, DDEE, MenuEE,
# DRWarnEE, DRSegEe, FormalCodeDoc,
# need separate functions for: sort, delete object code, mergetool
#  example file path :
# C:\ProgramData\MEDITECH\MTUNV.Universe\S6.1N.Ring\Michael\PgmSource\HR\IAS.REGION\ee.driver\ee.driver.npr


class CsNprFile():

    def __init__(self, view):
        self.view = view
        # head is the fullpath to the file.
        head = str(self.view.file_name())
        # work and temp are the working values
        # grab after the word MEDITECH then strip off the leading \
        self.work = re.split('MEDITECH', head)

    def csnpr_file_setup(self, view):
        pass
