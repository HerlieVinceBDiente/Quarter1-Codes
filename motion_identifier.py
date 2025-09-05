# Motion Type Identifier Template

# Function 1: Convert velocity to m/s

def convert_velocity(value, unit):

    if unit == "m/s":
        return value
    elif unit == "ft/s":
        return value * 0.3048
    elif unit == "km/s":
        return value * 1000
    elif unit == "mi/s":
        return value * 1609.34
    else:
        print("Unsupported unit for velocity")
        return None
    

# Function 2: Convert acceleration to m/s²

def convert_acceleration(value, unit):

    if unit == "m/s²":
        return value
    elif unit == "ft/s²":
        return value * 0.3048
    elif unit == "km/s²":
        return value * 1000
    elif unit == "mi/s²":
        return value * 1609.34
    else:
        print("Unsupported unit for acceleration")
        return None
 

# Function 3: Determine motion type

def motion_type(v, a):

    if v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    elif v == 0:
        return "At Rest"
    else:
        return "Undefined Motion"
 

# --- Main Program ---

# Step 1: Input velocity

v_value = float(input("Enter velocity value: "))

v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

 

# Step 2: Input acceleration

a_value = float(input("Enter acceleration value: "))

a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

 

# Step 3: Convert to SI units

v_si = convert_velocity(v_value, v_unit)      

a_si = convert_acceleration(a_value, a_unit)  

 
# Step 4: Determine motion type

motion = motion_type(v_si, a_si)   
           
 
# Step 5: Display results

print(f"Velocity in m/s: {v_si}")
print(f"Acceleration in m/s²: {a_si}")
print(f"Motion type is: {motion}")
