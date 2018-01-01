import re
import sys

from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QTableWidgetItem, QMessageBox

import gui.MainWindow_UI as MainWindow_UI
from addChargeDialog import addChargeDialog
from addMbrWindow import addMbrWindow
from function import Function


class MainWindow(QWidget, MainWindow_UI.Ui_Form):
    SymbolAll = '*'

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.function = Function()
        self.endDateEdt.setDate(QDate.currentDate())
        self.initSlots()
        self.chargeTable.setHorizontalHeaderLabels(['id', '成员', '类型', '金额（元）', '日期', '备注'])
        self.memberTable.setHorizontalHeaderLabels(['id', '姓名', '备注'])
        self.memberTable.setColumnHidden(0, True)
        self.chargeTable.setColumnHidden(0, True)
        self.updateMemberUI()
        self.updateTypeUI()
        self.updateChargeTable()

    def initSlots(self):
        self.filtrateBtn.clicked.connect(self.updateChargeTable)
        self.revertBtn.clicked.connect(self.revertCondition)
        # TypeOperation
        self.delTypeBtn.clicked.connect(self.delType)
        self.addTypeBtn.clicked.connect(self.addType)
        # Member
        self.addMbrBtn.clicked.connect(self.addMbr)
        self.delMbrBtn.clicked.connect(self.delMbr)
        self.memberTable.itemChanged.connect(self.modifyMbr)
        # Charge
        self.chargeTable.itemDoubleClicked.connect(self.storeCurrentValue)
        self.chargeTable.itemChanged.connect(self.modifyCharge)
        self.chargeBtn.clicked.connect(self.addCharge)
        self.delChargeBtn.clicked.connect(self.delCharge)

    def updateChargeTable(self):
        self.chargeTable.itemChanged.disconnect(self.modifyCharge)
        endDate = self.endDateEdt.date().toString('yyyy-MM-dd')
        startDate = self.startDateEdt.date().toString('yyyy-MM-dd')
        member = self.mbrCBox.currentText()
        type = self.typeCBox.currentText()
        charges = self.function.getChargeList(startDate, endDate, member, type)
        rowCount = 0
        for charge in charges:
            rowCount += 1
        self.chargeTable.setRowCount(rowCount)
        rowCount = 0
        for charge in charges:
            id = QTableWidgetItem(str(charge.id))
            type = QTableWidgetItem(charge.type_id)
            amount = QTableWidgetItem(str(charge.amount))
            member = QTableWidgetItem(charge.username_id)
            info = QTableWidgetItem(charge.info)
            date = QTableWidgetItem(charge.date)

            id.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            type.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            amount.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            member.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            info.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            date.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            # type.setTextAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
            a = map(lambda x: x.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter),
                    (id, type, amount, member, info, date))
            self.chargeTable.setItem(rowCount, 0, id)
            self.chargeTable.setItem(rowCount, 1, member)
            self.chargeTable.setItem(rowCount, 2, type)
            self.chargeTable.setItem(rowCount, 3, amount)
            self.chargeTable.setItem(rowCount, 4, date)
            self.chargeTable.setItem(rowCount, 5, info)
            print(charge.amount, charge.info, charge.type_id)
            rowCount += 1
        # self.chargeTable.resizeColumnsToContents()
        self.chargeTable.resizeColumnToContents(5)
        self.chargeTable.itemChanged.connect(self.modifyCharge)

    def updateMemberUI(self):
        # 这一句是为了防止更新UI的时候出发itemChange信号
        self.memberTable.itemChanged.disconnect(self.modifyMbr)
        members = self.function.getMbrList()
        self.mbrCBox.clear()
        self.mbrCBox.addItem(self.SymbolAll)
        for member in members:
            self.mbrCBox.addItem(member.name)
        # todo 调整cbox的大小
        i = 0
        for member in members:
            i += 1
        self.memberTable.setRowCount(i)
        i = 0
        for member in members:
            id = QTableWidgetItem(str(member.id))
            name = QTableWidgetItem(member.name)
            info = QTableWidgetItem(member.info)
            name.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            info.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.memberTable.setItem(i, 0, id)
            self.memberTable.setItem(i, 1, name)
            self.memberTable.setItem(i, 2, info)
            i += 1
        self.memberTable.resizeColumnToContents(1)
        # 重新连接信号和槽函数
        self.memberTable.itemChanged.connect(self.modifyMbr)

    def updateTypeUI(self):
        self.typeList.clear()
        types = self.function.getTypeList()
        self.typeCBox.clear()
        self.typeCBox.addItem(self.SymbolAll)
        for type in types:
            self.typeCBox.addItem(type.type)
            self.typeList.addItem(type.type)
        # todo 调整cbox的大小

    # 类型操作
    def delType(self):
        if self.typeList.currentRow() == -1:
            return
        self.function.delType(self.typeList.currentItem().text())
        self.updateTypeUI()
        self.updateChargeTable()

    def addType(self):
        text, ok = QInputDialog.getText(self, "添加类型", "输入类型")
        if ok:
            self.function.addType(text)
        self.updateTypeUI()

    # 成员操作
    def addMbr(self):
        dialog = addMbrWindow(self)
        result = dialog.exec()
        if result:
            self.function.addMbr(*dialog.getResult())
            self.updateMemberUI()

    def modifyMbr(self, item):
        if (item.column() == 1):
            QMessageBox.about(self, '警告', '不允许更改用户名！')
            self.updateMemberUI()
            return
        id = int(self.memberTable.item(item.row(), 0).text())
        name = self.memberTable.item(item.row(), 1).text()
        info = self.memberTable.item(item.row(), 2).text()
        self.function.modifyMbr(id, name, info)
        self.updateMemberUI()

    def delMbr(self):
        reply = QMessageBox.question(self, '确认', '删除成员的同时会删除所有该成员的账单，是否继续？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.No:
            return
        id = int(self.memberTable.item(self.memberTable.currentRow(), 0).text())
        self.function.delMbr(id)
        self.updateMemberUI()
        self.updateChargeTable()

    def revertCondition(self):
        self.mbrCBox.setCurrentIndex(0)
        self.typeCBox.setCurrentIndex(0)
        self.startDateEdt.setDate(QDate.fromString('2000-01-01', 'yyyy-MM-dd'))
        self.endDateEdt.setDate(QDate.currentDate())
        self.updateChargeTable()

    def storeCurrentValue(self, item):
        self.preValue = item.text()

    # 账单操作
    def addCharge(self):
        dialog = addChargeDialog(self.function.members, self.function.types, self)
        ok = dialog.exec()
        if ok:
            self.function.addCharge(*dialog.getResult())
            print(dialog.getResult())
            self.updateChargeTable()

    def delCharge(self):
        id = int(self.chargeTable.item(self.chargeTable.currentRow(), 0).text())
        self.function.delCharge(id)
        self.updateChargeTable()

    def modifyCharge(self, item):
        id = int(self.chargeTable.item(item.row(), 0).text())
        member = self.chargeTable.item(item.row(), 1).text()
        type = self.chargeTable.item(item.row(), 2).text()
        amount = float(self.chargeTable.item(item.row(), 3).text())
        date = self.chargeTable.item(item.row(), 4).text()
        info = self.chargeTable.item(item.row(), 5).text()
        if self.checkMbr(member) and self.checkType(type) and self.checkDate(date):
            self.function.modifyCharge(id, member, type, amount, date, info)
        else:
            item.setText(self.preValue)
            QMessageBox.warning(self, '提示', '您输入的数据有误，请确认后再修改', QMessageBox.Yes,
                                QMessageBox.Yes)
            item.setSelected(True)

    def checkMbr(self, string):
        # 下面的代码段要求任何对数据库的members表进行改动的操作必须要重新调用getMbrList()来更新funciton.member，也就是说要重新调用updateMbrUI()
        if string is None:
            return False
        for member in self.function.members:
            if member.name == string:
                return True
        return False

    def checkType(self, string):
        if string is None:
            return False
        # 下面的代码段要求任何对数据库的types表进行改动的操作必须要重新调用getTypeList()来更新funciton.type，也就是说要重新调用updateTypeUI()
        for type in self.function.types:
            if type.type == string:
                return True
        return False

    def checkDate(self, string):
        if string is None:
            return False
        if re.match(r'^[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}', string) is None:
            return False
        if QDate.isValid(*tuple(map(int, string.split('-')))):
            return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())
