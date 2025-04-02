from gui.qt.common import *
import cv2


# Page example using setGeometry to position objects
#! *** press 'esc' to exit after running ***
class PAGE_EX1(NFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName('page_ex1')
        
        #~ text labels
        self.label1 = QLabel(self, text='label1')
        self.label1.setGeometry(QRect(0, 0, 150, 150))
        self.label1.setStyleSheet("""
            color: white;
            font-size: 28px;
            background-color: transparent;
        """)

        self.label2 = QLabel(self, text='label2')
        self.label2.setGeometry(QRect(200, 0, 150, 100))
        self.label2.setStyleSheet("""
            color: red;
            font-size: 22px;
            background-color: blue;
        """)

        self.label3 = QLabel(self, text='label3')
        self.label3.setGeometry(QRect(400, 0, 200, 100))
        self.label3.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.label3.setStyleSheet("""
            color: blue;
            font-size: 18px;
            background-color: yellow;
        """)

        self.label4 = QLabel(self, objectName='label4', text='label4') # objectName='label4' links it to the style defined in assets/style.css > #page_ex1 > #label4
        self.label4.setGeometry(QRect(600, 0, 150, 150))

        #~ Push buttons
        self.btn1 = QPushButton(self, text='btn1')
        self.btn1.setGeometry(QRect(0, 200, 100, 100))
        self.btn1.clicked.connect(self.__on_btn1)
        self.btn1.setStyleSheet("""
            QPushButton {
                background-color: rgb(68,68,68);
                color: white;
                font-size: 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(102,102,102);
            }
            QPushButton:pressed {
                background-color: rgb(42,130,218);
            }
        """)

        self.btn2_counter = 0
        self.btn2 = QPushButton(self, text=f'btn2: {self.btn2_counter}')
        self.btn2.setGeometry(QRect(150, 200, 100, 100))
        self.btn2.clicked.connect(self.__on_btn2)
        self.btn2.setStyleSheet("""
            QPushButton {
                background-color: rgb(68,68,0);
                color: white;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: rgb(102,102,0);
            }
            QPushButton:pressed {
                background-color: rgb(42,130,218);
            }
        """)

        self.btn3 = QPushButton(self, objectName='my_btn', text='btn3') # objectName='mybtn' links it to the style defined in assets/style.css > #page_ex1 > #mybtn
        self.btn3.setGeometry(QRect(300, 200, 100, 100))
        self.btn3.clicked.connect(lambda: print('button 3 was clicked!'))

        self.btn4 = QPushButton(self, objectName='my_btn', text='btn4') # objectName='mybtn' links it to the style defined in assets/style.css > #page_ex1 > #mybtn
        self.btn4.setGeometry(QRect(450, 200, 100, 100))
        self.btn4.clicked.connect(lambda: print('button 4 was clicked!'))

        #~ Image
        img_user = cv2.imread(vp.images + 'Logo Eypisa Ovalado.png')
        width = 150
        height = 150
        img_user = cv2.resize(img_user, (width, height), interpolation=cv2.INTER_AREA)
        _height, _width, _ = img_user.shape
        bytes_per_line = 3 * _width
        img_user = QImage(img_user.data, _width, _height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        self.label_img = QLabel(self)
        self.label_img.setGeometry(QRect(0, 400, width, height))
        self.label_img.setPixmap(QPixmap.fromImage(img_user))

        #~ Push buttons to trigger the global signals defined in gui/qt/common.py (only effective when running main.py)        
        self.btn_previous_page = QPushButton(self, objectName='simple_btn', text='previous page')
        self.btn_previous_page.setGeometry(300, 400, 250, 100)
        self.btn_previous_page.clicked.connect(gsig.previous_page.emit)

        self.btn_next_page = QPushButton(self, objectName='simple_btn', text='next page')
        self.btn_next_page.setGeometry(600, 400, 250, 100)
        self.btn_next_page.clicked.connect(gsig.next_page.emit)


    def __on_btn1(self):
        print(f'button 1 was clicked!')

    def __on_btn2(self):
        self.btn2_counter += 1
        print(f'button 2 was clicked! Counter incremented to {self.btn2_counter}')
        self.btn2.setText(f'btn2: {self.btn2_counter}')

    #? PyQt Events
    def showEvent(self, a0):
        return super().enterEvent(a0)

    def enterEvent(self, a0):
        return super().enterEvent(a0)

    def hideEvent(self, a0) -> None: 
        return super().hideEvent(a0)



if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    with open('assets/style.css', 'r') as f:
        app.setStyleSheet(f.read())

    gui = QLabel()
    page = PAGE_EX1(gui)
    if os.name == 'nt':
        page.setGeometry(QRect(0, 0,int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
        gui.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        gui.show()
    else: gui.showFullScreen()
    
    page.show()
    sys.exit(app.exec_())
