from kivy.app import App
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='horizontal')

        # Create buttons
        button1 = Button(text='Go to Page 1', on_press=self.go_to_page1)
        button2 = Button(text='Go to Page 2', on_press=self.go_to_page2)
        button3 = Button(text='QUIT', on_press=self.quit_application)

        # Add buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        # Add the layout to the screen
        self.add_widget(layout)

    def go_to_page1(self, instance):
        self.manager.current = 'page1'

    def go_to_page2(self, instance):
        self.manager.current = 'page2'

    def go_to_page3(self, instance):
        self.manager.current = 'page3'

    def quit_application(self, instance):  # Updated method name
        App.get_running_app().stop()

class Page1(Screen):
    def __init__(self, **kwargs):
        super(Page1, self).__init__(**kwargs)
        self.add_widget(Button(text='Back to Home', on_press=self.go_to_home))

    def go_to_home(self, instance):
        self.manager.current = 'home'

class Page2(Screen):
    def __init__(self, **kwargs):
        super(Page2, self).__init__(**kwargs)
        self.add_widget(Button(text='Back to Home', on_press=self.go_to_home))

    def go_to_home(self, instance):
        self.manager.current = 'home'

class Page3(Screen):
    def __init__(self, **kwargs):
        super(Page3, self).__init__(**kwargs)
        self.add_widget(Button(text='Back to Home', on_press=self.go_to_home))

    def go_to_home(self, instance):
        self.manager.current = 'home'

class MyApp(App):
    def build(self):
        # Create a ScreenManager
        sm = ScreenManager()

        # Create screens
        home_screen = HomePage(name='home')
        page1_screen = Page1(name='page1')
        page2_screen = Page2(name='page2')
        page3_screen = Page3(name='page3')

        # Add screens to the ScreenManager
        sm.add_widget(home_screen)
        sm.add_widget(page1_screen)
        sm.add_widget(page2_screen)
        sm.add_widget(page3_screen)

        return sm

if __name__ == '__main__':
    MyApp().run()