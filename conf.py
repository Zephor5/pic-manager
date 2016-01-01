#! /usr/bin/python2.7
# coding=utf-8
import cPickle
import os

_Title = 'PicManager'
_Version = '1.0'
_Author = 'Zephor'


class MC(object):
    """docstring for MainConfig"""

    def __init__(self):
        self.confDir = '.' + os.sep + 'conf' + os.sep
        self.iniFile = self.confDir + 'ini.data'
        self.size = (800, 600)
        self.imPath = '.' + os.sep + 'images' + os.sep
        self.welIm = self.imPath + 'welcome.png'
        self.welT = 500
        self.icon = self.imPath + 'icon.ico'
        self.listFolder = ['']
        self.sashPos = 0
        self.maxSashPos = 240
        self.imTypes = ['jpg', 'jpeg', 'png', 'bmp', 'gif']  # 均小写
        self.imConSize = (180, 190)
        self.waitingFrameSize = (180, 80)
        self.waitingIm = self.imPath + 'waiting.gif'

        self.init_conf()

        if self.check_ini():
            self.load()

    def check_ini(self):
        if os.path.isdir(self.confDir):
            if os.path.isfile(self.iniFile):
                return True
            else:
                try:
                    ini = open(self.iniFile, 'w')
                    cPickle.dump(self.pack(), ini)
                    ini.close()
                    return True
                except Exception:
                    raise
        else:
            try:
                os.mkdir(self.confDir)
                self.check_ini()
            except Exception:
                raise RuntimeError("Can't make confdir!")

    def init_conf(self):
        self.defaultPath = self.listFolder[-1] if self.listFolder else ''

    def pack(self):
        self.customData = {
            'size': self.size,
            'welT': self.welT,
            'listFolder': self.listFolder,
            'defaultPath': self.defaultPath,
            'sashPos': self.sashPos
        }
        return self.customData

    def unpack(self):
        cD = self.customData
        self.size = cD['size']
        self.welT = cD['welT']
        self.listFolder = cD['listFolder']
        self.defaultPath = cD['defaultPath']
        self.sashPos = cD['sashPos']

    def load(self):
        if os.path.getsize(self.iniFile) > 0:
            ini = open(self.iniFile)
            self.customData = cPickle.load(ini)
            self.unpack()
            ini.close()
            return True
        else:
            os.remove(self.iniFile)
            return False

    def save(self):
        try:
            ini = open(self.iniFile, 'w')
            cPickle.dump(self.pack(), ini)
            ini.close()
            return True
        except Exception, e:
            raise e

    def addListFolder(self, folders=['']):
        c = self.listFolder[:]
        for n in xrange(0, len(folders)):
            if not folders[n]:
                continue
            for fl in folders:
                if fl == '' or folders[n] == fl:
                    continue
                if fl in folders[n]:
                    folders[n] = ''
        while '' in folders:
            folders.remove('')
        if not c or c == ['']:
            self.listFolder = folders
        else:
            for x in folders:
                canAdd = 0
                if x not in c:
                    for l in c:
                        if x in l and l not in x:
                            self.listFolder.remove(l)
                            canAdd = 1
                        elif x not in l and l not in x:
                            canAdd = 1
                if canAdd:
                    self.listFolder.append(x)
        self.init_conf()

    def delListFolder(self, folders=['']):
        if folders and folders != ['']:
            for f in folders:
                if f in self.listFolder:
                    self.listFolder.remove(f)

    def setSize(self, size=(800, 600)):
        self.size = size

    def setWelT(self, welT=3000):
        self.welT = welT

    def setSashPos(self, sashPos=0):
        self.sashPos = sashPos


class UI(object):
    """docstring for conf.UI"""

    def __init__(self):
        pass
