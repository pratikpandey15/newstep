# Voltage Gain Calculation using gm

   def gain():
       kn = 0.5       # Transconductance parameter
       VGS = 3.5      # Gate-Source voltage (V)
       Vth = 2.0      # Threshold voltage (V)
       RD = 4700      # Drain resistor (ohms)

       # Transconductance gm
       gm = kn * (VGS - Vth)

       # Voltage Gain
       Av = -gm * RD

       print(f"Transconductance gm = {gm:.4f} A/V")
       print(f"Voltage Gain Av     = {Av:.2f} V/V")
       print(f"Gain in dB          = {20 * (Av**2)**0.5:.2f} dB")
