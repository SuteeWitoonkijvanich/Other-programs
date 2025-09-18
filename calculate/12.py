def solve_dice_problem():
    """
    คำนวณความน่าจะเป็นของผลรวมและผลต่างของแต้มลูกเต๋า 2 ลูก
    """
    
    # จำนวนวิธีทั้งหมดที่เป็นไปได้จากการทอดลูกเต๋า 2 ลูก (6 x 6)
    total_outcomes = 6 * 6
    print(f"จำนวนวิธีทั้งหมดในการทอดลูกเต๋า 2 ลูก: {total_outcomes} วิธี")
    
    # 1. ความน่าจะเป็นที่ผลรวมของแต้มเป็น 10
    
    # เหตุการณ์ที่ผลรวมเป็น 10
    sum_10_outcomes = [(4, 6), (5, 5), (6, 4)]
    count_sum_10 = len(sum_10_outcomes)
    
    # คำนวณความน่าจะเป็น
    probability_sum_10 = count_sum_10 / total_outcomes
    
    print("\n---")
    print("1. ผลรวมของแต้มเป็น 10")
    print(f"จำนวนวิธีที่ผลรวมเป็น 10: {count_sum_10} วิธี")
    print(f"ความน่าจะเป็น: {count_sum_10}/{total_outcomes} = {probability_sum_10:.4f}")
    
    # 2. ความน่าจะเป็นที่ผลต่างของแต้มเป็น 2
    
    # เหตุการณ์ที่ผลต่างเป็น 2
    diff_2_outcomes = [(1, 3), (3, 1), (2, 4), (4, 2), (3, 5), (5, 3), (4, 6), (6, 4)]
    count_diff_2 = len(diff_2_outcomes)
    
    # คำนวณความน่าจะเป็น
    probability_diff_2 = count_diff_2 / total_outcomes
    
    print("\n---")
    print("2. ผลต่างของแต้มเป็น 2")
    print(f"จำนวนวิธีที่ผลต่างเป็น 2: {count_diff_2} วิธี")
    print(f"ความน่าจะเป็น: {count_diff_2}/{total_outcomes} = {probability_diff_2:.4f}")

# เรียกใช้ฟังก์ชันเพื่อคำนวณและแสดงผล
solve_dice_problem()