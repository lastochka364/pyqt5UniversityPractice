import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import Pizza



class MainUI(QtWidgets.QMainWindow, Pizza.Pizzeria):
    def __init__(self):
        super().__init__()
        self.mUi = uic.loadUi('Main.ui')
        self.pizzaInfo()
        self.pizzaPhoto()

        self.mUi.bMakeOrder.clicked.connect(self.makeOrder)
        self.mUi.aMakeOrder.triggered.connect(self.makeOrder)

        self.mUi.setWindowTitle("Pizzeria")
        self.mUi.setWindowIcon(QtGui.QIcon("img\\icons\\application-blue.png"))
        self.mUi.aMakeOrder.setIcon(QtGui.QIcon("img\\icons\\application--pencil.png"))

        self.orderWin = None

        self.mUi.show()

    def pizzaInfo(self):
        txt = Pizza.Pizzeria.__str__(self)
        self.mUi.PizzaInfo.setText(txt)

    def pizzaPhoto(self):
        ph = QtGui.QPixmap(self.photo_of_the_day)
        self.mUi.PizzaPhoto.setPixmap(ph)

    def makeOrder(self):
            if self.orderWin is None:
                self.orderWin = OrderUI()
            else:
                self.orderWin.close()
                self.orderWin = None


class OrderUI(QtWidgets.QWidget, Pizza.Order):
    def __init__(self):
        super().__init__()
        self.oUi = uic.loadUi('Order.ui')
        self.dialogs()
        self.icons()

        self.ord = Pizza.Order(self.c)

        self.oUi.AddMushrooms.clicked.connect(self.pMushroom_ingr)
        self.oUi.AddPineapple.clicked.connect(self.pPineapple_ingr)
        self.oUi.AddOlives.clicked.connect(self.pOlives_ingr)
        self.oUi.AddCorn.clicked.connect(self.pCorn_ingr)
        self.oUi.AddMozarella.clicked.connect(self.pMozarella_ingr)
        self.oUi.AddSuluguni.clicked.connect(self.pSuluguni_ingr)
        self.oUi.AddTofu.clicked.connect(self.pTofu_ingr)
        self.oUi.AddParmesan.clicked.connect(self.pParmesan_ingr)

        self.oUi.RmMushrooms.clicked.connect(self.mMushroom_ingr)
        self.oUi.RmPineapple.clicked.connect(self.mPineapple_ingr)
        self.oUi.RmOlives.clicked.connect(self.mOlives_ingr)
        self.oUi.RmCorn.clicked.connect(self.mCorn_ingr)
        self.oUi.RmMozarella.clicked.connect(self.mMozarella_ingr)
        self.oUi.RmSuluguni.clicked.connect(self.mSuluguni_ingr)
        self.oUi.RmTofu.clicked.connect(self.mTofu_ingr)
        self.oUi.RmParmesan.clicked.connect(self.mParmesan_ingr)

        self.oUi.bAddIngr.clicked.connect(self.orderInfo_)
        self.oUi.bSave.clicked.connect(self.save)

        self.oUi.setWindowTitle("Changing order")
        self.oUi.setWindowIcon(QtGui.QIcon("img\\icons\\information.png"))

        self.oUi.show()

    def dialogs(self):
        self.fname_, self.lname_, self.phone_ = '', '', ''

        self.qidFname = QtWidgets.QInputDialog
        self.qidLname = QtWidgets.QInputDialog
        self.qidPhone = QtWidgets.QInputDialog

        fname, ok = self.qidFname().getText(self, 'First Name', "Enter your first name:")
        if ok == True:
            self.fname_ = fname
            while self.fname_ == '':
                fname, ok = self.qidFname().getText(self, 'First Name', f"You have not entered anything.\n" \
                    f"Please, enter your first name:")
                self.fname_ = fname
                if ok == False:
                    break
        else:
            self.qidFname().done(0)
        
        lname, ok = self.qidLname.getText(self, 'Last Name', "Enter your last name:")
        if ok == True:
            self.lname_ = lname
            while self.lname_ == '':
                lname, ok = self.qidLname.getText(self, 'Last Name', f"You have not entered anything.\n" \
                    f"Please, enter your last name:")
                self.lname_ = lname
                if ok == False:
                    break
        else:
            self.qidLname().done(0)
        
        phone, ok = self.qidPhone.getText(self, 'Phone', "Enter your phone:")
        if ok == True:
            self.phone_ = phone
            while self.phone_ == '':
                phone, ok = self.qidPhone.getText(self, 'First Name', f"You have not entered anything.\n" \
                    f"Please, enter your phone number:")
                self.phone_ = phone
                if ok == False:
                    break
        else:
            self.qidPhone().done(0)

        self.c = Pizza.Customer(self.fname_, self.lname_, self.phone_)

    def icons(self):
        self.plus_lst = [self.oUi.AddMushrooms, self.oUi.AddPineapple, self.oUi.AddOlives,
        self.oUi.AddCorn, self.oUi.AddMozarella, self.oUi.AddSuluguni, 
        self.oUi.AddTofu, self.oUi.AddParmesan]
        self.minus_lst = [self.oUi.RmMushrooms, self.oUi.RmPineapple, self.oUi.RmOlives,
        self.oUi.RmCorn, self.oUi.RmMozarella, self.oUi.RmSuluguni, 
        self.oUi.RmTofu, self.oUi.RmParmesan]

        for button in self.plus_lst:
            button.setIcon(QtGui.QIcon('img\\icons\\plus.png'))

        for button in self.minus_lst:
            button.setIcon(QtGui.QIcon('img\\icons\\minus.png'))


    def pMushroom_ingr(self):
        self.ord.add_ingredients("Mushrooms")
        self.oUi.LMush.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def pPineapple_ingr(self):
        self.ord.add_ingredients("Pineapple")
        self.oUi.LPine.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def pOlives_ingr(self):
        self.ord.add_ingredients("Olives")
        self.oUi.LOlives.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def pCorn_ingr(self):
        self.ord.add_ingredients("Corn")
        self.oUi.LCorn.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def pMozarella_ingr(self):
        self.ord.add_ingredients("Mozarella")
        self.oUi.LMozza.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def pSuluguni_ingr(self):
        self.ord.add_ingredients("Suluguni")
        self.oUi.LSulu.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def pTofu_ingr(self):
        self.ord.add_ingredients("Tofu")
        self.oUi.LTofu.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def pParmesan_ingr(self):
        self.ord.add_ingredients("Parmesan")
        self.oUi.LParmes.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))
        

    def mMushroom_ingr(self):
        self.ord.remove_ingredients("Mushrooms")
        self.oUi.LMush.clear()
        if "Mushrooms" in self.ord.added():
            self.oUi.LMush.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))
        
    def mPineapple_ingr(self):
        self.ord.remove_ingredients("Pineapple")
        self.oUi.LPine.clear()
        if "Pineapple" in self.ord.added():
            self.oUi.LPine.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def mOlives_ingr(self):
        self.ord.remove_ingredients("Olives")
        self.oUi.LOlives.clear()
        if "Olives" in self.ord.added():
            self.oUi.LOlives.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def mCorn_ingr(self):
        self.ord.remove_ingredients("Corn")
        self.oUi.LCorn.clear()
        if "Corn" in self.ord.added():
            self.oUi.LCorn.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def mMozarella_ingr(self):
        self.ord.remove_ingredients("Mozarella")
        self.oUi.LMozza.clear()
        if "Mozarella" in self.ord.added():
            self.oUi.LMozza.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def mSuluguni_ingr(self):
        self.ord.remove_ingredients("Suluguni")
        self.oUi.LSulu.clear()
        if "Suluguni" in self.ord.added():
            self.oUi.LSulu.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def mTofu_ingr(self):
        self.ord.remove_ingredients("Tofu")
        self.oUi.LTofu.clear()
        if "Tofu" in self.ord.added():
            self.oUi.LTofu.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def mParmesan_ingr(self):
        self.ord.remove_ingredients("Parmesan")
        self.oUi.LParmes.clear()
        if "Parmesan" in self.ord.added():
            self.oUi.LParmes.setPixmap(QtGui.QPixmap('img\\icons\\plus-circle.png'))

    def orderInfo_(self):
        self.oUi.orderInfo.setText(self.ord.make_purchase())

    def save(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', '/', 'Plain Text (*.txt)')
        if fileName[0]:
            f = open(fileName[0], 'w')
            with f:
                f.write(self.oUi.orderInfo.toPlainText())
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainUI()
    sys.exit(app.exec())