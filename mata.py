"""Set of diffrent math expressions and exe"""
import math
num_a = 6
num_b = 2

#1. Sum and difference
print(f"{num_a} + {num_b} = {sum}")
print ("---------------------")

difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")
print("----------------")

#2. Float division

division = num_a / num_b
print(f"{num_a} / {num_b} = {division}")
print("----------------------------")

#3. Integer division

division = num_a // num_b
print(f"{num_a} // {num_b} = {division}")

#4. Powerful operations
multiply_numbers = num_a * num_b
print(f"{num_a} * {num_b} = {multiply_numbers}")

#5. Find average
average = (num_a + num_b) / 2
print(f"({num_a} + {num_b}) / 2 = {average}")

#6. Area of a circle
radius = 10
print("Pi" , math.pi)
print (10 ** 2 * math.pi)
print("------------------------")

#7. Area of an equilateral triangle

side_length = 5

triangle_area = (math.sqrt(3) / 4) * side_length ** 2
print(triangle_area)
triangle_area = round(triangle_area)
print(triangle_area)
print(f"triangle area is {triangle_area} if side length is {side_length}")
print("------------------------")


#8. Calculate discriminant
a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)
print(f"The solution are {sol1} and {sol2}" )

#9. Calculate hypotenuse length
a = 5
b = 4

c = math.sqrt(a ** 2 + b ** 2)
print(c)
#Length_of_height = float (input("Enter the length of the Base in cms: "))
#Length_of_height = float (input(" Enter the length of the Height in cms: ")
#length_of_the_hypotenuse = ((length_of_base)**2 + (length_of_height)**2)**0.5
#print (f"The length of the hypotenuse is {length_of_the_hypotenuse} cms. ")
print("------------------------")

#10. Calculate cathetus length
a = 5
c = 7

b = math.sqrt(c ** 2 - a ** 2)
print (b)

print("------------------------")

#11. Time converter
seconds = 9325
hours = seconds / 3600
minutes = seconds / 60
print(hours)
print(minutes)
print(f"{seconds} seconds is {hours} in hours and {minutes} in minutes")
print("------------------------")

#12. Student helper

angle = 35
sine = math.sin(angle)
cosine = math.cos(angle)

sine = round(sine, 1)
cosine = round(cosine, 1)
print(sine)
print(cosine)
print(f"Angle {angle} sin is {sine}")
print(f"Angle {angle} sin is {cosine}")
print("------------------------")

#13. Greetings

n = 4
lots_of_heys = "Hey" * n
print(lots_of_heys)

print("------------------------")






#14. Adding numbers
num_a = "6"
num_b = "2"

string_numbers = (num_a +num_b)
print(string_numbers)

print("------------------------")












