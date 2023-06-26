from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from datetime import *
import pyodbc
from kivymd.uix.toolbar import MDTopAppBar

Builder.load_string("""
<Button>:
    size_hint: (1, 0.5)
    bold: True
    background_color: '#2237be'
    background_normal: ''
    font_size: 15
    size_hint_y: None
    height: 50

<RedButton@Button>:
    background_color: '#AD1035'

<RoundedButton@Button>:
    background_color: 0, 0, 0, 0
    canvas.before:
        Color: 
            rgba: (.5, 0.54, 1, 1) 
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [30,]

<TextInput>:
    multiline: False
    padding_y: 20, 10
    size_hint_y: None
    height: 30

<CheckBox>:
    color: 'black'

<StartScreen>:
    MDGridLayout:
        cols: 1
        size_hint: (0.6, 0.7)
        pos_hint: {"center_x":0.5, "center_y":0.5}
        Image:
            source: "image.png"
        Label:
            text: "Find your teacher"
            text_size: self.width, None
            font_size: 25
            color: '#3346FF'
        Label:
            text: "Search for your perfect teacher across native speakers and passionates"
            text_size: self.width, None
            font_size: 15
            color: '#565875'
        RoundedButton:
            text: "Get Started"
            on_press: root.manager.current = 'login'

<LoginScreen>:
    id: login_screen
    user: email_id
    password: password_id
    MDAnchorLayout:
        anchor_x: 'left'
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(10)
            spacing: dp(5)
            Image:
                source: "image2.png"
                size_hint_y: None
                width: 120
                allow_stretch: True
            Label:
                text: "Sign In"
                font_size: 25
                color: 'black'
                text_size: self.size
                halaign: 'left'
                # font: 'roboto'
            Label:
                text: "Email"
                font_size: 15
                color: 'black'
                text_size: self.size
                halaign: 'left'
            TextInput:
                id: email_id
                text: 'email@example.com' 
                font_size: 10
                multiline: False 
                padding_y: 10, 10
            Label:
                text: "Password"
                font_size: 15
                color: 'black'
                text_size: self.size
                halaign: 'left'
            TextInput: 
                id: password_id
                text: 'password' 
                font_size: 10
                multiline: False 
                padding_y: 10, 10
                # size_hint_y: None
                # height: 30
                # size_hint_x: None
                # width: 300
            Label:
                text: "Forgot password?"
                font_size: 15
                color: 'black'
                text_size: self.size
                halaign: 'left'
            Label:
                id: error_label
                text: ""
                font_size: 15
                color: 'black'
                text_size: self.size
                halaign: 'left'
            Button:
                text: 'Sign In'
                on_press: root.login()
                    # root.manager.current = 'choose'
                    # root.manager.transition.direction = "left"
            RedButton:
                text: 'Sign Up'
                on_press: 
                    root.manager.current = 'signup'
                    root.manager.transition.direction = "left"

<SignUpScreen>:
    first: first_id
    surname: surname_id
    phone: phone_id
    birth_date: birth_date_id
    email_address: email_address_id
    password: password_id
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(10)
        spacing: dp(5)
        MDTopAppBar:
            title: "Back to Sign In"
            md_bg_color: '#2237be'
            right_action_items: [["arrow-left", lambda x: app.callback(x), "Back"]]
        Label:
            text: "Sign Up"
            font_size: 25
            color: 'black'
        TextInput: 
            id: first_id
            text: 'Name'
            font_size: 10
            multiline: False 
            padding_y: 10, 10
        TextInput: 
            id: surname_id
            text: 'Surname'
            font_size: 10
            multiline: False 
            padding_y: 10, 10    
        TextInput: 
            id: phone_id
            text: 'Phone number'
            font_size: 10
            multiline: False 
            padding_y: 10, 10
        TextInput: 
            id: birth_date_id
            text: 'Birth date'
            font_size: 10
            multiline: False 
            padding_y: 10, 10
        TextInput:
            id: email_address_id
            text: 'Email address'
            font_size: 10
            multiline: False 
            padding_y: 10, 10
        TextInput: 
            id: password_id
            text: 'Password'
            font_size: 10
            multiline: False 
            padding_y: 10, 10
        GridLayout:
            cols: 4
            Label:
                text: "Teacher"
                font_size: 20
                color: 'black'
            CheckBox:
                id: teacher
                on_active: root.checkbox_click(self, self.active, "Teacher")      
            Label:
                text: "Student"
                font_size: 20
                color: 'black'
            CheckBox:
                id: student
                on_active: root.checkbox_click(self, self.active, "Student")
        GridLayout:
            cols:1
            Label:
                id: output_label
                text: ""
                color: 'black'
            RedButton:
                text: 'Sign Up'
                on_press: root.sign_up()
                # root.manager.current = 'choose'               


<ChooseLanguage>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        MDLabel:
            text: "Hi, which language would you like to practice?"
            font_size: 25
            color: '#ad1035'
        MDRaisedButton:
            id: language
            text: "Language"
            pos_hint:{"center_x":0.5, "center_y":1}
            on_release: root.dropdown_languages()
        MDRaisedButton:
            id: level
            text: "Level"
            pos_hint:{"center_x":0.5, "center_y":1}
            on_release: root.dropdown_levels()
        MDGridLayout:
            adaptive_height: True
            cols: 4
            Label:
                text: "Online"
                font_size: 20
                color: 'black'
            CheckBox:
                id: online
                group: "online_onsite"
                on_active: root.checkbox_click(self, self.active)      
            Label:
                text: "Onsite"
                font_size: 20
                color: 'black'
            CheckBox:
                id: onsite
                group: "online_onsite"
                on_active: root.checkbox_click(self, self.active)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)       
            MDRaisedButton:
                id: city
                text: "City"
                pos_hint:{"center_x":0.5, "center_y":1}
                on_release: root.dropdown_cities()
            RedButton:
                text: 'Search'
                on_press: 
                    app.show_records()
                    app.count_records()
                    root.manager.current = 'search' 
                    root.manager.transition.direction = "left"

<SearchResults>:
    MDFloatingActionButton:
        icon: "arrow-left"
        pos_hint: {"center_x": .8, "center_y": .1}
        text_color: [1, 1, 1, 1]
        md_bg_color: [0, 0, 1, 1]
        user_font_size: 50
        on_press: 
            root.manager.current = 'choose'
            root.manager.transition.direction = "right"
            root.delete_records()
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(10)
        MDGridLayout:
            cols: 1
            Label:
                id: count
                font_size: 10
                color: 'black'
            Label:
                text: "Available lessons:"
                font_size: 20
                color: 'black'
        MDGridLayout:
            cols: 4
            Label:
                id: search_results_name
                font_size: 15
                color: 'black'
            Label:
                id: search_results_date_element
                font_size: 15
                color: 'black'
            Label:
                id: search_results_start
                font_size: 15
                color: 'black'
            Label:
                id: search_results_end
                font_size: 15
                color: 'black' 
""")


