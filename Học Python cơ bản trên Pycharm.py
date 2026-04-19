                                    # Thực hành bài cơ bản cùng Python
# Bài 1: Viết trương trình đầu tiên
print ("=== Bài 1: Viết trương trình đầu tiên ===")

print ("Hello, world!")
# Bài 2: Biến và Kiểu dữ liệu trong Python
print ("=== Bài 2: Biến và Kiểu dữ liệu trong Python ===")

# Đây là 1 câu chuyện ngắn
print ("Cuộc trò chuyện của Độ và Vũ")
print ("Độ: Alo Vũ hả em")
print ("Vũ: Không phải anh ơi")
print ("Độ: Thôi em đừng có chối, em mà chối là anh đăng hết thông tin của em lên mạng đấy")

print ("")

# Tạo biến và thay đổi câu chuyện ngắn trên
charactor1 = "Pin"
charactor2 = "Sữa"

print (f"Cuộc trò chuyện của {charactor1} và {charactor2}")
print (f"{charactor1}: Alo {charactor2} hả {charactor2}")
print (f"{charactor2}: Không phải {charactor1} ơi")
print (f"{charactor1}: Thôi {charactor2} đừng có chối, {charactor2} mà chối là {charactor1} đăng hết thông tin của {charactor2} lên mạng đấy")
# Bây giờ câu chuyện đã có những cái tên khác

print ("")

# Thêm một ví dụ nữa về thay đổi câu chuyện ngắn bằng biến, nhưng lần này có sự khác biệt

print (f"Cuộc trò chuyện của {charactor1} và {charactor2}")
print (f"{charactor1}: Alo {charactor2} hả {charactor2}")

print ("")

charactor1 = "Lỳ"
charactor2 = "Nguyên"

print (f"{charactor2}: Không phải {charactor1} ơi")
print (f"{charactor1}: Thôi {charactor2} đừng có chối, {charactor2} mà chối là {charactor1} đăng hết thông tin của {charactor2} lên mạng đấy")
# Lần này Lại tách ra thành 2 câu chuyện, biến charactor1 và charactor2 đã bị đổi giá trị và sẽ được sử dụng tiếp nếu không bị đổi giá trị sau này

# Các biến sử dụng kiểu dữ liệu khác như

# Number (Số):
SoA = 1
SoB = 5
SoC = 3.6
SoD = 6.7

# String (Chuỗi):
ChuoiA = "A"
ChuoiB = "B"
ChuoiC = "Bò"
ChuoiD = "Cá"
ChuoiE = "!"
ChuoiF = "#"
ChuoiG = "Pin love 36"
ChuoiH = "Pin love Python"

# Boolean (Bool)
Pin_dep_trai = True
Sua_dep_trai = False

print ("")

# Bài 3: Thao tác với String (Chuỗi)
print ("=== Bài 3: Thao tác với String (Chuỗi) ===")

# Câu lệnh gốc
print ("Độ Mixi bán khô gà và bã mía")

print ("")

# Cho 1 phần String xuống dòng (Cách 1)
print ("=Cho 1 phần String xuống dòng (Cách 1)=")
print ("Độ Mixi bán \nkhô gà và bả mía")

print ("")

# Cho 1 phần String xuống dòng (Cách 2)
print ("=Cho 1 phần String xuống dòng (Cách 2)=")
print ("""Độ Mixi bán
khô gà và bã mía""")

print ("")

# Thêm dấu ngoặc kép vào String mà không kết thúc String
print ("=Thêm dấu ngoặc ke vào String mà không kết thúc String=")
print ("Anh Độ Mixi bán \"Khô gà\" và \"Bã mía\"")

print ("")

# In biến có sẵn String
print ("=n biến có sẵn chuỗi=")
Do_Mixi = "Độ Mixi bán khô gà và bã mía"

print (Do_Mixi)

print ("")

# Ghép String vào 1 biến đã có String
print ("=Ghép String vào 1 biến đã có String=")
print (Do_Mixi + " ngon lắm")

print ("")

# Hàm phổ biến để thao tác với String
print ("=Hàm phổ biến để thao tác với String=")
print ("")

