import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Pack Creator")

# UI Elements
title = customtkinter.CTkLabel(app, text="Create Pack")
title.pack(padx=10, pady=20)

# Input
pack_title_input = tkinter.StringVar()
pack_title = customtkinter.CTkEntry(app, width=500, height=50, textvariable=pack_title_input)
pack_title.pack()

pack_description_input = tkinter.StringVar()
pack_description = customtkinter.CTkEntry(app, width=500, height=300, textvariable=pack_description_input)
pack_description.pack(pady=10)

key_input = tkinter.StringVar(value="C")
key = customtkinter.CTkOptionMenu(app, height=30, width=100, values=["C", "C#", "D"], variable=key_input)
key.pack(pady=20)

# run app
app.mainloop()
