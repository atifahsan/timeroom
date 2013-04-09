#!/usr/bin/python

import os
import sys
import glob
from PySide import QtCore, QtGui
import ConfigParser
from Timelapse import Timelapse
import SideCar

from TimeroomMainWindow import Ui_TimeroomMainWindow

class TimelapseGridModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        self.sections = ['Sidecar', 'Rating', 'Aperture', 'Shutter Speed', 'ISO', 'Curves', 'Gradients']
        self.timelapse = None

        super(TimelapseGridModel, self).__init__(parent)

    def emitChanged(self):
        topLeft = self.createIndex(0, len(self.sections)-1)
        bottomRight = self.createIndex(len(self.timelapse.filenames) - 1, len(self.sections)-1)
        self.dataChanged.emit(topLeft, bottomRight)

    def setRootPath(self, path):
        self.timelapse = Timelapse(path)
        self.endResetModel()

    def initialize(self):
        self.timelapse.initialize()
        self.emitChanged()

    def readFiles(self):
        ret = True
        try:
            self.timelapse.readSideCars()
        except SideCar.SideCarCorruptError, err:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("%s appears to be corrupt (%s)." % (err.filename, err.reason))
            msgBox.exec_()
            ret = False
        self.emitChanged()
        return ret

    def rowCount(self, parent):
        if not self.timelapse:
            return 0
        return len(self.timelapse.filenames)

    def columnCount(self, parent):
        if not self.timelapse:
            return 0
        return len(self.sections)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None

        filename = self.timelapse.filenames[index.row()]
        if index.column() == 0:
            return filename
        else:
            try:
                sidecar = self.timelapse.sidecars[index.row()]
                if index.column() == 1:
                    rating = sidecar.getRating()
                    if rating == 0: return ''
                    else: return rating
                elif index.column() == 2:
                    return 'f/%s' % (float(sidecar.getFNumber()))
                elif index.column() == 3:
                    return str(sidecar.getExposureTime())
                elif index.column() == 4:
                    return sidecar.getISOSpeedRating()
                elif index.column() == 5:
                    return sidecar.getCurvesCount()
                elif index.column() == 6:
                    return sidecar.getGradientsCount()
            except IndexError:
                return ''

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.sections[section]

class TimeroomMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TimeroomMainWindow, self).__init__(parent)
        self.ui = Ui_TimeroomMainWindow()
        self.ui.setupUi(self)

        # Set up folder navigator
        model = QtGui.QFileSystemModel()
        model.setRootPath(QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.DesktopLocation))
        model.setReadOnly(True)
        model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        self.ui.dirView.setModel(model)
        self.ui.dirView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        for section in range(1, self.ui.dirView.header().count()):
            self.ui.dirView.header().hideSection(section)

        # Set up file list
        model = TimelapseGridModel()
        self.ui.tableView.setModel(model)
        self.ui.tableView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        # Set up integration
        model = self.ui.dirView.selectionModel() # https://bugreports.qt-project.org/browse/PYSIDE-79
        model.selectionChanged.connect(self.loadDir)
        self.ui.tableView.model().dataChanged.connect(self.updateControls)

        # Handle buttons
        self.ui.action_Read.triggered.connect(self.readFiles)
        self.ui.action_Initialize.triggered.connect(self.initialize)
        self.ui.action_Process.triggered.connect(self.process)
        self.ui.action_Save.triggered.connect(self.saveFiles)
        self.ui.action_About.triggered.connect(self.showAbout)
        self.ui.action_Exit.triggered.connect(self.close)

    def initialize(self):
        msgBox = QtGui.QMessageBox()
        try:
            self.ui.tableView.model().initialize()
            self.updateControls()
            msgBox.setText("Initialized %d keyframes.  Don't forget to save." % (len(self.ui.tableView.model().timelapse.keyframes)))
        except:
            msgBox.setText("Unknown error (no error handling yet).")

        msgBox.exec_()

    def process(self):
        msgBox = QtGui.QMessageBox()

        try:
            timelapse = self.ui.tableView.model().timelapse
            timelapse.ignore_grads = not self.ui.action_Process_Gradients.isChecked()
            timelapse.ignore_curves = not self.ui.action_Process_Curves.isChecked()
            timelapse.process()
            msgBox.setText("Processed %d sidecars.  Don't forget to save." % (len(self.ui.tableView.model().timelapse.filenames)))
        except StandardError, e:
            msgBox.setText("Unknown error \"%s\" (no error handling yet)." % (e))

        msgBox.exec_()

    def showAbout(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Timeroom https://github.com/lewisthompson/timeroom")
        msgBox.exec_()

    def loadDir(self):
        idx = self.ui.dirView.selectionModel().currentIndex()
        path = self.ui.dirView.model().filePath(idx)
        self.ui.action_Read.setEnabled(False)
        self.ui.tableView.model().setRootPath(path)

        idx = self.ui.tableView.model().index(0, 0)
        self.ui.tableView.setRootIndex(idx)
        self.updateControls()

    def readFiles(self):
        ret = self.ui.tableView.model().readFiles()
        if not ret:
            self.ui.action_Initialize.setEnabled(False)
            self.ui.action_Process.setEnabled(False)
            self.ui.action_Save.setEnabled(False)
        else:
            self.updateControls()

    def saveFiles(self):
        self.ui.tableView.model().timelapse.saveSideCars()

    def updateControls(self):
        files = len(self.ui.tableView.model().timelapse.filenames)
        sidecars = len(self.ui.tableView.model().timelapse.sidecars)
        keyframes = len(self.ui.tableView.model().timelapse.keyframes)

        self.ui.action_Read.setEnabled(False)
        self.ui.action_Initialize.setEnabled(False)
        self.ui.action_Process.setEnabled(False)
        self.ui.action_Save.setEnabled(False)

        if files >= 2:
            self.ui.action_Read.setEnabled(True)
        if sidecars >= 2:
            self.ui.action_Initialize.setEnabled(True)
        if keyframes >= 2:
            self.ui.action_Process.setEnabled(True)
            self.ui.action_Save.setEnabled(True)

        self.ui.statusBar.showMessage('%d XMP files (%d keyframes)' % (files, keyframes))

if __name__ == "__main__":
    # Read config file
    if getattr(sys, 'frozen', False):
        configfile = os.path.dirname(sys.executable)
    elif __file__:
        configfile = os.path.abspath(os.path.dirname(__file__))
    configfile = os.path.join(configfile, 'timeroom.ini')
    config = ConfigParser.RawConfigParser()
    config.read(configfile)
    try:
        path = config.get('Timeroom', 'directory')
    except ConfigParser.NoSectionError:
        config.add_section('Timeroom')
        path = os.getcwd()
    except ConfigParser.NoOptionError:
        path = os.getcwd()

    # Initialise GUI
    app = QtGui.QApplication(sys.argv)
    gui = TimeroomMainWindow()
    idx = gui.ui.dirView.model().index(path)
    gui.ui.dirView.setCurrentIndex(idx)
    gui.show()
    app.exec_()

    # Write config file
    idx = gui.ui.dirView.selectionModel().currentIndex()
    path = gui.ui.dirView.model().filePath(idx)
    config.set('Timeroom', 'directory', path)
    with open(configfile, 'wb') as configfile:
        config.write(configfile)

    sys.exit(0)
