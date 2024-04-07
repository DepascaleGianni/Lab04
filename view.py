import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        #Row 1
        self.t = ft.Text(value='')
        self._ddLanguage = ft.Dropdown(label="Select the language",
                                       width=self.page.width,
                                       on_change=self.__controller.handleLanguageSelection
                                       )
        self._fillDdLanguage()

        r1 = ft.Row([self._ddLanguage],width=self.page.width)

        #Row 2
        self.t2 = ft.Text(text_align=ft.TextAlign.RIGHT)
        self._ddSearchType = ft.Dropdown(label="Select the type of your search",
                                         width=300,
                                         options=[ft.dropdown.Option("Default"),
                                                  ft.dropdown.Option("Linear"),
                                                  ft.dropdown.Option("Dicotomic")],
                                         on_change=self.__controller.handleSearchType)
        self._txtIn = ft.TextField(label="your text", hint_text="Please enter the text here",
                                  width=600, on_submit=self.__controller.handleSpellCheck)

        self._btnInput = ft.ElevatedButton(text="Submit", on_click=self.__controller.handleSpellCheck)

        r2 = ft.Row([self._ddSearchType,self._txtIn,self._btnInput])

        #Row 3

        self._lvOut = ft.ListView()

        self.page.add(r1,self.t,r2,self.t2,self._lvOut)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def _fillDdLanguage(self):
        self._ddLanguage.options.append((ft.dropdown.Option("English")))
        self._ddLanguage.options.append((ft.dropdown.Option("Italian")))
        self._ddLanguage.options.append((ft.dropdown.Option("Spanish")))

