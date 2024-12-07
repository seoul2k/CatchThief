import sys,math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import QTimer, Qt,pyqtSignal

class LoadingCircle(QWidget):
    closed_signal = pyqtSignal()  # 定义一个信号用于通知主窗口关闭
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setFixedSize(300, 450)
        self.text = "Loading."
        self.setWindowTitle("Loading.")
        self.initUI()
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(100)
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.update_text)
        self.timer1.start(1000)
        self.closetimer = QTimer(self)
        self.closetimer.timeout.connect(self.closewindow)
        self.closetimer.start(5000)
        
    def initUI(self):
        layout = QVBoxLayout(self)
        self.loading_label = QLabel(self.text, self)
        font = QFont()
        font.setPointSize(16)
        self.loading_label.setFont(font)
        self.loading_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.loading_label)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        radius = 30
        center_x, center_y = self.width() // 2, self.height() // 2 - 40
        num_points = 8
        
        for i in range(num_points):
            angle_rad = (i * 360 / num_points + self.angle) * 3.14159 / 180
            x = int(center_x + radius * 0.7 * math.cos(angle_rad)) - 5
            y = int(center_y + radius * 0.7 * math.sin(angle_rad)) - 5
            
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(QColor(0, 128, 255)))
            painter.drawEllipse(x, y, 10, 10)

    def update_angle(self):
        self.angle += 5
        self.loading_label.setText(self.text)
        if self.angle >= 360:
            self.angle -= 360
        self.update()


    def update_text(self):
        self.text += "."
        if self.text == "Loading....":
            self.text = "Loading."
        self.setWindowTitle(self.text)
        self.update()
    
    def closewindow(self):
        self.closetimer.stop()
        self.timer.stop()
        self.timer1.stop()
        self.close()
        self.closed_signal.emit()
if __name__ == '__main__':
    import math
    app = QApplication(sys.argv)
    window = LoadingCircle()
    window.resize(300, 450)
    window.show()
    sys.exit(app.exec_())



