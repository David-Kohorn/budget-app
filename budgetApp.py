from PyQt5.QtWidgets import QApplication, QLabel

# Configuration of app
app = QApplication([])
app.setStyle('Fusion')


label = QLabel('Budegt App!')
label.show()

if __name__ == "__main__":
    app.exec()