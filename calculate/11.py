def solve_base_conversion():
    """
    คำนวณเลขฐานสิบที่บวกกับเลข 1000 ใช้เลขฐาน 8 แล้วได้ผลลัพธ์เป็น 1000 ฐานสิบ
    """
    # เลขฐานแปดที่ต้องการแปลง
    base8_number = "1000"
    
    # แปลงเลขฐานแปดเป็นเลขฐานสิบ โดยใช้ฟังก์ชัน int()
    decimal_equivalent = int(base8_number, 8)
    
    # คำนวณหาเลขที่ต้องบวก
    target_sum = 1000
    missing_number = target_sum - decimal_equivalent

    # แสดงผลลัพธ์
    print(f"เลข 1000 ฐาน 8 มีค่าเท่ากับ {decimal_equivalent} ในระบบเลขฐานสิบ")
    print(f"ดังนั้น เลขที่ต้องบวกคือ {target_sum} - {decimal_equivalent} = {missing_number}")

# เรียกใช้ฟังก์ชันเพื่อคำนวณ
solve_base_conversion()