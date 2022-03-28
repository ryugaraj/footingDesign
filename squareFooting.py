import sys
import math
import os
import numpy as np
from scipy.interpolate import interp1d

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QApplication, QGridLayout, QDoubleSpinBox, \
    QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QPushButton, QFrame


class FootingGenerator(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

        self.left = 20
        self.top = 50
        self.width = 1500
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.title = 'Footing Generator'
        self.setWindowTitle(self.title)

        # MENUBAR

        self.exit = QAction('Exit', self)
        self.exit.triggered.connect(self.programExit)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        fileMenu.addAction(self.exit)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(QVBoxLayout())
        self.setCentralWidget(self.mainWidget)

        # BOXES AND THE TIME RANGE

        boxes = QWidget()
        boxes.setLayout(QGridLayout())

        self.sbc = QDoubleSpinBox(self)
        self.sbc.setRange(1, 100000)
        self.sbc.setValue(200)
        self.sbc.setSingleStep(1)

        #self.sbc.valueChanged.connect(self.selectionchange)

        self.clearCover = QDoubleSpinBox(self)
        self.clearCover.setRange(50, 100000)
        self.clearCover.setValue(1)
        self.clearCover.setSingleStep(1)

        #self.clearCover.valueChanged.connect(self.selectionchange)

        self.sizeColumn = QDoubleSpinBox(self)
        self.sizeColumn.setRange(0, 100000)
        self.sizeColumn.setValue(450)
        self.sizeColumn.setSingleStep(1)

        #self.sizeColumn.valueChanged.connect(self.selectionchange)

        self.axialLoad = QDoubleSpinBox(self)
        self.axialLoad.setRange(0, 100000)
        self.axialLoad.setValue(1600)
        self.axialLoad.setSingleStep(1)

        #self.axialLoad.valueChanged.connect(self.selectionchange)

        self.label1 = QLabel("Safe Bearing Capacity (KN/sq.m)")
        self.label2 = QLabel("Clear Cover (in mm)")
        self.label3 = QLabel("Size of Column (in mm)")
        self.label4 = QLabel("Axial Load (in KN)")
        self.label5 = QLabel("Grade of Concrete")
        self.label6 = QLabel("Grade of Steel")

        self.submitButton = QPushButton(self)
        self.submitButton.setStyleSheet('QPushButton {background-color: #7393B3; color: white;}')
        self.submitButton.setText('Submit')
        self.submitButton.clicked.connect(self.selectionchange)

        submitLayout = QWidget()
        submitLayout.setLayout(QGridLayout())
        submitLayout.layout().addWidget(self.submitButton, 0, 4)

        self.cbConcrete = QComboBox()
        self.cbConcrete.addItems(["M20", "M25", "M30"])
        #self.cbConcrete.currentIndexChanged.connect(self.selectionchange)

        self.cbSteel = QComboBox()
        self.cbSteel.addItems(["Fe250", "Fe415", "Fe500"])
        #self.cbSteel.currentIndexChanged.connect(self.selectionchange)

        boxes.layout().addWidget(self.label1, 0, 0)
        boxes.layout().addWidget(self.label2, 0, 1)
        boxes.layout().addWidget(self.label3, 0, 2)
        boxes.layout().addWidget(self.label4, 0, 3)
        boxes.layout().addWidget(self.sbc, 1, 0)
        boxes.layout().addWidget(self.clearCover, 1, 1)
        boxes.layout().addWidget(self.sizeColumn, 1, 2)
        boxes.layout().addWidget(self.axialLoad, 1, 3)

        area = QWidget()
        area.setLayout(QHBoxLayout())
        self.label7 = QLabel("Plan area:")
        self.label7.setFont(QFont("Arial", 15))
        self.label7.setStyleSheet("color: black")
        self.label8 = QLabel("")
        self.label8.setStyleSheet("background-color: white; border: 2px solid #7393B3;")
        self.label8.setFont(QFont("Arial", 15))
        area.layout().addWidget(self.label7)
        area.layout().addWidget(self.label8)

        netUpwardPressure = QWidget()
        netUpwardPressure.setLayout(QHBoxLayout())
        self.label9 = QLabel("Net upward soil pressure:")
        self.label9.setFont(QFont("Arial", 15))
        self.label10 = QLabel("")
        self.label10.setStyleSheet("background-color: white; border: 2px solid #7393B3;")
        self.label10.setFont(QFont("Arial", 15))
        netUpwardPressure.layout().addWidget(self.label9)
        netUpwardPressure.layout().addWidget(self.label10)

        depthOfFooting1 = QWidget()
        depthOfFooting1.setLayout(QHBoxLayout())
        self.label11 = QLabel("Depth of footing:")
        self.label11.setFont(QFont("Arial", 15))
        self.label12 = QLabel("")
        self.label12.setStyleSheet("background-color: white; border: 2px solid #7393B3;")
        self.label12.setFont(QFont("Arial", 15))
        depthOfFooting1.layout().addWidget(self.label11)
        depthOfFooting1.layout().addWidget(self.label12)

        areaOfReinforcement = QWidget()
        areaOfReinforcement.setLayout(QHBoxLayout())
        self.label13 = QLabel("Area of reinforcement:")
        self.label13.setFont(QFont("Arial", 15))
        self.label14 = QLabel("")
        self.label14.setStyleSheet("background-color: white; border: 2px solid #7393B3;")
        self.label14.setFont(QFont("Arial", 15))
        areaOfReinforcement.layout().addWidget(self.label13)
        areaOfReinforcement.layout().addWidget(self.label14)

        self.line = QFrame()
        #self.line.setGeometry(QRect(60, 110, 751, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.mainWidget.layout().addWidget(boxes)
        self.mainWidget.layout().addWidget(self.label5)
        self.mainWidget.layout().addWidget(self.cbConcrete)
        self.mainWidget.layout().addWidget(self.label6)
        self.mainWidget.layout().addWidget(self.cbSteel)
        self.mainWidget.layout().addWidget(submitLayout)
        self.mainWidget.layout().addWidget(self.line)
        self.mainWidget.layout().addWidget(area)
        self.mainWidget.layout().addWidget(netUpwardPressure)
        self.mainWidget.layout().addWidget(depthOfFooting1)
        self.mainWidget.layout().addWidget(areaOfReinforcement)

        self.show()

    @staticmethod
    def programExit():
        os._exit(0)

    def selectionchange(self):

        newLoad = self.axialLoad.value() + self.axialLoad.value() * 0.15
        area = newLoad / self.sbc.value()

        size = math.sqrt(area)
        size = float("{:.1f}".format(size))

        planArea = size * size

        self.label8.setText(str(size) + " * " + str(size) + " = " + str(planArea) + " sq.m")

        netUpwardSoilPressure = (newLoad * 1.5) / planArea
        netUpwardSoilPressure = float("{:.2f}".format(netUpwardSoilPressure))
        self.label10.setText(str(netUpwardSoilPressure) + " kN/sq.m")

        depthOfFooting1 = 300

        tauv1 = 1
        tauc1 = 0

        while tauv1 > tauc1:
            designLoad = newLoad * 1.5
            moment = (designLoad * (size - self.sizeColumn.value() / 1000) * (
                    size - self.sizeColumn.value() / 1000)) / (
                             size * 8)

            concrete = int(self.cbConcrete.currentText()[1:3])
            steel = int(self.cbSteel.currentText()[2:5])

            calc1 = 1 - math.sqrt(
                1 - (4.6 * moment * 1000000) / (concrete * size * 1000 * depthOfFooting1 * depthOfFooting1))

            areaOfSteel = 0.5 * concrete * size * 1000 * depthOfFooting1 * calc1 / steel

            percentageSteel = 100 * areaOfSteel / (size * 1000 * depthOfFooting1)
            percentageSteel = float("{:.2f}".format(percentageSteel))

            if concrete == 20:
                ptpercentage = [0.15, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.5, 2.75, 3.00]
                tauc = [0.28, 0.36, 0.48, 0.56, 0.62, 0.67, 0.72, 0.75, 0.79, 0.81, 0.82, 0.82, 0.82]
            elif concrete == 25:
                ptpercentage = [0.15, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.5, 2.75, 3.00]
                tauc = [0.29, 0.36, 0.49, 0.57, 0.64, 0.70, 0.74, 0.78, 0.82, 0.85, 0.88, 0.90, 0.92]
            else:
                ptpercentage = [0.15, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.5, 2.75, 3.00]
                tauc = [0.29, 0.37, 0.50, 0.59, 0.66, 0.71, 0.76, 0.80, 0.84, 0.88, 0.91, 0.94, 0.96]

            tauc1 = 0

            prevIndex = 0
            nextIndex = 0
            for i in range(1, 13):
                if ptpercentage[i] > percentageSteel:
                    nextIndex = i
                    break
                prevIndex = i

            slope = (tauc[nextIndex] - tauc[prevIndex]) / (ptpercentage[nextIndex] - ptpercentage[prevIndex])
            tauc1 = tauc[prevIndex] + slope * (percentageSteel - ptpercentage[prevIndex])

            ultimateShear = designLoad * (size - self.sizeColumn.value() / 1000 - 2 * depthOfFooting1 / 1000) / (
                    2 * size)
            tauv1 = ultimateShear / (size * depthOfFooting1)

            #print("tauc is " + str(tauc1) + " and tauv is "+str(tauv1)+" for depth " + str(depthOfFooting1))

            depthOfFooting1 += 25

        depthOfFooting1 -= 25

        taup = 0
        taupApplied = 1
        depthOfFooting2 = depthOfFooting1

        while taup < taupApplied:
            taup = 0.25 * math.sqrt(concrete)
            a = self.sizeColumn.value() / 1000
            d = depthOfFooting2 / 1000
            l = size
            taupApplied = designLoad * (l * l - (a + d) * (a + d)) / (l * l * 4 * (a + d) * d * 1000)
            depthOfFooting2 += 25

        depthOfFooting2 -= 25

        if steel == 415:
            steelConstant = 0.138
        elif steel == 250:
            steelConstant = 0.148
        else:
            steelConstant = 0.133

        depthOfFooting3 = math.sqrt(moment/(steelConstant*concrete*size))

        depth = max(depthOfFooting1, depthOfFooting2, depthOfFooting3)

        self.label12.setText(str(depth) + " mm")

        unitMoment = moment / size

        calc2 = 1 - math.sqrt(
            1 - (4.6 * unitMoment * 1000000) / (concrete * 1000 * depth * depth))

        unitAreaOfSteel = 0.5 * concrete * 1000 * depth * calc2 / steel
        unitAreaOfSteel = float("{:.2f}".format(unitAreaOfSteel))
        self.label14.setText(str(unitAreaOfSteel) + " sq.mm/m")

        diaOfBar = [6, 8, 10, 12, 16, 20, 25, 32, 40]

        for i in diaOfBar:
            spacing = 1000 * 3.14 * i * i / (4*unitAreaOfSteel)
            spacing = float("{:.0f}".format(spacing))
            if 100 <= spacing <= 300:
                print("Spacing for " + str(i) + " mm dia bars is " + str(spacing))





    def showDialogBox(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Information: ")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


app = QApplication(sys.argv)
ex = FootingGenerator()
app.exec_()
