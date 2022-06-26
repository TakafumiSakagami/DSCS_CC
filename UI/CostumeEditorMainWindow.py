from PyQt5 import QtWidgets
from UI.ModelRendererWidget import ModelRendererWidget

class CostumeEditorMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.render_widget = ModelRendererWidget(self)
        
        self.setCentralWidget(self.render_widget)
        
        self.setGeometry(100,100,800,600)
        self.setWindowTitle("Costume Editor")
