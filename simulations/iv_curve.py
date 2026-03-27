# ID vs VDS Characteristic Curves

   import numpy as np
   import matplotlib.pyplot as plt

   def iv_curve():
       kn = 0.5       # Transconductance parameter
       Vth = 2.0      # Threshold voltage (V)
       VGS_values = [2.5, 3.0, 3.5, 4.0, 4.5]  # Different VGS values

       VDS = np.linspace(0, 10, 200)

       plt.figure(figsize=(8, 5))

       for VGS in VGS_values:
           Id = []
           for vds in VDS:
               if VGS < Vth:
                   Id.append(0)
               elif vds < (VGS - Vth):
                   Id.append(kn * ((VGS - Vth) * vds - 0.5 * vds**2))
               else:
                   Id.append(0.5 * kn * (VGS - Vth)**2)

           plt.plot(VDS, Id, label=f"VGS = {VGS}V")

       plt.title("MOSFET ID vs VDS Characteristics")
       plt.xlabel("VDS (V)")
       plt.ylabel("ID (A)")
       plt.legend()
       plt.grid(True)
       plt.savefig("graphs/iv_curve.png")
       plt.show()
       print("IV Curve saved to graphs/iv_curve.png")
