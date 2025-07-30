from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt

class PcbSelector(QWidget):
    def __init__(self, buttonName):
        super().__init__()
        self.fileSelect = QPushButton(buttonName)
        self.fileSelect.clicked.connect(self.loadFile)

        self.filePath = None

        self.pixmap = QPixmap(200,200)
        self.pixmap.fill(QColor(Qt.white))

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)


        layout = QVBoxLayout(self)
        layout.addWidget(self.label, stretch=9)
        layout.addWidget(self.fileSelect, stretch=1)

        layout.setSpacing(0)

        self.setLayout(layout)
    
    def getFilePath(self):
        print(self.filePath)
        return self.filePath
    

    def resizeEvent(self, event):
        self.label.setPixmap(self.pixmap.scaledToHeight(self.label.height()*.9,Qt.SmoothTransformation)) 
        #pixmap height * aspect ratio is the equal to its width
        buttonWidth = self.label.height()*.9 *(self.pixmap.width()/self.pixmap.height())
        self.fileSelect.setMaximumWidth(buttonWidth)
        return super().resizeEvent(event)
    
    def loadFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*.*)")
        if filePath:
            print(f"Selected file: {filePath}")
        self.filePath = filePath
        print(self.pixmap.load(filePath))
        self.label.setPixmap(self.pixmap.scaledToHeight(self.height()*9/10))
    



        
