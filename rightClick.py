import sys
import qrc_resources

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QToolBar, QAction, QSpinBox, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QPainterPath 

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel("Nikita")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createRCActions()
    
    def contextMenuEvent(self, event):

        rqContextMenu = QMenu(self.centralWidget)
        
        presetsMenu = QMenu("HU Presets", self)
        presetsMenu.addAction(self.rqSoftTissueAction)
        presetsMenu.addAction(self.rqLungAction)
        presetsMenu.addAction(self.rqBoneAction)
        presetsMenu.addAction(self.rqLiverAction)
        presetsMenu.addAction(self.rqAngioAction)
        presetsMenu.addAction(self.rqColonAction)
        presetsMenu.addAction(self.rqInverseAction)
        presetsMenu.addSeparator()

        rqContextMenu.addMenu(presetsMenu)

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
        

        rqContextMenu.addMenu(toolsMenu)
        rqContextMenu.addSeparator()
        rqContextMenu.addAction(self.rcMoveAction)
        rqContextMenu.addAction(self.rcSeriesAction)
        rqContextMenu.addAction(self.rcTurnAction)
        rqContextMenu.addAction(self.rcMPRAction)
        rqContextMenu.addSeparator()
        rqContextMenu.addAction(self.rcCopyAction)
        rqContextMenu.addAction(self.rcGroupAction)
        rqContextMenu.addAction(self.rcDeleteAction)
        rqContextMenu.addAction(self.rcRefreshAction)

        

        rqContextMenu.setWindowFlag(Qt.FramelessWindowHint)
        rqContextMenu.setAttribute(Qt.WA_TranslucentBackground)
        rqContextMenu.setWindowFlags(rqContextMenu.windowFlags() | Qt.NoDropShadowWindowHint)
        toolsMenu.setWindowFlag(Qt.FramelessWindowHint)
        toolsMenu.setAttribute(Qt.WA_TranslucentBackground)
        toolsMenu.setWindowFlags(rqContextMenu.windowFlags() | Qt.NoDropShadowWindowHint)
        presetsMenu.setWindowFlag(Qt.FramelessWindowHint)
        presetsMenu.setAttribute(Qt.WA_TranslucentBackground)
        presetsMenu.setWindowFlags(rqContextMenu.windowFlags() | Qt.NoDropShadowWindowHint)
        # rqContextMenu.setStyleSheet(
        #     """
        #     background:#494B4E;
        #     border-top-left-radius:6px;
        #     border-bottom-left-radius:6px;
        #     border-top-right-radius:{0}px;
        #     border-bottom-right-radius:{0}px;
        #     box-shadow: none;
        #     """.format(radius)
        # )

        rqContextMenu.exec(event.globalPos())

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

CSS = """

    * {font-family: Verdana;}
    
    QMenu {
    background-color: #494B4E;
    border: 1px black solid;
    border-radius: 6px;
    width: 200px;
    padding: 15px 0 0px;
    }

    QMenu::item{
    color: #DDDDDD;
    padding: 5px 117px 5px 15px;
    margin-bottom: 20x;
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    }

    QMenu::item:selected{
    background-color: #21262D;
    /*border-top: 1px solid black;*/
    /*border-bottom: 1px solid black;*/
    
    }
    
    QMenu::icon {
    padding: 0 0 0 25px;
    }

    /* */
    QMenu::separator {
    background-color: #21262D;
    width: 1px;
    height: 1px;
    margin: 5px 0 5px;
    }
    """
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(CSS)
    win = Window()
    win.show()
    sys.exit(app.exec_())