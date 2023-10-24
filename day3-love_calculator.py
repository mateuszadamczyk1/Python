name1 = input("Insert first name: ")
name2 = input("Insert second name: ")

combined = name1 + name2

lower = combined.lower()

t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")

first_digit = t + r + u + e

l = combined.count("l")
o = combined.count("o")
v = combined.count("v")
e = combined.count("e")

second_digit = l + o + v + e

score = str(first_digit) + str(second_digit)
final_score = int(score)


if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}.You go together like coke and mentos")
elif final_score > 40 and final_score <50:
    print(f"Your score is {final_score}. You are alright together")
else:
    print(f"Your score is {final_score}")        