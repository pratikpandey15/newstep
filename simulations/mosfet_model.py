# MOSFET Core Physics — Id equations, operating regions

   def mosfet_model():
       Vth = 2.0      # Threshold voltage (V)
       kn = 0.5       # Process transconductance (A/V²)
       VGS = 3.5      # Gate-Source voltage (V)
       VDS = 5.0      # Drain-Source voltage (V)

       if VGS < Vth:
           region = "Cutoff"
           Id = 0

       elif VDS < (VGS - Vth):
           region = "Linear"
           Id = kn * ((VGS - Vth) * VDS - 0.5 * VDS**2)

       else:
           region = "Saturation"
           Id = 0.5 * kn * (VGS - Vth)**2

       print(f"Region: {region}")
       print(f"Drain Current Id = {Id:.4f} A")
