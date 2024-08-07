import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

class Pendulum_nonlinear_model:

    def __init__(self, g, l, b):
        self.g = g
        self.l = l
        self.b = b

        # Definice systému diferenciálních rovnic
    def equations_nonlinear(self, y, t):
        theta, omega = y
        dtheta_dt = omega
        domega_dt = - (self.g / self.l) * np.sin(theta) - self.b * omega
        return [dtheta_dt, domega_dt]
    
    def run (self, phi0, omega0, t0, tf, dt):
        t = np.arange(t0, tf, dt)
        theta = np.zeros_like(t)
        omega = np.zeros_like(t)
        y0 = [phi0, omega0]
        theta[0] = phi0
        omega[0] = omega0

        theta, omega = odeint(self.equations_nonlinear, y0, t).T

        return theta, omega, t

class Pendulum_linear_model:

    def __init__(self, g, l, b):
        self.g = g
        self.l = l
        self.b = b

        # Definice systému diferenciálních rovnic
    def equations_linear(self, y, t):
        theta, omega = y
        dtheta_dt = omega
        domega_dt = - (self.g / self.l) * (theta) - self.b * omega
        return [dtheta_dt, domega_dt]
    
    def run (self, phi0, omega0, t0, tf, dt):
        t = np.arange(t0, tf, dt)
        theta = np.zeros_like(t)
        omega = np.zeros_like(t)
        y0 = [phi0, omega0]
        theta[0] = phi0
        omega[0] = omega0

        theta, omega = odeint(self.equations_linear, y0, t).T

        return theta, omega, t

if __name__ == "__main__":

    # Definice parametrů
    g = 9.81  # gravitační zrychlení
    l = 1.0   # délka kyvadla
    b = 0.5   # tlumicí koeficient

    t0 = 0 # počáteční čas
    tf = 10 # konečný čas
    dt = 0.01 # krok času

    phi0 = np.pi/2
    omega0 = 0

    pendulum = Pendulum_nonlinear_model(g, l, b)
    angle, angular_vel, time = pendulum.run(phi0, omega0, t0, tf, dt)

    pendulum_lin = Pendulum_linear_model(g, l, b)
    angle_lin, angular_vel_lin, time_lin = pendulum_lin.run(phi0, omega0, t0, tf, dt)
    # Graf
    plt.figure(figsize=(10, 5))
    plt.plot(time, angle, label='Úhel (theta)')
    plt.plot(time, angular_vel, label='Úhlová rychlost (omega)')
    plt.xlabel('Čas (s)')
    plt.ylabel('Hodnota')
    plt.legend()
    plt.title('Pohyb kyvadla (nelineární model)')
    plt.grid(True)
    plt.savefig('pendulum_simulation.png')  # Uložení grafu do souboru

    plt.figure(figsize=(10, 5))
    plt.plot(time_lin, angle_lin, label='Úhel (theta)')
    plt.plot(time_lin, angular_vel_lin, label='Úhlová rychlost (omega)')
    plt.xlabel('Čas (s)')
    plt.ylabel('Hodnota')
    plt.legend()
    plt.title('Pohyb kyvadla (lineární model)')
    plt.grid(True)
    plt.savefig('pendulum_simulation_lin.png')  # Uložení grafu do souboru