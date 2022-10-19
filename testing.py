import sys
import qrc_resources

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel("Nikita")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self.button = QPushButton("Hello",self)
        self.button.clicked.connect(self.showPrintWidget)

    def contextMenuEvent(self, event):
        rqContextMenu = RightClickMenu(self.centralWidget)

        rqContextMenu.exec(event.globalPos())

    def showPrintWidget(self):
        a = PrintWidget()
        a.show()

class RightClickMenu(QMenu):
    def __init__(self,parent):
        super().__init__()
        self._createRCActions()
        self._createContextMenu()

    def _createContextMenu(self):
        
        presetsMenu = QMenu("HU Presets", self)
        presetsMenu.addAction(self.rqSoftTissueAction)
        presetsMenu.addAction(self.rqLungAction)
        presetsMenu.addAction(self.rqBoneAction)
        presetsMenu.addAction(self.rqLiverAction)
        presetsMenu.addAction(self.rqAngioAction)
        presetsMenu.addAction(self.rqColonAction)
        presetsMenu.addAction(self.rqInverseAction)
        presetsMenu.addSeparator()

        self.addMenu(presetsMenu)

        toolsMenu = QMenu("Tools", self)
        toolsMenu.addAction(self.rqSubMenuLengthAction)
        toolsMenu.addAction(self.rqOvalAction)
        toolsMenu.addAction(self.rqRectangleAction)
        toolsMenu.addAction(self.rqPolygonAction)
        toolsMenu.addAction(self.rqArrowAction)
        toolsMenu.addAction(self.rqPointAction)
        toolsMenu.addAction(self.rqAngleAction)
        toolsMenu.addAction(self.rqOpenPolygonAction)
        toolsMenu.addAction(self.rqFlatfootAngleAction)
        toolsMenu.addAction(self.rqFlatfootAngleAction)
        toolsMenu.addAction(self.rqCobbAngleAction)
        toolsMenu.addAction(self.rqRemoveAction)
        

        self.addMenu(toolsMenu)


        self.addSeparator() 
        self.addAction(self.rcMoveAction)
        self.addAction(self.rcSeriesAction)
        self.addAction(self.rcTurnAction)
        self.addAction(self.rcMPRAction)
        self.addSeparator()
        self.addAction(self.rcCopyAction)
        self.addAction(self.rcGroupAction)
        self.addAction(self.rcDeleteAction)
        self.addAction(self.rcRefreshAction)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(self.windowFlags() | Qt.NoDropShadowWindowHint)
        toolsMenu.setWindowFlag(Qt.FramelessWindowHint)
        toolsMenu.setAttribute(Qt.WA_TranslucentBackground)
        toolsMenu.setWindowFlags(self.windowFlags() | Qt.NoDropShadowWindowHint)
        presetsMenu.setWindowFlag(Qt.FramelessWindowHint)
        presetsMenu.setAttribute(Qt.WA_TranslucentBackground)
        presetsMenu.setWindowFlags(self.windowFlags() | Qt.NoDropShadowWindowHint)

    def _createRCActions(self):
        self.rcMoveAction = QAction("Move",self)
        self.rcSeriesAction = QAction("Series",self)
        self.rcTurnAction = QAction("Turn",self)
        self.rcMPRAction = QAction("MPR",self)
        self.rcCopyAction = QAction("Copy",self)
        self.rcGroupAction = QAction("Group",self)
        self.rcDeleteAction = QAction("Delete",self)
        self.rcRefreshAction = QAction("Refresh",self)

        self.rqSoftTissueAction = QAction("Soft-Tissue",self)
        self.rqSoftTissueAction.setShortcut("f5")
        self.rqLungAction = QAction("Lung",self)
        self.rqLungAction.setShortcut("f6")
        self.rqBoneAction = QAction("Bone",self)
        self.rqBoneAction.setShortcut("f7")
        self.rqLiverAction = QAction("Liver",self)
        self.rqLiverAction.setShortcut("f8")
        self.rqAngioAction = QAction("Angio",self)
        self.rqColonAction = QAction("Colon",self)
        self.rqInverseAction = QAction("Inverse",self)

        self.rqSubMenuLengthAction = QAction(QIcon("icons/length_icon.png"),"Length",self)
        self.rqOvalAction = QAction(QIcon("icons/oval_icon.png"), "Oval",self)
        self.rqRectangleAction = QAction(QIcon("icons/rectangle_icon.png"), "Rectangle",self)
        self.rqPolygonAction = QAction(QIcon("icons/polygon_icon.png"), "Polygon",self)
        self.rqArrowAction = QAction(QIcon("icons/arrow_icon.png"), "Arrow",self)
        self.rqPointAction = QAction(QIcon("icons/point_icon.png"), "Point",self)
        self.rqAngleAction = QAction(QIcon("icons/angle_icon.png"), "Angle",self)
        self.rqOpenPolygonAction = QAction(QIcon("icons/open_polygon_icon.png"), "Open polygon",self)
        self.rqFlatfootAngleAction = QAction(QIcon("icons/flatfoot_angle_icon.png"), "Flatfoot angle",self)
        self.rqCobbAngleAction = QAction(QIcon("icons/cobb_angle_icon.png"), "CobbAngle",self)
        self.rqRemoveAction = QAction(QIcon("icons/remove_icon.png"), "Remove",self)
    
class PrintWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Print")
        
        self._createFrom()
    
    def _createFrom(self):
        label1 = QLabel("First Name")
        label2 = QLabel("Last Name")
        label3 = QLabel("Extra")
        label4 = QLabel("Choose catergory")

        input1 = QLineEdit()
        input2 = QLineEdit()
        input3_1 = QLineEdit()
        input3_2 = QLineEdit()

        inputBox = QVBoxLayout()
        inputBox.addWidget(input3_1)
        inputBox.addWidget(input3_2)

        categoryBox = QHBoxLayout()
        categoryBox.addWidget(QRadioButton("Category 1"))
        categoryBox.addWidget(QRadioButton("Category 2"))
        categoryBox.addStretch()

        formLayout = QFormLayout()
        formLayout.addRow(label1,input1)
        formLayout.addRow(label2,input2)
        formLayout.addRow(label3,inputBox)
        formLayout.addRow(label4,categoryBox)
        formLayout.addRow(QPushButton("Submit"))
        self.setLayout(formLayout)

        self.show()


CSS = """
    QMenu {
    background-color: #494B4E;
    border-radius: 6px;
    padding-top: 20px;
    padding-bottom: 14px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    font-family: Verdana;
    }
    
    QMenu::item{
    color: #DDDDDD;
    padding-top: 5px;
    padding-bottom: 4px;
    padding-left: 15px;
    padding-right: 90px;
    }

    QMenu::item:selected{
    background-color: #21262D;
    
    }
    QMenu::icon {
        padding-right: 20px;
    }
    QMenu::right-arrow 
    {
        image: url(icons/right_arrow_icon.png);
        margin-right: 20px;
    }

    """
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(CSS)
    win = Window()
    win.show()
    sys.exit(app.exec_())