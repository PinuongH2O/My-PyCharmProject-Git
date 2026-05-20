# Bài 15: Cải tiến ứng dụng máy tính
num1 = float(input("Nhập sô thứ nhất: "))
operator = input("Nhập phép toán (+, -, *, /): ")
num2 = float(input("Nhập số thứ hai: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Lỗi: Toán tử không hợp lệ")
