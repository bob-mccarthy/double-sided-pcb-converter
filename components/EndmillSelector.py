from PySide6.QtWidgets import QWidget, QHBoxLayout,QVBoxLayout, QCheckBox, QLabel
from PySide6.QtCore import Qt, Signal
import math


# TODO make it so at least one of the checkboxes has to be selected
class EndmillSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.endMillSizes = [1/32, 1/16, 1/8] #end mill diameter in inches
        self.currEndMillSize = math.floor(1/32 * 1000) #end mill diameter in mil
        self.checkboxes = []
        layout = QHBoxLayout()
        for endMillSize in self.endMillSizes:
            self.checkboxes.append(LabelCheckBox(f"{endMillSize}\""))
            layout.addWidget(self.checkboxes[-1])
        for i in range(len(self.checkboxes)):
            #need to set default arg in lambda so it captures value of i and not the variable i
            self.checkboxes[i].toggled.connect(lambda checked, ind = i : self.__handleCheckboxChange(ind) if checked else ())
        self.checkboxes[0].setCheckState(Qt.CheckState.Checked)
        self.setLayout(layout)
    
    def getEndmillSize(self):
        return self.currEndMillSize

        
    def __handleCheckboxChange(self,unchangedIndex):
        self.currEndMillSize = math.floor(self.endMillSizes[unchangedIndex] * 1000)
        for i in range(len(self.checkboxes)):
            if i == unchangedIndex:
                continue
            self.checkboxes[i].setCheckState(Qt.CheckState.Unchecked)
    
    
        
        
class LabelCheckBox(QWidget):
    toggled = Signal(bool)

    def __init__(self, label):
        super().__init__()
        self.label = QLabel(label)
        self.checkbox = QCheckBox()
        self.checkbox.clicked.connect(self.__emitSignal)
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.checkbox, alignment=Qt.AlignHCenter)
        layout.addWidget(self.label, alignment=Qt.AlignHCenter)
        layout.setSpacing(4)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

    def setCheckState(self, checkState):
        self.checkbox.setCheckState(checkState)

    def __emitSignal(self, currState):
        self.toggled.emit(currState)


