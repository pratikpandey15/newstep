# Default Constants for MOSFET Amplifier Simulation

   # MOSFET Parameters
   Vth = 2.0        # Threshold Voltage (V)
   kn = 0.5         # Process Transconductance (A/V²)
   W_L = 10         # Width to Length Ratio

   # Circuit Parameters
   VDD = 12.0       # Supply Voltage (V)
   R1 = 100000      # Biasing Resistor 1 (ohms)
   R2 = 50000       # Biasing Resistor 2 (ohms)
   RD = 4700        # Drain Resistor (ohms)
   RS = 1000        # Source Resistor (ohms)

   # Simulation Parameters
   VGS_default = 3.5   # Default Gate-Source Voltage (V)
   VDS_default = 5.0   # Default Drain-Source Voltage (V)
   VDS_max = 10.0      # Max VDS for plotting (V)