## Hàm upper()
print ("Hàm upper()")
print (Do_Mixi.upper())

print ("")

## Hàm lower()
print ("Hàm lower()")
print (Do_Mixi.lower())

print ("")

## Hàm isupper()
print ("Hàm isupper()")
print (Do_Mixi.isupper())

print ("")

## Hàm islower()
print ("Hàm islower()")
print (Do_Mixi.islower())

print ("")

## Chồng hàm
print ("Chồng hàm")
print (Do_Mixi.upper().isupper())

print ("")

## Hàm len()
print ("Hàm len()")
print (len(Do_Mixi))

print ("")

## Sử dụng dấu ngoặc vuông để chỉ định 1 chữ cái trông biến
print ("Sử dụng dấu ngoặc vuông để chỉ định 1 chữ cái trông biến")
print (Do_Mixi[3])
print (Do_Mixi[6])

print ("")

## Hàm index()
print ("Hàm index()")
print (Do_Mixi.index("M"))
print (Do_Mixi.index("i"))
print (Do_Mixi.index("x"))
print (Do_Mixi.index("i"))

print (Do_Mixi.index("bán khô gà và bã mía"))

print ("")

## Hàm replace()
print ("Hàm replace()")
print (Do_Mixi.replace("Độ", "Pin"))

print ("")

# Bài 4: Dữ liệu dạng số và các hàm số toán học
print ("=== Bài 4: Dữ liệu dạng số và các hàm số toán học ===")

print ("")

# Đơn giản hiển thị 1 số lên màn hình
print ("=Đơn giản hiển thị 1 số lên màn hình=")
print (36)

print ("")

# Thực hiện phép tính đơn giản
print ("=Thực hiện phép tính đơn giản=")
print (36+67) #Chẳng hạn
print (3.6 - 6.7)

print ("")

# Thực hiện phép tính phức tạp hơn
print ("=Thực hiện phép tính phức tạp hơn=")
print (2*3+5/6)
print (2.5*(3.14+5.4)/6.7)

print ("")

# Thực hiện phép tính phức tạp hơn nữa
print ("=Thực hiện phép tính phức tạp hơn nữa=")
print (5%2)
print ((5/2)/2)

# In biến Number
print ("=In biến Number=")

#! Tạo biến
Thanh_Hoa = 36
Am_Thanh_Hoa = -36
Thanh_Hoa_Thuc = 3.6
So_thuc = 6.1

#! In biến Number
print (Thanh_Hoa)

print ("")

# Hàm số học cơ bản
print ("Hàm số học cơ bản")
## Hàm str()
print ("Hàm str()")
print (str(Thanh_Hoa) + " là số của Thanh Hoá")

print ("")

## Hàm abs()
print ("Hàm abs()")
print ("Giá trị tuyệt đối của \"Am_Thanh_Hoa\" là: " + str(abs(Am_Thanh_Hoa)))

print ("")

## Hàm pow()
print ("Hàm pow()")
print ("Thanh_Hoa mũ 3 bằng: "+ str(pow(Thanh_Hoa, 3)))
print ("3 mũ Thanh_Hoa bằng: " + str(pow(3, Thanh_Hoa)))
print ("36 mũ 3 bằng: " + str(pow(36, 3)))

print ("")

## Hàm max()
print ("Hàm max()")
print ("Số lớn nhất giữa 2 và 3 là: " + str(max(2, 3)))
print ("Số lớn nhất giữa 2, 3 và 4 là: " + str(max(2, 3, 4)))
print ("Sô lớn nhất giữa \"Thanh_Hoa\" và 3 là: " + str(max(3, Thanh_Hoa)))

print ("")

## Hàm min()
print ("Hàm min()")
print ("Số bé nhất giữa 2 và 3 là: " + str(min(2, 3)))
print ("Số bé nhất giữa 2, 3 và 4 là: " + str(min(2, 3, 4)))
print ("Sô bé nhất giữa \"Thanh_Hoa\" và 3 là: " + str(min(3, Thanh_Hoa)))

print ("")

