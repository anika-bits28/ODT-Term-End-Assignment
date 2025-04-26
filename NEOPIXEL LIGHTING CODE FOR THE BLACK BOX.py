# =============================================
# BLACK BOX - TERROR LIGHTING SYSTEM
# ESP32 MicroPython Code for NeoPixel LED Strip
# =============================================
#
# HOW TO USE THIS CODE:
# 1. Connect NeoPixel strip to GPIO Pin 4 on ESP32
# 2. Upload this script
# 3. Watch the horror unfold...
#
# LIGHTING SEQUENCE:
# 1. Flickering yellow "candle" effect (single LED)
# 2. Amber "breathing" glow (all LEDs)
# 3. Rapid blue "strobe" flashes
# 4. Final eerie blue ambience
# =============================================

# ----------------------------
# SECTION 1: SETUP
# ----------------------------
from machine import Pin  # To control GPIO pins
import neopixel          # To control NeoPixel LEDs
import time              # For timing/delays

# Configure NeoPixel LED strip
NUM_LEDS = 7             # How many LEDs in your strip?
LED_PIN = Pin(4)         # Which GPIO pin? (Change if needed)

# Initialize the strip
np = neopixel.NeoPixel(LED_PIN, NUM_LEDS)

# ----------------------------
# SECTION 2: FLICKERING YELLOW
# (Like a dying candle)
# ----------------------------
# Pattern of brightness levels for flicker effect
flicker_pattern = [
    5, 10, 15, 25, 35, 45, 60,  # Gradual increase
    200,                          # Sudden bright flash
    70, 80, 100, 120,            # Uneven decay
    255,                         # Max brightness
    130, 110, 90,                # Drop
    220,                         # Secondary flash
    60, 30, 10                   # Fade to darkness
]

# Apply pattern to FIRST LED only (index 0)
for brightness in flicker_pattern:
    # Set LED to yellow (red + green, no blue)
    np[0] = (brightness, brightness, 0)
    np.write()                  # Send data to LEDs
    time.sleep(0.07)            # Short delay between steps

# ----------------------------
# SECTION 3: AMBER BREATHING
# (Like something lurking closer)
# ----------------------------
breathing_value = 0             # Start at darkness

while breathing_value <= 255:   # Ramp up to max brightness
    for led in range(NUM_LEDS): # Affect ALL LEDs
        # Amber = Red + partial Green (no blue)
        np[led] = (breathing_value, int(breathing_value * 0.5), 0)

    np.write()
    breathing_value += 5        # Increase brightness
    time.sleep(0.05)            # Controls "breathing" speed

# ----------------------------
# SECTION 4: BLUE STROBE FLASHES
# (Like lightning or electric sparks)
# ----------------------------
NUM_FLASHES = 8                 # How many flashes?
FLASH_DELAY = 0.1               # Time between on/off

for _ in range(NUM_FLASHES):
    # Turn ALL LEDs blue (R=0, G=0, B=100)
    for led in range(NUM_LEDS):
        np[led] = (0, 0, 100)
    np.write()
    time.sleep(FLASH_DELAY)     # Keep on briefly

    # Turn ALL LEDs off
    for led in range(NUM_LEDS):
        np[led] = (0, 0, 0)
    np.write()
    time.sleep(FLASH_DELAY)     # Keep off briefly

# ----------------------------
# SECTION 5: FINAL BLUE AMBIENCE
# (Eerie permanent glow)
# ----------------------------
for led in range(NUM_LEDS):
    np[led] = (0, 0, 100)      # Set all to dim blue
np.write()

# =============================================
# END OF SEQUENCE - LEDs WILL STAY BLUE

