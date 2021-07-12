from tkinter import *

# Labels
BUTTON_TEXT = 'Refresh'

# CSS
NOTIFY_COLOR_SUCCESS = 'green'
NOTIFY_COLOR_ERR = 'red'


class NotifierFrame:

    def __init__(self, master, frame_padding: int, reset_function):
        self.main_frame = LabelFrame(master=master, borderwidth=0, padx=frame_padding, pady=frame_padding)
        self.notification_lbl = Label(master=self.main_frame, padx=10, pady=10)
        self.submit_btn = Button(master=self.main_frame, text=BUTTON_TEXT, width=10, command=reset_function)

        self.notification_lbl.pack()
        self.submit_btn.pack()
        self.main_frame.pack()

    def set_success_message(self, message: str):
        self.notification_lbl.config(text=message, fg=NOTIFY_COLOR_SUCCESS)

    def set_error_message(self, message: str):
        self.notification_lbl.config(text=message, fg=NOTIFY_COLOR_ERR)

    def clear_message(self):
        self.set_success_message(message='')
