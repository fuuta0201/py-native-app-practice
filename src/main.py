import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    def decrement_click(e):
        counter.data -= 1
        counter.value = str(counter.data)
        counter.update()
        print(e)

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.FloatingActionButton(
                                icon=ft.Icons.REMOVE, on_click=decrement_click),
                            counter,
                            ft.FloatingActionButton(
                                icon=ft.Icons.ADD, on_click=increment_click),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # 縦方向中央
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 横方向中央
                expand=True
            )
        )
    )


ft.app(main)
