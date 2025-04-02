from gui.qt.common import *
from gui.pages.example1 import PAGE_EX1
from gui.pages.example2 import PAGE_EX2


#! *** press 'q' to exit after running ***
class PAGE_MASTER(NStackedWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_ex1:PAGE_EX1 = self.addWidget(PAGE_EX1())
        self.page_ex2:PAGE_EX2 = self.addWidget(PAGE_EX2())
        # Add more pages here

        gsig.previous_page.connect(self.__previous_page)
        gsig.next_page.connect(self.__next_page)

        self.page_count = self.count()
        self.page = 0
        self.setCurrentIndex(self.page)

    def __previous_page(self):
        self.setCurrentIndex(self.currentIndex()-1)
    def __next_page(self):
        self.setCurrentIndex(self.currentIndex()+1)
    def setCurrentIndex(self, index: int) -> None:
        return super().setCurrentIndex(index)
    def setCurrentWidget(self, w: QWidget) -> None:
        return super().setCurrentWidget(w)
    def hideEvent(self, a0: QHideEvent) -> None:
        return super().hideEvent(a0)
    def showEvent(self, a0: QShowEvent) -> None:
        return super().showEvent(a0)




if __name__ == "__main__":
    with open('assets/style.css', 'r') as f:
        qapp.setStyleSheet(f.read())
    
    app = PAGE_MASTER()
    if os.name == 'nt':
        app.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        app.show()
    else:
        app.showFullScreen()

    sys.exit(qapp.exec_())

