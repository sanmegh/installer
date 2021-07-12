import time
from tkinter import *

import clients.app_service_client as service_client
from components.frame__add_new_library import AddNewDirectoryFrame
from components.frame__library_list import LibraryList
from components.frame__notifier import NotifierFrame

# App Config
APP_TITLE = 'DriveMan: Library Manager'
APP_LOGO = 'app-logo.png'
APP_RESOLUTION = '800x600'

# Notifications
NOTIFY_MSG_ADD = 'Directory added successfully.'
NOTIFY_MSG_RESCAN = 'Directory scanning scheduled.'
NOTIFY_MSG_REMOVE = 'Directory removed.'

# CSS
FRAME_PADDING = 20


class Application:

    def __init__(self):
        root_window = Tk()
        root_window.title(APP_TITLE)
        root_window.call('wm', 'iconphoto', root_window._w, PhotoImage(file=APP_LOGO))
        root_window.geometry(APP_RESOLUTION)

        self.library_list_frame = LibraryList(
            master=root_window, frame_padding=FRAME_PADDING, rescan_action=self.__rescan_directory_command, remove_action=self.__remove_directory_command
        )
        self.add_library_frame = AddNewDirectoryFrame(
            master=root_window, frame_padding=FRAME_PADDING, submit_action=self.__create_new_directory
        )
        self.notifier_frame = NotifierFrame(
            master=root_window, frame_padding=FRAME_PADDING, reset_function=self.__load
        )

        self.__load()
        root_window.mainloop()

    def __load(self):
        self.notifier_frame.clear_message()
        try:
            library_list = service_client.load_libraries()
            self.library_list_frame.set_library_list(library_list=library_list)
            self.library_list_frame.reload()
            self.add_library_frame.reset()
        except Exception as ex:
            self.notifier_frame.set_error_message(str(ex))

    def __create_new_directory(self):
        try:
            dir_type = self.add_library_frame.get_directory_type().upper()
            dir_path = self.add_library_frame.get_directory_path()
            service_client.add_library(dir_type, dir_path)
            time.sleep(1)
            self.__load()
            self.notifier_frame.set_success_message(NOTIFY_MSG_ADD)
        except Exception as ex:
            self.notifier_frame.set_error_message(str(ex))

    def __rescan_directory_command(self, directory_id):
        try:
            service_client.rescan_library(directory_id)
            self.notifier_frame.set_success_message(NOTIFY_MSG_RESCAN)
        except Exception as ex:
            self.notifier_frame.set_error_message(str(ex))

    def __remove_directory_command(self, directory_id):
        try:
            service_client.remove_library(directory_id)
            self.notifier_frame.set_success_message(NOTIFY_MSG_REMOVE)
        except Exception as ex:
            self.notifier_frame.set_error_message(str(ex))


Application()
