import pyautogui
import customtkinter as ctkinter
class EntryWidget(ctkinter.CTkEntry):
    def init(self, master):
        super().init(master, placeholder_text="Input your message", width=90, height=32)
        self.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
    def get_value(self):
        entry_msg = str(self.get())
        return entry_msg
class Gui(ctkinter.CTk):
    def init(self, master):
        super().init(master)
        self.title("Spammer")
        self.geometry("300x150")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.entry_widget = EntryWidget(self)
        self.entry_widget.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.button = ctkinter.CTkButton(self, text="Start", command=self.click_button)
        self.button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    def click_button(self):
        user_message = self.entry_widget.get_value()
        while True:
            pyautogui.typewrite(user_message, 0.1)
            pyautogui.press("enter")
if name == 'main':
    app = Gui(None)
    app.mainloop()





