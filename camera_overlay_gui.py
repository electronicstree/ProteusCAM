# camera_overlay_gui.py
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QSpinBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QSlider
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from camera_overlay import OverlayWindow

MAX_WIDTH = 240
MAX_HEIGHT = 320

class VCAMLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProteusCAM Overlay")
        icon_path = os.path.abspath("Proteuscam.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(280, 230)  # Increased height to fit link

        self.overlay = OverlayWindow(MAX_WIDTH, MAX_HEIGHT)

        # === Width Controls ===
        width_label = QLabel("Width:")
        self.width_spin = QSpinBox()
        self.width_spin.setRange(8, MAX_WIDTH)
        self.width_spin.setSingleStep(8)
        self.width_spin.setValue(MAX_WIDTH)
        self.width_spin.setFixedHeight(25)
        self.width_spin.setFixedWidth(100)
        self.width_spin.valueChanged.connect(self.update_overlay)

        width_layout = QHBoxLayout()
        width_layout.addWidget(width_label)
        width_layout.addStretch()
        width_layout.addWidget(self.width_spin)

        # === Height Controls ===
        height_label = QLabel("Height:")
        self.height_spin = QSpinBox()
        self.height_spin.setRange(8, MAX_HEIGHT)
        self.height_spin.setSingleStep(8)
        self.height_spin.setValue(MAX_HEIGHT)
        self.height_spin.setFixedHeight(25)
        self.height_spin.setFixedWidth(100)
        self.height_spin.valueChanged.connect(self.update_overlay)

        height_layout = QHBoxLayout()
        height_layout.addWidget(height_label)
        height_layout.addStretch()
        height_layout.addWidget(self.height_spin)

        # === Opacity Controls ===
        opacity_label = QLabel("Opacity:")
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.setTickInterval(10)
        self.opacity_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.opacity_slider.valueChanged.connect(self.opacity_changed)

        opacity_layout = QHBoxLayout()
        opacity_layout.addWidget(opacity_label)
        opacity_layout.addWidget(self.opacity_slider)

        # === Toggle Button ===
        self.toggle_btn = QPushButton("Show Overlay")
        self.toggle_btn.setFixedSize(120, 35)
        self.toggle_btn.clicked.connect(self.toggle_overlay)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.toggle_btn)
        button_layout.addStretch()

        # === Website Link ===
        link_label = QLabel('<a href="https://electronicstree.com">ELECTRONICSTREE.COM</a>')
        link_label.setOpenExternalLinks(True)
        link_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        link_label.setStyleSheet("color: #1a73e8; font-weight: bold;")

        # === Main Layout ===
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)
        layout.addLayout(width_layout)
        layout.addLayout(height_layout)
        layout.addLayout(opacity_layout)
        layout.addLayout(button_layout)
        layout.addWidget(link_label)  

        self.setLayout(layout)

    def update_overlay(self):
        w = self.width_spin.value()
        h = self.height_spin.value()
        if self.overlay.isVisible():
            self.overlay.update_rectangle(w, h)

    def opacity_changed(self, value):
        self.overlay.set_opacity(value / 100.0)

    def toggle_overlay(self):
        if self.overlay.isVisible():
            self.overlay.hide()
            self.toggle_btn.setText("Show Overlay")
        else:
            self.overlay.update_rectangle(
                self.width_spin.value(), self.height_spin.value()
            )
            self.overlay.set_opacity(self.opacity_slider.value() / 100.0)
            self.overlay.show()
            self.toggle_btn.setText("Hide Overlay")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Ensure correct directory

    app = QApplication(sys.argv)
    icon_path = os.path.abspath("Proteuscam.ico")
    app.setWindowIcon(QIcon(icon_path))

    launcher = VCAMLauncher()
    launcher.show()
    sys.exit(app.exec())
