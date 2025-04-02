from gui.qt.common import *
import cv2


# Page example with image as background
#! *** press 'esc' to exit after running ***
class PAGE_EX3(NFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName('page_ex3')

        #~ set image as background
        pixmap = QPixmap(vp.images + 'Logo Eypisa Ovalado.png')
        # scaled_pixmap = pixmap.scaled(SCREEN_WIDTH, SCREEN_HEIGHT, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation) # keep image's aspect ratio
        scaled_pixmap = pixmap.scaled(SCREEN_WIDTH, SCREEN_HEIGHT, Qt.IgnoreAspectRatio, Qt.SmoothTransformation) # ignore image aspect ratio

        bg = QLabel(self)
        bg.setPixmap(scaled_pixmap)
        bg.setGeometry(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        bg.lower()

        #~ Push buttons to trigger the global signals defined in gui/qt/common.py (only effective when running main.py)        
        self.btn_previous_page = QPushButton(self, objectName='simple_btn', text='previous page')
        self.btn_previous_page.setGeometry(300, 400, 250, 100)
        self.btn_previous_page.clicked.connect(gsig.previous_page.emit)

        self.btn_next_page = QPushButton(self, objectName='simple_btn', text='next page')
        self.btn_next_page.setGeometry(600, 400, 250, 100)
        self.btn_next_page.clicked.connect(gsig.next_page.emit)


    #? PyQt Events
    def showEvent(self, a0):
        return super().enterEvent(a0)

    def enterEvent(self, a0):
        return super().enterEvent(a0)

    def hideEvent(self, a0) -> None: 
        self.start_timer.kill()
        return super().hideEvent(a0)



if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    with open('assets/style.css', 'r') as f:
        app.setStyleSheet(f.read())

    gui = QLabel()
    page = PAGE_EX3(gui)
    if os.name == 'nt':
        page.setGeometry(QRect(0, 0,int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
        gui.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        gui.show()
    else: gui.showFullScreen()
    
    page.show()
    sys.exit(app.exec_())
