import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""

# 練習７
def main_proc():
    global cx, cy    
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk() # 練習１
    root.title("迷えるこうかとん")

    # キャンバスのサイズ設定
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack() # 練習２

    # 練習３ こうかとん表示
    tori = tk.PhotoImage(file="fig/0.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")

    # 練習４
    key = "" # 現在押されているキーを表す変数

    # 練習５
    root.bind("<KeyPress>", key_down)
    # 練習６
    root.bind("<KeyRelease>", key_up)

    # 練習７
    main_proc()

    root.mainloop()