import math

def calculate_trigonometric_values(degrees):
    radians = math.radians(degrees)
    sin_value = math.sin(radians)
    cos_value = math.cos(radians)
    tan_value = math.tan(radians)
    
    return sin_value, cos_value, tan_value

angle_degrees = float(input("Enter the angle in degrees: "))

sin_val, cos_val, tan_val = calculate_trigonometric_values(angle_degrees)

print(f"sin({angle_degrees}°) = {sin_val}")
print(f"cos({angle_degrees}°) = {cos_val}")
print(f"tan({angle_degrees}°) = {tan_val}")
