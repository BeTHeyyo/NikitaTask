import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMenu


class WindowWithToolbar:
    def __init__(self):
        super().__init__()

    def menu_items(self)->list:
        pass


class Window1(WindowWithToolbar, QMainWindow):
    def __init__(self):
        WindowWithToolbar.__init__(self)
        QMainWindow.__init__(self)

        # New menu with actions
        self.menu = QMenu('one')
        self.menu.addActions([QAction('two', self), QAction('three', self)])

    def menu_items(self):
        return [self.menu]


class Window2(WindowWithToolbar, QMainWindow):
    def __init__(self):
        WindowWithToolbar.__init__(self)
        QMainWindow.__init__(self)

    def menu_items(self):
        # Only actions
        return [QAction('three', self), QAction('four', self)]


class MainWindow(WindowWithToolbar, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, parent=None)

        self.window1 = Window1()
        self.window2 = Window2()

        self.menu = QMenu('File')
        self.helloAction = QAction('Hello')
        self.menu.addAction(self.helloAction)

        self._build_menu()

    def menu_items(self)->list:
        return [self.menu]

    def _build_menu(self):
        self._add_menu_items(self)
        self._add_menu_items(self.window1)
        self._add_menu_items(self.window2)

    def _add_menu_items(self, windowWithToolbar: WindowWithToolbar):
        for menu_item in windowWithToolbar.menu_items():
            if isinstance(menu_item, QMenu):
                self.menuBar().addMenu(menu_item)
            elif isinstance(menu_item, QAction):
                self.menuBar().addAction(menu_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())