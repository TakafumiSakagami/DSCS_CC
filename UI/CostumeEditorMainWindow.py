from PyQt5 import QtWidgets
from UI.ModelRendererWidget import ModelRendererWidget

class CostumeEditorMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.widget = QtWidgets.QWidget(self)
        self.widget_layout = QtWidgets.QVBoxLayout()
        
        self.initSelectionBar()
        self.initViewportSplitter()
        self.initViewport()
        self.initBuildArea()
        
        self.widget.setLayout(self.widget_layout)
        self.setCentralWidget(self.widget)
        
        
        self.setGeometry(100,100,800,600)
        self.setWindowTitle("Costume Editor")

    def initSelectionBar(self):
        selection_bar = QtWidgets.QWidget(self)
        sb_layout = QtWidgets.QHBoxLayout()
        
        char_widget = QtWidgets.QWidget(selection_bar)
        char_layout = QtWidgets.QHBoxLayout()
        char_label = QtWidgets.QLabel("Character: ", char_widget)
        self.char_combobox = QtWidgets.QComboBox(char_widget)
        char_layout.addWidget(char_label)
        char_layout.addWidget(self.char_combobox)
        char_widget.setLayout(char_layout)
        
        costume_widget = QtWidgets.QWidget(selection_bar)
        costume_layout = QtWidgets.QHBoxLayout()
        costume_label = QtWidgets.QLabel("Costume: ", char_widget)
        self.costume_combobox = QtWidgets.QComboBox(char_widget)
        costume_layout.addWidget(costume_label)
        costume_layout.addWidget(self.costume_combobox)
        costume_widget.setLayout(costume_layout)
        
        self.export_button = QtWidgets.QPushButton("Export", selection_bar)
        
        sb_layout.addWidget(char_widget)
        sb_layout.addWidget(costume_widget)
        sb_layout.addWidget(self.export_button)
        selection_bar.setLayout(sb_layout)
        sb_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize);
             
        self.widget_layout.addWidget(selection_bar)
        
    def initViewportSplitter(self):
        self.viewport_splitter = QtWidgets.QSplitter(self)
        self.widget_layout.addWidget(self.viewport_splitter)
        
    def initViewport(self):
        self.render_widget = ModelRendererWidget(self.viewport_splitter)
        self.viewport_splitter.addWidget(self.render_widget)
        
    def initBuildArea(self):
        self.build_area = QtWidgets.QLabel("BUILD AREA", self.viewport_splitter)
        self.viewport_splitter.addWidget(self.build_area)
        