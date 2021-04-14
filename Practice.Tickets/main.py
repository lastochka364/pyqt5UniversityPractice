import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QImage
import json
import Tickets

class MainUI(QtWidgets.QMainWindow, Tickets.Tickets):
    def __init__(self):
        super().__init__()
        self.mUi = uic.loadUi('ui\\Main.ui')
        self.eUi = uic.loadUi('ui\\EventDialog.ui')
        self.bUi = uic.loadUi('ui\\TicketsBuyDialog.ui')

        self.mUi.setWindowTitle('Tickets')
        self.mUi.setWindowIcon(QIcon('icons\\application-blue.png'))
        self.eUi.setWindowTitle('Add Event')
        self.eUi.setWindowIcon(QIcon('icons\\application--pencil.png'))
        self.bUi.setWindowTitle('Buy Ticket')
        self.bUi.setWindowIcon(QIcon('icons\\application--pencil.png'))

        self.aAddEvent = QtWidgets.QAction(QIcon('icons\\application-plus.png'), 'Add event..', self)
        self.aAddEvent.setStatusTip('Add your event...')
        self.aAddEvent.triggered.connect(self.eUi.show)

        self.aGetTickInfo = QtWidgets.QAction(QIcon('icons\\information-button.png'), 'Get ticket info.', self)
        self.aGetTickInfo.setStatusTip('Find out what tickets are available.')
        self.aGetTickInfo.triggered.connect(self.getTickInfo)

        self.aBuyTick = QtWidgets.QAction(QIcon('icons\\shopping-basket--plus.png'), 'Buy ticket(s)..', self)
        self.aBuyTick.setStatusTip('Buy ticket(s).')
        self.aBuyTick.triggered.connect(self.bUi.show)

        self.aConstructTickByNum = QtWidgets.QAction(QIcon('icons\\search.png'), 'Search ticket in base..', self)
        self.aConstructTickByNum.setStatusTip('Check if your ticket is in a base already.')
        self.aConstructTickByNum.triggered.connect(self.constructTickByNum)

        self.aSaveEvents = QtWidgets.QAction(QIcon('icons\\json-file.png'), 'Save .json file.', self)
        self.aSaveEvents.setStatusTip('Save your event to a .json file.')
        self.aSaveEvents.triggered.connect(self.saveJsonEvent)

        self.aOpenEvents = QtWidgets.QAction(QIcon('icons\\app-json-icon.png'), 'Open .json file.', self)
        self.aOpenEvents.setStatusTip('Open an existing .json file for choosing the event you want to open.')
        self.aOpenEvents.triggered.connect(self.openJsonEvent)

        self.mUi.toolBar.setMovable(False)
        self.mUi.toolBar.addAction(self.aAddEvent)
        self.mUi.toolBar.addAction(self.aGetTickInfo)
        self.mUi.toolBar.addAction(self.aBuyTick)
        self.mUi.toolBar.addAction(self.aConstructTickByNum)
        self.mUi.toolBar.addAction(self.aSaveEvents)
        self.mUi.toolBar.addAction(self.aOpenEvents)

        self.eUi.bOk.clicked.connect(self.saveEvent)
        self.eUi.bCancel.clicked.connect(self.cancelEvent)

        self.bUi.buyRegular.clicked.connect(self.buyRegular)
        self.bUi.buyEarly.clicked.connect(self.buyEarly)
        self.bUi.buyStudent.clicked.connect(self.buyStudent)
        self.bUi.buyLate.clicked.connect(self.buyLate)
        self.bUi.bOk.clicked.connect(self.saveTicket)
        self.bUi.bCancel.clicked.connect(self.cancelTicket)

        self.Event = Tickets.Event
        self.totalTickets = None
        self.totalPrice = None

        self.mUi.show()

    def addEvent(self, day=None, month=None, year=None, price=None, info=None):
        try:
            self.EventInit = self.Event(day, month, year, price, info)
        except Exception:
            pass
        self.mUi.eventsInfo.setText(self.EventInit.__str__())

        self.bUi.buyInfo.clear()

        self.bUi.costRegular.setText(
            f"Cost of regular ticket: {self.EventInit.get_tick_price('Regular')}$")
        self.bUi.costEarly.setText(
            f"Cost of early ticket: {self.EventInit.get_tick_price('Early')}$")
        self.bUi.costStudent.setText(
            f"Cost of student ticket: {self.EventInit.get_tick_price('Student')}$")
        self.bUi.costLate.setText(
            f"Cost of late ticket: {self.EventInit.get_tick_price('Late')}$")

    def saveEvent(self):
        self.day = self.eUi.dateEvent.date().day()
        self.month = self.eUi.dateEvent.date().month()
        self.year = self.eUi.dateEvent.date().year()
        
        self.price = self.eUi.SbPrice.value()
        self.info = self.eUi.TeInfo.toPlainText()

        self.addEvent(self.day, self.month, self.year, self.price, self.info)
        self.eUi.close()

    def cancelEvent(self):
        self.eUi.close()
        
    def getTickInfo(self):
        self.qidTicket, tick = QtWidgets.QInputDialog, ''
        tick, ok = self.qidTicket().getText(self, 'Enter ticket type:', 
                                            f'Please, enter ticket type you want to find out info about.\n'\
                                            f'Available types of tickets:\n' \
                                            f'Regular, Early, Student, Late')
        if ok == True:
            self.tickInfo = self.EventInit.get_tick_info(tick)
            self.tickPrice = self.EventInit.get_tick_price(tick)
            while tick == '':
                tick, ok = self.qidTicket().getText(self, 'Enter ticket type:', 
                                            f'You have not entered anything.\n' \
                                            f'Available types of tickets:\n' \
                                            f'Regular, Early, Student, Late')
                self.tickInfo = self.EventInit.get_tick_info(tick)
                self.tickPrice = self.EventInit.get_tick_price(tick)
                self.mUi.ticketsInfo.setText(f'{self.tickInfo}\nPrice: {self.tickPrice}$')
                if ok == False:
                    break
            self.mUi.ticketsInfo.setText(f'{self.tickInfo}\nPrice: {self.tickPrice}$')
        else:
            self.qidTicket().done(0)

    def buyRegular(self):
        self.regular = self.EventInit.buy_ticket('Regular')
        self.bUi.buyInfo.setText(f"{self.regular}")
        
    def buyEarly(self):
        self.early = self.EventInit.buy_ticket('Early')
        self.bUi.buyInfo.setText(f"{self.early}")

    def buyStudent(self):
        self.student = self.EventInit.buy_ticket('Student')
        self.bUi.buyInfo.setText(f"{self.student}")

    def buyLate(self):
        self.late = self.EventInit.buy_ticket('Late')
        self.bUi.buyInfo.setText(f"{self.late}")

    def saveTicket(self):
        i = float()
        self.dctTick = self.EventInit.get_dct()
        self.totalTickets = [*self.dctTick.values()]
        self.total = [self.EventInit.get_tick_price(i) for i in self.totalTickets]
        self.totalPrice = sum(self.total[:len(self.total)])
            
        self.mUi.ticketsInfo.setText(f'You have bought the next tickets:\n' \
                                    f'{self.totalTickets}\n' \
                                    f'Total price: {self.totalPrice}$')

        self.bUi.close()

    def cancelTicket(self):
        self.bUi.buyInfo.clear()
        self.bUi.close()

    def constructTickByNum(self):
        self.qidNum = QtWidgets.QInputDialog
        num, ok = self.qidNum().getText(self, 'Enter ticket unique number:', 
            f"Enter your unique ticket number, and we will check for it's availability in our base.")
        if ok == True:
            self.num = num
            self.mUi.ticketsInfo.setText(self.EventInit.construct_tick_by_num(self.num))
            self.qidNum().done(0)
        else:
            if self.totalTickets == None and self.totalPrice == None:
                self.bUi.close()
            else:
                self.mUi.ticketsInfo.setText(f'You have bought the next tickets:\n' \
                                        f'{self.totalTickets}\n' \
                                        f'Total price: {self.totalPrice}$')
                self.qidNum().done(0)

    def saveJsonEvent(self):
        try:
            event = {
                "day":self.day, "month":self.month, "year":self.year, "price":self.price, "info":self.info
                }
        except Exception:
            pass
        else:
            JSave = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', '/', 'JSON file (*.json)')
            if JSave[0]:
                f = open(JSave[0], 'w')
                with f:
                    json.dump(event, f, sort_keys=True, indent=4)

    def openJsonEvent(self):
        JOpen = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/', 'JSON file (*.json)')
        if JOpen[0]:
            f = open(JOpen[0])
            with f:
                data = json.load(f)
        
        self.day, self.month, self.year = data['day'], data['month'], data['year']
        self.price, self.info = data['price'], data['info']
        self.EventInit = self.Event(self.day, self.month, self.year, self.price, self.info)
        
        self.mUi.eventsInfo.setText(self.EventInit.__str__())
        
        self.bUi.costRegular.setText(
            f"Cost of regular ticket: {self.EventInit.get_tick_price('Regular')}$")
        self.bUi.costEarly.setText(
            f"Cost of early ticket: {self.EventInit.get_tick_price('Early')}$")
        self.bUi.costStudent.setText(
            f"Cost of student ticket: {self.EventInit.get_tick_price('Student')}$")
        self.bUi.costLate.setText(
            f"Cost of late ticket: {self.EventInit.get_tick_price('Late')}$")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainUI()
    sys.exit(app.exec())
