import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QSlider, QRadioButton, QButtonGroup, QMessageBox
)
from PyQt5.QtCore import Qt

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.resize(500, 350) 

        layout = QVBoxLayout()
        layout.setSpacing(12)  #spacing between widgets

        # Password length slider
        self.length_label = QLabel("Password Length: 12")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(4, 32)
        self.slider.setValue(12)
        self.slider.valueChanged.connect(self.update_length_label)

        # Complexity options
        self.radio_letters = QRadioButton("Letters Only (A-Z, a-z)")
        self.radio_letters.setChecked(True)
        self.radio_digits = QRadioButton("Letters + Digits (A-Z, a-z, 0-9)")
        self.radio_symbols = QRadioButton("Letters + Digits + Symbols (!@#...)")

        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.radio_letters)
        self.radio_group.addButton(self.radio_digits)
        self.radio_group.addButton(self.radio_symbols)

        # Output field
        self.output = QLineEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Your generated password will appear here...")

        # Buttons
        self.generate_button = QPushButton("🔐 Generate Password")
        self.copy_button = QPushButton("📋 Copy to Clipboard")

        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        # Add widgets to layout
        layout.addWidget(self.length_label)
        layout.addWidget(self.slider)

        layout.addWidget(QLabel("Select Complexity:"))
        layout.addWidget(self.radio_letters)
        layout.addWidget(self.radio_digits)
        layout.addWidget(self.radio_symbols)

        layout.addWidget(self.generate_button)
        layout.addWidget(self.output)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def update_length_label(self):
        self.length_label.setText(f"Password Length: {self.slider.value()}")

    def generate_password(self):
        length = self.slider.value()
        if self.radio_letters.isChecked():
            chars = string.ascii_letters
        elif self.radio_digits.isChecked():
            chars = string.ascii_letters + string.digits
        elif self.radio_symbols.isChecked():
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters
        password = ''.join(random.choice(chars) for _ in range(length))
        self.output.setText(password)

    def copy_to_clipboard(self):
        password = self.output.text()
        if password:
            QApplication.clipboard().setText(password)
            QMessageBox.information(self, "Success", "Password copied to clipboard!")
        else:
            QMessageBox.warning(self, "Empty", "Please generate a password first.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
