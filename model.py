import numpy as np

def change_state(x, x1, x2):

    if np.array_equal(x, x1):
        return x2.copy()
    
    elif np.array_equal(x, x2):
        return x1.copy()

def get_valence_signal(x, x1, x2, R1, R2):

    if np.array_equal(x, x1):
        return R1
    elif np.array_equal(x, x2):
        return R2
    
def compute_p_change(y):

    if y<0.05:
        return 0.05
    else:
        return y
    
class BCM:
    
    def __init__(self, block_threshold, tau_w=100, tau_theta=50, theta0=0.):

        self.tau_w = tau_w
        self.tau_theta = tau_theta

        self.theta = theta0

        self.block_threshold = block_threshold
    
    def get_weights_update(self, x, y, R):

        theta_dot = - 1/self.tau_theta * (self.theta - y**2)

        w_dot = R*x*y*(y - self.theta)/self.tau_w
        
        if not self.block_threshold:
            self.theta = self.theta + theta_dot
        
        return w_dot