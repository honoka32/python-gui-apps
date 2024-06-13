import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

label2 = tk.Label(window, text="西暦を入力してください", bg=bg_color, fg=fg_color)
label2.pack(pady=10)


def date():  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(entry1.get())
    if seireki >= 1868 and seireki <= 1911:
        if (seireki - 1867) == 1:
            label1.config(text=f"西暦{seireki}年は明治元年です")
        else:
            label1.config(text=f"西暦{seireki}年は明治{seireki-1867}年です")
    elif seireki >= 1912 and seireki <= 1925:
        if (seireki - 1911) == 1:
            label1.config(text=f"西暦{seireki}年は大正元年です")
        else:
            label1.config(text=f"西暦{seireki}年は大正{seireki-1911}年です")
    elif seireki >= 1926 and seireki <= 1988:
        if (seireki - 1925) == 1:
            label1.config(text=f"西暦{seireki}年は昭和元年です")
        elif seireki == 1984:
            label1.config(text=f"西暦{seireki}は松岡俊亮の生まれた年です")
        else:
            label1.config(text=f"西暦{seireki}年は昭和{seireki-1925}年です")
    elif seireki >= 1989 and seireki <= 2018:
        if (seireki - 1988) == 1:
            label1.config(text=f"西暦{seireki}年は平成元年です")
        else:
            label1.config(text=f"西暦{seireki}年は平成{seireki-1988}年です")
    elif seireki >= 2019 and seireki <= 2050:
        if (seireki - 2018) == 1:
            label1.config(text=f"西暦{seireki}年は令和元年です")
        else:
            label1.config(text=f"西暦{seireki}年は令和{seireki-2018}年です")
    else:
        label1.config(text="対応していない西暦です")


# label1.config(text=f"{user_input1}+")  # 画面に出力


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="変換", command=date)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
