from PyQt5.uic import loadUi

from tabs import TABS
from dialogs.dialog import *

from utils import *


class YouTubeHelper(QMainWindow):
    sig_error = pyqtSignal(str)
    resized = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.sig_error.connect(self.show_error)
        self.resized.connect(self.on_resize)
        self.init_API()
        self.showMaximized()

    def init_ui(self):
        loadUi(os.path.join(os.path.abspath('.'), 'Main.ui'), self)
        self.init_menu()
        self.init_tabs()
        self.allVideos = AllVideos(self, self.allVideosBox)
        self.downloadVideos = DownloadVideos(self, self.downloadVideosBox)
        self.search_types = QButtonGroup()
        self.search_types.addButton(self.search, 0)
        self.search_types.addButton(self.channel, 1)
        self.search_types.addButton(self.playlist, 2)
        self.search_types.buttonClicked.connect(self.toggletype)
        QShortcut(QKeySequence('Ctrl+V'), self).activated.connect(self.paste)
        QShortcut(QKeySequence(Qt.Key_Backspace), self).activated.connect(self.downloadVideos.delete)
        QShortcut(QKeySequence(Qt.Key_Delete), self).activated.connect(self.downloadVideos.delete)
        self.downloadBtn.clicked.connect(self.download_tab.download)
        self.downloadAllBtn.clicked.connect(self.download_tab.downloadAll)
        width = self.geometry().width()
        height = self.geometry().height()
        left = (QApplication.desktop().width() - width)/2
        top = (QApplication.desktop().height() - height)/2
        self.setGeometry(QRect(left, top, width, height))
        # self.centralwidget.setStyleSheet("#centralwidget {border-image: url(./Wallpaper.jpg);} color: white;")
        # self.setStyleSheet("background: transparent;")
        self.setFocus()
        self.preferences_diag = PreferencesDialog(self)
        self.show()

    def init_API(self):
        try:
            f = open('api_key.txt', 'r')
            api_key = f.readline()
            f.close()
            # Create an API object with the API key
            self.API = API(self, api_key=api_key)
        except:
            self.main_window.sig_error.emit('No API Key loaded \n Search results will be limited to one.')
            self.API = API(self)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(QMainWindow, self).resizeEvent(event)

    def on_resize(self):
        size = self.tab_manager.currentWidget().geometry()
        self.search_tab.verticalLayoutWidget.setGeometry(size)
        self.download_tab.verticalLayoutWidget.setGeometry(size)
        self.import_tab.verticalLayoutWidget.setGeometry(size)

    def paste(self):
        idx = self.tab_manager.currentIndex()
        self.tab_manager.setCurrentIndex(2)
        for link in QApplication.clipboard().text().splitlines():
            self.API.importlink(link)
        self.tab_manager.setCurrentIndex(idx)

    def toggletype(self):
        if self.search_types.checkedId() > 0:
            self.general_box.setVisible(False)
        else:
            self.general_box.setVisible(True)

    def init_menu(self):
        action_bindings = {
            'exit': self.close,
            'preferences': self.show_preferences,
            'documentation': self.show_documentation,
            'about': self.show_about
        }
        for action in self.file.actions() + self.options.actions() + self.help.actions():
            if action.objectName() in action_bindings.keys():
                action.triggered.connect(action_bindings[action.objectName()])

    def init_tabs(self):
        for tab in TABS:
            self.tab_manager.addTab(tab(main_window=self), tab.display_name)

    def show_preferences(self):
        self.preferences_diag.show_dialog()

    @staticmethod
    def show_documentation():
        documentation_diag = DocumentationDialog()
        documentation_diag.show_dialog()

    @staticmethod
    def show_about():
        about_diag = AboutDialog()
        about_diag.show_dialog()

    @staticmethod
    @pyqtSlot(str)
    def show_error(error_msg):
        error_dialog = ErrorDialog(error_msg)
        error_dialog.exec_()


def launch_app():
    import sys
    app = QApplication(sys.argv)
    yt = YouTubeHelper()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys.excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook
    launch_app()
