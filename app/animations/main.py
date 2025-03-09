import flet as ft

class AnimationsUtils:

    @staticmethod
    def animation_shrink(obj: ft.Control, event: ft.ControlEvent):
        if not hasattr(obj, "state_shrink"):
            obj.state_shrink = False
        if not obj.state_shrink:
            obj.state_shrink = True
            obj.scale = ft.transform.Scale(
                .65,
                alignment=ft.alignment.center_right
            )
        else:
            obj.state_shrink = False
            obj.scale = ft.transform.Scale(
                1,
                alignment=ft.alignment.center_right
            )
        obj.update()