def get_application_stylesheet(colors):
    """Genereer de applicatie stylesheet met Windows 95 thema.
    
    Args:
        colors: Een dictionary met kleurdefinities voor de applicatie
        
    Returns:
        Een string met de complete Qt stylesheet
    """
    return f"""
        QMainWindow {{
            background-color: {colors['background']};
        }}
        
        QWidget {{
            color: {colors['text']};
            font-family: 'MS Sans Serif', 'MS Shell Dlg 2', sans-serif;
            font-size: 11px;
        }}
        
        QLabel {{
            font-size: 11px;
            padding: 2px;
            color: {colors['text']};
        }}
        
        QLabel#header_label {{
            font-size: 13px;
            font-weight: bold;
            color: {colors['header']};
            padding: 4px 0;
        }}
        
        /* Windows 95 beveled button style - raised appearance */
        QPushButton {{
            background-color: {colors['button_face']};
            color: {colors['window_text']};
            border: 2px outset {colors['button_face']};
            border-top-color: {colors['button_highlight']};
            border-left-color: {colors['button_highlight']};
            border-bottom-color: {colors['button_shadow']};
            border-right-color: {colors['button_shadow']};
            padding: 3px 12px;
            font-weight: normal;
            font-size: 11px;
            min-height: 23px;
            min-width: 75px;
        }}
        
        QPushButton:hover {{
            background-color: {colors['button_face']};
        }}
        
        QPushButton:pressed {{
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
            background-color: {colors['button_face']};
        }}
        
        QPushButton#primary_button {{
            background-color: {colors['button_face']};
            color: {colors['window_text']};
        }}
        
        QPushButton#primary_button:hover {{
            background-color: {colors['button_face']};
        }}
        
        QPushButton#primary_button:pressed {{
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
        }}
        
        QPushButton#danger_button {{
            background-color: {colors['button_face']};
            color: {colors['error']};
        }}
        
        QPushButton#danger_button:hover {{
            background-color: {colors['button_face']};
        }}
        
        QPushButton#danger_button:pressed {{
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
        }}
        
        QToolButton {{
            background-color: {colors['button_face']};
            border: 2px outset {colors['button_face']};
            border-top-color: {colors['button_highlight']};
            border-left-color: {colors['button_highlight']};
            border-bottom-color: {colors['button_shadow']};
            border-right-color: {colors['button_shadow']};
            padding: 2px;
            color: {colors['window_text']};
        }}
        
        QToolButton:hover {{
            background-color: {colors['button_face']};
        }}
        
        QToolButton:pressed {{
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
        }}
        
        QFrame#sidebar {{
            background-color: {colors['background']};
            border-right: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
        }}
        
        QFrame#content_panel {{
            background-color: {colors['window']};
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
        }}
        
        QListWidget {{
            background-color: {colors['window']};
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
            padding: 2px;
            outline: none;
            color: {colors['window_text']};
        }}
        
        QListWidget::item {{
            padding: 2px;
            color: {colors['window_text']};
        }}
        
        QListWidget::item:selected {{
            background-color: {colors['highlight']};
            color: {colors['highlight_text']};
        }}
        
        QListWidget::item:hover:!selected {{
            background-color: {colors['button_face']};
        }}
        
        QTableWidget {{
            background-color: {colors['window']};
            alternate-background-color: {colors['button_face']};
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
            gridline-color: {colors['button_shadow']};
            outline: none;
            color: {colors['window_text']};
        }}
        
        QTableWidget::item {{
            padding: 2px;
            color: {colors['window_text']};
        }}
        
        QTableWidget::item:selected {{
            background-color: {colors['highlight']};
            color: {colors['highlight_text']};
        }}
        
        QHeaderView::section {{
            background-color: {colors['button_face']};
            color: {colors['window_text']};
            padding: 4px;
            border: 1px solid {colors['button_shadow']};
            border-top: 1px solid {colors['button_highlight']};
            border-left: 1px solid {colors['button_highlight']};
            font-weight: bold;
            font-size: 11px;
        }}
        
        QSplitter::handle {{
            background-color: {colors['button_face']};
            border: 1px solid {colors['button_shadow']};
        }}
        
        QStatusBar {{
            background-color: {colors['button_face']};
            color: {colors['window_text']};
            padding: 2px;
            border-top: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
        }}
        
        QTabWidget::pane {{
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
            top: -1px;
            background-color: {colors['window']};
        }}
        
        QTabBar::tab {{
            background-color: {colors['button_face']};
            color: {colors['window_text']};
            border: 1px solid {colors['button_shadow']};
            border-bottom: none;
            padding: 3px 8px;
            margin-right: 1px;
            min-width: 60px;
            font-size: 11px;
        }}
        
        QTabBar::tab:selected {{
            background-color: {colors['window']};
            border: 1px solid {colors['button_shadow']};
            border-bottom: 1px solid {colors['window']};
            color: {colors['window_text']};
        }}
        
        QTabBar::tab:hover:!selected {{
            background-color: {colors['button_face']};
        }}
        
        QTabBar::close-button {{
            subcontrol-position: right;
            subcontrol-origin: padding;
            width: 16px;
            height: 16px;
            margin: 1px;
            background-color: {colors['button_face']};
            border: 1px solid {colors['button_shadow']};
        }}
        
        QTabBar::close-button:hover {{
            background-color: {colors['button_face']};
            border: 1px solid {colors['button_dark_shadow']};
        }}
        
        QTabBar::close-button:pressed {{
            background-color: {colors['button_face']};
            border: 1px inset {colors['button_face']};
        }}
        
        QPlainTextEdit, QTextEdit {{
            background-color: {colors['window']};
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
            padding: 2px;
            selection-background-color: {colors['highlight']};
            selection-color: {colors['highlight_text']};
            font-family: 'Courier New', 'Courier', monospace;
            font-size: 10px;
            color: {colors['window_text']};
        }}
        
        QLineEdit {{
            background-color: {colors['window']};
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
            padding: 2px;
            color: {colors['window_text']};
            font-size: 11px;
        }}
        
        QComboBox {{
            background-color: {colors['window']};
            border: 2px inset {colors['button_face']};
            border-top-color: {colors['button_shadow']};
            border-left-color: {colors['button_shadow']};
            border-bottom-color: {colors['button_highlight']};
            border-right-color: {colors['button_highlight']};
            padding: 2px;
            color: {colors['window_text']};
            font-size: 11px;
        }}
        
        QComboBox::drop-down {{
            border: none;
            width: 20px;
        }}
        
        QComboBox::down-arrow {{
            image: none;
            border-left: 4px solid transparent;
            border-right: 4px solid transparent;
            border-top: 4px solid {colors['window_text']};
            width: 0;
            height: 0;
        }}
        
        QScrollBar:vertical {{
            background-color: {colors['button_face']};
            width: 17px;
            border: 1px inset {colors['button_face']};
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {colors['button_shadow']};
            min-height: 20px;
            border: 1px outset {colors['button_face']};
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {colors['dark_bg']};
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
        
        QScrollBar:horizontal {{
            background-color: {colors['button_face']};
            height: 17px;
            border: 1px inset {colors['button_face']};
        }}
        
        QScrollBar::handle:horizontal {{
            background-color: {colors['button_shadow']};
            min-width: 20px;
            border: 1px outset {colors['button_face']};
        }}
        
        QScrollBar::handle:horizontal:hover {{
            background-color: {colors['dark_bg']};
        }}
        
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
            width: 0px;
        }}
    """

