# camera_overlay.py

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPen, QColor, QCursor
from PyQt6.QtCore import Qt

class OverlayWindow(QWidget):
    def __init__(self, width=128, height=64):
        super().__init__()

        self.rect_width = width
        self.rect_height = height
        self.opacity = 1.0  # Default to fully opaque

        # Get screen under the cursor
        cursor_pos = QCursor.pos()
        for screen in QApplication.screens():
            if screen.geometry().contains(cursor_pos):
                self.screen_geo = screen.geometry()
                break
        else:
            self.screen_geo = QApplication.primaryScreen().geometry()

        self.setGeometry(self.screen_geo)

        # Set window flags and transparency
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    def update_rectangle(self, width, height):
        self.rect_width = width
        self.rect_height = height
        self.update()

    def set_opacity(self, opacity: float):
        """Set the opacity of the overlay (0.0 to 1.0)."""
        self.opacity = max(0.0, min(opacity, 1.0))  # Clamp between 0–1
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(self.opacity)

        pen = QPen(QColor(255, 0, 0), 2)
        painter.setPen(pen)

        center_x = self.width() // 2
        center_y = self.height() // 2

        x0 = center_x - self.rect_width // 2
        y0 = center_y - self.rect_height // 2

        painter.drawRect(x0, y0, self.rect_width, self.rect_height)
