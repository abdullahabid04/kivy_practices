from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class mywindow(GridLayout):
    def __init__(self, **kwargs):
        super(mywindow, self).__init__(**kwargs)

        self.cols = 0

        self.add_widget(Label(text="Name", x=100, y=550, height=25, width=50))
        self.add_widget(Label(text="Age", x=100, y=450, height=25, width=50))
        self.add_widget(Label(text="Qualification", x=100, y=350, height=25, width=50))
        self.add_widget(Label(text="Program", x=100, y=250, height=25, width=50))
        self.add_widget(Label(text="Gender", x=100, y=150, height=25, width=50))
        self.add_widget(Label(text="Domicile", x=100, y=50, height=25, width=50))

        self.s_name = TextInput(x=200, y=550, height=25, width=100)
        self.s_age = TextInput(x=200, y=450, height=25, width=100)
        self.s_qualification = TextInput(x=200, y=350, height=25, width=100)
        self.s_program = TextInput(x=200, y=250, height=25, width=100)
        self.s_gender = TextInput(x=200, y=150, height=25, width=100)
        self.s_domicile = TextInput(x=200, y=50, height=25, width=100)

        self.add_widget(self.s_name)
        self.add_widget(self.s_age)
        self.add_widget(self.s_qualification)
        self.add_widget(self.s_program)
        self.add_widget(self.s_gender)
        self.add_widget(self.s_domicile)

        self.submit_button = Button(text="Submit", x=725, y=500, height=25, width=50, on_press=self.submit)
        self.add_widget(self.submit_button)

        self.reset_button = Button(text="reset", x=725, y=300, height=25, width=50, on_press=self.reset)
        self.add_widget(self.reset_button)

        self.exit_button = Button(text="exit", x=725, y=100, height=25, width=50)
        self.add_widget(self.exit_button)

    def submit(self, instance):
        self.name = self.s_name.text
        self.age = self.s_age.text
        self.qualification = self.s_qualification.text
        self.program = self.s_program.text
        self.gender = self.s_gender.text
        self.domicile = self.s_domicile.text

        self.s_name_label = Label(text="Student Name : " + self.name, x=400, y=550, height=25, width=50)
        self.s_age_label = Label(text="Student Age : " + self.age, x=400, y=450, height=25, width=50)
        self.s_qualification_label = Label(text="Student Qualification : " + self.qualification, x=400, y=350,
                                           height=25, width=50)
        self.s_program_label = Label(text="Student Program : " + self.program, x=400, y=250, height=25, width=50)
        self.s_gender_label = Label(text="Student Gender : " + self.gender, x=400, y=150, height=25, width=50)
        self.s_domicile_label = Label(text="Student Domicile : " + self.domicile, x=400, y=50, height=25, width=50)

        self.add_widget(self.s_name_label)
        self.add_widget(self.s_age_label)
        self.add_widget(self.s_qualification_label)
        self.add_widget(self.s_program_label)
        self.add_widget(self.s_gender_label)
        self.add_widget(self.s_domicile_label)

    def reset(self, instance):
        self.s_name.text = ""
        self.s_age.text = ""
        self.s_qualification.text = ""
        self.s_program.text = ""
        self.s_gender.text = ""
        self.s_domicile.text = ""

        self.remove_widget(self.s_name_label)
        self.remove_widget(self.s_age_label)
        self.remove_widget(self.s_qualification_label)
        self.remove_widget(self.s_program_label)
        self.remove_widget(self.s_gender_label)
        self.remove_widget(self.s_domicile_label)


class myApp(App):
    def build(self):
        return mywindow()


if __name__ == '__main__':
    myApp().run()
