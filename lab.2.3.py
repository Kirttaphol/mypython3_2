print("วิธีคำนวณ BMI ในการหาค่าคัชนีนวลกาย")
kg = int(input("น้ำหนัก: "))
cm = int(input("สวนสูง: "))
bmi = kg/(cm/100)**2
if bmi<18.50:
    print("น้ำหนักน้อย")
elif bmi>=18.50 and bmi <= 22.90:
    print("ปกติ")
elif bmi>=23 and bmi <= 24.90:
    print("ท้วม")
elif bmi>=25 and bmi <= 29.90:
    print("อ้วน")
elif bmi>=30:
    print("อ้วนมาก")