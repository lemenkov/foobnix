'''
Created on Feb 27, 2010

@author: ivan
'''
import pickle
import LOG
import os


class Singleton(type):
    def __call__(self, *args, **kw):
        if self.instance is None:
            self.instance = super(Singleton, self).__call__(*args, **kw)
        return self.instance
    
    def __init__(self, name, bases, dict):
        super(Singleton, self).__init__(name, bases, dict)
        self.instance = None

class FConfiguration:
    __metaclass__ = Singleton
    
    def __init__(self):
        self.mediaLibraryPath = "/home/ivan/Music"
        self.supportTypes = [".mp3", ".ogg", ".ape", "flac"]
        self.isRandom = False
        self.isRepeat = True
        self.isPlayOnStart = True
        self.savedPlayList = []
        self.savedSongIndex = 0
        self.volumeValue = 0
        self.vpanelPostition = 300
        self.hpanelPostition = 300
        
        
        instance = self._loadCfgFromFile()
        if instance:
            try:
                self.mediaLibraryPath = instance.mediaLibraryPath
                self.isRandom = instance.isRandom
                self.isRepeat = instance.isRepeat
                self.isPlayOnStart = instance.isPlayOnStart
                self.savedPlayList = instance.savedPlayList
                self.savedSongIndex = instance.savedSongIndex
                self.volumeValue = instance.volumeValue
                self.vpanelPostition = instance.vpanelPostition
                self.hpanelPostition = instance.hpanelPostition
            except AttributeError:
                LOG.debug("Configuraton attributes are changed")                
                os.remove("foobnix_conf.pkl")
            #self.currentSong = None
            #self.currentSongIndex = None
            #self.currentPlayListSongs = None

    def save(self):
        FConfiguration()._saveCfgToFile()               
        
    def _saveCfgToFile(self):
        #conf = FConfiguration()
        save_file = file("foobnix_conf.pkl", 'w')
        pickle.dump(self, save_file)
        save_file.close()
        LOG.debug("Save configuration")
            
    def _loadCfgFromFile(self): 
        try:       
            load_file = file("foobnix_conf.pkl", "r")
        except IOError:
            LOG.debug("file not exists")
            return None
        try:        
            conf = pickle.load(load_file)
        except AttributeError:
            LOG.debug("Error loading configuration")
            conf = FConfiguration()
            return conf
        
        load_file.close()    
        
        LOG.debug("Load configuration")
        return conf
