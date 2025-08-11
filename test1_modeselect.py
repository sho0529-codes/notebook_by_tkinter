import tkinter as tk
from tkinter import ttk

# 初期項目
root = tk.Tk()
root.title("NoteBook by Tkinter (presented by sho0529-codes)")
input_text = ""
input_path = None
output_text = ""
output_path = None

def mode_select():
    mode_list = ["README", "Plan", "Report", "None", ]
    combo = ttk.Combobox(root, values=mode_list)
    combo.set(mode_list[-1])  # 初期値
    combo.pack()

    def push_button():
        select_mode = combo.get()
        if select_mode in mode_list:
            print("選択されたモード：", select_mode)
        else:
            print("無効なモード：", select_mode)

    button = tk.Button(root, text="確定", command=push_button)  # push_button()にしない
    button.pack()

mode_select()
root.mainloop()
