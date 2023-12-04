import subprocess
import sys

def install(packege):
        subprocess.check_call([sys.executable, "-m", "pip", "install", packege])

try:
    import pyautogui as pt
    import time
    import tkinter as tk
    from tkinter import Label, Entry, Button, ttk
    from itertools import cycle

except:
    list1 = ['tkinter','PyAutoGUI','time','itertools']
    for i in list1:
        install(i)



class Devastorix:
    def __init__(self, root):
        self.root = root
        self.root.title("Devastorix")
        self.root.geometry("800x720")
        self.root.configure(bg="#1E1E1E")
        self.root.resizable(False, False)

        self.bg_color = "#1E1E1E"
        self.fg_color = "#FFFFFF"
        self.fg1_color = "#83E42B"
        self.fg2_color = "#FF0000"
        self.entry_bg_color = "#222222"

        self.create_widgets()

    def create_widgets(self):
        self.root.config(bg=self.bg_color)

        self.header_label = Label(
            self.root, text="Devastorix", font=("System", 55, "bold"), bg=self.bg_color, fg=self.fg1_color
        )
        self.header_label.pack(pady=17)

        Label(self.root, text="Message:", font=("System", 17, "bold"), bg=self.bg_color, fg=self.fg1_color).pack(
            pady=5)
        self.message_entry = Entry(self.root, width=35, font=("System", 17), bg=self.entry_bg_color,
                                    fg=self.fg_color)
        self.message_entry.pack(pady=15)

        Label(self.root, text="Limit:", font=("System", 17, "bold"), bg=self.bg_color, fg=self.fg1_color).pack(
            pady=5)
        self.limit_entry = Entry(self.root, width=35, font=("System", 17), bg=self.entry_bg_color,
                                  fg=self.fg_color)
        self.limit_entry.pack(pady=15)

        Label(self.root, text="Sleep Time (s):", font=("System", 17, "bold"), bg=self.bg_color,
              fg=self.fg1_color).pack(pady=5)
        self.sleep_time_entry = Entry(self.root, width=35, font=("System", 17), bg=self.entry_bg_color,
                                      fg=self.fg_color)
        self.sleep_time_entry.insert(0, "1")
        self.sleep_time_entry.pack(pady=15)

        self.send_button = Button(
            self.root, text="Send Messages", command=self.send_messages, font=("System", 17, "bold"),
            bg=self.bg_color, fg=self.fg1_color
        )
        self.send_button.pack(pady=10)

        self.result_label = Label(
            self.root, text="", font=("System", 17), bg=self.bg_color, fg=self.fg2_color
        )
        self.result_label.pack(pady=15)

    def send_messages(self):
        message = self.message_entry.get()
        limit = self.limit_entry.get()
        sleep_time = self.sleep_time_entry.get()

        try:
            limit = int(limit)
            sleep_time = float(sleep_time)

            if limit < 1 or sleep_time < 0:
                raise ValueError("Limit must be greater than 0 and Sleep Time must be non-negative.")
        except ValueError as e:
            self.result_label.config(text=str(e))
            return

        for countdown in range(5, 0, -1):
            self.result_label.config(text=f"Sending messages in {countdown} seconds...")
            self.root.update_idletasks()
            time.sleep(1)

        self.result_label.config(text="Sending messages...")

        loading_symbols = cycle(["◐", "◓", "◑", "◒"])  

        progress_frame = tk.Frame(self.root, bg=self.bg_color)
        progress_frame.pack(pady=20)

        progress_label = Label(progress_frame, text="", font=("System", 20), bg=self.bg_color, fg=self.fg1_color)
        progress_label.pack()

        progress_bar = ttk.Progressbar(
            progress_frame, orient="horizontal", length=400, mode="determinate", style="Custom.Horizontal.TProgressbar"
        )
        progress_bar.pack(pady=10)
        progress_bar["value"] = 0
        self.root.update_idletasks()

        i = 0
        while i < limit:
            pt.typewrite(message)
            pt.press("enter")

            progress_bar["value"] = (i + 1) * 100 / limit
            progress_label.config(text=f"Sending messages... {next(loading_symbols)}")
            self.root.update_idletasks()

            i += 1
            time.sleep(sleep_time)

        progress_frame.destroy()
        self.result_label.config(text=f"Sent {limit} messages")

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Custom.Horizontal.TProgressbar", thickness=30, troughcolor="#1E1E1E", bordercolor="#1E1E1E",
                background="#83E42B", troughrelief="flat", lightcolor="#1E1E1E",
                darkcolor="#1E1E1E", troughborderwidth=0)
    Devastorix(root)
    icon_path = "./icon.ico"
    root.iconbitmap(icon_path)
    root.mainloop()


if __name__ == "__main__":
    main()
