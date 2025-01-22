import tkinter as tk
import tkinter.messagebox
from collections import namedtuple

PopupMessage = namedtuple(
    typename="PopupMessage",
    field_names=["title", "body"],
)


def show_messages(messages: list[PopupMessage]) -> None:
    """Shows `messages` sequentially as popup windows"""
    tk_root = tk.Tk()
    tk_root.withdraw()

    for message in messages:
        tkinter.messagebox.showinfo(
            title=message.title,
            message=message.body,
        )

    tk_root.destroy()
