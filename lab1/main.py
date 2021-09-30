# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt

sequence = []


def calculate_sequence(a, m, r_n, n):
    for x in range(0, n):
        r_n = a * r_n % m
        sequence.append(r_n / m)


def calculate_period():
    x_v_index_matchers = []

    for i in range(0, len(sequence)):
        if sequence[i] == sequence[-1]:
            x_v_index_matchers.append(i)

    if len(x_v_index_matchers) < 2:
        return 0

    return x_v_index_matchers[1] - x_v_index_matchers[0]


def calculate_aperiodic_interval(period):
    aperiodic_length = 0
    while sequence[aperiodic_length] != sequence[aperiodic_length + period]:
        aperiodic_length += 1
    return period + aperiodic_length


def calculate_implicit_criteria():
    criteria_matchers = 0
    for i in range(0, len(sequence), 2):
        if sequence[i] ** 2 + sequence[i + 1] ** 2 < 1:
            criteria_matchers += 1
    print('\nActual: ', 2 * criteria_matchers / len(sequence), '\nExpected: ', np.pi / 4)


def show_hist():
    weights = np.ones_like(sequence) / float(len(sequence))
    plt.hist(sequence, bins=np.linspace(0, 1, 21), weights=weights, histtype='bar', color='green', rwidth=0.9)
    plt.hlines(1 / 20, 0, 1)
    plt.show()


def show_params():
    print('Mean value: ', np.mean(sequence))
    print('Variance value: ', np.var(sequence))
    print('Standard deviation value: ', np.std(sequence))


def main():
    a = int(input("Enter 'a' value: "))
    m = int(input("Enter 'm' value: "))
    r0 = int(input("Enter 'R0' value: "))
    n = 1000000

    calculate_sequence(a, m, r0, n)

    calculate_implicit_criteria()

    period = calculate_period()
    print("Period: ", period)

    aperiodic_interval = calculate_aperiodic_interval(period)
    print("Aperiodic interval: ", aperiodic_interval)

    show_params()

    show_hist()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
