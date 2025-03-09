import flet as ft
from app.components import (
    Header
)

from app.screens import (
    HomeScreen,
    NavigationScreen
)

from app.providers import (
    ScreenStackProvider
)


def main(page: ft.Page):
    page.title = "Ai Agent Chat"

    page.window.height = 800
    page.window.width = 1400

    page.window.left = 400

    screen_stack = ScreenStackProvider()

    header = Header(
        handle_animaton_shrink=screen_stack.home_screen.handle_animation_shrink
    )

    page.add(
        header,
        screen_stack,
    )


if __name__ == "__main__":
    ft.app(
        target=main,
    )