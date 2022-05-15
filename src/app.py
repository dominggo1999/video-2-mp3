from PyQt5.QtWidgets import QPushButton, QMainWindow, QHBoxLayout, QApplication, QWidget, QFileDialog
from PyQt5.QtCore import QProcess
import sys
import random


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.fileDialog = QFileDialog()
        self.fileDialog.setFileMode(QFileDialog.AnyFile)
        self.fileDialog.setNameFilters(["Videos (*.mp4)"])

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)

        view = QHBoxLayout()
        view.addWidget(self.btn)

        w = QWidget()
        w.setLayout(view)

        self.setWindowTitle("Hello World")
        self.setCentralWidget(w)
        self.show()

    def start_process(self):
        print("start")
        if self.fileDialog.exec_():
            filenames = self.fileDialog.selectedFiles()
            print(filenames)
            if(len(filenames)):
                # Change button state to loading
                self.btn.setText("Converting")
                self.btn.setDisabled(True)

                self.p = QProcess()
                self.p.finished.connect(self.process_finished)
                self.p.error.connect(self.process_error)

                r = str(random.randint(0, 100000000))
                self.p.start(
                    "./bin/ffmpeg", ['-i', filenames[0], "D:/results/" + r + ".mp3"])

        pass

    def process_finished(self):
        print("Converting finished")
        self.p = None
        self.btn.setText("Execute")
        self.btn.setDisabled(False)

    def process_error(self):
        print("Something went wrong")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