# Declare screens
class StartScreen(Screen):
    pass


class LoginScreen(Screen):
    user = ObjectProperty()
    password = ObjectProperty()
    def login(self):
        try:
            f = open("connection.txt", "r")
            lines = f.readlines()
            server = lines[0].strip()
            database = lines[1].strip()
            username = lines[2].strip()
            password = lines[3].strip()
            f.close()
            con = pyodbc.connect(
                'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
                autocommit=True)
            cur = con.cursor()
            # Prepare the stored procedure execution script and parameter values
            storedProc = "Exec [dbo].[p_login] @email = ?, @password = ?"
            params = (self.user.text,self.password.text)

            # Execute Stored Procedure With Parameters
            cur.execute(storedProc, params)
            con.commit()
            con.close()
            self.manager.current = 'choose'
            self.manager.transition.direction = "left"
        except:
            self.ids.error_label.text = "User doesn't exist"

class SignUpScreen(Screen, Widget):
    checks = []

    def checkbox_click(self, instance, value, status):
        if value == True:
            SignUpScreen.checks.append(status)
            stat = ''
            for x in SignUpScreen.checks:
                stat = f'{stat} {x}'
            self.ids.output_label.text = f'You selected: {stat}'
        else:
            SignUpScreen.checks.remove(status)
            stat = ''
            for x in SignUpScreen.checks:
                stat = f'{stat} {x}'
            self.ids.output_label.text = f'You selected: {stat}'

    first = ObjectProperty()
    surname = ObjectProperty()
    phone = ObjectProperty()
    birth_date = ObjectProperty()
    email_address = ObjectProperty()
    password = ObjectProperty()
    def sign_up(self):
        try:
            f = open("connection.txt", "r")
            lines = f.readlines()
            server = lines[0].strip()
            database = lines[1].strip()
            username = lines[2].strip()
            password = lines[3].strip()
            f.close()
            con = pyodbc.connect(
                'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
                autocommit=True)
            cur = con.cursor()
            # Prepare the stored procedure execution script and parameter values
            storedProc = "Exec [dbo].[p_insert_user] @name = ?, @surname = ?, @birthdate = ?, @email = ?, @phone = ?, @isteacher = ?, @isstudent = ?, @password = ?"
            params = (self.first.text,
                      self.surname.text,
                      self.birth_date.text,
                      self.email_address.text,
                      self.phone.text,
                      1 if self.ids.teacher.active else 0,
                      1 if self.ids.student.active else 0,
                      self.password.text)

            # Execute Stored Procedure With Parameters
            cur.execute(storedProc, params)
            con.commit()
            con.close()
            self.manager.current = 'choose'
            self.manager.transition.direction = "left"
        except:
            print(self.first.text,
                      self.surname.text,
                      self.birth_date.text,
                      self.email_address.text,
                      self.phone.text,
                      1 if self.ids.teacher.active else 0,
                      1 if self.ids.student.active else 0,
                      self.password.text)

    def switch(self):
        self.manager.current = 'login'
        self.manager.transition.direction = "right"


