# One-Dimensional Superposition of Sine Waves
    Linear Superposition of Waveforms and Resultant Interference Patterns.

Modeling and visualization of the superposition 
principle in one dimension.

* Python 3.11.4
* Matplotlib 3.7.2 
* Seaborn 0.12.2 
* NumPy 1.25.2

---
### Main Project Files
* [Standalone Module](sine_wave_superposition.py)
* [IPython Notebook / Jupyter Notebook](sine_wave_superposition_notebook.ipynb)
---

## Content
#### Theoretical Background
* [Wave Equation](#wave-equation)
* [Superposition Principle](#superposition-principle)

#### Parameters
* [Wave Model Parameters](#wave-model-parameters)
* [Superposition Plot Parameters](#superposition-plot-parameters)

#### Implementation
* [Modeling of sine wave superposition phenomena and interference patterns](#modeling-of-sine-wave-superposition-phenomena-and-interference-patterns)

---

### Wave Equation

The sine wave equation in one-dimension can be represented as:

$$y(x, t) = A \sin(kx \pm \omega t + \phi)$$

where:

$y(x,t)$ is the wave displacement at position $x$ and time $t$;
$A$ is the amplitude;
$k = \frac{2\pi}{\lambda}$ is the wave number;
$\omega = 2\pi f$ is the angular frequency;
$\phi$ is the phase offset;
$+$ or $−$ depends on the direction of propagation (right or left).


### Superposition Principle

The superposition principle states that when two or more waves overlap in space, 
the resultant wave is the algebraic sum of their individual waves. 

When two waves $W_1$ and $W_2$ interfere, the resultant wave $W_R$ can be given by:

$$W_R(x, t) = W_1(x, t) + W_2(x, t)$$

#### Interference patterns

Interference patterns are the result of the superposition of two or more waves.
These patterns can be either constructive or destructive depending on the phase 
and amplitude of the interacting waves.  These patterns can display areas of both constructive and 
destructive interference, and they are commonly seen in phenomena like double-slit experiments and 
sound wave interference.

- Constructive Interference

Constructive interference occurs when two or more waves meet at a point and their wave 
crests perfectly coincide. This results in a new wave with an amplitude that is the sum of the 
individual amplitudes. If $A_1$ and $A_2$ are the amplitudes of the two interacting waves, 
the amplitude $A$ of the resulting wave is:

$$A = A_1 + A_2$$

- Destructive Interference

Destructive interference occurs when two or more waves meet at a point and their wave crests 
perfectly negate each other. The wave amplitude at that point becomes zero or is reduced.
The amplitude $A$ of the resulting wave will be:

$$A = | A_1 - A_2 |$$

---

### Wave Model Parameters
>model_sinewave()

|                | Parameter             | Type                      | Description                                                    |
|:---------------|:----------------------|:--------------------------|:---------------------------------------------------------------|
| x              | Positions of the wave | numpy.ndarray             | Positions where the wave is evaluated (m).                     |
| t              | Time of evaluation    | float                     | Time at which the wave is evaluated (s).                       |
| A              | Amplitude             | float                     | Maximum displacement from equilibrium (m).                     |
| wavelength     | Wavelength            | float                     | Length of one complete wave cycle (m).                         |
| frequency      | Frequency             | float                     | Number of oscillations per second (Hz).                        |
| phi            | Phase offset          | float (optional)          | Shifts the wave horizontally (radians).                        |
| propagation    | Propagation direction | string (optional)         | 'Right' for positive x-direction, 'Left' for negative.         |
| phase_polarity | Phase polarity        | string (optional)         | 'Positive' retains form, 'Negative' flips the wave vertically. |

These parameters can be used to represent the waves in the model:

$$y(x, t) = A \sin\left( \frac{2\pi}{\text{wavelength}} \cdot x - 2\pi \cdot \text{frequency} \cdot t + \phi \right)$$

### Superposition Plot Parameters
>plot_wave_superposition()

|               | Parameter                 | Type            | Description                                  |
|:--------------|:--------------------------|:----------------|:---------------------------------------------|
| wave_1_params | Wave 1 Parameters         | dictionary      | Wave 1 model_sinewave Parameters             |
| wave_2_params | Wave 2 Parameters         | dictionary      | Wave 2 model_sinewave Parameters             |
| dark_theme    | Dark Theme                | bool (optional) | If True, uses a dark background for the plot |

---

### Modeling of sine wave superposition phenomena and interference patterns

#### ex. 1 - Standing waves
#### Parameters:

|                |       Parameter        | $W_1$  | $W_2$ |
|:--------------:|:----------------------:|:------:|:-----:|
|      $A$       |       Amplitude        |   1    |   1   |
|   $\lambda$    |       Wavelength       |   1    |   1   |
|      $f$       |       Frequency        |   1    |   1   |
|     $\phi$     |      Phase offset      |   1    |   1   |
|  propagation   | Propagation direction  |   1    |   1   |
| phase polarity |     Phase polarity     |   1    |   1   |

|             | Parameter  | Value |
|:-----------:|:----------:|:-----:|
| dark_theme  | Dark Theme | True  |

#### Output:

<p align='left'>
  <img src='img/(3,2,1)[lt].png' width=60% />
</p>

#### ex. 2 - Wave beats
#### Parameters:

|                |       Parameter        | $W_1$  | $W_2$ |
|:--------------:|:----------------------:|:------:|:-----:|
|      $A$       |       Amplitude        |   1    |   1   |
|   $\lambda$    |       Wavelength       |   1    |   1   |
|      $f$       |       Frequency        |   1    |   1   |
|     $\phi$     |      Phase offset      |   1    |   1   |
|  propagation   | Propagation direction  |   1    |   1   |
| phase polarity |     Phase polarity     |   1    |   1   |

|             | Parameter  | Value |
|:-----------:|:----------:|:-----:|
| dark_theme  | Dark Theme | True  |

#### Output:

<p align='left'>
  <img src='img/(3,2,1)[lt].png' width=60% />
</p>