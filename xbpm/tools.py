"""General tools to use with xbpm calculations."""

import numpy as _np
import mathphys.constants as _cts
import xraylib as _xl

ECHARGE = _cts.elementary_charge
EMASS = _cts.electron_mass
LSPEED = _cts.light_speed
PLANK_REDUCED = _cts.reduced_planck_constant
PI = _np.pi


class XBPMFunctions:
    """Class with generic xbpm methods."""

    def __init__(self):
        self._elements = [
            'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
            'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
            'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
            'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
            'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
            'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
            'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
            'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
            'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb',
            'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
            'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
            'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh']
        

    def calc_coef_absorption(self, elem, energy):
        """Absorption coefficient calculation.
        
        Args: 
            elem (int or str): Element Mass or Element symbol.
            energy (float): Target Energy [keV].
        
        Returns:
            Absorption coeficient.
        """
        if elem in self._elements:
            return _xl.CS_Energy_CP(compound=elem, E=energy)
        
        elif  type(elem) is int and 1 <= elem and elem <= 107:
            return _xl.CS_Energy(Z=elem, E=energy)

        else:
            raise ValueError('Element does not exist.')