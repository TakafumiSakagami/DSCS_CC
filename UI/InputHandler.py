from PyQt5 import QtCore

class InputHandler:
    def __init__(self):
        self.active_keys = set()
        self.mouse_delta = QtCore.QPoint(0, 0)
        self.mouse_position = QtCore.QPoint(0, 0)
        
    def getMouseDelta(self):
        return self.mouse_delta
    
    def getMousePos(self):
        return self.mouse_position
    
    def updateMousePosition(self, pos):
        self.mouse_delta = pos - self.mouse_position
        self.mouse_position = pos
        
    def registerKey(self, key):
        self.active_keys.add(key)
        
    def unregisterKey(self, key):
        self.active_keys.remove(key)
        
    def isKeyActive(self, key):
        return key in self.active_keys


class ActionHandler:
    def __init__(self):
        self.input_handler = InputHandler()
        
        self.rotate_command = [QtCore.Qt.RightButton]
        self.translate_command = [QtCore.Qt.Key_Shift, QtCore.Qt.RightButton]
        self.zoom_command = []
        
    def checkAction(self, action):
        return all([self.input_handler.isKeyActive(key) for key in action])
        
    def shouldRotateCamera(self):
        return self.checkAction(self.rotate_command)
    
    def shouldTranslateCamera(self):
        return self.checkAction(self.translate_command)
    