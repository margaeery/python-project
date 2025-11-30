import os
import sys

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"C:\Users\Маргарита\AppData\Local\Programs\Python\Python313\Lib\site-packages\PyQt5\Qt5\plugins"

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

def on_button_click():
    label.setText("Кнопка нажата!")

app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt5 с кнопкой")
window.resize(150, 100)

layout = QVBoxLayout()

label = QLabel("Жду нажатия...")
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

button = QPushButton("Нажми меня")
button.clicked.connect(on_button_click)
layout.addWidget(button)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())
