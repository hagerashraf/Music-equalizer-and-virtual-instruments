# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task3GUIFINAL.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 700)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget_3.setGeometry(QtCore.QRect(2, 0, 802, 518))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.layoutWidget_3)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_3.setObjectName("widget_3")
        self.splitter_3 = QtWidgets.QSplitter(self.widget_3)
        self.splitter_3.setGeometry(QtCore.QRect(0, 10, 761, 291))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.MainGraph = QtWidgets.QWidget(self.splitter_3)
        self.MainGraph.setMinimumSize(QtCore.QSize(400, 0))
        self.MainGraph.setObjectName("MainGraph")
        self.MainSpectroControls_3 = QtWidgets.QWidget(self.splitter_3)
        self.MainSpectroControls_3.setMinimumSize(QtCore.QSize(60, 0))
        self.MainSpectroControls_3.setMaximumSize(QtCore.QSize(65, 16777215))
        self.MainSpectroControls_3.setObjectName("MainSpectroControls_3")
        self.MainControl = QtWidgets.QToolBox(self.MainSpectroControls_3)
        self.MainControl.setGeometry(QtCore.QRect(0, 2, 69, 281))
        self.MainControl.setObjectName("MainControl")
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setGeometry(QtCore.QRect(0, 0, 69, 227))
        self.page_13.setObjectName("page_13")
        self.SpectroButton = QtWidgets.QPushButton(self.page_13)
        self.SpectroButton.setGeometry(QtCore.QRect(0, 20, 61, 23))
        self.SpectroButton.setObjectName("SpectroButton")
        self.PlayButton = QtWidgets.QPushButton(self.page_13)
        self.PlayButton.setGeometry(QtCore.QRect(0, 60, 61, 23))
        self.PlayButton.setObjectName("PlayButton")
        self.OpenFileButton = QtWidgets.QPushButton(self.page_13)
        self.OpenFileButton.setGeometry(QtCore.QRect(0, 0, 61, 23))
        self.OpenFileButton.setStyleSheet("radius:\"3\";")
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.PauseButton = QtWidgets.QPushButton(self.page_13)
        self.PauseButton.setGeometry(QtCore.QRect(0, 80, 61, 23))
        self.PauseButton.setObjectName("PauseButton")
        self.FasterButton = QtWidgets.QPushButton(self.page_13)
        self.FasterButton.setGeometry(QtCore.QRect(0, 140, 61, 23))
        self.FasterButton.setObjectName("FasterButton")
        self.SlowerButton = QtWidgets.QPushButton(self.page_13)
        self.SlowerButton.setGeometry(QtCore.QRect(0, 120, 61, 23))
        self.SlowerButton.setObjectName("SlowerButton")
        self.ZoomInButton = QtWidgets.QPushButton(self.page_13)
        self.ZoomInButton.setGeometry(QtCore.QRect(0, 180, 61, 23))
        self.ZoomInButton.setObjectName("ZoomInButton")
        self.ZoomOutButton = QtWidgets.QPushButton(self.page_13)
        self.ZoomOutButton.setGeometry(QtCore.QRect(0, 200, 61, 23))
        self.ZoomOutButton.setObjectName("ZoomOutButton")
        self.MainControl.addItem(self.page_13, "")
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setGeometry(QtCore.QRect(0, 0, 69, 227))
        self.page_14.setObjectName("page_14")
        self.AudioVolumeSlider = QtWidgets.QSlider(self.page_14)
        self.AudioVolumeSlider.setGeometry(QtCore.QRect(20, 20, 22, 61))
        self.AudioVolumeSlider.setMaximum(10)
        self.AudioVolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.AudioVolumeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.AudioVolumeSlider.setTickInterval(1)
        self.AudioVolumeSlider.setObjectName("AudioVolumeSlider")
        self.MainVolumeLabel_3 = QtWidgets.QLabel(self.page_14)
        self.MainVolumeLabel_3.setGeometry(QtCore.QRect(10, -10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MainVolumeLabel_3.setFont(font)
        self.MainVolumeLabel_3.setObjectName("MainVolumeLabel_3")
        self.SpectroLabel_3 = QtWidgets.QLabel(self.page_14)
        self.SpectroLabel_3.setGeometry(QtCore.QRect(10, 90, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SpectroLabel_3.setFont(font)
        self.SpectroLabel_3.setObjectName("SpectroLabel_3")
        self.PaletteComboBox = QtWidgets.QComboBox(self.page_14)
        self.PaletteComboBox.setGeometry(QtCore.QRect(0, 120, 61, 22))
        self.PaletteComboBox.setObjectName("PaletteComboBox")
        self.PaletteComboBox.addItem("")
        self.Spec_minSLider = QtWidgets.QSlider(self.page_14)
        self.Spec_minSLider.setGeometry(QtCore.QRect(0, 162, 61, 20))
        self.Spec_minSLider.setMaximum(255)
        self.Spec_minSLider.setOrientation(QtCore.Qt.Horizontal)
        self.Spec_minSLider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Spec_minSLider.setObjectName("Spec_minSLider")
        self.Spec_MaxSlider = QtWidgets.QSlider(self.page_14)
        self.Spec_MaxSlider.setGeometry(QtCore.QRect(0, 202, 61, 20))
        self.Spec_MaxSlider.setMaximum(255)
        self.Spec_MaxSlider.setTracking(True)
        self.Spec_MaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Spec_MaxSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Spec_MaxSlider.setObjectName("Spec_MaxSlider")
        self.MainControl.addItem(self.page_14, "")
        self.SpectroChannel = QtWidgets.QWidget(self.splitter_3)
        self.SpectroChannel.setObjectName("SpectroChannel")
        self.verticalLayout_3.addWidget(self.widget_3)
        self.Equalizer_5 = QtWidgets.QWidget(self.layoutWidget_3)
        self.Equalizer_5.setObjectName("Equalizer_5")
        self.EqualizerControl = QtWidgets.QToolBox(self.Equalizer_5)
        self.EqualizerControl.setGeometry(QtCore.QRect(10, 20, 91, 171))
        self.EqualizerControl.setObjectName("EqualizerControl")
        self.ImageDisplay = QtWidgets.QWidget()
        self.ImageDisplay.setGeometry(QtCore.QRect(0, 0, 91, 117))
        self.ImageDisplay.setObjectName("ImageDisplay")
        self.ImageOFInstHolder = QtWidgets.QLabel(self.ImageDisplay)
        self.ImageOFInstHolder.setGeometry(QtCore.QRect(6, 2, 81, 111))
        self.ImageOFInstHolder.setObjectName("ImageOFInstHolder")
        self.EqualizerControl.addItem(self.ImageDisplay, "")
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setGeometry(QtCore.QRect(0, 0, 91, 117))
        self.page_22.setObjectName("page_22")
        self.Instrument1 = QtWidgets.QPushButton(self.page_22)
        self.Instrument1.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.Instrument1.setObjectName("Instrument1")
        self.Instrument2 = QtWidgets.QPushButton(self.page_22)
        self.Instrument2.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.Instrument2.setObjectName("Instrument2")
        self.Instrument3 = QtWidgets.QPushButton(self.page_22)
        self.Instrument3.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.Instrument3.setObjectName("Instrument3")
        self.EqualizerControl.addItem(self.page_22, "")
        self.EqualizerVolume = QtWidgets.QSlider(self.Equalizer_5)
        self.EqualizerVolume.setGeometry(QtCore.QRect(180, 20, 22, 141))
        self.EqualizerVolume.setMaximum(10)
        self.EqualizerVolume.setOrientation(QtCore.Qt.Vertical)
        self.EqualizerVolume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EqualizerVolume.setObjectName("EqualizerVolume")
        self.EqualizerGain = QtWidgets.QSlider(self.Equalizer_5)
        self.EqualizerGain.setGeometry(QtCore.QRect(280, 20, 22, 141))
        self.EqualizerGain.setMaximum(10)
        self.EqualizerGain.setOrientation(QtCore.Qt.Vertical)
        self.EqualizerGain.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EqualizerGain.setObjectName("EqualizerGain")
        self.verticalSlider_24 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_24.setGeometry(QtCore.QRect(380, 20, 22, 141))
        self.verticalSlider_24.setMaximum(10)
        self.verticalSlider_24.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_24.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_24.setObjectName("verticalSlider_24")
        self.verticalSlider_25 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_25.setGeometry(QtCore.QRect(480, 20, 22, 141))
        self.verticalSlider_25.setMaximum(10)
        self.verticalSlider_25.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_25.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_25.setObjectName("verticalSlider_25")
        self.verticalSlider_26 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_26.setGeometry(QtCore.QRect(580, 20, 22, 141))
        self.verticalSlider_26.setMaximum(10)
        self.verticalSlider_26.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_26.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_26.setObjectName("verticalSlider_26")
        self.verticalSlider_27 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_27.setGeometry(QtCore.QRect(680, 20, 22, 141))
        self.verticalSlider_27.setMaximum(10)
        self.verticalSlider_27.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_27.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_27.setObjectName("verticalSlider_27")
        self.VolumeLabel_19 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_19.setGeometry(QtCore.QRect(170, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_19.setFont(font)
        self.VolumeLabel_19.setObjectName("VolumeLabel_19")
        self.VolumeLabel_20 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_20.setGeometry(QtCore.QRect(280, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_20.setFont(font)
        self.VolumeLabel_20.setObjectName("VolumeLabel_20")
        self.VolumeLabel_21 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_21.setGeometry(QtCore.QRect(380, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_21.setFont(font)
        self.VolumeLabel_21.setObjectName("VolumeLabel_21")
        self.Equalizer_6 = QtWidgets.QWidget(self.Equalizer_5)
        self.Equalizer_6.setGeometry(QtCore.QRect(420, 180, 800, 210))
        self.Equalizer_6.setObjectName("Equalizer_6")
        self.verticalSlider_28 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_28.setGeometry(QtCore.QRect(180, 20, 22, 141))
        self.verticalSlider_28.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_28.setObjectName("verticalSlider_28")
        self.verticalSlider_29 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_29.setGeometry(QtCore.QRect(280, 20, 22, 141))
        self.verticalSlider_29.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_29.setObjectName("verticalSlider_29")
        self.verticalSlider_30 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_30.setGeometry(QtCore.QRect(380, 20, 22, 141))
        self.verticalSlider_30.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_30.setObjectName("verticalSlider_30")
        self.verticalSlider_31 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_31.setGeometry(QtCore.QRect(480, 20, 22, 141))
        self.verticalSlider_31.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_31.setObjectName("verticalSlider_31")
        self.verticalSlider_32 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_32.setGeometry(QtCore.QRect(580, 20, 22, 141))
        self.verticalSlider_32.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_32.setObjectName("verticalSlider_32")
        self.verticalSlider_33 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_33.setGeometry(QtCore.QRect(680, 20, 22, 141))
        self.verticalSlider_33.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_33.setObjectName("verticalSlider_33")
        self.VolumeLabel_22 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_22.setGeometry(QtCore.QRect(170, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_22.setFont(font)
        self.VolumeLabel_22.setObjectName("VolumeLabel_22")
        self.VolumeLabel_23 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_23.setGeometry(QtCore.QRect(280, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_23.setFont(font)
        self.VolumeLabel_23.setObjectName("VolumeLabel_23")
        self.VolumeLabel_24 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_24.setGeometry(QtCore.QRect(380, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_24.setFont(font)
        self.VolumeLabel_24.setObjectName("VolumeLabel_24")
        self.VolumeLabel_25 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_25.setGeometry(QtCore.QRect(470, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_25.setFont(font)
        self.VolumeLabel_25.setObjectName("VolumeLabel_25")
        self.VolumeLabel_26 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_26.setGeometry(QtCore.QRect(570, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_26.setFont(font)
        self.VolumeLabel_26.setObjectName("VolumeLabel_26")
        self.VolumeLabel_27 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_27.setGeometry(QtCore.QRect(670, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_27.setFont(font)
        self.VolumeLabel_27.setObjectName("VolumeLabel_27")
        self.verticalLayout_3.addWidget(self.Equalizer_5)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_6)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 761, 531))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.piano = QtWidgets.QPushButton(self.page_19)
        self.piano.setGeometry(QtCore.QRect(20, 170, 181, 171))
        self.piano.setText("")
        self.piano.setObjectName("piano")
        self.textEdit = QtWidgets.QTextEdit(self.page_19)
        self.textEdit.setGeometry(QtCore.QRect(240, 10, 256, 61))
        self.textEdit.setObjectName("textEdit")
        self.drums = QtWidgets.QPushButton(self.page_19)
        self.drums.setGeometry(QtCore.QRect(280, 170, 191, 171))
        self.drums.setText("")
        self.drums.setObjectName("drums")
        self.bangos = QtWidgets.QPushButton(self.page_19)
        self.bangos.setGeometry(QtCore.QRect(530, 170, 191, 171))
        self.bangos.setText("")
        self.bangos.setObjectName("bangos")
        self.stackedWidget.addWidget(self.page_19)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.label = QtWidgets.QLabel(self.page_20)
        self.label.setGeometry(QtCore.QRect(200, 200, 461, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pianoplay2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pianoA = QtWidgets.QPushButton(self.page_20)
        self.pianoA.setGeometry(QtCore.QRect(200, 360, 31, 28))
        self.pianoA.setObjectName("pianoA")
        self.pianoS = QtWidgets.QPushButton(self.page_20)
        self.pianoS.setGeometry(QtCore.QRect(250, 360, 31, 28))
        self.pianoS.setObjectName("pianoS")
        self.pianoD = QtWidgets.QPushButton(self.page_20)
        self.pianoD.setGeometry(QtCore.QRect(300, 360, 31, 28))
        self.pianoD.setObjectName("pianoD")
        self.pianoF = QtWidgets.QPushButton(self.page_20)
        self.pianoF.setGeometry(QtCore.QRect(340, 360, 31, 28))
        self.pianoF.setObjectName("pianoF")
        self.pianoG = QtWidgets.QPushButton(self.page_20)
        self.pianoG.setGeometry(QtCore.QRect(390, 360, 31, 28))
        self.pianoG.setObjectName("pianoG")
        self.pianoH = QtWidgets.QPushButton(self.page_20)
        self.pianoH.setGeometry(QtCore.QRect(440, 360, 31, 28))
        self.pianoH.setObjectName("pianoH")
        self.pianoJ = QtWidgets.QPushButton(self.page_20)
        self.pianoJ.setGeometry(QtCore.QRect(480, 360, 31, 28))
        self.pianoJ.setObjectName("pianoJ")
        self.pianoK = QtWidgets.QPushButton(self.page_20)
        self.pianoK.setGeometry(QtCore.QRect(530, 360, 31, 28))
        self.pianoK.setObjectName("pianoK")
        self.pianoL = QtWidgets.QPushButton(self.page_20)
        self.pianoL.setGeometry(QtCore.QRect(580, 360, 31, 28))
        self.pianoL.setObjectName("pianoL")
        self.pianoLast = QtWidgets.QPushButton(self.page_20)
        self.pianoLast.setGeometry(QtCore.QRect(620, 360, 31, 28))
        self.pianoLast.setObjectName("pianoLast")
        self.pianoE = QtWidgets.QPushButton(self.page_20)
        self.pianoE.setGeometry(QtCore.QRect(230, 280, 31, 28))
        self.pianoE.setObjectName("pianoE")
        self.pianoR = QtWidgets.QPushButton(self.page_20)
        self.pianoR.setGeometry(QtCore.QRect(280, 280, 31, 28))
        self.pianoR.setObjectName("pianoR")
        self.pianoT = QtWidgets.QPushButton(self.page_20)
        self.pianoT.setGeometry(QtCore.QRect(370, 280, 31, 28))
        self.pianoT.setObjectName("pianoT")
        self.pianoY = QtWidgets.QPushButton(self.page_20)
        self.pianoY.setGeometry(QtCore.QRect(420, 280, 31, 28))
        self.pianoY.setObjectName("pianoY")
        self.pianoI = QtWidgets.QPushButton(self.page_20)
        self.pianoI.setGeometry(QtCore.QRect(550, 280, 31, 28))
        self.pianoI.setObjectName("pianoI")
        self.pianoU = QtWidgets.QPushButton(self.page_20)
        self.pianoU.setGeometry(QtCore.QRect(460, 280, 31, 28))
        self.pianoU.setObjectName("pianoU")
        self.pianoO = QtWidgets.QPushButton(self.page_20)
        self.pianoO.setGeometry(QtCore.QRect(600, 280, 31, 28))
        self.pianoO.setObjectName("pianoO")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_20)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.label_2 = QtWidgets.QLabel(self.page_23)
        self.label_2.setGeometry(QtCore.QRect(190, 130, 421, 281))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_23)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 531, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../bangos1.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.bangosW = QtWidgets.QPushButton(self.page_23)
        self.bangosW.setGeometry(QtCore.QRect(540, 210, 31, 28))
        self.bangosW.setObjectName("bangosW")
        self.bangosQ = QtWidgets.QPushButton(self.page_23)
        self.bangosQ.setGeometry(QtCore.QRect(270, 200, 31, 28))
        self.bangosQ.setObjectName("bangosQ")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.label_4 = QtWidgets.QLabel(self.page_24)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 671, 391))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../blog-graphics-labeled-drum-kit.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.drumsC = QtWidgets.QPushButton(self.page_24)
        self.drumsC.setGeometry(QtCore.QRect(540, 380, 31, 31))
        self.drumsC.setObjectName("drumsC")
        self.drumsB = QtWidgets.QPushButton(self.page_24)
        self.drumsB.setGeometry(QtCore.QRect(580, 240, 31, 31))
        self.drumsB.setObjectName("drumsB")
        self.drumsZ = QtWidgets.QPushButton(self.page_24)
        self.drumsZ.setGeometry(QtCore.QRect(260, 320, 31, 31))
        self.drumsZ.setObjectName("drumsZ")
        self.drumsM = QtWidgets.QPushButton(self.page_24)
        self.drumsM.setGeometry(QtCore.QRect(390, 240, 31, 31))
        self.drumsM.setObjectName("drumsM")
        self.drumsV = QtWidgets.QPushButton(self.page_24)
        self.drumsV.setGeometry(QtCore.QRect(660, 320, 31, 31))
        self.drumsV.setObjectName("drumsV")
        self.drumsX = QtWidgets.QPushButton(self.page_24)
        self.drumsX.setGeometry(QtCore.QRect(360, 340, 31, 31))
        self.drumsX.setObjectName("drumsX")
        self.drums1 = QtWidgets.QPushButton(self.page_24)
        self.drums1.setGeometry(QtCore.QRect(290, 190, 31, 31))
        self.drums1.setObjectName("drums1")
        self.drumsN = QtWidgets.QPushButton(self.page_24)
        self.drumsN.setGeometry(QtCore.QRect(480, 250, 31, 31))
        self.drumsN.setObjectName("drumsN")
        self.drumsSlash = QtWidgets.QPushButton(self.page_24)
        self.drumsSlash.setGeometry(QtCore.QRect(460, 350, 31, 31))
        self.drumsSlash.setObjectName("drumsSlash")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_24)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.MainControl.setCurrentIndex(0)
        self.EqualizerControl.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SpectroButton.setText(_translate("MainWindow", "Spectro"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.OpenFileButton.setText(_translate("MainWindow", "Open File"))
        self.PauseButton.setText(_translate("MainWindow", "Stop"))
        self.FasterButton.setText(_translate("MainWindow", "Faster"))
        self.SlowerButton.setText(_translate("MainWindow", "Slower"))
        self.ZoomInButton.setText(_translate("MainWindow", "Zoom in"))
        self.ZoomOutButton.setText(_translate("MainWindow", "Zoom out"))
        self.MainControl.setItemText(self.MainControl.indexOf(self.page_13), _translate("MainWindow", "Page 1"))
        self.MainVolumeLabel_3.setText(_translate("MainWindow", "Volume"))
        self.SpectroLabel_3.setText(_translate("MainWindow", "Spectro"))
        self.PaletteComboBox.setItemText(0, _translate("MainWindow", "Palettes"))
        self.MainControl.setItemText(self.MainControl.indexOf(self.page_14), _translate("MainWindow", "Page 2"))
        self.ImageOFInstHolder.setText(_translate("MainWindow", "Image of Instr."))
        self.EqualizerControl.setItemText(self.EqualizerControl.indexOf(self.ImageDisplay), _translate("MainWindow", "Page 1"))
        self.Instrument1.setText(_translate("MainWindow", "Inst 1"))
        self.Instrument2.setText(_translate("MainWindow", "Inst 2"))
        self.Instrument3.setText(_translate("MainWindow", "Inst 3"))
        self.EqualizerControl.setItemText(self.EqualizerControl.indexOf(self.page_22), _translate("MainWindow", "Page 2"))
        self.VolumeLabel_19.setText(_translate("MainWindow", "Volume"))
        self.VolumeLabel_20.setText(_translate("MainWindow", "Gain"))
        self.VolumeLabel_21.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_22.setText(_translate("MainWindow", "Volume"))
        self.VolumeLabel_23.setText(_translate("MainWindow", "Gain"))
        self.VolumeLabel_24.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_25.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_26.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_27.setText(_translate("MainWindow", "Label3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Tab 1"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Choose an instrument to play</span></p></body></html>"))
        self.pianoA.setText(_translate("MainWindow", "A"))
        self.pianoS.setText(_translate("MainWindow", "S"))
        self.pianoD.setText(_translate("MainWindow", "D"))
        self.pianoF.setText(_translate("MainWindow", "F"))
        self.pianoG.setText(_translate("MainWindow", "G"))
        self.pianoH.setText(_translate("MainWindow", "H"))
        self.pianoJ.setText(_translate("MainWindow", "J"))
        self.pianoK.setText(_translate("MainWindow", "K"))
        self.pianoL.setText(_translate("MainWindow", "L"))
        self.pianoLast.setText(_translate("MainWindow", ":"))
        self.pianoE.setText(_translate("MainWindow", "E"))
        self.pianoR.setText(_translate("MainWindow", "R"))
        self.pianoT.setText(_translate("MainWindow", "T"))
        self.pianoY.setText(_translate("MainWindow", "Y")) 
        self.pianoI.setText(_translate("MainWindow", "I"))
        self.pianoU.setText(_translate("MainWindow", "U"))
        self.pianoO.setText(_translate("MainWindow", "O"))
        self.pushButton_3.setText(_translate("MainWindow", "back to menu"))
        self.bangosW.setText(_translate("MainWindow", "W"))
        self.bangosQ.setText(_translate("MainWindow", "Q"))
        self.pushButton_4.setText(_translate("MainWindow", "back to menu"))
        self.drumsC.setText(_translate("MainWindow", "C"))
        self.drumsB.setText(_translate("MainWindow", "B"))
        self.drumsZ.setText(_translate("MainWindow", "Z"))
        self.drumsM.setText(_translate("MainWindow", "M"))
        self.drumsV.setText(_translate("MainWindow", "V"))
        self.drumsX.setText(_translate("MainWindow", "X"))
        self.drums1.setText(_translate("MainWindow", ","))
        self.drumsN.setText(_translate("MainWindow", "N"))
        self.drumsSlash.setText(_translate("MainWindow", "/"))
        self.pushButton_5.setText(_translate("MainWindow", "back to menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
