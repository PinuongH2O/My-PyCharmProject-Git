# Danh sách công việc
task = []

# Tạo hàm menu
def display_task():
    print ("\n === To Do list ===")
    print ("1. Thêm công việc")
    print ("2. Xem danh sách làm việc ")
    print ("3. Xoá công việc")
    print ("4. Thoát")

# Lặp lại menu
while True:
    display_task()
    choice = input("Nhập (1-4): ")
    if choice == "1":
        tasks = input("Tên công việc: ")
        task.append (tasks)
        print ("Đã thêm công việc thành công!")

    elif choice == "2":
        print ("\nDanh sách công việc đã thêm")
        for index, tasks in enumerate(task, start=1):
            print (f"{index}. {task}")

    elif choice == "3":
        index = int(input("Nhập công việc bạn muốn xoá: ")) -1
        if 0 <= index < len(task):
            remove = task.pop(index)
            print ("Đã xoá: ", remove)
        else:
            print ("Số thứ tự không hợp lệ!!!")

    elif choice == "4":
        print ("Tạm biệt!")
        break

    else:
        print ("Lựa chọn không hợp lệ!!!")

