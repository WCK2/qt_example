from gui.qt.nframe import *
from gui.qt.nstackedwidget import NStackedWidget
from gui.workers.ntimer import NTimer
from utils.config import vp, settings



signal.signal(signal.SIGINT, signal.SIG_DFL)    
qapp = QApplication(sys.argv)

class GlobalSignals(QObject):
    previous_page = pyqtSignal()
    next_page = pyqtSignal()
    reset_signal = pyqtSignal()
    home_signal = pyqtSignal()
    def __new__(cls, *args, **kw):
         if not hasattr(cls, '_instance'):
             orig = super(GlobalSignals, cls)
             cls._instance = orig.__new__(cls, *args, **kw)
         return cls._instance
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


gsig = GlobalSignals()
gsig.previous_page.connect(lambda: print('previous page signal emitted'))
gsig.next_page.connect(lambda: print('next page signal emitted'))




if __name__=="__main__":
    gsig.home_signal.connect(lambda:print("hello"))
    gsig.home_signal.emit()



