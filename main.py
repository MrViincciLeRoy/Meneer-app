from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import DashboardScreen, SettingsScreen
from data_manager import load_subjects

class MainApp(App):
    """
    Main application class that initializes and manages the app screens.
    """
    def build(self):
        # Load data on startup
        self.subjects = load_subjects()

        # Initialize Screen Manager
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MainApp().run()
