import tkinter as tk
import tkinter.messagebox as tkm

def num_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num, f"{num}のボタンが押されました")
    entry.insert(tk.END, num)
    
def equal_click(event):
    eqn = entry.get() # getメソッドは引数いらない
    res = eval(eqn) # 式の評価
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

root = tk.Tk()
root.title("電卓")
root.geometry("300x700") #練習１

entry = tk.Entry(root, width=10, font=("", 40), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
numbers = list(range(9, -1, -1)) # 数字のリスト
enzanshi = ["+", "-", "*", "/"] # 演算子のリスト

for i, num in enumerate(numbers + enzanshi, 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width = 4, height = 2)
    btn.bind("<1>", num_click)
    btn.grid(row=r, column=c)
    c += 1
    if i % 3 == 0:
        r += 1
        c = 0

# equalボタンの追加
btn = tk.Button(root, text=f"=", font=("Times New Roman", 30), width = 4, height = 2)
btn.bind("<1>", equal_click)
btn.grid(row=r, column=c)

root.mainloop()