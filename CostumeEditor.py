import sys

from PyQt5 import QtWidgets

from UI.CostumeEditorMainWindow import CostumeEditorMainWindow
    
def testInit(w):
    path = "testdata/pc002"
    w.render_widget.loadModel(path, path + "_bn01.anim")

if __name__ == '__main__':
   app = QtWidgets.QApplication([])
   w = CostumeEditorMainWindow()
   
   # Just for quick render testing
   w.render_widget.glInitialised.connect(lambda : testInit(w))
   
   w.show()
   sys.exit(app.exec_())
