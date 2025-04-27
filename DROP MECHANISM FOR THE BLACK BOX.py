# ================================================
# BLACK BOX - SERVO-CONTROLLED DROP MECHANISM
# ESP32 MicroPython Code for Latch Release System
# ================================================
#
# FUNCTIONAL OVERVIEW:
# Controls a servo motor that releases a latch,
# allowing a prop (e.g. dead doll) to fall suddenly.
#
# WIRING INSTRUCTIONS:
# - Servo signal wire → GPIO14
# - Servo power → 5V(VIN on ESP32)
# - Servo ground → GND
#
# SAFETY NOTE:
# Test without doll first to verify torque adequacy.
# ================================================

# Import required libraries
from machine import Pin, PWM  # GPIO and PWM control
import time                   # For timing delays

# Initialize servo on GPIO14 with 50Hz frequency
# (Standard for most hobby servos)
servoceiling = PWM(Pin(14), freq=50)

# ------------------------------------------
# PHASE 1: LATCH CLOSED (HOLDING POSITION)
# ------------------------------------------
# Duty cycle 77 = ~90 degree position
# (Adjust this value to match your latch's closed state)
servoceiling.duty(77)
time.sleep(0.5)  # Stabilization delay

# ------------------------------------------
# PHASE 2: LATCH OPENED (RELEASE TRIGGER)
# ------------------------------------------
# Duty cycle 26 = ~0 degree position
# (Adjust to ensure full latch disengagement)
servoceiling.duty(26)
time.sleep(0.5)  # Ensures complete movement
