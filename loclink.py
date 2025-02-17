import re
import tkinter as tk
from tkinter import filedialog

# Hàm để hiển thị hộp thoại chọn tệp và lưu kết quả
def select_file_and_save_results():
    try:
        # Tạo cửa sổ Tkinter ẩn
        root = tk.Tk()
        root.withdraw()

        # Hiển thị hộp thoại chọn tệp đầu vào
        input_file_path = filedialog.askopenfilename(
            title="Chọn tệp .txt",
            filetypes=(("All files", "*.*"), ("Text files", "*.txt") )
        )

        # Nếu người dùng chọn tệp đầu vào
        if input_file_path:
            print(f"Đã chọn tệp đầu vào: {input_file_path}")
            # Đọc nội dung tệp đầu vào
            with open(input_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Tìm các URL TikTok
            pattern = r'https://www\.tiktok\.com/@[\w\.]+/video/\d+'
            matches = re.findall(pattern, content)

            # Nếu tìm thấy kết quả, hiển thị hộp thoại chọn nơi lưu
            if matches:
                print(f"Tìm thấy {len(matches)} URL TikTok.")
                output_file_path = filedialog.asksaveasfilename(
                    title="Chọn nơi lưu kết quả",
                    defaultextension=".txt",
                    filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
                )

                # Nếu người dùng chọn nơi lưu
                if output_file_path:
                    # Ghi kết quả vào tệp
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write("\n".join(matches))
                    print(f"Kết quả đã được lưu vào: {output_file_path}")
                else:
                    print("Người dùng đã hủy chọn nơi lưu.")
            else:
                print("Không tìm thấy URL TikTok nào trong tệp.")
        else:
            print("Người dùng đã hủy chọn tệp đầu vào.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Gọi hàm để hiển thị pop-up
select_file_and_save_results()
