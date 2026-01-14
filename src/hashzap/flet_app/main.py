import flet as ft
from hashzap.config import Config, logger


def main(page: ft.Page):
    page.title = "Hashzap | Flet Chat"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.window_width = 400
    page.window_height = 600

    # Componentes da UI
    chat = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=10,
        padding=20,
    )

    def on_message_received(message):
        """Callback recebido via PubSub"""
        if message["type"] == "chat":
            msg_bubble = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            message["user"],
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.PRIMARY,
                        ),
                        ft.Text(message["text"], size=14),
                    ],
                    spacing=2,
                ),
                bgcolor=ft.colors.GREY_100,
                border_radius=10,
                padding=10,
                alignment=ft.alignment.center_left,
            )
            chat.controls.append(msg_bubble)
        elif message["type"] == "system":
            chat.controls.append(
                ft.Text(
                    message["text"],
                    size=12,
                    italic=True,
                    color=ft.colors.GREY_600,
                    text_align=ft.TextAlign.CENTER,
                )
            )
        page.update()

    page.pubsub.subscribe(on_message_received)

    def send_click(e):
        if not message_field.value.strip():
            return

        page.pubsub.send_all(
            {
                "type": "chat",
                "user": user_name.value,
                "text": message_field.value.strip(),
            }
        )
        message_field.value = ""
        page.update()

    user_name = ft.TextField(
        label="Seu Nome",
        width=150,
        border_radius=25,
        content_padding=15,
    )

    message_field = ft.TextField(
        hint_text="Digite uma mensagem...",
        expand=True,
        border_radius=25,
        on_submit=send_click,
        content_padding=15,
    )

    # Janela de entrada (Login)
    def join_chat(e):
        if not user_name.value.strip():
            user_name.error_text = "Nome Obrigatório!"
            page.update()
            return

        login_dialog.open = False
        page.pubsub.send_all(
            {"type": "system", "text": f"--- {user_name.value} entrou no chat ---"}
        )
        page.add(
            ft.AppBar(
                title=ft.Text("Hashzap"),
                bgcolor=ft.colors.PRIMARY,
                color=ft.colors.WHITE,
                center_title=True,
            ),
            ft.Container(content=chat, expand=True, bgcolor=ft.colors.BLUE_GREY_50),
            ft.Container(
                content=ft.Row(
                    [
                        message_field,
                        ft.IconButton(
                            ft.icons.SEND_ROUNDED,
                            on_click=send_click,
                            icon_color=ft.colors.PRIMARY,
                        ),
                    ],
                    spacing=10,
                ),
                padding=10,
                bgcolor=ft.colors.WHITE,
            ),
        )
        page.update()

    login_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Bem-vindo ao Hashzap"),
        content=ft.Column(
            [ft.Text("Escolha como quer ser chamado no chat:"), user_name], tight=True
        ),
        actions=[ft.ElevatedButton("Entrar no Chat", on_click=join_chat)],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    page.dialog = login_dialog
    login_dialog.open = True
    page.update()


if __name__ == "__main__":
    logger.info(f"Iniciando app Flet na porta {Config.FLET_PORT}...")
    ft.app(target=main, port=Config.FLET_PORT)
