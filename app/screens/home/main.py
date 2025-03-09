import flet as ft
from app.animations import AnimationsUtils
from app.components import MessageCard, Loading
from app.model_llm import get_answer

class HomeScreen(ft.Container):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.width = 1400
        self.bgcolor = ft.Colors.WHITE
        self.expand = True
        self.animate_scale = ft.animation.Animation(
            duration=600,   
            curve=ft.animation.AnimationCurve.DECELERATE     
        )
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.all(10)

        self.content_chats = ft.ListView(
            height=600,
            width=self.width,
            controls=[
                MessageCard("ai", message="Hello, how can I help you?"),
                MessageCard("human", message="I need help with my account."),
            ],
        )

        self.text_field = ft.TextField(
            hint_text="Type a message",
            expand=True,
        )

        self.input_chat = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.Icons.INSERT_EMOTICON,
                        size=24,
                    ),
                    self.text_field,
                    ft.IconButton(
                        icon=ft.Icons.SEND,
                        icon_size=24,
                        on_click=self.handle_chat,
                    ),
                ],
            ),
        )

        self.content = ft.Column(
            controls=[
                self.content_chats,
                self.input_chat,
            ]
        )

    def handle_animation_shrink(self, event: ft.ControlEvent):
        AnimationsUtils.animation_shrink(self, event)

    def handle_chat(self, event: ft.ControlEvent):
        loading = Loading()
        self.content_chats.controls.extend(
           [
                MessageCard("human", message=self.text_field.value),
                loading,
           ]
        )
        self.content_chats.update()
        # loading.infinite_animation()

        answer_from_ai = get_answer(self.text_field.value)
        print(answer_from_ai)
        self.content_chats.controls.pop()
        self.content_chats.controls.append(
            MessageCard("ai", message=answer_from_ai)
        )
        self.content_chats.update()
