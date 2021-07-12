from tkinter import *
from tkinter import filedialog

# Constants
DIRECTORY_TYPES = ['Movie', 'Show', 'Music', 'Ebook', 'Photo']

# Labels
FRAME_TITLE = 'Add new library'
SELECT_TYPE_DEFAULT_LBL = 'Select library type'
BTN_BROWSE_LBL = 'Browse for directory'
BTN_ADD_LBL = 'Add'
ERR_DIRECTORY_TYPE = 'Select library type'
ERR_DIRECTORY_PATH = 'Choose directory path'


class AddNewDirectoryFrame:

    def __init__(self, master, frame_padding: int, submit_action):
        self.main_frame = LabelFrame(master=master, text=FRAME_TITLE, padx=frame_padding, pady=frame_padding)
        self.browse_btn = Button(master=self.main_frame, text=BTN_BROWSE_LBL, width=60)
        self.submit_action = submit_action
        self.new_dir_type = StringVar()
        self.new_dir_path = StringVar()
        self.main_frame.pack()
        self.reset()

    def __browse_directory(self):
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.new_dir_path.set(selected_directory)
            self.browse_btn['text'] = selected_directory
        else:
            self.new_dir_path.set('')
            self.new_dir_type.set(SELECT_TYPE_DEFAULT_LBL)

    def reset(self):
        # Directory type
        self.new_dir_type.set(SELECT_TYPE_DEFAULT_LBL)
        dir_type_select = OptionMenu(self.main_frame, self.new_dir_type, *DIRECTORY_TYPES)
        dir_type_select.config(width=15)

        # Directory path
        self.new_dir_path.set(BTN_BROWSE_LBL)
        self.browse_btn['command'] = self.__browse_directory
        self.browse_btn['text'] = self.new_dir_path.get()

        # Submit
        submit_button = Button(master=self.main_frame, text=BTN_ADD_LBL, width=20, command=self.submit_action)

        dir_type_select.grid(row=0, column=0)
        self.browse_btn.grid(row=0, column=1)
        submit_button.grid(row=1, column=0, columnspan=2)

    def get_directory_type(self):
        if self.new_dir_type.get() != SELECT_TYPE_DEFAULT_LBL:
            return self.new_dir_type.get()
        else:
            raise Exception(ERR_DIRECTORY_TYPE)

    def get_directory_path(self):
        if self.new_dir_path.get() != BTN_BROWSE_LBL:
            return self.new_dir_path.get()
        else:
            raise Exception(ERR_DIRECTORY_PATH)
