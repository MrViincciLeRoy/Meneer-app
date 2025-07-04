from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import DashboardScreen, SettingsScreen
from data_manager import load_subjects
import os
import sys

# Add this block to help PyInstaller find the data files
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Update data manager to use the resource path
data_manager.DATA_FILE_PATH = resource_path('data/subjects.json')


class MainApp(App):
    """
    Main application class that initializes and manages the app screens.
    """
    def build(self):
        self.subjects = load_subjects()
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MainApp().run()
