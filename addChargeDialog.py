from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog

from gui.addChargeDialog_UI import Ui_Dialog


class addChargeDialog(QDialog, Ui_Dialog):
    def __init__(self, members, types, parent=None):
        super(addChargeDialog, self).__init__(parent)
        self.setupUi(self)
        for member in members:
            self.mbrCBox.addItem(member.name)
        for type in types:
            self.typeCBox.addItem(type.type)
        self.dateEdit.setDate(QDate.currentDate())

    def getResult(self):
        return self.mbrCBox.currentText(), self.typeCBox.currentText(), self.amountSpinBox.value(), self.dateEdit.date().toString(
            'yyyy-MM-dd'), self.infoTextEdit.toPlainText()