def get_tab_corner_stylesheet():
    """Genereer de stylesheet voor de tab corner widget met de + knop"""
    return """
        QToolButton {
            background-color: #C0C0C0;
            border: 2px outset #C0C0C0;
            border-top-color: #FFFFFF;
            border-left-color: #FFFFFF;
            border-bottom-color: #808080;
            border-right-color: #808080;
            padding: 2px;
            font-weight: bold;
            font-size: 12px;
            color: #000000;
            font-family: 'MS Sans Serif', 'MS Shell Dlg 2', sans-serif;
        }
        QToolButton:hover {
            background-color: #C0C0C0;
        }
        QToolButton:pressed {
            border: 2px inset #C0C0C0;
            border-top-color: #808080;
            border-left-color: #808080;
            border-bottom-color: #FFFFFF;
            border-right-color: #FFFFFF;
        }
    """

def get_context_menu_stylesheet():
    """Genereer de stylesheet voor context menu's"""
    return """
        QMenu {
            background-color: #C0C0C0;
            border: 2px outset #C0C0C0;
            border-top-color: #FFFFFF;
            border-left-color: #FFFFFF;
            border-bottom-color: #808080;
            border-right-color: #808080;
            padding: 2px;
            color: #000000;
            font-family: 'MS Sans Serif', 'MS Shell Dlg 2', sans-serif;
            font-size: 11px;
        }
        QMenu::item {
            padding: 3px 20px 3px 25px;
            color: #000000;
        }
        QMenu::item:selected {
            background-color: #000080;
            color: #FFFFFF;
        }
        QMenu::separator {
            height: 1px;
            background-color: #808080;
            margin: 2px 10px;
        }
    """

def get_header_label_stylesheet():
    """Genereer de stylesheet voor header labels"""
    return "color: #000080; font-weight: bold; font-size: 11px; font-family: 'MS Sans Serif', 'MS Shell Dlg 2', sans-serif;"

def get_db_info_label_stylesheet():
    """Genereer de stylesheet voor database info label"""
    return "color: #000000; padding: 4px 0; font-size: 11px; font-family: 'MS Sans Serif', 'MS Shell Dlg 2', sans-serif;"

def get_tables_header_stylesheet():
    """Genereer de stylesheet voor tables header"""
    return "color: #000080; font-weight: bold; font-size: 11px; margin-top: 4px; font-family: 'MS Sans Serif', 'MS Shell Dlg 2', sans-serif;"

def get_row_count_label_stylesheet():
    """Genereer de stylesheet voor row count label"""
    return "color: #808080; font-size: 10px; font-style: italic; padding: 4px 0; font-family: 'MS Sans Serif', 'MS Shell Dlg 2', sans-serif;"
