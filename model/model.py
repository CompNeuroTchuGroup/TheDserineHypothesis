"""
This module contains the implementation of the R-BCM learning rule.
"""

def compute_p_change(y):
    """
    Returns the probability of changing the state, 
    given the current level of post-synaptic activity y.
    """

    if y<0.05:
        return 0.05
    else:
        return y

class RBCM:
    """
    Implementation of the R-BCM learning rule.

    Parameters
    ----------
    block_threshold : bool
        If True, the threshold is not updated
    tau_w : float
        Time constant for the weight update
    tau_theta : float
        Time constant for the threshold update
    theta0 : float
        Initial value of the threshold
    """

    def __init__(self, block_threshold, tau_w=100, tau_theta=50, theta0=0.):

        self.tau_w = tau_w
        self.tau_theta = tau_theta

        self.theta = theta0

        self.block_threshold = block_threshold

    def get_weights_update(self, x, y, R):
        """
        Returns the weight update for the R-BCM learning rule, and updates the threshold.

        Parameters
        ----------
        x : array
            Pre-synaptic activity
        y : float
            Post-synaptic activity
        R : float
            Valence signal

        Returns
        -------
        array
            Weight update
        """

        theta_dot = - 1/self.tau_theta * (self.theta - y**2)

        w_dot = -R*x*y*(y - self.theta)/self.tau_w

        if not self.block_threshold:
            self.theta = self.theta + theta_dot

        return w_dot
    