import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


team = [
    "ポン・デ・リング",
    "ポン・デ・ストロベリー",
    "フレンチクルーラー",
    "オールドファッション",
    "チョコレート",
    "エンゼルクリーム",
]
num = len(team)

label0 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label0.pack(pady=10)

label0.config(text=team[random.randrange(num)])


def button_action1():
    user_input = entry1.get()  # 関数の定義 ※ボタンが押されたときの動き
    entry1.delete(0, 100)
    if label0.cget("text") == user_input:
        label0.config(text=team[random.randrange(num)])


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)


# ボタンの作成
button1 = tk.Button(window, text="OK", command=button_action1)
button1.pack(pady=10)


# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
