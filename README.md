# **THE BLACK BOX: ENGINEERED HORROR INSTALLATION**  
*An ESP32-Based Multisensory Fear Experience*  

## **Project Overview**  
The Black Box is an immersive horror system combining three distinct terror mechanisms:  
1. **Atmospheric Lighting System** (Psychological dread)  
2. **Sudden Drop Mechanism** (Physical startle)  
3. **Almirah Door Trigger** (Environmental surprise)  

---

## **1. LIGHTING SYSTEM ("The Flicker")**  
### Technical Implementation  
- **Controller**: ESP32  
- **Components**: NeoPixel LED Strip (7+ LEDs)  
- **GPIO**: Pin 4  

### Fear Profile  
| Phase | Effect | Psychological Target |  
|-------|--------|-----------------------|  
| 1 | Erratic yellow flicker | Pattern recognition failure |  
| 2 | Pulsing amber glow | Uncanny valley effect |  
| 3 | Violent blue strobes | Startle reflex activation |  
| 4 | Frozen blue ambience | Sensory deprivation |  


## **2. DROP MECHANISM ("The Fall")**  
### Technical Implementation  
- **Controller**: ESP32  
- **Components**: SG90 Servo, Custom Latch  
- **GPIO**: Pin 14  

### Movement Sequence  
| Step | Action | Duration | Purpose |  
|------|--------|----------|---------|  
| 1 | Latch engaged (duty 77) | 500ms | Secure payload |  
| 2 | Latch released (duty 26) | 500ms | Trigger drop |  

## **3. ALMIRAH DOOR SYSTEM ("The Reveal")**  
### Technical Implementation  
- **Controller**: ESP32  
- **Components**: MG996R Servo, Door Linkage  
- **GPIO**: Pin 18  

### Action Timeline  
1. **10-second hold**: Door closed (duty 77)  
2. **Sudden opening**: 135° movement (duty 26)  
3. **1-second display**: Fully open position  

## **INTEGRATION GUIDE**  
### Wiring Summary  
| System | Power | Signal | Ground |  
|--------|-------|--------|--------|  
| Lighting | 5V | GPIO4 | GND |  
| Drop Mech | External 5V | GPIO14 | GND |  
| Almirah | External 5V | GPIO18 | GND |  

## **SAFETY PROTOCOLS**  
1. Always test mechanisms without payloads first  
2. Secure all moving parts with mechanical stops  
3. Maximum continuous operation: 90 seconds  
4. Emergency stop circuit recommended



FINAL WARNING
If components start working when unplugged:

Say "nope" very firmly

Slowly back away

Consider holy water

Now go make some memories! (The kind that require therapy.)

[END DOCUMENT]

P.S. Not responsible for paranormal residue or new phobias.


