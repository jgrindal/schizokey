import numpy as np
import time
from machine import Machine

class Exp:
    # Machine parameters
    k = 100
    n = 10
    r = 10

    def __init__(self):
        print("Creating machines : k=" + str(self.k) + ", n=" +str(self.n) + ", l=" + str(self.r))
        self.Alice = Machine(self.k, self.n, self.r)
        self.Bob = Machine(self.k, self.n, self.r)
        self.Eve = Machine(self.k, self.n, self.r)

        self.sync_weights()

    def random(self):
        return np.random.randint(-self.r, self.r + 1, [self.k, self.n])

    def sync_weights(self):
        sync = False  # Flag to check if weights are sync
        nb_updates = 0  # Update counter
        nb_eve_updates = 0  # To count the number of times eve updated
        start_time = time.time()  # Start time
        sync_history = []  # to store the sync score after every update

        while not sync:

            X = self.random()  # Create random vector of dimensions [k, n]

            tauA = self.Alice(X)  # Get output from Alice
            tauB = self.Bob(X)  # Get output from Bob
            tauE = self.Eve(X)  # Get output from Eve

            self.Alice.update(tauB, update_rule)  # Update Alice with Bob's output
            self.Bob.update(tauA, update_rule)  # Update Bob with Alice's output

            # Eve would update only if tauA = tauB = tauE
            if tauA == tauB == tauE:
                Eve.update(tauA, update_rule)
                nb_eve_updates += 1

            nb_updates += 1

            score = 100 * sync_score(Alice, Bob)  # Calculate the synchronization of the 2 machines

            sync_history.append(score)  # Add sync score to history, so that we can plot a graph later.

            sys.stdout.write('\r' + "Synchronization = " + str(int(score)) + "%   /  Updates = " + str(
                nb_updates) + " / Eve's updates = " + str(nb_eve_updates))
            if score == 100:  # If synchronization score is 100%, set sync flag = True
                sync = True

        end_time = time.time()
        time_taken = end_time - start_time  # Calculate time taken


if __name__ == "__main__":
    Exp()
