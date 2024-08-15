import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

class Pendulum_nonlinear_model:

    def __init__(self, g, l, b, theta0, omega0):
        self.g = g
        self.l = l
        self.b = b
        self.theta = theta0
        self.omega = omega0
        self.external_force = 0

    def equations_nonlinear(self, y, t):
        theta, omega = y
        #  derivace theta a omega
        dtheta_dt = omega
        domega_dt = + (self.g / self.l) * np.sin(theta) - self.b * omega + self.external_force
        return [dtheta_dt, domega_dt]
    
    def update (self, dt=0.01, external_force=0):
        self.external_force = external_force
        t = np.arange(0, dt, 0.01)
        # Řešení diferenciálních rovnic
        solution = odeint(self.equations_nonlinear, [self.theta, self.omega], t)
        # Aktualizace theta a omega na poslední hodnoty
        self.theta, self.omega = solution[-1]
        return solution[:, 0], solution[:, 1]  # vrací theta a omega

    def get_positions(self, width, height):
        # Oprava orientace o 90° pro správnou svislou pozici kyvadla
        # Posun o 90° zajišťuje, že výchozí pozice bude dolů
        adjusted_theta = self.theta - np.pi/2 
        
        # Vypočtení souřadnic
        x = width / 2 + self.l * np.cos(adjusted_theta) * 100
        y = height / 2 + self.l * np.sin(adjusted_theta) * 100
        return int(x), int(y)

class Pendulum_linear_model:

    def __init__(self, g, l, b, theta0, omega0):
        self.g = g
        self.l = l
        self.b = b
        self.theta = theta0
        self.omega = omega0
        self.external_force = 0

        # Definice systému diferenciálních rovnic
    def equations_linear(self, y, t):
        theta, omega = y
        dtheta_dt = omega
        domega_dt = + (self.g / self.l) * (theta) - self.b * omega + self.external_force
        return [dtheta_dt, domega_dt]

    def update(self, dt=0.01, external_force=0):
        self.external_force = external_force
        t = np.arange(0, dt, 0.01)
        # Řešení diferenciálních rovnic
        solution = odeint(self.equations_linear, [self.theta, self.omega], t)
        # Aktualizace theta a omega na poslední hodnoty
        self.theta, self.omega = solution[-1]
        return solution[:, 0], solution[:, 1]  # vrací theta a omega

    def get_positions(self, width, height):
        # Oprava orientace o 90° pro správnou svislou pozici kyvadla
        # Posun o 90° zajišťuje, že výchozí pozice bude dolů
        adjusted_theta = self.theta - np.pi / 2

        # Vypočtení souřadnic
        x = width / 2 + self.l * np.cos(adjusted_theta) * 100
        y = height / 2 + self.l * np.sin(adjusted_theta) * 100
        return int(x), int(y)

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

    pendulum = Pendulum_nonlinear_model(g, l, b, theta0=phi0, omega0=omega0)
    angle, angular_vel = pendulum.update(dt=60/1000, external_force=0)

    pendulum_lin = Pendulum_linear_model(g, l, b, theta0=phi0, omega0=omega0)
    angle_lin, angular_vel_lin = pendulum_lin.update(dt=60/1000, external_force=0)
