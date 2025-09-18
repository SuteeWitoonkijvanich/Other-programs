def Calculate(x):
    """
    คำนวณปริมาณน้ำที่เหลือในถังหลังจากผ่านไป x วัน

    Args:
        x (int): จำนวนวัน

    Returns:
        float: ปริมาณน้ำที่เหลือในถัง (ลิตร)
    """
    initial_amount = 5832
    remaining_fraction = 2 / 3
    remaining_water = initial_amount * (remaining_fraction ** x)
    return remaining_water

# ตัวอย่างการใช้งาน:
# หาปริมาณน้ำที่เหลือหลังจาก 1 วัน
print(f"ปริมาณน้ำที่เหลือหลังจาก 1 วัน: {Calculate(1):.2f} ลิตร")

# หาปริมาณน้ำที่เหลือหลังจาก 3 วัน
print(f"ปริมาณน้ำที่เหลือหลังจาก 3 วัน: {Calculate(3):.2f} ลิตร")
print(f"ปริมาณน้ำที่เหลือหลังจาก 4 วัน: {Calculate(4):.2f} ลิตร")