from gui.qt.common import *
from gui.workers.ntimer import NTimer
from utils.helper import generate_random_text


# Page example using Layouts to position objects
#! *** press 'esc' to exit after running ***
class PAGE_EX2(NFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName('page_ex2')
        
        #~ Create a container frame and layout that will vertically align some text labels
        container = QFrame(self)
        container.setGeometry(QRect(0, 0, SCREEN_WIDTH, 200))

        hbox = QVBoxLayout(container)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(10)  # Optional: space between labels

        self.label1 = QLabel(objectName='my_label', text=f'label1: {generate_random_text(10, 50)}')
        self.label2 = QLabel(objectName='my_label', text=f'label2: {generate_random_text(10, 50)}')
        self.label3 = QLabel(objectName='my_label', text=f'label3: {generate_random_text(10, 50)}')
        self.label4 = QLabel(objectName='my_label', text=f'label4: {generate_random_text(10, 50)}')

        hbox.addWidget(self.label1)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.label3)
        hbox.addWidget(self.label4)

        #~ Second container: horizontal button layout
        container2 = QFrame(self)
        container2.setGeometry(QRect(0, 200, SCREEN_WIDTH, 150))  # Placed below the first container

        hbox = QHBoxLayout(container2)
        hbox.setContentsMargins(20, 10, 20, 10)
        hbox.setSpacing(100) # this spacing value will adjust the pushbutton's sizes to fit accordingly into the layout since the pushbuttons do not have any size restrictions set

        self.btn1 = QPushButton(objectName='my_btn', text='Button 1')
        self.btn2 = QPushButton(objectName='my_btn', text='Button 2')
        self.btn3 = QPushButton(objectName='my_btn', text='Button 3')
        self.btn3 = QPushButton(objectName='my_btn', text='Button 3')
        # self.btn3.setFixedWidth(500) # uncomment to see how this affects the other button widths

        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)

        #~ button that will set a value to True and start a timer to reset the value after some time
        self.start_timer = NTimer(2500, lambda: self.__change_led(False), repeat=False)

        self.btn_start = QPushButton(self, objectName='simple_btn', text='start')
        self.btn_start.setGeometry(QRect(50, 400, 150, 100))
        self.btn_start.clicked.connect(lambda: self.__change_led(True))
        self.btn_start.clicked.connect(self.start_timer.start)

        #~ Push buttons to trigger the global signals defined in gui/qt/common.py (only effective when running main.py)        
        self.btn_previous_page = QPushButton(self, objectName='simple_btn', text='previous page')
        self.btn_previous_page.setGeometry(300, 400, 250, 100)
        self.btn_previous_page.clicked.connect(gsig.previous_page.emit)

        self.btn_next_page = QPushButton(self, objectName='simple_btn', text='next page')
        self.btn_next_page.setGeometry(600, 400, 250, 100)
        self.btn_next_page.clicked.connect(gsig.next_page.emit)


    def __change_led(self, b):
        s = 'on' if b else 'off'
        print(f'turning LED {s}')

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
    page = PAGE_EX2(gui)
    if os.name == 'nt':
        page.setGeometry(QRect(0, 0,int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
        gui.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        gui.show()
    else: gui.showFullScreen()
    
    page.show()
    sys.exit(app.exec_())
