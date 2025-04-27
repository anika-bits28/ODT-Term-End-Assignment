# ==============================================
# ALMIRAH DOOR CONTROL SYSTEM
# ESP32 MicroPython Servo Controller
# ==============================================
#
# FUNCTION:
# Controls a servo motor attached to an almirah door
# to create sudden opening and delayed closing action
#
# HARDWARE SETUP:
# - Servo signal wire → GPIO18
# - Servo power → 5V (VIN PIN ESP32)
# - Servo ground → GND
# - Ensure servo has mechanical clearance for full movement
# ==============================================

from machine import Pin, PWM  # Import necessary libraries
import time                   # For time delays

# Initialize servo on GPIO18 with 50Hz frequency
# (Standard PWM frequency for hobby servos)
servo2 = PWM(Pin(18), freq=50)

# ==============================================
# DOOR CLOSED POSITION (READY STATE)
# ==============================================
# Duty cycle 77 corresponds to ~0 degree position
# (Door remains closed and locked)
servo2.duty(77)

# Maintain closed position for 10 seconds
# (Builds anticipation before sudden opening)
time.sleep(10)

# ==============================================
# DOOR OPENING SEQUENCE (SCARE TRIGGER)
# ==============================================
# Duty cycle 26 moves servo to ~135 degrees
# (Door swings open suddenly)
servo2.duty(26)

# Hold open position for 1 second
# (Allows full visibility/effect)
time.sleep(1)

# ==============================================
# NEXT STEPS (FOR CONTINUOUS OPERATION):
# 1. Add servo2.duty(77) here to re-close door
# 2. Adjust time delays for different pacing
# 3. Integrate with motion sensor trigger
# ==============================================

# TROUBLESHOOTING NOTES:
# 1. If door doesn't open fully: adjust duty values
# 2. If movement is jerky: check power supply
# 3. If servo overheats: reduce operation frequency
# 4. For heavier doors: use high-torque servo model
