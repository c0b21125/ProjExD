import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym
    

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
    ket = "" # 現在押されているキーを表す変数

    # 練習５
    root.bind("<KeyPress>", key_down)

    root.mainloop()