## Hàm round()
print ("Hàm round()")
print ("Làm tròn số 3.6 thành: " + str(round(3.6)))
print ("Làm tròn số 3.2 thành: " + str(round(3.2)))
print ("Làm tròn Thanh_Hoa_Thuc thành: " + str(round(Thanh_Hoa_Thuc)))
print ("Làm tròn So_Thuc thành: " + str(round(So_thuc)))

print ("")

# Hàm số học với thư viện "math"
print ("Hàm số học với thư viện \"math\"")
import math as ma

## Hàm floor()
print ("Hàm floor()")
print ("Làm tròn xuống số 3.6 thành: " + str(ma.floor(3.6)))
print ("Làm tròn xuống số 3.2 thành: " + str(ma.floor(3.2)))
print ("Làm tròn xuống Thanh_Hoa_Thuc thành: " + str(ma.floor(Thanh_Hoa_Thuc)))
print ("Làm tròn xuống So_Thuc thành: " + str(ma.floor(So_thuc)))

print ("")

## Hàm ceil()
print("Hàm ceil()")
print ("Làm tròn lên số 3.6 thành: " + str(ma.ceil(3.6)))
print( "Làm tròn lên số 3.2 thành: " + str(ma.ceil(3.2)))
print ("Làm tròn lên Thanh_Hoa_Thuc thành: " + str(ma.ceil(Thanh_Hoa_Thuc)))
print ("Làm tròn lên So_Thuc thành: " + str(ma.ceil(So_thuc)))

print ("")

## Hàm sqrt()
print ("Hàm sqrt()")
print ("Căn bậc 2 của 36 là: " + str(ma.sqrt(36)))
print ("Căn bậc 2 của Thanh_Hoa là: " + str(ma.sqrt(Thanh_Hoa)))

print ("")

# Bài 5: Nhận dữ liệu người dùng nhập vào
print ("=== Bài 5: Nhận dữ liệu người dùng nhập vào ===")

print ("")

# Sử dụng hàm input() để nhận dữ liệu người dùng nhập vào
print ("=Sử dụng hàm input() để nhận dữ liệu người dùng nhập vào=")
Ten_nguoi_dung = input("Tên bạn là gì? ")
Tuoi_nguoi_dung = float(input("Bạn năm nay bao nhiêu tuổi? "))
print ("Xin chào, " + Ten_nguoi_dung + "! Rất vui được gặp bạn!" + "Năm nay bạn " + str(Tuoi_nguoi_dung) +"tuổi á!")

print ("")

# Thu ngắn hàm print() bằng "f" string
print ("=Thu ngắn hàm print() bằng \"f\" string=")
print (f"Xin chào, {Ten_nguoi_dung}! Rất vui được gặp bạn! Năm nay bạn {Tuoi_nguoi_dung} tuổi á!")

print ("")

# Bài 7: Nối chuỗi với hàm format()
print ("=== Bài 7: Nối chuỗi với hàm format() ===")

# Cách 1:
print ("=Cách 1:=")
print ("Xin chào, " + Ten_nguoi_dung + "! Rất vui được gặp bạn!" + "Năm nay bạn " + str(float(Tuoi_nguoi_dung))  +"tuổi á!")

print ("")

# Cách 2:
print ("=Cách 2:=")
print (f"Xin chào, {Ten_nguoi_dung}! Rất vui được gặp bạn! Năm nay bạn {float(Tuoi_nguoi_dung)} tuổi á!")

print ("")

# Cách 3 (Bài học chính):
print ("=Cách 3 (Bài học chính):=")
print ("Xin chào, {}! Rất vui được gặp bạn! Năm nay bạn {} tuổi á!".format(Ten_nguoi_dung, Tuoi_nguoi_dung))

#! Hoặc
print ("Xin chào, Năm nay bạn {1} tuổi á! Rất vui được gặp {0}! ".format(Ten_nguoi_dung, Tuoi_nguoi_dung))

print ("")

# Bài 8: Dữ liệu dạng danh sách (List)
print ("=== Bài 8: Dữ liệu dạng danh sách (List) ===")









