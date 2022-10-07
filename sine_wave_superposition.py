# _________ _________ _________
# Sine wave superposition

# Author: Sebastian Mag. | Date: Oct 06/2022
# Source code: https://github.com/cmd098/sine-wave-superposition

# Summary:
# Modeling and visualization of the superposition principle for two traveling sine waves
# by definition of the general form y(t) = Asin(ωt)
# _________ _________ _________

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set custom matplotlib default font
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['mathtext.fontset'] = 'stix'

def plot_wave_superposition(wa1, wf1, wa2, wf2, ipw1=False, ipw2=False):
    """
    Models two traveling sine waves by definition of the General form y(t) = Asin(ωt)
    and plots their superposition and resultant wave

    Args:
        wa1 (float, Positve): Wave 1 - Amplitude in mm
        wf1 (float, Real): Wave 1 - Frequency in Hz
        wa2 (float, Positive): Wave 2 - Amplitude in mm
        wf2 (float, Real): Wave 2 - Frequency in Hz

        ipw1 (bool, [optional]): Wave 1 - Inverts wave polarity [Defaults to False]
        ipw2 (bool, [optional]): Wave 2 - Inverts wave polarity [Defaults to False]

    About wave modeling:
        Positive frequencies will be displayed as leftward traveling
        Negative frequencies will be displayed as rightward traveling
        Inverting the polarity will shift the wave phase by 180°
    """

    # Initialize figure and axes

    sns.set_theme()
    fig, ax = plt.subplots(2, 2, figsize=(15, 6), sharex='all')
    fig.subplots_adjust(wspace=0.15, hspace=0.4)
    fig.subplots_adjust(top=0.79)

    # Initialize objects to animate

    w1, = ax[0, 0].plot([], [], color='#7383c3')  # wave 1
    w2, = ax[1, 0].plot([], [], color='#71768b')  # wave 2

    sw1, = ax[0, 1].plot([], [], color='#7383c3')  # superposed wave 1
    sw2, = ax[0, 1].plot([], [], color='#71768b')  # superposed wave 2

    rw, = ax[1, 1].plot([], [], color='#53587a')  # resultant wave

    # Set axes ticks, labels and limits

    wa = [abs(wa1), abs(wa2)]  # wave amplitudes

    plt.setp(ax, xlim=(0, 5), ylim=(-(sum(wa) + 2), sum(wa) + 2))

    for x in range(2):
        for y in range(2):
            ax[x, y].set_yticks(np.linspace(-sum(wa), sum(wa), 7))
            ax[x, y].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

    ax[1, 0].set_xticks(np.arange(0, 5, 1))
    ax[1, 0].set_xticklabels([l.get_text() + r'$x 10^{-2}$' for l in ax[1, 1].get_xticklabels()])

    plt.setp(ax[1, 0].get_xticklabels()[0], visible=False)
    plt.setp(ax[1, 1].get_xticklabels()[0], visible=False)

    # Sine wave modeling - General form as a function of time (t)
    x = np.arange(0.05, 4.95, 0.001)  # t=5.10^-2 s; (5 cs)

    def animate(i):

        # y(t) = Asin(ωt); ω = 2πf

        p = -1 if ipw1 else 1
        w1y = wa1 * p * np.sin((2 * np.pi * (wf1 * 0.01)) * x + 0.17 * i)
        p = -1 if ipw2 else 1
        w2y = wa2 * p * np.sin((2 * np.pi * (wf2 * 0.01)) * x + 0.17 * i)

        w1.set_data(x, w1y)
        w2.set_data(x, w2y)
        sw1.set_data(x, w1y)
        sw2.set_data(x, w2y)
        rw.set_data(x, w1y + w2y)

        return w1, w2, sw1, sw2, rw

    # Add titles and labels

    fig.suptitle('Superposition of Sine waves', size=18, x=0.23)
    plt.figtext(0.125, 0.89, r'$y_(t) = A\sin(\omega t+ \varphi)$', fontsize=14)

    fig.supxlabel('Time (s)')
    fig.supylabel('Displacement (mm)', x=0.06)

    direction = 'longrightarrow' if (wf1 < 0) else 'longleftarrow'
    ax[0, 0].set_title(r'$W_1$ | Frequency: {0} Hz | Amplitude: {1} mm |  $\{2}$'
                       .format(abs(wf1), wa1, direction), size=14, pad=16, loc='left')

    direction = 'longrightarrow' if (wf2 < 0) else 'longleftarrow'
    ax[1, 0].set_title(r'$W_2$ | Frequency: {0} Hz | Amplitude: {1} mm |  $\{2}$'
                       .format(abs(wf2), wa2, direction), size=14, pad=16, loc='left')

    ax[0, 1].set_title(r'Wave superposition | $W_1 + W_2$', size=14, pad=16, loc='left')
    ax[1, 1].set_title(r'Resultant wave | $W_R = W_1 + W_2$', size=14, pad=16, loc='left')

    animation = FuncAnimation(fig, animate, frames=200, interval=25, blit=True)
    file_name = f'Sine wave superposition (w1A={wa1}mm, w1f={wf1}Hz) + (w2A={wa2}mm, w2f={wf2}Hz)'

    # Save animation (.gif)
    # animation.save(f'{file_name}.gif', writer='pillow', fps=30, dpi=120)

    # Save last frame as an image (.png)
    # fig.savefig(f'{file_name}.png', bbox_inches='tight', pad_inches=0.3, dpi=140)

    # Display figure
    plt.show()

# ______ Implementation | Output ______

plot_wave_superposition(10, 140, 10, -140)

# plot_wave_superposition(10, 180, 10, 180, True)
# plot_wave_superposition(10, 180, 20, -240, True)
# plot_wave_superposition(10, 320, 10, -240, True, True)
