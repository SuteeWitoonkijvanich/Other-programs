from math import comb

def solve_fruit_probability():
    """
    คำนวณความน่าจะเป็นที่จะหยิบผลไม้ชนิดละ 1 ลูก
    """
    total_fruits = 10
    mango = 1
    
    # คำนวณจำนวนมังคุดและส้ม
    mangosteen = (total_fruits - mango) // 3
    orange = 2 * mangosteen

    # ตรวจสอบความถูกต้องของจำนวนผลไม้
    if (orange + mangosteen + mango) != total_fruits:
        print("Invalid fruit count based on the problem statement.")
        return

    # คำนวณจำนวนวิธีทั้งหมดในการหยิบ 3 ลูกจาก 10 ลูก
    total_combinations = comb(total_fruits, 3)

    # คำนวณจำนวนวิธีที่จะหยิบได้ผลไม้ชนิดละ 1 ลูก
    favorable_combinations = comb(orange, 1) * comb(mangosteen, 1) * comb(mango, 1)

    # คำนวณความน่าจะเป็น
    probability = favorable_combinations / total_combinations

    # แสดงผลลัพธ์
    print(f"จำนวนส้ม: {orange} ลูก")
    print(f"จำนวนมังคุด: {mangosteen} ลูก")
    print(f"จำนวนมะม่วง: {mango} ลูก")
    print(f"วิธีทั้งหมดในการหยิบ 3 ลูก: {total_combinations} วิธี")
    print(f"วิธีที่จะหยิบได้ชนิดละ 1 ลูก: {favorable_combinations} วิธี")
    print(f"ความน่าจะเป็น: {probability:.2f} ({favorable_combinations}/{total_combinations})")

# เรียกใช้ฟังก์ชัน
solve_fruit_probability()