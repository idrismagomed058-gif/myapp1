from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        pak=FloatLayout()
        bt1=Button(text="Добавить",color="blue",font_size=32,size_hint=(None,None),size=(200,100),pos=(400,470),
                   on_press=self.new_win)
        bt2=Button(text="Уменшить",color="blue",font_size=32,size_hint=(None,None),size=(200,100),pos=(400,300),
                   on_press=self.smm)
        bt3=Button(text="Настройки",color="blue",font_size=32,size_hint=(None,None),size=(200,100),pos=(400,130),
                   on_press=self.sett)
        l1=Label(text="Программа для финансовой помощи",color="black",pos=(40,300),font_size=34)
        background = Image(source=r"C:\Users\user\Pictures\b00614eb1e68f6eb68fa4b6a35becaa1.jpg",
                           allow_stretch=True,
                           keep_ratio=False,
                           size_hint=(1, 1),
                           pos_hint={'x': 0, 'y': 0})
        pak.add_widget(background)
        pak.add_widget(l1)
        pak.add_widget(bt1)
        pak.add_widget(bt2)
        pak.add_widget(bt3)
        self.add_widget(pak)
    def new_win(self,instance):
        self.manager.current="Dolgi"
    def smm(self,instance):
        self.manager.current="mnb"
    def sett(self,instance):
        self.manager.current="set"


class Dolgi(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        l=FloatLayout()
        bg=Image(source=r"C:\Users\user\Pictures\dc0e2f6ea76de8a4e627a0dab9e89911.jpg",
                 allow_stretch=True,
                 keep_ratio=False,
                 size_hint=(1,1),
                 pos_hint={'x': 0, 'y': 0})

        bt=Button(text="Назад",color="blue",font_size=32,size_hint=(None,None),size=(200,100),pos=(400,300),
                  on_press=self.back)
        l.add_widget(bg)
        l.add_widget(bt)
        self.add_widget(l)
    def back(self,instance):
        self.manager.current="Main"


class Small(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        l=FloatLayout()
        bg=Image(source=r"C:\Users\user\Pictures\b00614eb1e68f6eb68fa4b6a35becaa1.jpg",
                 allow_stretch=True,
                 keep_ratio=False,
                 size_hint=(1,1),
                 pos_hint={'x': 0, 'y': 0})

        bt=Button(text="Назад",color="blue",font_size=32,size_hint=(None,None),size=(200,100),pos=(400,300),
                  on_press=self.back)
        l.add_widget(bg)
        l.add_widget(bt)
        self.add_widget(l)
    def back(self,instance):
        self.manager.current="Main"








class Setting(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        l=FloatLayout()
        bg=Image(source=r"C:\Users\user\Pictures\11910012822.jpg",
                 allow_stretch=True,
                 keep_ratio=False,
                 size_hint=(1,1),
                 pos_hint={'x': 0, 'y': 0})

        bt=Button(text="Назад",color="blue",font_size=32,size_hint=(None,None),size=(200,100),pos=(400,300),
                  on_press=self.back)
        l.add_widget(bg)
        l.add_widget(bt)
        self.add_widget(l)
    def back(self,instance):
        self.manager.current="Main"








class DolgiZaimy(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(MainScreen(name="Main"))
        sm.add_widget(Dolgi(name="Dolgi"))
        sm.add_widget(Small(name="mnb"))
        sm.add_widget(Setting(name="set"))
        return sm
    
if __name__=="__main__":
    DolgiZaimy().run()


        
        
    

if __name__=='__main__':
    DolgiZaimy().run()
