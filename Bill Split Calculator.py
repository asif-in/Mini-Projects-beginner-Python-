print("Bill Split Calculator")
bill_amount = float(input())
tip_perc = float(input())
num_people = int(input())

total = bill_amount + (tip_perc / 100) * bill_amount
total_per_person = total / num_people

print(f"Total (including tip): ${total}")
print(f"Each person pays: ${total_per_person}")
