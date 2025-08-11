import tkinter as tk
from tkinter import ttk

# 初期項目
root = tk.Tk()
root.title("NoteBook by Tkinter (presented by sho0529-codes)")
input_text = ""
input_path = None
output_text = ""
output_path = "notebook_by_tkinter/test2_READMEmode_newfile.md"

def README_mode():
    # 入力欄
    text = tk.Text(root, width=100)
    text.pack()

    # ショートカットボタン
    shortcut_button1 = tk.Button(root, text="見出し1", command=lambda: shortcut(1), width=10)
    shortcut_button1.pack(side=tk.LEFT)
    shortcut_button2 = tk.Button(root, text="見出し2", command=lambda: shortcut(2), width=10)
    shortcut_button2.pack(side=tk.LEFT)
    shortcut_button3 = tk.Button(root, text="見出し3", command=lambda: shortcut(3), width=10)
    shortcut_button3.pack(side=tk.LEFT)
    shortcut_button4 = tk.Button(root, text="箇条書き", command=lambda: shortcut(4), width=10)
    shortcut_button4.pack(side=tk.LEFT)

    # 保存ボタン
    save_button = tk.Button(root, text="保存", command=lambda: save_text(), width=10)
    save_button.pack(side=tk.LEFT)

    def insert_template(template):
        text.insert(tk.INSERT, template)

    def shortcut(mode):
        mode_list = [1, 2, 3, 4, ]
        if int(mode) in mode_list:
            mode = int(mode)
            if mode == 1:
                insert_template("# ")
            elif mode == 2:
                insert_template("## ")
            elif mode == 3:
                insert_template("### [0.py](0.py)")
            elif mode == 4:
                insert_template("- ")
        else:
            print("無効なショートカット：", mode)
    
    def save_text():
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
    
    def override_text():
        pass

README_mode()
root.mainloop()
