import flet as ft
from weather_scraper import get_today_weather


def main(page: ft.Page):
    result = ft.Text(value="天気を取得してください", size=30)

    def on_click(e):
        result.value = "取得中..."
        page.update()

        weather = get_today_weather()
        result.value = f"今日の天気: {weather}"
        page.update()

    get_button = ft.ElevatedButton(text="今日の天気を調べる", on_click=on_click)

    page.add(
        ft.Column(
            [result, get_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )


ft.app(target=main)
