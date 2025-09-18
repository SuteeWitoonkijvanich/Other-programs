def print_inverted_triangle():
    # รับค่าจำนวนแถวจากผู้ใช้
    try:
        rows = int(input("Enter number of rows: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # ลูปชั้นนอกสำหรับจำนวนแถว
    for i in range(rows, 0, -1):
        # ลูปสำหรับพิมพ์ช่องว่างเพื่อให้รูปอยู่กึ่งกลาง
        for j in range(rows - i):
            print(" ", end="")
        
        # ลูปสำหรับพิมพ์เครื่องหมายดอกจัน
        for k in range(2 * i - 1):
            print("*", end="")
        
        # ขึ้นบรรทัดใหม่เมื่อจบลูปชั้นใน
        print()

# เรียกใช้ฟังก์ชัน
print_inverted_triangle()