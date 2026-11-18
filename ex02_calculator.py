"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
print("2024 + 1000 =", 2024 + 1000)

# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
so_tien_con_lai = 150000 - 35000 * 3
print(f"Số tiền còn lại: {so_tien_con_lai} VNĐ")

# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
ban_kinh = 7
dien_tich = 3.14159 * ban_kinh**2
print(f"Diện tích hình tròn: {dien_tich:.2f}")

# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
so_keo_moi_nguoi = 100 // 7
so_keo_con_du = 100 % 7
print(f"Mỗi người được: {so_keo_moi_nguoi} viên")
print(f"Còn dư: {so_keo_con_du} viên")

# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
c = 37
f = c * 9 / 5 + 32
print(f"{c}°C = {f}°F")
