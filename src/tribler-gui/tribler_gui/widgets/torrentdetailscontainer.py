from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from tribler_gui.utilities import get_ui_file_path


class TorrentDetailsContainer(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        uic.loadUi(get_ui_file_path('torrent_details_container.ui'), self)
