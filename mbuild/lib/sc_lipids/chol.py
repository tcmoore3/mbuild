import mbuild as mb
import numpy as np

class Chol(mb.Compound):
    def __init__(self):
        """Returns a CHOL with the head-to-tail vector pointing in +z.
        """
        super(Chol, self).__init__(name='chol')
        mb.load('chol.pdb', compound=self, relative_to_module=self.__module__)
        mb.coordinate_transform.z_axis_transform(self, 
                new_origin=self[2], point_on_z_axis=self[63])
