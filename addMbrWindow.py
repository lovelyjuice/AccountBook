from PyQt5.QtWidgets import QDialog

from gui.addMbrDialog import Ui_Dialog


class addMbrWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(addMbrWindow, self).__init__(parent)
        self.setupUi(self)

    def getResult(self):
        return self.nameEdit.text(), self.infoEdit.text()
