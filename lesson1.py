# digits = [5, 4.3, 5]
# digits[1] = 43
# digits.append(5867)

# print(digits[3])

n = int(input("Enter length: "))

user_list = []

i = 0
while i < n:
		string = "ennter element #" + str(i + 1) + ": "
		user_list.append(input(string))    
		i += 1
    

print(user_list)