import random

games_played = 0

while True:
    print ("==Main menu==")
    print ("1. Chơi/Play")
    print ("2. Xem lại ván đấu/ Watchinh gameplay before")
    print ("3. Kết thúc/End")

    choice = input("Chọn: ")

    if choice == "1":
        print ("Bắt đầu thôi")

        print ("\nChọn độ khó")
        print ("1. Dễ/Begin")
        print ("2. Vừa/Normal")
        print ("3. Khó/Hardest")
        print ("4. Điên/Crazy")

        dificult = input("Chọn độ khó/ choose: ")

        if dificult == "1":
            max_number = 10
        elif dificult == "2":
            max_number = 50
        elif dificult == "3":
            max_number = 100
        elif dificult == "4":
            max_number = 200
        else:
            print ("Độ khó không có/None difficult")
            continue

        secret_numbers = random.randint(1, max_number)

        print (f"\nTôi đã chọn số từ 1 đến {max_number}")

        attempts = 0

        while True:
            guess = int(input("Tôi đoán là: "))
            attempts += 1

            if guess == secret_numbers:
                print ("Bạn thắng rồi/You win")
                print ("Số lần đoán", attempts)
                games_played += 1
                break

            elif guess < secret_numbers:
                print ("⬆ Cao hơn bạn nghĩ ấy/Higher")

            elif guess > secret_numbers:
                print ("⬇ Thấp hơn bạn nghĩ ấy/Lower")

    elif choice == "2":
        print ("\n📊 Số ván đã chạm mức", games_played)

    elif choice == "3":
        print ("Tạm biệt, bái bai")
        break

    else:
        print (" Lựa chọn không hợp lệ")