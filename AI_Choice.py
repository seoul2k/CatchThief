from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox
from AI_Choice_ui import Ui_AI_Choice
from PyQt5.QtCore import Qt,pyqtSignal
from AIPolice import GraphWidget_AIPOLICE
from AIThief import GraphWidget_AITHEIF
from Loading import LoadingCircle

class AI_Choice(QWidget, Ui_AI_Choice):
    closed_signal = pyqtSignal()  # 定义一个信号用于通知主窗口关闭
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("选择角色")
        self.Police.clicked.connect(self.Police_clicked)
        self.Thief.clicked.connect(self.Thief_clicked)
        self.back.clicked.connect(self.show_main_window)
        self.police = None  # 初始化游戏窗口为None
        self.thief = None  # 初始化游戏窗口为None
        self.setWindowFlags(Qt.Window)  # 确保这是一个独立窗口

    def show_police_window(self):
        if self.thief is None:
            self.thief = GraphWidget_AITHEIF(parent=self)
            self.thief.closed_signal.connect(self.show_main_window)
        self.thief.setWindowFlags(Qt.Window)
        self.thief.show()
        
    def Police_clicked(self):
        self.hide()
        self.loading = LoadingCircle(self)
        self.loading.setWindowFlags(Qt.Window)  # 确保这是一个独立窗口
        self.loading.show()
        self.loading.closed_signal.connect(self.show_police_window)

    def Thief_clicked(self):
        self.hide()
        self.loading = LoadingCircle(self)
        self.loading.setWindowFlags(Qt.Window)  # 确保这是一个独立窗口
        self.loading.show()
        self.loading.closed_signal.connect(self.show_thief_window)
        
    def show_thief_window(self):
        if self.police is None:
            self.police = GraphWidget_AIPOLICE(parent=self)
            self.police.closed_signal.connect(self.show_main_window)
            self.police.setWindowFlags(Qt.Window)
        self.police.show()
    
    def show_main_window(self):
        self.thief = None
        self.police = None
        self.loading = None
        self.hide()
        self.closed_signal.emit()
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = AI_Choice()
    w.show()
    sys.exit(app.exec_())