import sys
import math
import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QApplication, QGridLayout, QDoubleSpinBox, \
    QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QPushButton, QFrame


class FootingGenerator(QMainWindow, QWidget):


    def __init__(self):
        super().__init__()

        self.txtItr = 1
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
        self.sbc.setValue(120)
        self.sbc.setSingleStep(1)

        # self.sbc.valueChanged.connect(self.selectionchange)

        self.clearCover = QDoubleSpinBox(self)
        self.clearCover.setRange(75, 100000)
        self.clearCover.setValue(1)
        self.clearCover.setSingleStep(1)

        # self.clearCover.valueChanged.connect(self.selectionchange)

        self.sizeColumn = QDoubleSpinBox(self)
        self.sizeColumn.setRange(0, 100000)
        self.sizeColumn.setValue(400)
        self.sizeColumn.setSingleStep(1)

        # self.sizeColumn.valueChanged.connect(self.selectionchange)

        self.sizeColumn2 = QDoubleSpinBox(self)
        self.sizeColumn2.setRange(0, 100000)
        self.sizeColumn2.setValue(600)
        self.sizeColumn2.setSingleStep(1)

        # self.sizeColumn2.valueChanged.connect(self.selectionchange)

        self.axialLoad = QDoubleSpinBox(self)
        self.axialLoad.setRange(0, 100000)
        self.axialLoad.setValue(600)
        self.axialLoad.setSingleStep(1)

        # self.axialLoad.valueChanged.connect(self.selectionchange)

        self.submitButton = QPushButton(self)
        self.submitButton.setStyleSheet('QPushButton {background-color: #7393B3; color: white;}')
        self.submitButton.setText('Submit')
        self.submitButton.clicked.connect(self.selectionchange)

        submitLayout = QWidget()
        submitLayout.setLayout(QGridLayout())
        submitLayout.layout().addWidget(self.submitButton, 0, 4)

        self.line = QFrame()
        # self.line.setGeometry(QRect(60, 110, 751, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.label1 = QLabel("Safe Bearing Capacity (KN/sq.m)")
        self.label2 = QLabel("Effective Cover (in mm)")
        self.label3 = QLabel("Length (in mm)")
        self.label15 = QLabel("Breadth (in mm)")
        self.label4 = QLabel("Axial Load (in KN)")
        self.label5 = QLabel("Grade of Concrete")
        self.label6 = QLabel("Grade of Steel")

        self.cbConcrete = QComboBox()
        self.cbConcrete.addItems(["M20", "M25", "M30"])
        # self.cbConcrete.currentIndexChanged.connect(self.selectionchange)

        self.cbSteel = QComboBox()
        self.cbSteel.addItems(["Fe250", "Fe415", "Fe500"])
        # self.cbSteel.currentIndexChanged.connect(self.selectionchange)

        boxes.layout().addWidget(self.label1, 0, 0)
        boxes.layout().addWidget(self.label2, 0, 1)
        boxes.layout().addWidget(self.label3, 0, 2)
        boxes.layout().addWidget(self.label15, 0, 3)
        boxes.layout().addWidget(self.label4, 0, 4)
        boxes.layout().addWidget(self.sbc, 1, 0)
        boxes.layout().addWidget(self.clearCover, 1, 1)
        boxes.layout().addWidget(self.sizeColumn, 1, 2)
        boxes.layout().addWidget(self.sizeColumn2, 1, 3)
        boxes.layout().addWidget(self.axialLoad, 1, 4)

        area = QWidget()
        area.setLayout(QHBoxLayout())
        self.label7 = QLabel("Plan Area")
        self.label7.setFont(QFont("Arial", 15))
        self.label8 = QLabel("")
        self.label8.setStyleSheet("background-color: white; border: 2px solid #61b2b8;")
        self.label8.setFont(QFont("Arial", 15))
        area.layout().addWidget(self.label7)
        area.layout().addWidget(self.label8)

        effectiveDepth = QWidget()
        effectiveDepth.setLayout(QHBoxLayout())
        self.label9 = QLabel("Effective depth of footing")
        self.label9.setFont(QFont("Arial", 15))
        self.label10 = QLabel("")
        self.label10.setStyleSheet("background-color: white; border: 2px solid #61b2b8;")
        self.label10.setFont(QFont("Arial", 15))
        effectiveDepth.layout().addWidget(self.label9)
        effectiveDepth.layout().addWidget(self.label10)

        depthOfFooting1 = QWidget()
        depthOfFooting1.setLayout(QHBoxLayout())
        self.label11 = QLabel("Overall depth")
        self.label11.setFont(QFont("Arial", 15))
        self.label12 = QLabel("")
        self.label12.setStyleSheet("background-color: white; border: 2px solid #61b2b8;")
        self.label12.setFont(QFont("Arial", 15))
        depthOfFooting1.layout().addWidget(self.label11)
        depthOfFooting1.layout().addWidget(self.label12)

        areaOfReinforcement = QWidget()
        areaOfReinforcement.setLayout(QHBoxLayout())
        self.label13 = QLabel("Area of Reinforcement")
        self.label13.setFont(QFont("Arial", 15))
        self.label14 = QLabel("")
        self.label14.setStyleSheet("background-color: white; border: 2px solid #61b2b8;")
        self.label14.setFont(QFont("Arial", 15))
        areaOfReinforcement.layout().addWidget(self.label13)
        areaOfReinforcement.layout().addWidget(self.label14)

        self.mainWidget.layout().addWidget(boxes)
        self.mainWidget.layout().addWidget(self.label5)
        self.mainWidget.layout().addWidget(self.cbConcrete)
        self.mainWidget.layout().addWidget(self.label6)
        self.mainWidget.layout().addWidget(self.cbSteel)
        self.mainWidget.layout().addWidget(submitLayout)
        self.mainWidget.layout().addWidget(self.line)
        self.mainWidget.layout().addWidget(area)
        self.mainWidget.layout().addWidget(effectiveDepth)
        self.mainWidget.layout().addWidget(depthOfFooting1)
        self.mainWidget.layout().addWidget(areaOfReinforcement)

        self.show()

    @staticmethod
    def programExit():
        os._exit(0)

    def selectionchange(self):

        filePath = "footing" + str(self.txtItr) + ".txt"
        sys.stdout = open(str(filePath), 'w')

        inputL = max(self.sizeColumn.value(), self.sizeColumn2.value())
        inputB = min(self.sizeColumn.value(), self.sizeColumn2.value())
        concrete = int(self.cbConcrete.currentText()[1:3])
        steel = int(self.cbSteel.currentText()[2:5])

        if concrete == 20:
            tauBD = 1.2
        elif concrete == 25:
            tauBD = 1.4
        elif concrete == 30:
            tauBD = 1.5
        elif concrete == 35:
            tauBD = 1.7
        else:
            tauBD = 1.9

        if steel == 415:
            steelConstant = 0.138
            tauBD = 1.6 * tauBD
        elif steel == 250:
            steelConstant = 0.148
        else:
            steelConstant = 0.133
            tauBD = 1.6 * tauBD

        print('\n')
        print("GIVEN DATA:")
        print("Axial Service Load = P = " + str(self.axialLoad.value()) + " kN")
        print("Size of Column = " + str(inputB) + " mm by " + str(inputL) + " mm")
        print("Safe Bearing Capacity of Soil = " + str(self.sbc.value()) + " kN/sq.m")
        print(self.cbConcrete.currentText() + " grade concrete and " + self.cbSteel.currentText() + " bars.")
        print("\n")

        newLoad = self.axialLoad.value() + self.axialLoad.value() * 0.10
        area = newLoad / self.sbc.value()
        area = float("{:.2f}".format(area))

        ratio = self.sizeColumn.value() / self.sizeColumn2.value()

        b = math.sqrt(area / ratio)
        l = ratio * b

        b = float("{:.0f}".format(b))
        l = float("{:.0f}".format(l))

        temp = max(l, b)
        b = min(l, b)
        l = temp

        planArea = l * b

        self.label8.setText(str(b) + " * " + str(l) + " = " + str(planArea) + " sq.m")

        netUpwardSoilPressure = (newLoad * 1.5) / planArea
        netUpwardSoilPressure = float("{:.2f}".format(netUpwardSoilPressure))

        m1 = netUpwardSoilPressure * l * (b - inputB / 1000) * (b - inputB / 1000) / 8

        m2 = netUpwardSoilPressure * b * (l - inputL / 1000) * (l - inputL / 1000) / 8

        mu = max(m1, m2)

        print("SIZE OF FOOTING:")
        print("Weight of Footing and back fill at 10% = " + str(self.axialLoad.value() * 0.1) + " kN")
        print("Total Load = " + str(newLoad) + " kN")
        print("Area of Footing = " + str(area) + " sq.m")
        print("Size of Footing = " + str(l) + " m * " + str(b) + " m")
        print("Net upward soil pressure at ultimate loads with a load factor of 1.5 = " + str(netUpwardSoilPressure) +
              " kN/sq.m")
        print("Ultimate Bending Moment in Longer Direction = " + str(m1) + " kN.m")
        print("Ultimate Bending Moment in Shorter Direction = " + str(m2) + " kN.m")

        print("Maximum Ultimate Moment = " + str(mu) + " kN.m")
        print("\n")

        if m1 > m2:
            depthMu = math.sqrt(m1 * 1000000 / (steelConstant * concrete * l * 1000))
        else:
            depthMu = math.sqrt(m2 * 1000000 / (steelConstant * concrete * b * 1000))

        depthMu = self.myround(depthMu, 25)

        tauv1 = 1
        tauc1 = 0
        tauv2 = 1
        tauc2 = 0

        designLoad = newLoad * 1.5

        print("ONE WAY SHEAR CALCULATIONS:")
        itr = 1
        while tauv1 > tauc1 or tauv2 > tauc2:

            calc1 = 1 - math.sqrt(
                1 - (4.6 * m1 * 1000000) / (concrete * l * 1000 * (depthMu - 12) * (depthMu - 12)))

            areaOfSteel = 0.5 * concrete * l * 1000 * (depthMu - 12) * calc1 / steel
            areaOfSteel = float("{:.2f}".format(areaOfSteel))

            calc2 = 1 - math.sqrt(
                1 - (4.6 * m2 * 1000000) / (concrete * b * 1000 * depthMu * depthMu))

            areaOfSteel2 = 0.5 * concrete * b * 1000 * depthMu * calc2 / steel
            areaOfSteel2 = float("{:.2f}".format(areaOfSteel2))

            percentageSteel = 100 * areaOfSteel / (l * 1000 * depthMu)
            percentageSteel = float("{:.2f}".format(percentageSteel))

            percentageSteel2 = 100 * areaOfSteel2 / (b * 1000 * depthMu)
            percentageSteel2 = float("{:.2f}".format(percentageSteel2))

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
            tauc2 = 0

            prevIndex = 0
            nextIndex = 0
            for i in range(1, 13):
                if ptpercentage[i] > percentageSteel:
                    nextIndex = i
                    break
                prevIndex = i

            slope = (tauc[nextIndex] - tauc[prevIndex]) / (ptpercentage[nextIndex] - ptpercentage[prevIndex])
            tauc1 = tauc[prevIndex] + slope * (percentageSteel - ptpercentage[prevIndex])

            prevIndex = 0
            nextIndex = 0
            for i in range(1, 13):
                if ptpercentage[i] > percentageSteel2:
                    nextIndex = i
                    break
                prevIndex = i

            slope2 = (tauc[nextIndex] - tauc[prevIndex]) / (ptpercentage[nextIndex] - ptpercentage[prevIndex])
            tauc2 = tauc[prevIndex] + slope2 * (percentageSteel2 - ptpercentage[prevIndex])

            ultimateShear = netUpwardSoilPressure * l * ((b - inputB / 1000) / 2 - depthMu / 1000)
            tauv1 = ultimateShear / (l * depthMu)

            ultimateShear2 = netUpwardSoilPressure * b * ((l - inputL / 1000) / 2 - depthMu / 1000)
            tauv2 = ultimateShear2 / (b * depthMu)

            ultimateShear = float("{:.2f}".format(ultimateShear))
            ultimateShear2 = float("{:.2f}".format(ultimateShear2))
            tauv1 = float("{:.4f}".format(tauv1))
            tauv2 = float("{:.4f}".format(tauv2))
            tauc1 = float("{:.4f}".format(tauc1))
            tauc2 = float("{:.4f}".format(tauc2))

            print("Iteration " + str(itr))
            print("Ast1 = " + str(areaOfSteel) + " sq.mm")
            print("Ast2 = " + str(areaOfSteel2) + " sq.mm")
            print("Pst1 = " + str(percentageSteel) + " %")
            print("Pst2 = " + str(percentageSteel2) + " %")
            print("One Way Shear in Longer Direction = " + str(ultimateShear) + " kN")
            print("One Way Shear in Shorter Direction = " + str(ultimateShear2) + " kN")

            # print("tauv1 = " + str(tauv1))
            # print("tauv2 = " + str(tauv2))
            # print("tauc1 = " + str(tauc1))
            # print("tauc2 = " + str(tauc2))

            print("tauc1 is " + str(tauc1) + " and tauv1 is " + str(tauv1) + " for depth " + str(depthMu) + " mm")
            print("tauc2 is " + str(tauc2) + " and tauv2 is " + str(tauv2) + " for depth " + str(depthMu) + " mm")
            print('\n')

            depthMu += 25
            itr += 1

        depthMu -= 25

        depthOfFooting2 = depthMu

        taup = 0.25 * math.sqrt(concrete)

        print("TWO WAY SHEAR CALCULATIONS:")
        flag = 0

        perimeter = 2 * (inputL / 1000 + depthOfFooting2 / 1000 + inputB / 1000 + depthOfFooting2 / 1000)
        punchingShear = netUpwardSoilPressure * (l * b - (inputL / 1000 + depthOfFooting2 / 1000) * (inputB / 1000 +
                                                                                                     depthOfFooting2 / 1000))

        punchingShearStress = punchingShear / (perimeter * depthOfFooting2)

        while taup < punchingShearStress:
            flag = 1
            taup = 0.25 * math.sqrt(concrete)
            perimeter = 2 * (inputL / 1000 + depthOfFooting2 + inputB / 1000 + depthOfFooting2)
            punchingShear = netUpwardSoilPressure * (l * b - (inputL / 1000 + depthOfFooting2) * (inputB / 1000 +
                                                                                                  depthOfFooting2))
            punchingShearStress = punchingShear / (perimeter * depthOfFooting2)
            print("For Depth of " + str(depthOfFooting2) + " mm")
            print("Punching Shear = " + str(punchingShear) + " kN")
            print("Punching Shear Stress = " + str(punchingShearStress) + " N/sq.mm")
            print("Permissible shear stress = " + str(taup) + " N/sq.mm")

            depthOfFooting2 += 25

        if flag == 0:
            print("No Iteration required")
            print("For Depth of " + str(depthOfFooting2) + " mm")
            print("Punching Shear = " + str(punchingShear) + " kN")
            print("Punching Shear Stress = " + str(punchingShearStress) + " N/sq.mm")
            print("Permissible shear stress = " + str(taup) + " N/sq.mm")

        else:
            depthOfFooting2 -= 25

        print('\n')

        depth = max(depthMu, depthOfFooting2)

        self.label10.setText(str(depth) + " mm")

        overallDepth = depth + self.clearCover.value()
        self.label12.setText(str(overallDepth) + " mm")

        unitMoment = m1 / l

        calc3 = 1 - math.sqrt(
            1 - (4.6 * unitMoment * 1000000) / (concrete * 1000 * depth * depth))

        unitAreaOfSteel = 0.5 * concrete * 1000 * depth * calc3 / steel
        unitAreaOfSteel = float("{:.2f}".format(unitAreaOfSteel))

        unitMoment2 = m2 / b

        calc4 = 1 - math.sqrt(
            1 - (4.6 * unitMoment2 * 1000000) / (concrete * 1000 * depth * depth))

        unitAreaOfSteel2 = 0.5 * concrete * 1000 * depth * calc4 / steel
        unitAreaOfSteel2 = float("{:.2f}".format(unitAreaOfSteel2))

        self.label14.setText(str(unitAreaOfSteel) + " sq.mm/m and " + str(unitAreaOfSteel2) + " sq.mm/m")

        print("Reinforcement Details:")
        print("Area of Reinforcement in Longer Direction = " + str(unitAreaOfSteel) + " sq.mm/m")
        print("Area of Reinforcement in Shorter Direction = " + str(unitAreaOfSteel2) + " sq.mm/m")

        diaOfBar = [6, 8, 10, 12, 16, 20, 25, 32, 40]

        for i in diaOfBar:
            spacing = 1000 * 3.14 * i * i / (4 * unitAreaOfSteel)
            spacing = float("{:.0f}".format(spacing))
            if 100 <= spacing <= 300:
                print("Spacing for Long " + str(i) + " mm dia bars is " + str(spacing))

        for i in diaOfBar:
            spacing2 = 1000 * 3.14 * i * i / (4 * unitAreaOfSteel2)
            spacing2 = float("{:.0f}".format(spacing2))
            if 100 <= spacing2 <= 300:
                print("Spacing for Short " + str(i) + " mm dia bars is " + str(spacing2))

        bearingStress = self.axialLoad.value() * 1.5 * 1000 / (inputB * inputL)
        a1 = min(l * b * 1000000, (inputB + 4 * depth) * (inputL + 4 * depth))
        areaRatio = a1 / (inputL * inputB)
        if areaRatio > 4:
            areaRatio = 4
        permissibleStress = 0.45 * concrete * math.sqrt(areaRatio)

        print('\n')
        print("Force Transfer at Column Base:")
        print("Ultimate Compressive force at Column Base " + str(self.axialLoad.value() * 1.5) + " kN")
        print("Limiting Bearing Stress at Column footing interface " + str(permissibleStress) + " N/sq.mm")
        print("Actual Bearing Stress " + str(bearingStress) + " N/sq.mm")

        if bearingStress < permissibleStress:
            print("Safe in Bearing Stress")
        else:
            print("Extend Column reinforcement into footing and bent at 90 degree.")

        developmentLength = 12 * steel / (4 * tauBD)

        print('\n')
        print("Check for Development Length")
        print("Development length is " + str(developmentLength) + " mm")

        self.txtItr += 1
        sys.stdout.close()

    def myround(self, x, base):
        return base * round(x / base)

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
