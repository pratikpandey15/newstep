<h1 align="center">⚡ Common Source MOSFET Amplifier Simulator</h1>

<p align="center">
A Python-based simulation of a <b>Common Source MOSFET Amplifier</b>  
with DC biasing, Q-point analysis, voltage gain computation, and I-V characteristics visualization.
</p>

<hr>

<h2>📁 Project Structure</h2>

<pre>
NextStep/
├── main.py                        # Entry point
├── requirements.txt               # Dependencies
├── simulations/
│   ├── mosfet_model.py            # Core MOSFET physics (regions + Id)
│   ├── biasing.py                 # DC Q-point calculation
│   ├── gain.py                    # gm + voltage gain
│   └── iv_curve.py                # ID vs VDS plotting
├── utils/
│   └── constants.py               # Default parameters
├── theory/
│   ├── mosfet_basics.md           # MOSFET fundamentals
│   └── amplifier_design.md        # Design equations
├── graphs/                        # Auto-generated graphs
└── report/                        # Final report
</pre>

<hr>

<h2>⚙️ How to Run</h2>

<h3>Step 1 — Install Dependencies</h3>

<pre>pip install -r requirements.txt</pre>

<h3>Step 2 — Run Simulation</h3>

<pre>python main.py</pre>

<hr>

<h2> Simulation Flow</h2>

<ol>
<li>Take user input (VGS, VDS, RD, Vth)</li>
<li>Determine MOSFET region:
    <ul>
        <li>Cutoff</li>
        <li>Triode</li>
        <li>Saturation</li>
    </ul>
</li>
<li>Compute Drain Current (ID)</li>
<li>Calculate Transconductance (gm)</li>
<li>Compute Voltage Gain (Av)</li>
<li>Generate I-V Characteristics Graph</li>
</ol>

<hr>

<h2> What This Simulates</h2>

<table border="1" cellpadding="8">
<tr>
<th>Module</th>
<th>Function</th>
</tr>
<tr>
<td><code>mosfet_model.py</code></td>
<td>Region detection + drain current calculation</td>
</tr>
<tr>
<td><code>biasing.py</code></td>
<td>Q-point (operating point) computation</td>
</tr>
<tr>
<td><code>gain.py</code></td>
<td>Transconductance (gm) and voltage gain</td>
</tr>
<tr>
<td><code>iv_curve.py</code></td>
<td>ID vs VDS graph generation</td>
</tr>
</table>

<hr>

<h2> Key Equations</h2>

<ul>
<li><b>Gate Voltage:</b> VG = VDD × R2 / (R1 + R2)</li>
<li><b>Drain Current (Saturation):</b> ID = 0.5 × kn × (VGS − Vth)²</li>
<li><b>Transconductance:</b> gm = 2ID / (VGS − Vth)</li>
<li><b>Voltage Gain:</b> Av = −gm × RD</li>
</ul>

<hr>

<h2> Assumptions</h2>

<ul>
<li>Long-channel MOSFET model</li>
<li>No channel-length modulation</li>
<li>Constant temperature</li>
<li>Ideal components</li>
</ul>

<hr>

<h2>Sample Output</h2>

<p><b>I-V Characteristics:</b></p>

<img src="graphs/iv_curve.png" width="500">

<p><b>Output:</b></p>

<ul>
<li>Drain Current (ID)</li>
<li>Transconductance (gm)</li>
<li>Voltage Gain (Av)</li>
</ul>

<hr>

<h2> Validation (Example)</h2>

<table border="1" cellpadding="8">
<tr>
<th>Parameter</th>
<th>Theoretical</th>
<th>Simulated</th>
</tr>
<tr>
<td>Gain</td>
<td>-10</td>
<td>-9.8</td>
</tr>
<tr>
<td>ID</td>
<td>2mA</td>
<td>2.05mA</td>
</tr>
</table>

<hr>

<h2>🛠️ Tech Stack</h2>

<ul>
<li>Python 3.x</li>
<li>NumPy</li>
<li>Matplotlib</li>
<li>SciPy</li>
</ul>

<hr>

<h2> Future Improvements</h2>

<ul>
<li>Frequency response (Bode plot)</li>
<li>GUI-based simulator</li>
<li>Real MOSFET datasheet comparison</li>
</ul>

<hr>

<h2> Author</h2>

<p><b>Your Name</b><br>
PRATIK PANDEY </p>

<hr>

<h2> Status</h2>

<p> Project in progress — expanding features and improving accuracy.</p>