class ChooseLanguage(Screen, Widget):
    def checkbox_click(self, instance, value):
        pass

    #Language

    def dropdown_languages(self):
        f = open("connection.txt", "r")
        lines = f.readlines()
        server = lines[0].strip()
        database = lines[1].strip()
        username = lines[2].strip()
        password = lines[3].strip()
        f.close()
        con = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
            autocommit=True)
        cur = con.cursor()
        cur.execute("select name from Languages")
        languages = cur.fetchall()

        self.language_list = [
            {
                "text": f"{i.name}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i.name}": self.menu_callback1(x),
            } for i in languages
        ]
        con.commit()
        con.close()
        self.menu = MDDropdownMenu(
            caller=self.ids.language,
            items=self.language_list,
            width_mult=4,
        )
        self.menu.open()

    #Level

    def dropdown_levels(self):
        f = open("connection.txt", "r")
        lines = f.readlines()
        server = lines[0].strip()
        database = lines[1].strip()
        username = lines[2].strip()
        password = lines[3].strip()
        f.close()
        con = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
            autocommit=True)
        cur = con.cursor()
        cur.execute("select level_abbrev from [Language levels]")
        levels = cur.fetchall()

        self.level_list = [
            {
                "text": f"{i.level_abbrev}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i.level_abbrev}": self.menu_callback2(x),
            } for i in levels
        ]
        con.commit()
        con.close()
        self.menu = MDDropdownMenu(
            caller=self.ids.level,
            items=self.level_list,
            width_mult=4,
        )
        self.menu.open()

    #City

    def dropdown_cities(self):
        f = open("connection.txt", "r")
        lines = f.readlines()
        server = lines[0].strip()
        database = lines[1].strip()
        username = lines[2].strip()
        password = lines[3].strip()
        f.close()
        con = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
            autocommit=True)
        cur = con.cursor()
        cur.execute("select city_name from Cities")
        cities = cur.fetchall()

        self.city_list = [
            {
                "text": f"{i.city_name}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i.city_name}": self.menu_callback3(x),
            } for i in cities
        ]
        con.commit()
        con.close()
        self.menu = MDDropdownMenu(
            caller=self.ids.city,
            items=self.city_list,
            width_mult=4,
        )
        self.menu.open()

    def menu_callback1(self, text_item1):
        self.ids.language.text = (text_item1)
        self.menu.dismiss()
    def menu_callback2(self, text_item2):
        self.ids.level.text = (text_item2)
        self.menu.dismiss()
    def menu_callback3(self, text_item3):
        self.ids.city.text = (text_item3)
        self.menu.dismiss()

