import flet as ft


class NavigationScreen(ft.Container):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.width = 1400
        self.bgcolor = ft.Colors.WHITE
        self.expand = True

        self.content = ft.Column(
            controls=[
                ft.Text(
                    value="Navigation Screen"
                )
            ]
        )