import threading

import customtkinter as ctk

from chatbot_app import AwesomeChatbotApp


def run_chatbot(app: AwesomeChatbotApp) -> None:
    """Run chatbot logic in a daemon thread so UI remains responsive."""
    app.run_chat_logic()


def main() -> None:
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = AwesomeChatbotApp(root)

    chatbot_thread = threading.Thread(
        target=run_chatbot,
        args=(app,),
        daemon=True,
        name="chatbot-logic-thread",
    )
    chatbot_thread.start()

    root.mainloop()


if __name__ == "__main__":
    main()