from constants import rad_e, kev_nm_conversion
from scipy.constants import N_A, elementary_charge

import numpy as np

def e_kev_to_wav_nm(e_kev=1):
    wav_nm = kev_nm_conversion / e_kev
    return wav_nm

def wav_nm_to_e_kev(wav_nm=1):
    e_kev = kev_nm_conversion / wav_nm
    return e_kev

def get_delta(wavelength_nm=0, energy_kev=12.4, density_gcm3=1, Z=1, A=1, degree=False):
    if wavelength_nm:
        wav_nm = wavelength_nm
    elif energy_kev:
        wav_nm = e_kev_to_wav_nm(energy_kev)
    else:
        return
    
    wav_m = wav_nm * 1e-9
    density_kgm3 = density_gcm3 * 1e3
    
    delta = N_A * rad_e * wav_m ** 2 * density_kgm3 * Z / (2 * np.pi * A)

    if degree:
        delta = np.degrees(delta)

    return delta





def fresnel(k_1, k_2):
    r12 = (k_1 - k_2) / (k_1 + k_2)
    return r12




