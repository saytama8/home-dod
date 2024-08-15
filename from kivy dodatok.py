from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image

# Определение переменных до классов
inst = '''Всім привіт! Сьогодні я вам покажу додаток на подобі програми про рибалку, у ньому ви можете дізнатися про 
багатьох відомих риб, які проживають у річках України:
1 - Карась звичайний
2 - Короп 
3 - Білий амур 
4 - Лящ 
5 - Сом 
6 - Щука'''

inst2 = '''1 - Карась звичайний
2 - Короп  
3 - Білий амур 
4 - Лящ 
5 - Сом 
6 - Щука'''

class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        green = (.15, .20, .05, .5)
        Window.clearcolor = green
        image = Image(source="image.jpg")

        lineV = FloatLayout(size_hint=(1, 1))
        line1 = BoxLayout(size_hint=(1, 0.4), pos_hint={"y": 0.7, "center_x": 0.5})
        line2 = BoxLayout(size_hint=(0.5, 0.05), pos_hint={"y": 0.4, "center_x": 0.5})
        line4 = BoxLayout(size_hint=(0.25, 0.1), pos_hint={"y": 0, "center_x": 0.5})

        label1 = Label(text=inst)
        line1.add_widget(label1)
        line1.add_widget(image)

        label2 = Label(text="Введіть номер риби, про яку ви хочете дізнатися")
        self.age = TextInput(multiline=False)
        line2.add_widget(label2)
        line2.add_widget(self.age)
        red = (.255, .0, .0, 1)

        but1 = Button(text="Інформація", background_color=red)
        anim = Animation(background_color=(0, 0, 1, 1), font_size=60, duration=3.5)
        anim2 = Animation(font_size=60, duration=3.5)
        anim3 = anim + anim2
        anim3.start(but1)

        line4.add_widget(but1)

        lineV.add_widget(line1)
        lineV.add_widget(line2)
        lineV.add_widget(line4)

        self.add_widget(lineV)
        but1.on_press = self.next_win1  

    def next_win1(self):
        global new_age
        age_text = self.age.text.strip()
        if age_text.isdigit():
            new_age = int(age_text)
            self.manager.current = 'main2'
            self.manager.transition.direction = "up"
        else:
            print("Помилка: введіть правильне число.")

class Main2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.info_labels = {
            1: "Карась звичайний: Риба з родини коропових, популярна серед рибалок.",
            2: "Короп: Велика риба, яка часто зустрічається в річках і ставках.",
            3: "Білий амур: Риба, яка відрізняється своєю великою величиною і швидким зростанням.",
            4: "Лящ: Риба з родини коропових, що живе в ріках і водоймах.",
            5: "Сом: Велика хижа риба, що мешкає в річках і ставках.",
            6: "Щука: Хижа риба з родини щукових, що зустрічається в прісних водоймах."
        }

        self.info_label = Label(size_hint=(1, 1), text="", halign="center", valign="middle")
        self.info_label.bind(size=self.info_label.setter('text_size'))
        
        lineF = FloatLayout(size_hint=(1, 1))
        lineF.add_widget(self.info_label)

        self.add_widget(lineF)

    def on_enter(self):
        # Используем глобальную переменную new_age для отображения информации
        self.info_label.text = self.info_labels.get(new_age, "Невірний номер риби")

class Win(App):
    def build(self):
        main_screen = ScreenManager()
        main_screen.add_widget(Main(name='main'))
        main_screen.add_widget(Main2(name='main2'))
        return main_screen

app = Win()
app.run()


