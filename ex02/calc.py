import tkinter as tk
import tkinter.messagebox as tkm
import math

def num_click(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)

# イコールボタン  
def equal_click(event):
    eqn = entry.get() # getメソッドは引数いらない
    res = eval(eqn) # 式の評価
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

# オールクリア
def allclear_click(event):
    entry.delete(0, tk.END)

# クリア
def clear_click(event):
    n = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, n[:-1])

# %で表示
def percent_click(event):
    per = entry.get()
    ans = eval(per) / 100
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

# 平方根
def sqrt_click(event):
    sq = entry.get()
    rsl = math.sqrt(eval(sq))
    entry.delete(0, tk.END)
    entry.insert(tk.END, rsl)

root = tk.Tk()
root.title("電卓")
root.geometry("400x800") #練習１

entry = tk.Entry(root, width=10, font=("", 40), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=4)

r, c = 1, 0
numbers = list(range(9, -1, -1)) # 数字のリスト
enzanshi = ["+", "-", "*", "/"] # 演算子のリスト

for i, num in enumerate(numbers + enzanshi, 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width = 4, height = 2, bg="white")
    btn.bind("<1>", num_click)
    btn.grid(row=r, column=c)
    c += 1
    if i % 4 == 0:
        r += 1
        c = 0

# equalボタンの追加
btn = tk.Button(root, text=f"=", font=("Times New Roman", 30), width = 4, height = 2, bg="blue")
btn.bind("<1>", equal_click)
btn.grid(row=r, column=c)

# オールクリアボタンの追加
btn = tk.Button(root, text=f"AC", font=("Times New Roman", 30), width = 4, height = 2, bg="red")
btn.bind("<1>", allclear_click)
btn.grid(row=r, column=c+1)

# クリア
btn = tk.Button(root, text=f"C", font=("Times New Roman", 30), width = 4, height = 2, bg="red")
btn.bind("<1>", clear_click)
btn.grid(row=r+1, column=c+1)

# %表示の追加
btn = tk.Button(root, text=f"%", font=("Times New Roman", 30), width = 4, height = 2, bg="white")
btn.bind("<1>", percent_click)
btn.grid(row=r+1, column=c-2)

# 平方根
btn = tk.Button(root, text=f"√", font=("Times New Roman", 30), width = 4, height = 2, bg="white")
btn.bind("<1>", sqrt_click)
btn.grid(row=r+1, column=c-1)

root.mainloop()