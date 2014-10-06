from PyQt4 import QtCore, QtGui
from ui_openlayers_layerproperty_dialog import Ui_dlgLayerProperty


class LayerPropertyDialog(QtGui.QDialog, Ui_dlgLayerProperty):
    def __init__(self, layer):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self._layer = layer
        self.cbGray.setChecked(self._layer.enableGrayscale)
        self.updateGrayToggle(self._layer.enableGrayscale)
        self.dsbRed.setValue(self._layer.grayscaleWeights[2])
        self.dsbGreen.setValue(self._layer.grayscaleWeights[1])
        self.dsbBlue.setValue(self._layer.grayscaleWeights[0])

        self.connect(self.cbGray, QtCore.SIGNAL('toggled(bool)'),
                     self.updateGrayToggle)
        self.connect(self.dsbRed, QtCore.SIGNAL('valueChanged(double)'),
                     self.updateRed)
        self.connect(self.dsbBlue, QtCore.SIGNAL('valueChanged(double)'),
                     self.updateGreen)
        self.connect(self.dsbGreen, QtCore.SIGNAL('valueChanged(double)'),
                     self.updateBlue)

    def updateGrayToggle(self, toggled):
        self._layer.enableGrayscale = toggled
        self.dsbRed.setEnabled(toggled)
        self.dsbGreen.setEnabled(toggled)
        self.dsbBlue.setEnabled(toggled)

    def updateRed(self, val):
        self._layer.grayscaleWeights[2] = val

    def updateGreen(self, val):
        self._layer.grayscaleWeights[1] = val

    def updateBlue(self, val):
        self._layer.grayscaleWeights[0] = val
