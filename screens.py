from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from components import TitleLabel, ActionButton

class DashboardScreen(Screen):
    """
    The main dashboard screen that users see after launching the app.
    """
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Use a custom component for the title
        title = TitleLabel(text='Welcome to Your Learning App!')
        
        # Get subject data from the app instance
        app = App.get_running_app()
        subjects_text = f"Loaded Subjects: {', '.join(app.subjects)}"
        info_label = Label(text=subjects_text)
        
        # Use a custom component for the button
        settings_button = ActionButton(text='Go to Settings')
        settings_button.bind(on_press=self.go_to_settings)
        
        layout.add_widget(title)
        layout.add_widget(info_label)
        layout.add_widget(settings_button)
        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'

class SettingsScreen(Screen):
    """
    A simple settings screen.
    """
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        title = TitleLabel(text='Settings')
        back_button = ActionButton(text='Back to Dashboard')
        back_button.bind(on_press=self.go_to_dashboard)
        
        layout.add_widget(title)
        layout.add_widget(Label(text='App settings and options would be here.'))
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_to_dashboard(self, instance):
        self.manager.current = 'dashboard'
