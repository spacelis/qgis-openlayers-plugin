# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_openlayers_layerproperty_dialog.ui'
#
# Created: Mon Oct  6 14:50:06 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dlgLayerProperty(object):
    def setupUi(self, dlgLayerProperty):
        dlgLayerProperty.setObjectName(_fromUtf8("dlgLayerProperty"))
        dlgLayerProperty.resize(400, 300)
        self.dialogButtonBox = QtGui.QDialogButtonBox(dlgLayerProperty)
        self.dialogButtonBox.setGeometry(QtCore.QRect(50, 250, 341, 32))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.dialogButtonBox.setObjectName(_fromUtf8("dialogButtonBox"))
        self.formLayoutWidget = QtGui.QWidget(dlgLayerProperty)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lbRed = QtGui.QLabel(self.formLayoutWidget)
        self.lbRed.setObjectName(_fromUtf8("lbRed"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbRed)
        self.dsbRed = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.dsbRed.setEnabled(False)
        self.dsbRed.setMinimum(0.1)
        self.dsbRed.setMaximum(1.0)
        self.dsbRed.setSingleStep(0.1)
        self.dsbRed.setProperty("value", 1.0)
        self.dsbRed.setObjectName(_fromUtf8("dsbRed"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dsbRed)
        self.lbGreen = QtGui.QLabel(self.formLayoutWidget)
        self.lbGreen.setObjectName(_fromUtf8("lbGreen"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbGreen)
        self.dsbGreen = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.dsbGreen.setEnabled(False)
        self.dsbGreen.setMinimum(0.1)
        self.dsbGreen.setMaximum(1.0)
        self.dsbGreen.setSingleStep(0.1)
        self.dsbGreen.setProperty("value", 1.0)
        self.dsbGreen.setObjectName(_fromUtf8("dsbGreen"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dsbGreen)
        self.lbBlue = QtGui.QLabel(self.formLayoutWidget)
        self.lbBlue.setObjectName(_fromUtf8("lbBlue"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbBlue)
        self.dsbBlue = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.dsbBlue.setEnabled(False)
        self.dsbBlue.setMinimum(0.1)
        self.dsbBlue.setMaximum(1.0)
        self.dsbBlue.setSingleStep(0.1)
        self.dsbBlue.setProperty("value", 1.0)
        self.dsbBlue.setObjectName(_fromUtf8("dsbBlue"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dsbBlue)
        self.cbGray = QtGui.QCheckBox(self.formLayoutWidget)
        self.cbGray.setObjectName(_fromUtf8("cbGray"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbGray)

        self.retranslateUi(dlgLayerProperty)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dlgLayerProperty.close)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dlgLayerProperty.close)
        QtCore.QMetaObject.connectSlotsByName(dlgLayerProperty)

    def retranslateUi(self, dlgLayerProperty):
        dlgLayerProperty.setWindowTitle(_translate("dlgLayerProperty", "Layer Properties", None))
        self.lbRed.setText(_translate("dlgLayerProperty", "Red", None))
        self.lbGreen.setText(_translate("dlgLayerProperty", "Green", None))
        self.lbBlue.setText(_translate("dlgLayerProperty", "Blue", None))
        self.cbGray.setText(_translate("dlgLayerProperty", "Grayscale", None))

