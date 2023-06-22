import tkinter
from system.config import *

class Result:
    def __init__(self, result):
        self.result = result
        self.selected = False

    def pack(self, frame):
        self.widgets = []

        master_frame = tkinter.Frame(master=frame, bg=COLOUR_BACKGROUND, pady=6)
        master_frame.pack()
        self.widgets.append(master_frame)
        left_frame = tkinter.Frame(master=master_frame, bg=COLOUR_BACKGROUND)
        left_frame.pack(side=tkinter.LEFT, anchor='w')
        self.widgets.append(left_frame)

        title_frame = tkinter.Frame(master=left_frame, bg=COLOUR_BACKGROUND)
        title_frame.pack()
        self.widgets.append(title_frame)
        data_frame = tkinter.Frame(master=left_frame, bg=COLOUR_BACKGROUND)
        data_frame.pack()
        self.widgets.append(data_frame)

        title = tkinter.Label(master=title_frame, text=self.result.title, bg=COLOUR_BACKGROUND)
        title.grid(row=0, column=0, sticky="W")
        self.widgets.append(title)

        desc = ""
        if self.result.type == "Album":
            if self.result.single:
                desc += "Single • "
            else:
                desc += "Album • "

        # Todo: Add support for multiple artists **without** overflowing the frame
        desc += f"{self.result.artists[0]['name']} • "

        if self.result.type == "Song":
            desc += f"{self.result.album['name']} • {self.result.duration}"
        elif self.result.type == "Album":
            desc += f"{self.result.year} • {self.result.track_count}"
        else:
            print(f"Could not find type of result:\n{self.result.data}")
        
        description = tkinter.Label(master=data_frame, text=desc, bg=COLOUR_BACKGROUND)
        description.grid(row=1, column=0, sticky="W")
        self.widgets.append(description)

        right_frame = tkinter.Frame(master=master_frame, bg=COLOUR_BACKGROUND)
        right_frame.pack(side=tkinter.RIGHT, anchor='e')
        self.widgets.append(right_frame)

        self.button = tkinter.Button(master=right_frame, text="-", padx=6, pady=2)
        self.button.bind("<Button-1>", self.click)
        self.button.pack()
        self.widgets.append(self.button)

    def destroy(self):
        self.widgets.reverse()
        for w in self.widgets:
            w.destroy()

    def click(self, _):
        if self.selected:
            self.selected = False
            self.button.configure(text="-")
        else:
            self.selected = True
            self.button.configure(text="+")
