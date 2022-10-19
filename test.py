import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MenuItem(QWidget):
    """docstring for MenuItem"""
    def __init__(self, text='test', icon=None, parent=None):
        super(MenuItem, self).__init__(parent)

        hbox = QHBoxLayout(self)
        # hbox.setContentsMargins(0, 0, 0, 0)
        label = QLabel(text)
        btn = QPushButton()
        if icon:
            btn.setIcon(icon)

        hbox.addWidget(label)
        hbox.addStretch()
        hbox.addWidget(btn)
        self.setMinimumWidth(parent.width())


class MyMenu(QWidget):
    """docstring for MyMenu"""
    def __init__(self, parent=None):
        super(MyMenu, self).__init__(parent)

        self.main_width = 200
        self.main_height = 150
        self.close_menu = False

        self.parent = parent
        self.setGeometry(0, 0, 200, 150)

        self.initUI()
        self.setWindowFlags(Qt.Popup)
        # self.setWindowModality(Qt.WindowModal)

    def initUI(self):
        main_frame = QWidget(self)
        main_v_layout = QVBoxLayout(main_frame)
        main_v_layout.setContentsMargins(0, 0, 0, 0)
        item_1 = MenuItem('item 1', parent=self)
        item_2 = MenuItem('item 2', parent=self)
        item_3 = MenuItem('item 3', parent=self)
        main_v_layout.addWidget(item_1)
        main_v_layout.addWidget(item_2)
        main_v_layout.addWidget(item_3)

    def animationShow(self):
        self.close_menu = False
        self.start_close_menu = True
        self.show()

        # PyQt4.QtCore.QRect(0, 0, 400, 23)
        rect = self.parent.rect()

        # PyQt4.QtCore.QPoint(199, 11)
        center_pos = rect.center()

        # PyQt4.QtCore.QPoint(654, 465)
        global_center_pos = self.parent.mapToGlobal(center_pos)

        height = rect.height()

        show_pos = QPoint(global_center_pos.x() - (self.width() / 2), global_center_pos.y() + height)
        # print show_pos

        self.move(show_pos)
        self.inAnimation(show_pos)

    def inAnimation(self, show_pos=None):
        start_height = QSize(self.main_width, 0)
        end_height = QSize(self.main_width, self.main_height)

        size_anim = QPropertyAnimation(self, 'size')
        size_anim.setStartValue(start_height)
        size_anim.setEndValue(end_height)
        size_anim.setDuration(160)
        size_anim.setEasingCurve(QEasingCurve.OutQuad)

        opacity_anim = QPropertyAnimation(self, 'windowOpacity')
        opacity_anim.setStartValue(0.0)
        opacity_anim.setEndValue(1.0)
        opacity_anim.setDuration(260)
        opacity_anim.setEasingCurve(QEasingCurve.OutQuad)

        self.in_anim_group = QParallelAnimationGroup()
        self.in_anim_group.addAnimation(size_anim)
        self.in_anim_group.addAnimation(opacity_anim)
        self.in_anim_group.start()

    def outAnimation(self):
        try:
            end_size = QSize(self.size().width(), 0)

            pos_anim = QPropertyAnimation(self, 'size')
            pos_anim.setEndValue(end_size)
            pos_anim.setDuration(200)
            pos_anim.setEasingCurve(QEasingCurve.InQuad)

            opacity_anim = QPropertyAnimation(self, 'windowOpacity')
            opacity_anim.setStartValue(1.0)
            opacity_anim.setEndValue(0.0)
            opacity_anim.setDuration(200)
            opacity_anim.setEasingCurve(QEasingCurve.InQuad)

            self.out_anim_group = QParallelAnimationGroup()
            self.out_anim_group.addAnimation(pos_anim)
            self.out_anim_group.addAnimation(opacity_anim)
            self.out_anim_group.finished.connect(self.closeMenu)
            self.out_anim_group.start()

        except RuntimeError as e:
            pass
        except Exception as e:
            print(e)

    def closeMenu(self):
        self.close_menu = True
        self.setVisible(False)

    def closeEvent(self, event):
        # super(MyMenu, self).closeEvent(event)
        if self.start_close_menu:
            self.outAnimation()
            self.start_close_menu = False

    def hideEvent(self, event):
        # print 'hideEvent', event
        super(MyMenu, self).hideEvent(event)

    def setVisible(self, visible):
        if self.close_menu:
            visible = False

        elif not visible:
            visible = True

        super(MyMenu, self).setVisible(visible)


class Win(QWidget):
    """docstring for Win"""
    def __init__(self):
        super(Win, self).__init__()

        vbox = QVBoxLayout(self)
        btn = QPushButton('call menu')
        vbox.addWidget(btn)

        self.menu = MyMenu(btn)
        btn.clicked.connect(self.menu.animationShow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())