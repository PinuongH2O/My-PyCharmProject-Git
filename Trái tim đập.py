import tkinter as tk
import math

# Tạo cửa sổ
root = tk.Tk()
root.title("Trái tim đang đập")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Hàm tạo điểm trái tim
def heart_points(scale):
    points = []
    for t in range(0, 360):
        t = math.radians(t)
        x = 16 * math.sin(t)**3
        y = (13 * math.cos(t)
             - 5 * math.cos(2*t)
             - 2 * math.cos(3*t)
             - math.cos(4*t))
        points.append((200 + x * scale, 200 - y * scale))
    return points

scale = 10
direction = 1

# Hàm animate
def animate():
    global scale, direction
    canvas.delete("all")

    pts = heart_points(scale)

    # Vẽ trái tim
    for i in range(len(pts)-1):
        canvas.create_line(pts[i], pts[i+1], fill="red", width=2)

    # Tạo hiệu ứng đập
    scale += direction * 0.3
    if scale > 12 or scale < 9:
        direction *= -1

    root.after(30, animate)

animate()
root.mainloop()