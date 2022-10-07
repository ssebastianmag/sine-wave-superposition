# Sine wave superposition

Modeling and visualization of the superposition principle for two traveling sine waves

* Python 3.10.4
* Matplotlib 3.6.0
* Seaborn 0.12.0
* NumPy 1.23.3

---
### Files / Modules - Execution alternatives
* [IPython Notebook / Jupyter Notebook](sine_wave_superposition.ipynb)
* [Module with command line arguments](sine_wave_superposition_run.py)
* [Main module - sine_wave_superposition.py](sine_wave_superposition.py)
---

### Superposition principle

>The superposition principle states that, for all linear systems, 
> the net response caused by two or more stimuli is the sum of the 
> responses that would have been caused by each stimulus individually.


The interaction of two or more waves traveling along the same medium will produce an interference pattern, containing 
a resultant wave composed of a vector sum with the displacement of each inidividual wave at any particular 
point in the medium where the interaction takes place.
<br><br>
<p align='left'>
  <img src='img/Sine wave superposition (w1A=10mm, w1f=180Hz) + (w2A=20mm, w2f=-240Hz).gif'/>
</p>
<br>
The modules in this repository present a very simple and minimal approach of modeling and plotting the 
superposition of two sine waves traveling in the same medium, with the displacement being measured in millimeters 
at the Y axis and time expressed as centiseconds along the X axis.
<br><br>
After describing the sine waves to superpose, the output will produce and save (in .gif format) a 
200-frame animation which can be used to describe the interference scenarios below:

- Constructive interference
- Destructive interference
- Wave beats
- Standing waves

The sine wave modeling is also simple and minimal on its requirements and supports the following attributes:
- Amplitude
- Frequency
- Direction
- Phase polarity
---

### Execution
#### Command line arguments:

```
$ python sine_wave_superposition_run.py --help
```

```
usage: sine_wave_superposition_run.py [-h] [-ipw1] [-ipw2] wa1 wf1 wa2 wf2

Model two traveling sine waves by definition of the General form y(t) = Asin(ωt)
and plot their superposition and resultant wave

About wave modeling:
 - Positive frequencies will be displayed as leftward traveling
 - Negative frequencies will be displayed as rightward traveling
 - Inverting the polarity will shift the wave phase by 180°

positional arguments:
  wa1         Wave 1 - Amplitude in mm
  wf1         Wave 1 - Frequency in Hz
  wa2         Wave 2 - Amplitude in mm
  wf2         Wave 2 - Frequency in Hz

options:
  -h, --help  show this help message and exit
  -ipw1       Wave 1 - Inverts wave polarity
  -ipw2       Wave 2 - Inverts wave polarity

```
---

Notice: _All of the samples below have a reduced frame length for compression purposes_

---

#### Input args:
    $ python sine_wave_superposition_run.py 10 180 20 -240 -ipw1

#### Output:

<p align='left'>
  <img src='img/Sine wave superposition (w1A=10mm, w1f=180Hz) + (w2A=20mm, w2f=-240Hz).gif'/>
</p>

---

#### Input args:
    $ python sine_wave_superposition_run.py 10 140 10 -140

#### Output:

<p align='left'>
  <img src='img/Sine wave superposition (w1A=10mm, w1f=140Hz) + (w2A=10mm, w2f=-140Hz).gif'/>
</p>

---

#### Input args:
    $ python sine_wave_superposition_run.py 10 180 10 180 -ipw1

#### Output:

<p align='left'>
  <img src='img/Sine wave superposition (w1A=10mm, w1f=180Hz) + (w2A=10mm, w2f=180Hz).gif'/>
</p>

---

#### Input args:
    $ python sine_wave_superposition_run.py 10 300 10 210

#### Output:

<p align='left'>
  <img src='img/Sine wave superposition (w1A=10mm, w1f=300Hz) + (w2A=10mm, w2f=210Hz).gif'/>
</p>

---

#### Input args:
    $ python sine_wave_superposition_run.py 20 90 10 -240

#### Output:

<p align='left'>
  <img src='img/Sine wave superposition (w1A=20mm, w1f=90Hz) + (w2A=10mm, w2f=-240Hz).gif'/>
</p>

---