class SearchResults(Screen):
    def delete_records(self):
        self.ids.search_results_name.text = ''
        self.ids.search_results_date_element.text = ''
        self.ids.search_results_start.text = ''
        self.ids.search_results_end.text = ''
        self.ids.count.text = ''


class NextScreen(Screen):
    pass


class LanguageAppApp(MDApp):
    def build(self):
        f = open("connection.txt", "r")
        lines = f.readlines()
        server = lines[0].strip()
        database = lines[1].strip()
        username = lines[2].strip()
        password = lines[3].strip()
        f.close()
        con = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
            autocommit=True)

        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (300, 500)

        # Create the screen manager
        sm = ScreenManager()
        s = Screen()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignUpScreen(name='signup'))
        sm.add_widget(NextScreen(name='next'))
        sm.add_widget(ChooseLanguage(name='choose'))
        sm.add_widget(SearchResults(name='search'))
        return sm

    def callback(self, instance_action_top_appbar_button):
        self.root.get_screen('signup').switch()

    def submit(self):
        pass

    def show_records(self):
        f = open("connection.txt", "r")
        lines = f.readlines()
        server = lines[0].strip()
        database = lines[1].strip()
        username = lines[2].strip()
        password = lines[3].strip()
        f.close()
        con = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
            autocommit=True)
        cur = con.cursor()
        view = "select name, StartTime, EndTime from v_teachers where language = ? and level = ? and city = ? and localization_id = ?"

        params = (self.root.get_screen('choose').ids.language.text,
                  self.root.get_screen('choose').ids.level.text,
                  self.root.get_screen('choose').ids.city.text,
                  1 if self.root.get_screen('choose').ids.online.active else 2)
        cur.execute(view, params)
        records = cur.fetchall()
        result = ''
        date_element = ''
        start = ''
        end = ''
        for record in records:
            result = f'{result}\n{record[0]}'
            date_element = f'{date_element}\n{record[1].date()}'
            dateformat = '%H:%M'
            start = f'{start}\n{record[1].strftime(dateformat)}'
            end = f'{end}\n{record[2].strftime(dateformat)}'
            self.root.get_screen('search').ids.search_results_name.text = f'{result}'
            self.root.get_screen('search').ids.search_results_date_element.text = f'{date_element}'
            self.root.get_screen('search').ids.search_results_start.text = f'{start}'
            self.root.get_screen('search').ids.search_results_end.text = f'{end}'

        con.commit()
        con.close()

    def count_records(self):
        f = open("connection.txt", "r")
        lines = f.readlines()
        server = lines[0].strip()
        database = lines[1].strip()
        username = lines[2].strip()
        password = lines[3].strip()
        f.close()
        con = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + '; DATABASE=' + database + '; UID=' + username + ';PWD=' + password,
            autocommit=True)
        cur = con.cursor()
        view = "select count(*) from v_teachers where language = ? and level = ? and city = ? and localization_id = ?"
        params = (self.root.get_screen('choose').ids.language.text,
                  self.root.get_screen('choose').ids.level.text,
                  self.root.get_screen('choose').ids.city.text,
                  1 if self.root.get_screen('choose').ids.online.active else 2)
        cur.execute(view, params)
        record = cur.fetchone()
        self.root.get_screen('search').ids.count.text = f'{record[0]} results'
        con.commit()
        con.close()


if __name__ == '__main__':
    LanguageAppApp().run()