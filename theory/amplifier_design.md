# MOSFET Amplifier Design

   ## Circuit Topology
   Common Source Amplifier is used in this project.
   It provides high voltage gain with 180° phase shift.

   ## DC Biasing — Voltage Divider
   VG = VDD × R2 / (R1 + R2)

   ## Q-Point (Operating Point)
   The Q-point must be in Saturation region for amplification.
   - ID = 0.5 × kn × (VGS - Vth)²
   - VDS = VDD - ID × RD

   ## Transconductance (gm)
   gm = kn × (VGS - Vth)

   ## Voltage Gain (Av)
   Av = -gm × RD

   ## Design Steps
   1. Choose VDD supply voltage
   2. Calculate VG using voltage divider
   3. Find Q-point (ID, VDS)
   4. Calculate gm
   5. Calculate Voltage Gain Av
   6. Plot ID vs VDS characteristics

   ## Important Formulas
   | Parameter | Formula |
   |-----------|---------|
   | VG | VDD × R2/(R1+R2) |
   | ID (Sat) | 0.5 × kn × (VGS-Vth)² |
   | gm | kn × (VGS-Vth) |
   | Av | -gm × RD |
