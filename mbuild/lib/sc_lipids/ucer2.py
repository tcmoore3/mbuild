import mbuild as mb
import numpy as np

class UCer2(mb.Compound):
    def __init__(self):
        """Returns a CER NS C24 with the head-to-tail vector pointing in +z.
        """
        super(UCer2, self).__init__(name='ucer2')
        mb.load('ucer2.pdb', compound=self, relative_to_module=self.__module__)
        mb.coordinate_transform.z_axis_transform(self, 
                new_origin=self[2], point_on_z_axis=self[58])
