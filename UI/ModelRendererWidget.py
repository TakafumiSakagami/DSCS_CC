import os

from PyQt5 import QtCore, QtGui, QtWidgets
import pyDSCSRenderer

from .InputHandler import ActionHandler


class ModelRendererWidget(QtWidgets.QOpenGLWidget):
    glInitialised = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.fps = 1./30 # Render at 30 fps
        
        self.renderer = pyDSCSRenderer.DSCSRenderer()
        self.clock = QtCore.QTimer()
        
        self.action_handler = ActionHandler()
        
        # Re-render and advance renderer time independently
        # Do this every time the clock ticks
        self.clock.timeout.connect(self.update)
        self.clock.timeout.connect(self.tick)
        self.clock.start(int(1000*self.fps)) # Tick once every 1000/30 milliseconds
        self.setFocusPolicy(QtCore.Qt.StrongFocus);
        
        
    """
    Automatically called during the Widget init once the
    OpenGL context has been initialised.
    Need to wait for context creation to init the renderer.
    """
    def initializeGL(self):
        self.renderer.initRenderer()
        self.renderer.setCameraPosition(0, 1, 3)
        self.renderer.setCameraTarget(0, 1, 0)
        self.glInitialised.emit()
        
    """
    Automatically called when the widget needs updating.
    """
    def update(self):
        self.checkActions()
        self.renderer.recalculateGlobalUniforms()
        self.repaint()

    """
    Automatically called when redrawing the widget.
    """
    def paintGL(self):
        self.renderer.refreshRenderSettings()
        self.renderer.render()
        
    """
    Automatically called when the widget is resized.
    """
    def resizeGL(self, width, height):
        self.renderer.setAspectRatio(width, height)
        self.repaint()
        
    """
    Used to advance the point in time the renderer will render at
    """
    def tick(self):
        self.renderer.advanceClock(1/30)
        
    def loadModel(self, model_path, anim_path=None):
        # Put some error handling in later
        if os.path.isfile(model_path + ".name"):
            m_id = self.renderer.loadModel(model_path)
            if anim_path is not None and os.path.isfile(anim_path):
                self.renderer.loadAnim(m_id, anim_path)
                
    def checkActions(self):
        self.registerMousePosition()
        if (self.action_handler.shouldTranslateCamera()):
            mdelta = self.action_handler.input_handler.getMouseDelta()
            self.renderer.translateCamera(mdelta.x(), mdelta.y())
            
        elif (self.action_handler.shouldRotateCamera()):
            mdelta = self.action_handler.input_handler.getMouseDelta()
            self.renderer.rotateOrbitCamera(mdelta.x(), mdelta.y())

    def wheelEvent(self, event):
        shift = event.angleDelta().y()
        if shift:
            self.renderer.zoomCamera(-shift)

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            event.ignore()
        else:
            self.action_handler.input_handler.registerKey(event.key())
            
    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            event.ignore()
        else:
            self.action_handler.input_handler.unregisterKey(event.key())
            
    def mousePressEvent(self, event):
        self.action_handler.input_handler.registerKey(event.button())
        
    def mouseReleaseEvent(self, event):
        self.action_handler.input_handler.unregisterKey(event.button())
        
    def registerMousePosition(self):
        self.action_handler.input_handler.updateMousePosition(QtGui.QCursor.pos())
