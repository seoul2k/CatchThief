# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox
import MainWindow as ui
from PyQt5.QtCore import Qt
from SingerPlayer import GraphWidget
from AI_Choice import AI_Choice
from Rule import Ui_Rule
from Loading import LoadingCircle
class MyRule(QDialog,Ui_Rule):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
class MyWidget(QWidget, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.SingerPlayer.clicked.connect(self.SingerPlayer_clicked)
        self.AI.clicked.connect(self.AI_clicked)
        self.RuleButton.clicked.connect(self.show_rule)
        self.singerplayerwindow = None  # 初始化游戏窗口为None
        self.aichoice = None  # 初始化游戏窗口为None
        self.myRule = None
    def show_singerplayer_window(self):
        if self.singerplayerwindow is None:
            self.singerplayerwindow = GraphWidget(parent=self)
            self.singerplayerwindow.closed_signal.connect(self.show_main_window)
        self.singerplayerwindow.setWindowFlags(Qt.Window)
        self.singerplayerwindow.show()
    def SingerPlayer_clicked(self):
        self.loading = LoadingCircle(self)
        self.loading.setWindowFlags(Qt.Window)  # 确保这是一个独立窗口
        self.loading.show()
        self.loading.closed_signal.connect(self.show_singerplayer_window)
        self.hide()

    def AI_clicked(self):
        if self.aichoice==None:
            self.aichoice = AI_Choice(self)
            self.aichoice.closed_signal.connect(self.show_main_window)
        self.aichoice.show()
        self.hide()

    def show_rule(self):    
        if self.myRule == None:
            self.myRule = MyRule()
        self.myRule.show()
        
    def show_main_window(self):
        self.singerplayerwindow = None  # 重置游戏窗口为None
        self.aichoice = None
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
"""if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMessageBox

    app = QApplication(sys.argv)
    w = GraphWidget_AIPOLICE()
    w.show()
    sys.exit(app.exec_())"""