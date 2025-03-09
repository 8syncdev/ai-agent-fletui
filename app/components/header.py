import flet as ft
from typing import (
    Literal,
    Dict,
)

Kwargs = Dict[
    Literal["handle_animaton_shrink"],
    ft.ControlEvent
]



class Header(ft.Container):


    def __init__(self, **kwargs: Kwargs):
        super().__init__()
        kwargs: Kwargs = kwargs
        self.height = 50
        self.width = 1400
        self.bgcolor = ft.Colors.DEEP_PURPLE_500
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.only(right=10)

        self.content = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_size=24,
                    icon_color=ft.Colors.WHITE,
                    on_click=kwargs.get("handle_animaton_shrink"),
                ),
                ft.CircleAvatar(
                    content=ft.Icon(
                        name=ft.Icons.PERSON,
                        size=24,
                        color=ft.Colors.WHITE,

                    ),
                    bgcolor=ft.Colors.PURPLE_500,
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )