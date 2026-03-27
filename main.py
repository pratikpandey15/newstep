# Main entry point for MOSFET Amplifier Simulation

   from simulations.mosfet_model import mosfet_model
   from simulations.biasing import biasing
   from simulations.gain import gain
   from simulations.iv_curve import iv_curve

   if __name__ == "__main__":
       print("MOSFET Amplifier Simulation Started...")
       mosfet_model()
       biasing()
       gain()
       iv_curve()
       print("Simulation Complete!")
