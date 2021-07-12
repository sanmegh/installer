from tkinter import *

# Labels
FRAME_TITLE = 'Libraries'
BTN_SCAN_LBL = 'Rescan'
BTN_REMOVE_LBL = 'Remove'


class LibraryList:

    def __init__(self, master, frame_padding: int, rescan_action, remove_action):
        self.main_frame = LabelFrame(master=master, text=FRAME_TITLE, padx=frame_padding, pady=frame_padding)
        self.rescan_action = rescan_action
        self.remove_action = remove_action
        self.library_list = []
        self.main_frame.pack()

    def set_library_list(self, library_list):
        self.library_list = library_list

    def reload(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        saved_dirs_row = 0
        for directory in self.library_list:
            directory_id = directory['id']
            type_lbl = Label(master=self.main_frame, text=directory['type'], anchor='w', width=15)
            path_lbl = Label(master=self.main_frame, text=directory['path'], anchor='w', width=50)
            rescan_btn = Button(master=self.main_frame, text=BTN_SCAN_LBL, width=8, command=lambda dir_id=directory_id: self.rescan_action(dir_id))
            remove_btn = Button(master=self.main_frame, text=BTN_REMOVE_LBL, width=8, command=lambda dir_id=directory_id: self.remove_directory(dir_id))
            type_lbl.grid(row=saved_dirs_row, column=0)
            path_lbl.grid(row=saved_dirs_row, column=1)
            rescan_btn.grid(row=saved_dirs_row, column=2)
            remove_btn.grid(row=saved_dirs_row, column=3)
            saved_dirs_row = saved_dirs_row + 1

    def remove_directory(self, directory_id):
        self.remove_action(directory_id)
        for d in self.library_list:
            if d['id'] == directory_id:
                self.library_list.remove(d)
                break
        self.reload()
