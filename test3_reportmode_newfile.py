import tkinter as tk
from tkinter import ttk

# 初期項目
root = tk.Tk()
root.title("NoteBook by Tkinter (presented by sho0529-codes)")
input_text = ""
input_path = None
output_text = ""
output_path = "notebook_by_tkinter/test3_reportmode_newfile.txt"

def README_mode():
    # 入力欄
    text = tk.Text(root, width=100)
    text.pack()
    text.insert("1.0", "「テーマ」\n\n\n「要件」\n\n\n「内容整理」\n\n\n「段落整理」\n\n\n「本文」")

    # 保存ボタン
    save_button = tk.Button(root, text="保存", command=lambda: save_text(), width=10)
    save_button.pack(side=tk.LEFT)

    def insert_template(template):
        text.insert(tk.INSERT, template)
    
    def save_text():
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
            print("save")
    
    def override_text():
        pass

README_mode()
root.mainloop()
