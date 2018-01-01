from model import *


class Function():
    def __init__(self) -> None:
        self.db = SqliteDatabase('database.db')
        self.db.connect()
        try:
            self.db.create_tables([Users, Types, Charges])
        except:
            pass

    def getChargeList(self, startDate, endDate, *args):
        a = {'username_id': args[0], 'type_id': args[1]}
        b = []
        for key in a:
            if a[key] == '*':
                b.append(key)
        for key in b:
            del a[key]
        endString = ''
        for key in a:
            endString += (' and ' + key + ' =? ')
        b = tuple(filter(lambda s: s != '*', args))
        sql = 'SELECT * FROM charges WHERE date>=? AND date<=?{0}'.format(endString)
        param = (startDate, endDate) + b
        self.charges = Users.raw(sql, *param)
        return self.charges

    def getTypeList(self):
        sql = 'SELECT * FROM types '
        self.types = Types.raw(sql)
        return self.types

    def getMbrList(self):
        sql = 'SELECT * FROM users'
        self.members = Users.raw(sql)
        return self.members

    def delType(self, typeText):
        delCharges = Charges.select().where(Charges.type == typeText)
        for charge in delCharges:
            charge.delete_instance()
        Types.get(type=typeText).delete_instance()

    def addType(self, typeText):
        Types(type=typeText).save()

    def addMbr(self, name, info):
        Users(name=name, info=info).save()

    def modifyMbr(self, id, name, info):
        user = Users.get(id=id)
        user.name = name
        user.info = info
        user.save()

    def delMbr(self, id):
        # 同时删除该成员的所有账单
        delCharges = Charges.select().where(Charges.username == Users.get(id=id).name)
        for charge in delCharges:
            charge.delete_instance()
        Users.get(id=id).delete_instance()

    def modifyCharge(self, id, member, type, amount, date, info):
        charge = Charges.get(id=id)
        charge.member = member
        charge.type = type
        charge.amount = amount
        charge.date = date
        charge.info = info
        charge.save()

    def addCharge(self, member, type, amount, date, info):
        Charges(username=member, type=type, amount=amount, date=date, info=info).save()

    def delCharge(self, id):
        Charges.get(id=id).delete_instance()


if __name__ == '__main__':
    f = Function()
    auser = Users(name='myname', info='myinfo')
    # auser.save()
    result = Users.get()
    print(result.name, result.info)
    for i in result:
        print(i.name, i.info)
