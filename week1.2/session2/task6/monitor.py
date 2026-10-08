# Week 1.2, Session 2: Task 6
'''
Your objective is to simulate a factory machine monitoring system using
sensor data. You will implement a program that uses user inputs to monitor
the status of a machine. Based on the inputs, your program should evaluate
the conditions and print instructions to the user.

## Instructions

### Step 1: Get User Inputs

You need to collect three inputs from the user:

1. The machine's temperature in degrees Celsius (integer)
2. The machine's pressure in PSI (integer)
3. The machine's operational status (1 for operating, 0 for stopped) (integer)

### Step 2: Evaluate Operating Conditions

Use conditional statements involving `if`, `elif` and `else` to evaluate
the operating temperature and pressure of the machine.

#### Temperature

- If the temperature is above 80°C, alert that the temperature is too high
  and recommend shutting down the machine.

- If the temperature is between 50°C and 80°C, indicate that the temperature
  is within safe limits.

- If the temperature is below 50°C, indicate that the machine temperature
  is low and no action is needed.

#### Pressure

- If the pressure exceeds 100 PSI, alert that high pressure is detected
  and recommend maintenance.

- If the pressure is between 70 PSI and 100 PSI, indicate that the
  pressure is stable.

- If the pressure is below 70 PSI, indicate that the pressure is low and the
  system is operating normally.

### Step 3: Determine Status

If the machine is currently operating, then if either temperature is too
high or pressure is too high, alert that the machine is running in unsafe
conditions and recommend shutting it down.

If everything is normal, indicate that the machine is running normally.

If the machine is not currently operating, indicate that it is stopped and
no immediate action is needed.
'''

temp = int(input("Enter the machine's temperature in degrees C: "))
pressure = int(input("Enter the machine's pressure in PSI: "))
status = int(input("Enter the machine's operational status (1 for operating, 0 for stopped): "))


#Temperature check
if temp > 80:
    print("Alert: Temperature is too high! Shutdown recommended.")
elif temp >= 50:
    print("Temperature is within safe parameters.")
else:
    print("No action needed : Machine temperature is low.")

#Pressure check
if pressure > 100:
    print("Alert: Pressure is high! Maintenance recommended.")
elif pressure >= 70:
    print("Pressure is within safe parameters and stable.")
else:
    print("No action needed : Machine pressure is low and system is operating normally.")

#Status check
if status == 1:
    if (temp > 80 or pressure > 100):
        print("Alert: Machine running in unsafe conditions. Shutdown recommended.")
    else:
        print("Machine is running normally.")
else:
    print("No immediate action needed : Machine is stopped.")