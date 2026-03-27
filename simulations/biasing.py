# DC Operating Point — Q-point Calculation

   def biasing():
       VDD = 12.0     # Supply voltage (V)
       R1 = 100000    # Resistor 1 (ohms)
       R2 = 50000     # Resistor 2 (ohms)
       RD = 4700      # Drain resistor (ohms)
       RS = 1000      # Source resistor (ohms)
       Vth = 2.0      # Threshold voltage (V)
       kn = 0.5       # Transconductance parameter

       # Voltage divider biasing
       VG = VDD * (R2 / (R1 + R2))
       VS = 0
       VGS = VG - VS

       # Q-point Drain Current
       if VGS > Vth:
           Id = 0.5 * kn * (VGS - Vth)**2
       else:
           Id = 0

       VD = VDD - Id * RD

       print(f"VG  = {VG:.2f} V")
       print(f"VGS = {VGS:.2f} V")
       print(f"Id  = {Id:.4f} A")
       print(f"VD  = {VD:.2f} V")
       print(f"Q-Point: (VDS={VD:.2f}V, ID={Id:.4f}A)")
