# --- --- --- --- --- --- --- --- ---
# One-Dimensional Superposition of Sine Waves

# Sebastian Mag | August 2023
# https://github.com/ssebastianmag/sine-wave-superposition

# Modeling and Visualization of linear superposition
# of waveforms and resultant interference patterns
# --- --- --- --- --- --- --- --- ---

from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def model_sinewave(x, t, A, wavelength, frequency, phi=0, propagation='right', phase_polarity='positive'):
    """ Calculate the displacement of a 1D sine wave at positions x and time t.
        Args:
            x (numpy.ndarray): positions at which the wave is evaluated (m)
            t (float): time at which the wave is evaluated (s)
            A (float): amplitude (m)
            wavelength (float): wavelength (m)
            frequency (float): frequency (Hz)
            phi (float, optional): phase offset of the wave (radians)
            propagation (str, optional): direction of wave propagation ('right' or 'left')
            phase_polarity (str, optional): vertical flipping of the wave ('positive' or 'negative')
        Returns:
            numpy.ndarray: wave displacement at a given position and time
    """

    # Wave number and Angular frequency
    k = 2 * np.pi / wavelength
    omega = 2 * np.pi * frequency

    # Phase polarity and Propagation direction factor
    polarity = 1 if phase_polarity.lower() == 'positive' else -1
    propagation_factor = -1 if propagation.lower() == 'right' else 1

    # Evaluate the sine wave at given x and t
    # y(x, t) = (+-) A * sin(k * x (+-) omega * t + phi)
    return polarity * A * np.sin(k * x + propagation_factor * omega * t + phi)


