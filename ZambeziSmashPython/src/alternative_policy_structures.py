# Alternative policy structures
import numpy as np

class irrigation_policy:
    """irrigation policy class represents different irrigation policies for all the irrigation districts"""

    def __init__(self, n_inputs, n_outputs, kw_dict):
        """
        The constructor initializes the irrigation policy classes with a number of inputs (n_inputs), a number of outputs (n_outputs)
        and information from the keyword dictionary (kw_dict) on the number of irrigation districts stored in self.I

        Parameters
        ----------
        n_inputs
        n_outputs
        kw_dict
        """
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.I = kw_dict['n_irr_districts']
        self.irr_parab_param = np.empty(0)
        self.irr_input_min = np.empty(0)
        self.irr_input_max = np.empty(0)

    def setParameters(self, IrrTheta):
        self.irr_parab_param = IrrTheta

    def clearParameters(self):
        self.irr_parab_param = np.empty(0)

    def get_output(self, input):
        """ 

        Parameters
        ----------
        self
        input

        Returns
        -------

        """
        input_inflow, input_w, irr_district, irr_district_idx = tuple(input)
        y = float()
        hdg, hdg_dn, m = tuple(3 * [float()])
        start_param_idx = int(irr_district_idx[irr_district-2])

        hdg = self.irr_parab_param[start_param_idx]
        m = self.irr_parab_param[start_param_idx+1]

        hdg_dn = hdg*( self.irr_input_max[irr_district-2] - self.irr_input_min[irr_district-2] )\
             + self.irr_input_min[irr_district-2]
        
        if input_inflow <= hdg_dn:
            y = min(input_inflow,input_w*(pow(input_inflow/hdg_dn,m)))
        else:
            y = min(input_inflow,input_w)

        return y
    
    def getFreeParameterNumber(self):
        return 2 * self.I

    def setMinInput(self, pV):
        self.irr_input_min = np.array(pV)

    def setMaxInput(self, pV):
        self.irr_input_max = np.array(pV)

#irrigation_policy(2,2,1)

