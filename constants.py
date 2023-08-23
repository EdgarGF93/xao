
import numpy as np
from scipy.constants import speed_of_light, elementary_charge, epsilon_0, m_e, h

rad_e = 1 / (4 * np.pi * epsilon_0) * elementary_charge ** 2 / (m_e * speed_of_light ** 2)
kev_nm_conversion = h * speed_of_light / 1e-9 / elementary_charge / 1e3