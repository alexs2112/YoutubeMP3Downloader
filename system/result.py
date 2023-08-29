import tkinter
from system.config import *

class Result:
    def __init__(self, result):
        self.result = result
        self.selected = False

    def pack(self, frame):
        self.widgets = []

        self.master_frame = tkinter.Frame(master=frame, bg=COLOUR_BACKGROUND, pady=6, highlightthickness=2, highlightbackground=COLOUR_DISABLED_BACKGROUND, width=400, height=60)
        self.master_frame.pack()
        self.master_frame.bind("<Button-1>", self.click)
        self.master_frame.pack_propagate(0)
        self.widgets.append(self.master_frame)
        left_frame = tkinter.Frame(master=self.master_frame, bg=COLOUR_BACKGROUND)
        left_frame.pack(side=tkinter.LEFT, anchor='w')
        self.widgets.append(left_frame)

        title_frame = tkinter.Frame(master=left_frame, bg=COLOUR_BACKGROUND)
        title_frame.pack(side=tkinter.TOP, anchor='w')
        self.widgets.append(title_frame)
        data_frame = tkinter.Frame(master=left_frame, bg=COLOUR_BACKGROUND)
        data_frame.pack(side=tkinter.BOTTOM, anchor='w')
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

    def destroy(self):
        self.widgets.reverse()
        for w in self.widgets:
            w.destroy()

    def click(self, _):
        if self.selected:
            self.selected = False
            self.master_frame.configure(highlightbackground=COLOUR_DISABLED_BACKGROUND)
        else:
            self.selected = True
            self.master_frame.configure(highlightbackground=COLOUR_FOREGROUND)
