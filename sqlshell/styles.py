def get_application_stylesheet(colors):
    """Generate the application's stylesheet using the provided color scheme.
    
    Args:
        colors: A dictionary containing color definitions for the application
        
    Returns:
        A string containing the complete Qt stylesheet
    """
    return f"""
        QMainWindow {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {colors['background']}, stop:1 {colors['background_end']});
        }}
        
        QWidget {{
            color: {colors['text']};
            font-family: 'Segoe UI', 'Arial', sans-serif;
        }}
        
        QLabel {{
            font-size: 13px;
            padding: 2px;
            color: {colors['text']};
        }}
        
        QLabel#header_label {{
            font-size: 16px;
            font-weight: bold;
            color: {colors['header']};
            padding: 8px 0;
        }}
        
        QPushButton {{
            background-color: {colors['secondary']};
            color: #06021b;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: bold;
            font-size: 13px;
            min-height: 30px;
        }}
        
        QPushButton:hover {{
            background-color: #5de285;
        }}
        
        QPushButton:pressed {{
            background-color: #3db85f;
        }}
        
        QPushButton#primary_button {{
            background-color: {colors['accent']};
            color: #06021b;
        }}
        
        QPushButton#primary_button:hover {{
            background-color: #5de285;
        }}
        
        QPushButton#primary_button:pressed {{
            background-color: #3db85f;
        }}
        
        QPushButton#danger_button {{
            background-color: {colors['error']};
            color: white;
        }}
        
        QPushButton#danger_button:hover {{
            background-color: #CB4335;
        }}
        
        QToolButton {{
            background-color: transparent;
            border: none;
            border-radius: 4px;
            padding: 4px;
            color: {colors['text']};
        }}
        
        QToolButton:hover {{
            background-color: rgba(131, 1, 255, 0.2);
        }}
        
        QFrame#sidebar {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {colors['background']}, stop:1 {colors['background_end']});
            border-radius: 0px;
            border-right: 1px solid {colors['border']};
        }}
        
        QFrame#content_panel {{
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            border: 1px solid {colors['border']};
        }}
        
        QListWidget {{
            background-color: rgba(47, 11, 100, 0.3);
            border-radius: 4px;
            border: 1px solid {colors['border']};
            padding: 4px;
            outline: none;
            color: {colors['text']};
        }}
        
        QListWidget::item {{
            padding: 8px;
            border-radius: 4px;
            color: {colors['text']};
        }}
        
        QListWidget::item:selected {{
            background-color: {colors['header']};
            color: white;
        }}
        
        QListWidget::item:hover:!selected {{
            background-color: rgba(131, 1, 255, 0.3);
        }}
        
        QTableWidget {{
            background-color: rgba(255, 255, 255, 0.95);
            alternate-background-color: rgba(240, 240, 240, 0.5);
            border-radius: 4px;
            border: 1px solid {colors['border']};
            gridline-color: rgba(76, 210, 117, 0.3);
            outline: none;
            color: #06021b;
        }}
        
        QTableWidget::item {{
            padding: 4px;
            color: #06021b;
        }}
        
        QTableWidget::item:selected {{
            background-color: rgba(76, 210, 117, 0.3);
            color: #06021b;
        }}
        
        QHeaderView::section {{
            background-color: {colors['header']};
            color: white;
            padding: 8px;
            border: none;
            font-weight: bold;
        }}
        
        QSplitter::handle {{
            background-color: {colors['border']};
        }}
        
        QStatusBar {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {colors['background']}, stop:1 {colors['background_end']});
            color: {colors['text']};
            padding: 8px;
            border-top: 1px solid {colors['border']};
        }}
        
        QTabWidget::pane {{
            border: 1px solid {colors['border']};
            border-radius: 4px;
            top: -1px;
            background-color: rgba(255, 255, 255, 0.95);
        }}
        
        QTabBar::tab {{
            background-color: rgba(47, 11, 100, 0.5);
            color: {colors['text']};
            border: 1px solid {colors['border']};
            border-bottom: none;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            padding: 8px 12px;
            margin-right: 2px;
            min-width: 80px;
        }}
        
        QTabBar::tab:selected {{
            background-color: rgba(255, 255, 255, 0.95);
            border-bottom: 1px solid rgba(255, 255, 255, 0.95);
            color: #06021b;
        }}
        
        QTabBar::tab:hover:!selected {{
            background-color: rgba(131, 1, 255, 0.3);
        }}
        
        QTabBar::close-button {{
            subcontrol-position: right;
            subcontrol-origin: padding;
            width: 18px;
            height: 18px;
            margin: 2px;
            border-radius: 3px;
            background-color: rgba(100, 100, 100, 0.4);
            border: 1px solid rgba(60, 60, 60, 0.6);
        }}
        
        QTabBar::close-button:hover {{
            background-color: rgba(231, 76, 60, 0.7);
            border: 1px solid rgba(200, 50, 40, 0.8);
            border-radius: 3px;
        }}
        
        QTabBar::close-button:pressed {{
            background-color: rgba(231, 76, 60, 0.9);
            border: 1px solid rgba(180, 40, 30, 1.0);
        }}
        
        QPlainTextEdit, QTextEdit {{
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 4px;
            border: 1px solid {colors['border']};
            padding: 8px;
            selection-background-color: rgba(76, 210, 117, 0.4);
            selection-color: #06021b;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 14px;
            color: #06021b;
        }}
    """

def get_tab_corner_stylesheet():
    """Get the stylesheet for the tab corner widget with the + button"""
    return """
        QToolButton {
            background-color: transparent;
            border: none;
            border-radius: 4px;
            padding: 4px;
            font-weight: bold;
            font-size: 16px;
            color: #4cd275;
        }
        QToolButton:hover {
            background-color: rgba(76, 210, 117, 0.2);
        }
        QToolButton:pressed {
            background-color: rgba(76, 210, 117, 0.4);
        }
    """

def get_context_menu_stylesheet():
    """Get the stylesheet for context menus"""
    return """
        QMenu {
            background-color: #2f0b64;
            border: 1px solid #4cd275;
            padding: 5px;
            color: #f0f0f0;
        }
        QMenu::item {
            padding: 5px 20px;
            color: #f0f0f0;
        }
        QMenu::item:selected {
            background-color: #8301ff;
            color: white;
        }
        QMenu::separator {
            height: 1px;
            background-color: #4cd275;
            margin: 5px 15px;
        }
    """

def get_header_label_stylesheet():
    """Get the stylesheet for header labels"""
    return "color: #8301ff; font-weight: bold; font-size: 14px;"

def get_db_info_label_stylesheet():
    """Get the stylesheet for database info label"""
    return "color: #d0d0d0; padding: 8px 0; font-size: 13px;"

def get_tables_header_stylesheet():
    """Get the stylesheet for tables header"""
    return "color: #8301ff; font-weight: bold; font-size: 14px; margin-top: 8px;"

def get_row_count_label_stylesheet():
    """Get the stylesheet for row count label"""
    return "color: #b0b0b0; font-size: 12px; font-style: italic; padding: 8px 0;" 