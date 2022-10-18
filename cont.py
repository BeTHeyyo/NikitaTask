from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
import sys
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QFont, QIcon


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.createWidgets()

    def createWidgets(self):
        self.my_button = QtWidgets.QPushButton(self)
        self.my_button.setText("My Widget")
        self.my_button.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.my_button:
            self.menu = QMenu()

            menuHUPresets = self.menu.addAction("HU presets")
            menuTools = self.menu.addAction("Tools")

            self.menu.addSeparator()

            menuMove = self.menu.addAction("Move")
            menuSeries = self.menu.addAction("Series")
            menuTurn = self.menu.addAction("Turn")
            menuMPR = self.menu.addAction("MPR")

            self.menu.addSeparator()

            menuCopy = self.menu.addAction("Copy")
            menuGroup = self.menu.addAction("Group")
            menuDelete = self.menu.addAction("Delete")
            menuRefresh = self.menu.addAction("Refresh") 


            selected_action = self.menu.exec_(event.globalPos())

            if selected_action == menuHUPresets:
                self.presetsSubMenu = QMenu()

                presetsSubMenuSoftTissueF5 = self.presetsSubMenu.addAction("Soft-Tissue F5")
                presetsSubMenuLungF6 = self.presetsSubMenu.addAction("Lung F6")
                presetsSubMenuBoneF7 = self.presetsSubMenu.addAction("Bone F7")
                presetsSubMenuLiverF8 = self.presetsSubMenu.addAction("Liver F8")
                presetsSubMenuAngio = self.presetsSubMenu.addAction("Angio")
                presetsSubMenuColon = self.presetsSubMenu.addAction("Colon")
                presetsSubMenuInverse = self.presetsSubMenu.addAction("Inverse")

                selected_action1 = self.presetsSubMenu.exec_(event.globalPos())

            if selected_action == menuTools:
                self.toolsSubMenu = QMenu()

                toolsSubMenuLength = self.toolsSubMenu.addAction("Length")
                toolsOval = self.toolsSubMenu.addAction("Oval")
                toolsRectangle = self.toolsSubMenu.addAction("Rectangle")
                toolsPolygon = self.toolsSubMenu.addAction("Polygon")
                toolsArrow = self.toolsSubMenu.addAction("Arrow")
                toolsPoint = self.toolsSubMenu.addAction("Point")
                toolsAngle = self.toolsSubMenu.addAction("Angle")
                toolsOpenPolygon = self.toolsSubMenu.addAction("Open polygon")
                toolsFlatfootAngle = self.toolsSubMenu.addAction("Flatfoot angle")
                toolsCobbAngle = self.toolsSubMenu.addAction("CobbAngle")
                toolsRemove = self.toolsSubMenu.addAction("Remove")

                selected_action2 = self.toolsSubMenu.exec_(event.globalPos())
            
        
        return super().eventFilter(source, event)

    




def showWindow():
    app = QApplication(sys.argv)
    app.setStyleSheet(
    "QMenu {"
    "background: #494B4E;"
    "border: 1px solid black;"
    "border-radius: 6px;"
    "width: 200px; "
    "padding: 15px 0 10px;"
    "} "

    "QMenu::item{"
    "color: #DDDDDD;"
    "padding: 5px 200px 4px 15px;"
    "margin: 0;"
    "font-family: 'Roboto';"
    "font-style: normal;"
    "font-weight: 400;"
    "font-size: 14px;"
    "line-height: 16px;"
    "}"

    "QMenu::item:selected{"
    "color: #DDDDDD;"
    "border-top: 1px solid black;"
    "border-bottom: 1px solid black;"
    "}"

    "QMenu::separator {"
    "color: #21262D;"
    "width: 1px;"
    "height: 2px;"
    "margin: 5px 0 5px;"
    "padding: 0;"
    "}"
    )
    app.setFont(QFont("Times"),"QMenu::item")
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

showWindow()