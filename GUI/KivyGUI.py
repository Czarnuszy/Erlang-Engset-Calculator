from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config
from main import Model
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')


class MyPageLayout(PageLayout):

    def change(self, variable):
        """
        :param variable: name of variable to calcluate
        """
        tab = [self.ids.traffic_input, self.ids.lines_input, self.ids.block_rate_input]

        if variable == 'traffic':
            tab[0].readonly = True
            tab[1].readonly = False
            tab[2].readonly = False
            tab[0].text = ""
        elif variable == "lines":
            tab[1].readonly = True
            tab[0].readonly = False
            tab[2].readonly = False
            tab[1].text = ""
        elif variable == "block":
            tab[2].readonly = True
            tab[1].readonly = False
            tab[0].readonly = False
            tab[2].text = ""

    def checkEnabled(self, arg):

        if arg.readonly:
            return False
        else:
            if arg == self.ids.lines_input:
                return int(arg.text)
            else:
                return float(arg.text)



    def calculate(self):
        try:

            traffic = self.checkEnabled(self.ids.traffic_input)
            lines = self.checkEnabled(self.ids.lines_input)
            block = self.checkEnabled(self.ids.block_rate_input)

            model = Model(traffic, lines, block)
            self.ids.result.text = str(model.calculate_erlang())
        except ValueError:
            popup = Popup(title='Input Popup',
                          content=Label(text='Wrong Input!!!'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()







class ErlangEngstetApp(App):
    def build(self):
        return MyPageLayout()

erlangApp = ErlangEngstetApp()
erlangApp.run()

