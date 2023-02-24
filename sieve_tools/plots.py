import matplotlib.pyplot as plt
import numpy as np
from sieve_tools import sieve

def plot_sieve():
    
    plt.plot(np.arange(100, 5000, 100), sieve.proportion_primes())
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")

    # plt.plot(np.arange(100, 5000, 100), sieve.proportion_primes())
    # plt.xlabel("N")
    # plt.ylabel("Proportion of primer numbers")
    # plt.xscale("log")
    # plt.yscale("log")import matplotlib.pyplot as plt
import numpy as np
from sieve_tools import sieve

def plot_sieve():
    
    plt.plot(np.arange(100, 5000, 100), sieve.proportion_primes())
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")

    # plt.plot(np.arange(100, 5000, 100), sieve.proportion_primes())
    # plt.xlabel("N")
    # plt.ylabel("Proportion of primer numbers")
    # plt.xscale("log")
    # plt.yscale("log")