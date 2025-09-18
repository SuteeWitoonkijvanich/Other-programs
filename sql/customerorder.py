import pandas as pd

# สร้าง DataFrame สำหรับตาราง Customer
customer_data = {
    'ID': ['C001', 'C002', 'C003', 'C004', 'C005','C006'],
    'Name': ['Will Peter', 'John Smith', 'Jame Born', 'Charlie Angel', 'Mickey Brown','test'],
    'Email': ['will.p@hotmail.com', 'john.smith@hotmail.com', 'jame.born@hotmail.com', 'charlie.angel@hotmail.com', 'mickey.b@hotmail.com','test@gmail.com'],
    'CountryCode': ['TH', 'EN', 'US', 'US', 'JP','US'],
    'Budget': [1000000, 2000000, 3000000, 4000000, 5000000, 400000],
    'Used': [600000, 800000, 2000000, 1000000, 1000000, 100000]
}
df_customer = pd.DataFrame(customer_data)

# สร้าง DataFrame สำหรับตาราง Order
order_data = {
    'ID': ['O001', 'O002', 'O003', 'O004'],
    'Date': ['2019-10-08', '2019-10-08', '2019-11-20', '2019-05-20'],
    'CustomerID': ['C002', 'C002', 'C003', 'C004'],
    'Amount': [50000, 45000, 50000, 40000]
}
df_order = pd.DataFrame(order_data)

# ข้อ 4: แสดงข้อมูล Used ที่มีค่ามากกว่า 500,000

filtered_customers = df_customer[df_customer['Used'] > 700000]
filtered_customers = df_customer[df_customer['Used'] < 1000000]
print("คำตอบข้อ 4:")
print(filtered_customers)

# ข้อ 5: เชื่อมข้อมูล 2 ตาราง โดยแสดงทุก Record ที่อยู่ในตาราง Customer
merged_data = pd.merge(df_customer, df_order, left_on='ID', right_on='CustomerID', how='left')

# ลบคอลัมน์ที่ไม่จำเป็น (CustomerID ที่ซ้ำซ้อน)
merged_data = merged_data.drop(columns=['CustomerID'])

# คำสั่ง print() นี้จะแสดงผลลัพธ์การเชื่อมตาราง
print("\nคำตอบข้อ 5:")
print(merged_data)