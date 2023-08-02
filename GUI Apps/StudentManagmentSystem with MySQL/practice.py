from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys


class AVGSpeed(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # making Widgets
        distance = QLabel("Distance(km):")
        self.distance_input = QLineEdit()

        self.cal_system = QComboBox(self)
        self.cal_system.addItems(["Metric", "Imperial"])
        self.cal_system.move(100, 100)

        time = QLabel("Time(Hours):")
        self.time_input = QLineEdit()
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        self.output_label = QLabel("")

        # Adding to Grid
        grid.addWidget(distance, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(time, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(self.cal_system, 0, 2)
        grid.addWidget(calculate_button, 2, 1, 1, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        self.setLayout(grid)

    def calculate(self):
        check_system = self.cal_system.currentText()
        speed = float(self.distance_input.text()) / float(self.time_input.text())
        if check_system == "Metric":
            speed = round(speed, 2)
            unit = "km/h"
        else:
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        self.output_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
window = AVGSpeed()
window.show()
sys.exit(app.exec())
