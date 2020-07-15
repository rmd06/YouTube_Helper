from PyQt5.uic import loadUi
from utils import *


class ImportTab(QWidget):
    display_name = 'Import Histories'
    
    def __init__(self, main_window):
        super().__init__()
        QThread.currentThread().setObjectName('import_tab')
        self.main_window = main_window
        self.main_window.import_tab = self
        self.init_ui()
        self.show()

    def init_ui(self):
        loadUi(os.path.join(os.path.abspath('.'), 'tabs/import_histories.ui'), self)
