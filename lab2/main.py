import numpy as np
import matplotlib.pyplot as plt
import random
import math
from functools import reduce


def generate_random_sequence(n):
    return list(map(lambda x: random.random(), range(0, int(n))))


def show_hist(sequence):
    weights = np.ones_like(sequence) / float(len(sequence))
    plt.hist(sequence, bins=np.linspace(min(sequence), max(sequence), 21),
             weights=weights, histtype='bar', color='purple', rwidth=0.95)
    plt.show()


def calculate_parameters(sequence):
    show_hist(sequence)
    print('\nМат ожидание: ', np.mean(sequence), '\nДисперсия: ',
          np.var(sequence), '\nСКО: ', np.std(sequence), '\n')


# a + (b - a) * x
def build_uniform_distribution(a, b):
    return list(map(lambda x: a + (b - a) * x, generate_random_sequence(1000000)))


# M + std * /(12/n) * (random - n/2)
def build_gauss_distribution(mean, std, n=6.0):
    return list(
        map(lambda x: mean + std * math.sqrt(12 / n) * (sum(generate_random_sequence(n)) - n / 2), range(0, 1000000)))


# -1/lambda * ln(R)
def build_exponential_distribution(lambda_param):
    return list(map(lambda x: - 1 / lambda_param * math.log(x), generate_random_sequence(1000000)))


# -1/lambda * ln(sum(yz))
def build_gamma_distribution(eta, lambda_param):
    return list(map(lambda x: -1 / lambda_param * math.log(reduce(lambda y, z: y * z, generate_random_sequence(eta))),
                    range(0, 1000000)))


#  2 * (b - x) / (b - a)^2
def build_min_triangle_distribution(a, b):
    return list(map(lambda x: a + (b - a) * min(generate_random_sequence(2)), range(0, 1000000)))


#  2 * (x - a) / (b - a)^2
def build_max_triangle_distribution(a, b):
    return list(map(lambda x: a + (b - a) * max(generate_random_sequence(2)), range(0, 1000000)))


# X = y + z
def build_simpson_distribution(a, b):
    return list(map(lambda x, y: x + y, build_uniform_distribution(a / 2, b / 2), build_uniform_distribution(a / 2, b / 2)))


def main():
    print('Равномерное распределение: ')
    calculate_parameters(build_uniform_distribution(float(input('A: ')), float(input('B: '))))

    print('Распределение Гаусса: ')
    calculate_parameters(build_gauss_distribution(float(input('Mean: ')), float(input('Std: ')), float(input('N: '))))

    print('Экспоненциальное распределение: ')
    calculate_parameters(build_exponential_distribution(float(input('λ: '))))

    print('Гамма распределение (int only): ')
    calculate_parameters(build_gamma_distribution(int(input('η: ')), int(input('λ: '))))

    print('Min треугольное распределение: ')
    calculate_parameters(build_min_triangle_distribution(float(input('A: ')), float(input('B: '))))

    print('Max треугольное распределение: ')
    calculate_parameters(build_max_triangle_distribution(float(input('A: ')), float(input('B: '))))

    print('Распределение Симпсона: ')
    calculate_parameters(build_simpson_distribution(float(input('A: ')), float(input('B: '))))


if __name__ == '__main__':
    main()
