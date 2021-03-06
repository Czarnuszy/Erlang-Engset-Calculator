from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config
from main import Model
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from GUI.graph import generate_graph
from math import floor
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')


class CustomPopup(Popup):
    pass


class EngsetPopup(Popup):
    pass


class CustPopup2(Popup):
    pass


class MyPageLayout(PageLayout):

    popup = Popup(title='Input Popup',
                  content=Label(text='Wrong Input!!!'),
                  size_hint=(None, None), size=(400, 400))

    lin = 1
    tab = []

    def ReadOnly(self, variable, algorithm):
        """
        :param variable: name of variable to calcluate
        :param algorithm: decides witch group of widgets should be changed
        """
        graph_inputs = []
        if algorithm == 'erlang':
            tab = [self.ids.traffic_input, self.ids.lines_input, self.ids.block_rate_input]
        if algorithm == 'engset':
            tab = [self.ids.engset_traffic, self.ids.engset_lines, self.ids.engset_block]

        if variable == 'traffic':
            tab[0].readonly = True
            tab[1].readonly = False
            tab[2].readonly = False

        elif variable == "lines":
            tab[1].readonly = True
            tab[0].readonly = False
            tab[2].readonly = False

        elif variable == "block":
            tab[2].readonly = True
            tab[1].readonly = False
            tab[0].readonly = False

    def checkEnabled(self, arg):

        if arg.readonly:
            return False
        else:
            if arg == self.ids.lines_input or arg == self.ids.engset_lines:
                return int(arg.text)
            else:
                return float(arg.text)



    def calculate(self, alg):
        """
        :param alg:  name of algorithm to use
        """

        if alg == 'erlang':
            try:
                traffic = self.checkEnabled(self.ids.traffic_input)
                lines = self.checkEnabled(self.ids.lines_input)
                block = self.checkEnabled(self.ids.block_rate_input)

                model = Model(traffic, lines, block)
                self.ids.result.text = str(model.calculate_erlang())
            except ValueError:
                self.popup.open()
        if alg == 'engset':
            try:
                traffic = self.checkEnabled(self.ids.engset_traffic)
                lines = self.checkEnabled(self.ids.engset_lines)
                block = self.checkEnabled(self.ids.engset_block)
                sources = self.checkEnabled(self.ids.sources)

                model = Model(traffic, lines, block, sources)
                self.ids.engset_result.text = str(model.calculate_engset())
            except ValueError:
                self.popup.open()

    def generate(self, graph):
        x = []
        y = []
        inputs = []
        for i in range(self.lin):
            y.append([])
        try:
            if graph == 'lines':
                if self.lin == 1:
                    inputs.append(int(self.ids.line_one_input.text))
                elif self.lin == 2:
                    inputs.append(int(self.ids.line_one_input.text))
                    inputs.append(int(self.ids.line_two_input.text))
                elif self.lin == 3:
                    inputs.append(int(self.ids.line_one_input.text))
                    inputs.append(int(self.ids.line_two_input.text))
                    inputs.append(int(self.ids.line_three_input.text))
                elif self.lin == 4:
                    inputs.append(int(self.ids.line_one_input.text))
                    inputs.append(int(self.ids.line_two_input.text))
                    inputs.append(int(self.ids.line_three_input.text))
                    inputs.append(int(self.ids.line_four_input.text))
                step = float(self.ids.spinner_id.text)
                n_steps = int(floor((float(self.ids.max_traffic.text) - float(self.ids.min_traffic.text)) / step))
                x.append(float(self.ids.min_traffic.text))
                for i in range(n_steps):
                    x.append(x[i] + step)
                    print(x[i])
                for i in range(self.lin):
                    for j in range(n_steps + 1):
                        model = Model(traffic=x[j], lines=inputs[i], blocking_rate=False)
                        y[i].append(model.calculate_erlang())
                        print(y[i])
            elif graph == 'block':
                if self.lin == 1:
                    inputs.append(float(self.ids.block_one_input.text))
                elif self.lin == 2:
                    inputs.append(float(self.ids.block_one_input.text))
                    inputs.append(float(self.ids.block_two_input.text))
                elif self.lin == 3:
                    inputs.append(float(self.ids.block_one_input.text))
                    inputs.append(float(self.ids.block_two_input.text))
                    inputs.append(float(self.ids.block_three_input.text))
                elif self.lin == 4:
                    inputs.append(float(self.ids.block_one_input.text))
                    inputs.append(float(self.ids.block_two_input.text))
                    inputs.append(float(self.ids.block_three_input.text))
                    inputs.append(float(self.ids.block_four_input.text))
                step = int(self.ids.spinner2_id.text)
                n_steps = int(floor((int(self.ids.max_lines.text) - int(self.ids.min_lines.text)) / step))
                x.append(int(self.ids.min_lines.text))
                print(n_steps)
                print(x)
                for i in range(n_steps):
                    x.append(x[i] + step)
                for i in range(self.lin):
                    for j in range(n_steps+1):
                        model = Model(traffic=False, lines= x[j], blocking_rate=inputs[i])
                        y[i].append(model.calculate_erlang())
                        print(y[i])

            generate_graph(x, y, inputs, graph)
        except ValueError:
            raise


    def GraphLines(self, num):
        tab = [self.ids.line_one_input, self.ids.line_two_input, self.ids.line_three_input,
               self.ids.line_four_input]
        self.lin = num
        for i in range(4):
            tab[i].readonly = True

        for i in range(num):
            tab[i].readonly = False

    def GraphLines2(self, num):
        tab = [self.ids.block_one_input, self.ids.block_two_input, self.ids.block_three_input,
               self.ids.block_four_input]
        self.lin = num
        for i in range(4):
            tab[i].readonly = True

        for i in range(num):
            tab[i].readonly = False

    def open_popup(self, type):
        if type == 'erlang':
            the_popup = CustomPopup()
        elif type == 'engset':
            the_popup = EngsetPopup()
        elif type == 'chart':
            the_popup = CustPopup2()
        the_popup.open()


class ErlangEngstetApp(App):
    def build(self):
        return MyPageLayout()


erlangApp = ErlangEngstetApp()
erlangApp.run()

