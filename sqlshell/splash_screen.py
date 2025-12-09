from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QPainter, QColor, QFont, QPen, QBrush, QLinearGradient
import os

class AnimatedSplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize properties for animations
        self._progress = 0.0
        self.next_widget = None
        
        # Set up the window properties
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.SplashScreen
        )
        
        # Set widget attributes
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)
        
        # Set fixed size - Windows 95 style window
        self.setFixedSize(400, 250)
        
        # Center the splash screen on the screen
        screen_geometry = self.screen().geometry()
        self.move(
            (screen_geometry.width() - self.width()) // 2,
            (screen_geometry.height() - self.height()) // 2
        )
        
        # Set up animations
        self.setup_animations()
        
        # Start boot sequence
        QTimer.singleShot(50, self.start_boot_sequence)
    
    def setup_animations(self):
        """Set up all animations for the boot sequence"""
        # Progress animation
        self.progress_anim = QPropertyAnimation(self, b"progress")
        self.progress_anim.setDuration(2000)
        self.progress_anim.setStartValue(0.0)
        self.progress_anim.setEndValue(1.0)
        self.progress_anim.setEasingCurve(QEasingCurve.Type.Linear)
        self.progress_anim.finished.connect(self._on_animation_finished)
    
    def start_boot_sequence(self):
        """Start the boot sequence"""
        # Start progress
        self.progress_anim.start()
    
    def paintEvent(self, event):
        """Custom paint event with Windows 95 style"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)  # No antialiasing for retro look
        
        # Windows 95 color scheme
        light_gray = QColor(212, 208, 200)  # Light gray
        dark_gray = QColor(128, 128, 128)   # Dark gray
        darker_gray = QColor(64, 64, 64)    # Darker gray
        black = QColor(0, 0, 0)              # Black
        white = QColor(255, 255, 255)       # White
        blue = QColor(0, 0, 128)            # Windows blue
        
        # Draw window background (light gray)
        painter.fillRect(0, 0, self.width(), self.height(), light_gray)
        
        # Draw window border (3D beveled effect)
        # Top and left - light (highlight)
        painter.setPen(QPen(white, 2))
        painter.drawLine(0, 0, self.width() - 1, 0)  # Top
        painter.drawLine(0, 0, 0, self.height() - 1)  # Left
        
        # Bottom and right - dark (shadow)
        painter.setPen(QPen(dark_gray, 2))
        painter.drawLine(0, self.height() - 1, self.width() - 1, self.height() - 1)  # Bottom
        painter.drawLine(self.width() - 1, 0, self.width() - 1, self.height() - 1)  # Right
        
        # Inner border (darker)
        painter.setPen(QPen(darker_gray, 1))
        painter.drawLine(2, 2, self.width() - 3, 2)  # Top inner
        painter.drawLine(2, 2, 2, self.height() - 3)  # Left inner
        painter.setPen(QPen(black, 1))
        painter.drawLine(2, self.height() - 3, self.width() - 3, self.height() - 3)  # Bottom inner
        painter.drawLine(self.width() - 3, 2, self.width() - 3, self.height() - 3)  # Right inner
        
        # Draw title bar area (Windows blue)
        title_bar_height = 25
        painter.fillRect(4, 4, self.width() - 8, title_bar_height, blue)
        
        # Title bar text
        painter.setPen(QPen(white, 1))
        painter.setFont(QFont("MS Sans Serif", 9, QFont.Weight.Bold))
        painter.drawText(8, 20, "R.A.L.P.H.")
        
        # Draw content area
        content_y = title_bar_height + 8
        content_height = self.height() - content_y - 60
        
        # Application title
        painter.setPen(QPen(black, 1))
        painter.setFont(QFont("MS Sans Serif", 12, QFont.Weight.Bold))
        title_text = "R.A.L.P.H."
        title_rect = painter.fontMetrics().boundingRect(title_text)
        title_x = (self.width() - title_rect.width()) // 2
        painter.drawText(title_x, content_y + 30, title_text)
        
        # Subtitle
        painter.setFont(QFont("MS Sans Serif", 8))
        subtitle_text = "Read/Analyze/Load/Parse Hub"
        subtitle_rect = painter.fontMetrics().boundingRect(subtitle_text)
        subtitle_x = (self.width() - subtitle_rect.width()) // 2
        painter.drawText(subtitle_x, content_y + 50, subtitle_text)
        
        # Draw Windows 95 style progress bar
        progress_y = self.height() - 50
        progress_x = 20
        progress_width = self.width() - 40
        progress_height = 20
        
        # Progress bar background (recessed 3D effect)
        # Outer border - dark
        painter.setPen(QPen(dark_gray, 1))
        painter.drawRect(progress_x, progress_y, progress_width, progress_height)
        
        # Inner highlight (top-left)
        painter.setPen(QPen(white, 1))
        painter.drawLine(progress_x + 1, progress_y + 1, progress_x + progress_width - 2, progress_y + 1)
        painter.drawLine(progress_x + 1, progress_y + 1, progress_x + 1, progress_y + progress_height - 2)
        
        # Inner shadow (bottom-right)
        painter.setPen(QPen(black, 1))
        painter.drawLine(progress_x + 1, progress_y + progress_height - 1, progress_x + progress_width - 1, progress_y + progress_height - 1)
        painter.drawLine(progress_x + progress_width - 1, progress_y + 1, progress_x + progress_width - 1, progress_y + progress_height - 1)
        
        # Fill progress bar
        if hasattr(self, '_progress') and self._progress > 0:
            fill_width = int((progress_width - 4) * self._progress)
            fill_x = progress_x + 2
            fill_y = progress_y + 2
            fill_height = progress_height - 4
            
            if fill_width > 0:
                # Progress bar fill (blue gradient)
                gradient = QLinearGradient(fill_x, fill_y, fill_x, fill_y + fill_height)
                gradient.setColorAt(0, QColor(0, 0, 200))  # Lighter blue
                gradient.setColorAt(1, QColor(0, 0, 128))  # Darker blue
                painter.fillRect(fill_x, fill_y, fill_width, fill_height, QBrush(gradient))
                
                # Progress bar fill highlight (top edge)
                painter.setPen(QPen(QColor(100, 150, 255), 1))
                painter.drawLine(fill_x, fill_y, fill_x + fill_width - 1, fill_y)
        
        # Draw status text
        painter.setPen(QPen(black, 1))
        painter.setFont(QFont("MS Sans Serif", 8))
        if hasattr(self, '_progress'):
            percent = int(self._progress * 100)
            status_text = f"Loading... {percent}%"
        else:
            status_text = "Loading... 0%"
        status_rect = painter.fontMetrics().boundingRect(status_text)
        status_x = (self.width() - status_rect.width()) // 2
        painter.drawText(status_x, progress_y - 5, status_text)
        
        super().paintEvent(event)
    
    @pyqtProperty(float)
    def progress(self):
        return self._progress
    
    @progress.setter
    def progress(self, value):
        self._progress = value
        self.update()
    
    def _on_animation_finished(self):
        """Handle animation completion"""
        if self.next_widget:
            QTimer.singleShot(200, self._finish_splash)
    
    def _finish_splash(self):
        """Clean up and show the main window"""
        # Stop all animations
        if hasattr(self, 'progress_anim'):
            self.progress_anim.stop()
        
        self.close()
        if self.next_widget:
            self.next_widget.show()
    
    def finish(self, widget):
        """Store the widget to show after animation completes"""
        self.next_widget = widget
        
        # Stop all animations
        if hasattr(self, 'progress_anim'):
            self.progress_anim.stop()
        
        # Close the splash screen and show the main window
        QTimer.singleShot(50, self._finish_splash)
