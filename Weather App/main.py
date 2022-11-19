
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
Window.size = (350, 580)

class Ui(BoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_file('design.kv')

        return Ui()


    def update_data(self):
        ciudad = self.root.ids.ciudad.text
        API = 'https://api.openweathermap.org/data/2.5/weather?q=' +ciudad+ '&appid=bc12083e70d2d22298c2df1cec7101d9'
        self.req = UrlRequest(url=API, on_success= self.resultado)


    def resultado(self, *args):
        json_datos = self.req.result
        try:
            temp = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
            presion = str(json_datos['main']['pressure']) + ' hPa'
            humedad = str(json_datos['main']['humidity']) + ' %'
            viento = str(int(json_datos['wind']['speed'])*18/5) + ' km/h'
            self.root.ids.temperatura.text = temp
            self.root.ids.humedad.text = humedad
            self.root.ids.viento.text = viento
            self.root.ids.presion.text = presion
        except BaseException as t:
            self.root.ids.temperatura.text = '-'
            self.root.ids.humedad.text = '-'
            self.root.ids.viento.text = '-'
            self.root.ids.presion.text = '-'


    def get_data_city(self):
        for i in range(4):
            if i == 0:
                API = 'https://api.openweathermap.org/data/2.5/weather?q='+'Trujillo'+'&appid=bc12083e70d2d22298c2df1cec7101d9'
                self.req1 = UrlRequest(url=API, on_success= self.ciudad_uno)
            if i == 1:
                API = 'https://api.openweathermap.org/data/2.5/weather?q='+'Arequipa'+'&appid=bc12083e70d2d22298c2df1cec7101d9'
                self.req2 = UrlRequest(url=API, on_success= self.ciudad_dos)
            if i == 2:
                API = 'https://api.openweathermap.org/data/2.5/weather?q='+'Lima'+'&appid=bc12083e70d2d22298c2df1cec7101d9'
                self.req3 = UrlRequest(url=API, on_success= self.ciudad_tres)
            if i == 3:
                API = 'https://api.openweathermap.org/data/2.5/weather?q='+'Cusco'+'&appid=bc12083e70d2d22298c2df1cec7101d9'
                self.req4 = UrlRequest(url=API, on_success= self.ciudad_cuatro)

    def ciudad_uno(self,*args):
        json_datos = self.req1.result
        try:
            self.root.ids.trujillo.text = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
        except BaseException as t:
            self.root.ids.trujillo.text = '-'

    def ciudad_dos(self,*args):
        json_datos = self.req2.result
        try:
            self.root.ids.arequipa.text = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
        except BaseException as t:
            self.root.ids.arequipa.text = '-'

    def ciudad_tres(self,*args):
        json_datos = self.req3.result
        try:
            self.root.ids.lima.text = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
        except BaseException as t:
            self.root.ids.lima.text = '-'

    def ciudad_cuatro(self,*args):
        json_datos = self.req4.result
        try:
            self.root.ids.cusco.text = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
        except BaseException as t:
            self.root.ids.cusco.text = '-'

if __name__=="__main__":
    MainApp().run()
