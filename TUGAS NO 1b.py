import numpy as np
import matplotlib.pyplot as plt

def parabola_simulation(alpha_degree, v0):
    alpha = np.radians(alpha_degree)
    g = 9.8  # gravitasi

    v0x = v0 * np.cos(alpha)  # komponen horizontal kecepatan awal
    v0y = v0 * np.sin(alpha)  # komponen vertikal kecepatan awal

    X = ((v0**2) * np.sin(2*alpha)) / (2*g)  # jarak horizontal maksimum
    Y = ((v0*2) * (np.sin(alpha)*2)) / (2*g)  # tinggi vertikal maksimum
    T = (2 * v0 * np.sin(alpha)) / g  # waktu mencapai jarak horizontal maksimum

    print(f"\nUntuk alpha = {alpha_degree}° dan v0 = {v0} m/s:")
    print("Jarak Horizontal Maksimum =", X, "m")
    print("Tinggi Vertikal Maksimum =", Y, "m")
    print("Waktu Mencapai Jarak Horizontal Maksimum =", T, "s")

    # Simulasi gerak parabola
    t = np.arange(0.0, T, 0.01)
    y = v0y * t - 0.5 * g * t**2
    x = v0x * t

    # Plot grafik
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='Jarak Horizontal (m)', ylabel='Jarak Vertikal (m)',
           title=f'Grafik Gerak Parabola\n(alpha = {alpha_degree}°, v0 = {v0} m/s)')
    ax.grid()
    plt.show()

# Variasi 1
parabola_simulation(45, 10)

# Variasi 2
parabola_simulation(30, 15)
