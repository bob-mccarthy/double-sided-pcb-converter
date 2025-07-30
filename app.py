import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from components.PcbSelector import PcbSelector
from components.EndmillSelector import EndmillSelector
from generateImages import generateImages


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flip PCB")
        
        self.endMillSelect = EndmillSelector()
        
        self.generateBoards = QPushButton("Generate Boards")
        
    
        self.frontCopper = PcbSelector('Front Copper')
        self.backCopper = PcbSelector('Back Copper')
        self.outline = PcbSelector('Outline')

        self.generateBoards.clicked.connect(lambda: generateImages(self.frontCopper.getFilePath(), self.backCopper.getFilePath(), self.outline.getFilePath()))
        
        self.pcbSelectors = [self.frontCopper, self.backCopper, self.outline]
        centralWidget = QWidget()
        
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.frontCopper)
        leftLayout.addWidget(self.backCopper)

        rightLayout = QVBoxLayout()

        rightLayout.addWidget(self.outline)
        rightLayout.addWidget(self.endMillSelect)
        rightLayout.addWidget(self.generateBoards)
        
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addLayout(leftLayout)
        horizontalLayout.addLayout(rightLayout)


        leftLayout.setSpacing(0)
        centralWidget.setLayout(horizontalLayout)
        self.setMaximumHeight(1000)
        self.setCentralWidget(centralWidget)
        

    def resizeEvent(self, event):
        return super().resizeEvent(event)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()