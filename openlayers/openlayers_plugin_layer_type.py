# -*- coding: utf-8 -*-
"""
/***************************************************************************
OpenLayers Plugin
A QGIS plugin

                             -------------------
begin                : 2010-02-03
copyright            : (C) 2010 by Pirmin Kalberer, Sourcepole
email                : pka at sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import qDebug
from qgis.core import QgsPluginLayerType
from openlayers_layer import OpenlayersLayer


class OpenlayersPluginLayerType(QgsPluginLayerType):

    def __init__(self, iface, add_callback, olLayerTypeRegistry):
        QgsPluginLayerType.__init__(self, OpenlayersLayer.LAYER_TYPE)
        self.iface = iface
        self.add_callback = add_callback
        self.olLayerTypeRegistry = olLayerTypeRegistry

    def createLayer(self):
        layer = OpenlayersLayer(self.iface, self.olLayerTypeRegistry)
        self.add_callback(layer)
        return layer

    def showLayerProperties(self, layer):
        qDebug('Property window called')
        from layerproperty_dialog import LayerPropertyDialog
        dlgLayerProperty = LayerPropertyDialog(layer)
        dlgLayerProperty.show()
        dlgLayerProperty.exec_()
        # FIXME need to rerender the map when the property dialog is closed
        return True