def plot_wave_superposition(wave_1_params, wave_2_params, dark_theme=False):
    """ Plot and animate the superposition of two 1D waves.

        Args:
            wave_1_params (dict): W1, wave 1 parameters
            wave_2_params (dict): W2, wave 2 parameters
            dark_theme (bool, optional): if True, uses a dark background for the plot
    """

    # Custom settings for plot aesthetics
    sns.set_theme()
    plt.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['mathtext.fontset'] = 'stix'
    if dark_theme:
        plt.style.use('dark_background')
        plt.rcParams.update({'grid.linewidth': 0.5, 'grid.alpha': 0.2})

    # Custom colormaps
    wave_1_cm = LinearSegmentedColormap.from_list(
        'wave_1_cm', colors=['#3c3060', '#3480a4', '#3c3060'], N=100
    )
    wave_2_cm = LinearSegmentedColormap.from_list(
        'wave_2_cm', colors=['#581e4f', '#d2204c', '#581e4f'], N=100
    )
    superposition_cm = LinearSegmentedColormap.from_list(
        'superposition_cm', colors=['#ddd7d7', '#3480a4', '#ddd7d7', '#d2204c', '#ddd7d7'], N=100)

    # Update function to animate the plot
    def update(num):
        # Adjust time step based on max frequency
        max_frequency = max(wave_1_params['frequency'], wave_2_params['frequency'])
        t = num * 0.025 / max_frequency

        # Calculate y-values for Wave 1, Wave 2, and Resultant Wave (Superposition)
        yw1 = model_sinewave(x, t, **wave_1_params)
        yw2 = model_sinewave(x, t, **wave_2_params)
        ywr = yw1 + yw2

        # Get custom color map colors for each object
        norm_val = num / 200
        wave_1_color = wave_1_cm(norm_val)
        wave_2_color = wave_2_cm(norm_val)
        superposition_color = superposition_cm(norm_val)

        # Update y-values and colors
        w1.set_ydata(yw1)  # Wave 1
        w1.set_color(wave_1_color)

        w2.set_ydata(yw2)  # Wave 2
        w2.set_color(wave_2_color)

        w1sp.set_ydata(yw1)  # W1 superimposed pattern
        w1sp.set_color(wave_1_color)

        w2sp.set_ydata(yw2)  # W2 superimposed pattern
        w2sp.set_color(wave_2_color)

        wr.set_ydata(ywr)  # Resultant wave
        wr.set_color(superposition_color)

        # Return updated line objects for animation
        return w1, w2, w1sp, w2sp, wr

    #  Function to set y-axis ticks and limits
    def set_axis_yticks_and_limits(subplot_ax, amplitude):
        y_ticks = np.linspace(-amplitude * 1.5, amplitude * 1.5, 7)
        subplot_ax.set_ylim(-amplitude * 1.5, amplitude * 1.5)
        subplot_ax.set_yticks(y_ticks)

    # Initialize plot figure
    fig, ax = plt.subplots(2, 2, figsize=(15, 7))
    fig.subplots_adjust(wspace=0.15, hspace=1)
    fig.subplots_adjust(top=0.76, bottom=0.14)

    # Set the x-axis range based on the maximum wavelength
    n = 500
    max_wavelength = max(wave_1_params['wavelength'], wave_2_params['wavelength'])
    x = np.linspace(0, 8 * max_wavelength, n)

    # Initialize line objects for animation
    w1, = ax[0, 0].plot(x, np.zeros(n), color='#7383c3', )  # Wave 1
    w2, = ax[1, 0].plot(x, np.zeros(n), color='#71768b')  # Wave 2
    w1sp, = ax[0, 1].plot(x, np.zeros(n), color='#7383c3', linestyle=':')  # W1 superimposed pattern
    w2sp, = ax[0, 1].plot(x, np.zeros(n), color='#71768b', linestyle=':')  # W2 superimposed pattern
    wr, = ax[1, 1].plot(x, np.zeros(n), color='#53587a')  # Resultant wave (Superposition)

    # Set y-limits and y-ticks for W1 and W2
    set_axis_yticks_and_limits(ax[0, 0], wave_1_params['A'])
    set_axis_yticks_and_limits(ax[1, 0],  wave_2_params['A'])

    # Set y-limits and y-ticks for superimposed pattern and resultant wave
    set_axis_yticks_and_limits(ax[0, 1], max(wave_1_params['A'], wave_2_params['A']))
    set_axis_yticks_and_limits(ax[1, 1], wave_1_params['A'] + wave_2_params['A'])

    # Set x-ticks at every half max wavelength
    xticks = np.arange(0, 8 * max_wavelength + 1, max_wavelength // 1)
    for subplot in ax.flatten():
        subplot.set_xticks(xticks)
        subplot.set_xticklabels(['{:.1f}'.format(tick) for tick in subplot.get_xticks()])
        subplot.set_yticklabels(['{:.1f}'.format(tick) for tick in subplot.get_yticks()])

    # Add title and subtitle
    fig.suptitle('One-Dimensional Superposition of Sine Waves', size=17, x=0.272)
    fig.text(0.123, 0.915, (
        'Wave Dynamics: Linear Superposition of Waveforms and Resultant Interference Patterns.'
    ), size=11, color='#c5c5c5' if dark_theme else '#4e4e4e')

    # Add [0, 0] and [1, 0] subplot titles
    for iteration, params in enumerate([wave_1_params, wave_2_params]):
        propagation = 'rightarrow' if params['propagation'].lower() == 'right' else 'leftarrow'
        propagation_operator = '-' if params['propagation'].lower() == 'right' else '+'
        phase_polarity_operator = '-' if params['phase_polarity'].lower() == 'negative' else ''
        wave_num = iteration + 1

        ax[iteration, 0].text(0, 1.4, (
            r'Wave {0} ($\{3}$): $\quad W_{0}(x, t) = {1} A \sin(k x {2} \omega t + \phi)$'
            .format(wave_num, phase_polarity_operator, propagation_operator, propagation)
        ), size=14, transform=ax[iteration, 0].transAxes)

        ax[iteration, 0].text(0, 1.11, (
            r'$A_{0} = {1:.2f} \, m, \quad f_{0} = {2:.2f} \, Hz,'
            r' \quad \lambda_{0} = {3:.2f} \, m, \quad \phi_{0} = {4:.4f}$'
            .format(wave_num, params['A'], params['frequency'], params['wavelength'], params['phi'])
        ), size=13, transform=ax[iteration, 0].transAxes)

    # Add [0, 1] and [1, 1] subplot titles
    ax[0, 1].text(0, 1.4, 'Superimposed Pattern:', size=14, transform=ax[0, 1].transAxes)
    ax[0, 1].text(0, 1.11, r'$W_1(x, t) \ \ and \ \ W_2(x, t)$', size=14, transform=ax[0, 1].transAxes)
    ax[1, 1].text(0, 1.4, 'Superposition:', size=14, transform=ax[1, 1].transAxes)
    ax[1, 1].text(0, 1.11, r'$W_R(x, t) = W_1(x, t) + W_2(x, t)$', size=14, transform=ax[1, 1].transAxes)

    # Add x-axis, y-axis labels
    fig.supylabel('Displacement (m)', x=0.06, size=14)
    fig.supxlabel('Position (m)', y=0.04, size=14)

    # Create and display the animation
    animation = FuncAnimation(fig, update, frames=200, interval=25, blit=True)
    # animation.save('sine_wave_superposition_2.gif', writer='pillow', fps=30, dpi=120)  # Save animation (.gif)
    plt.show()


# - - - Example sine wave superpositions
if __name__ == '__main__':

    # 1. Standing waves
    plot_wave_superposition(
        wave_1_params={'A': 5, 'wavelength': 10, 'frequency': 90, 'phi': 0.0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        wave_2_params={'A': 5, 'wavelength': 10, 'frequency': 90, 'phi': 0.0,
                       'propagation': 'left', 'phase_polarity': 'positive'},
        dark_theme=True
    )

    # 2. Wave beats
    plot_wave_superposition(
        wave_1_params={'A': 5, 'wavelength': 4, 'frequency': 10, 'phi': 0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        wave_2_params={'A': 5, 'wavelength': 5, 'frequency': 20, 'phi': 0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        dark_theme=True
    )

    # 3. Constructive Interference
    plot_wave_superposition(
        wave_1_params={'A': 10, 'wavelength': 10, 'frequency': 90, 'phi': 0.0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        wave_2_params={'A': 5, 'wavelength': 10, 'frequency': 90, 'phi': 0.0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        dark_theme=True
    )

    # 4. Destructive Interference
    plot_wave_superposition(
        wave_1_params={'A': 10, 'wavelength': 10, 'frequency': 90, 'phi': 0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        wave_2_params={'A': 5, 'wavelength': 10, 'frequency': 90, 'phi': np.pi,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        dark_theme=True
    )

    # 5. Perfect Destructive Interference (Cancellation)
    plot_wave_superposition(
        wave_1_params={'A': 10, 'wavelength': 10, 'frequency': 90, 'phi': 0.0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        wave_2_params={'A': 10, 'wavelength': 10, 'frequency': 90, 'phi': np.pi,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        dark_theme=True
    )

    # 6. Fundamental Frequency + 2nd Harmonic
    plot_wave_superposition(
        wave_1_params={'A': 5, 'wavelength': 4, 'frequency': 90, 'phi': 0.0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        wave_2_params={'A': 2.5, 'wavelength': 2, 'frequency': 180, 'phi': 0.0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        dark_theme=True
    )

    # 7. General superposition
    plot_wave_superposition(
        wave_1_params={'A': 10, 'wavelength': 6, 'frequency': 90, 'phi': 0.0,
                       'propagation': 'right', 'phase_polarity': 'positive'},
        wave_2_params={'A': 5, 'wavelength': 10, 'frequency': 110, 'phi': 0.0,
                       'propagation': 'left', 'phase_polarity': 'negative'},
        dark_theme=True
    )
