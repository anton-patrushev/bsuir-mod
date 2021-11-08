import numpy
import random


def print_p(p):
    for i in range(len(p)):
        print('P' + str(i + 1) + ': ' + str(p[i]))

    print('P: ' + str(sum(p)))
    print('\n')


def print_results(Q, A, Potk, Pbl, Lo, Lc, Wo, Wc, K1, K2):
    print('Q: ', Q)
    print('A: ', A)
    print('P отк: ', Potk)
    print('P бл: ', Pbl)
    print('L оч: ', Lo)
    print('L с: ', Lc)
    print('W оч: ', Wo)
    print('W с: ', Wc)
    print('K1: ', K1)
    print('K2: ', K2)

def simulate_theory_part():
    p1 = 0.25
    p2 = 0.2
    p3 = 0.5
    q1 = 1 - p1
    q2 = 1 - p2
    q3 = 1 - p3

# 1         2                       3                                                 4              5                                                 6                                                 7
    matrix = numpy.array([
        [(q1 - 1), (q1 * p2),               (q1 * p2 * p3),                                   (q1 * p3),     0.,                                               0.,                                               0.],                   # P1
        [p1,       (p1 * p2 + q1 * q2 - 1), (p1 * p2 * p3 + q1 * q2 * p3),                    (p1 * p3),     (q1 * p2 * p3),                                   0.,                                               0.],                   # P2
        [0.,       (p1 * q2),               (p1 * p2 * q3 + p1 * q2 * p3 + q1 * q2 * q3 - 1), (p1 * q3),     (p1 * p2 * p3 + q1 * p2 * q3 + q1 * q2 * p3),     (q1 * p2 * p3),                                   0.],                   # P3
        [0.,       0.,                      (q1 * p2 * q3),                                   (q1 * q3 - 1), 0.,                                               0.,                                               0.],                   # P4
        [0.,       0.,                      (p1 * q2 * q3),                                   0.,            (p1 * p2 * q3 + p1 * q2 * p3 + q1 * q2 * q3 - 1), (p1 * p2 * p3 + q1 * p2 * q3 + q1 * q2 * p3),     (p2 * p3)],            # P5
        [0.,       0.,                      0.,                                               0.,            (p1 * q2 * q3),                                   (p1 * p2 * q3 + p1 * q2 * p3 + q1 * q2 * q3 - 1), (p2 * q3 + q2 * p3)],  # P6
        [1.,       1.,                      1.,                                               1.,            1.,                                               (p1 * q2 * q3 + 1),                               (q2 * q3)]             # P7
    ])

    vector = numpy.array([0., 0., 0., 0., 0., 0., 1.])
    P = numpy.linalg.solve(matrix, vector)

    print_p(P)

    P1 = P[0]
    P2 = P[1]
    P3 = P[2]
    P4 = P[3]
    P5 = P[4]
    P6 = P[5]
    P7 = P[6]

    Pbl = P7
    K1 = (P2 + P3 + P5 + P6 + P7)
    K2 = (P3 + P4 + P5 + P6 + P7)
    A = (p2 * K1) + (p3 * K2)
    q = 1
    Potk = 0
    Lo = (P5 + 2 * P6 + 2 * P7)
    Lc = (P2 + 2 * P3 + P4 + 3 * P5 + 4 * P6 + 5 * P7)
    Wo = Lo / (p1 * (1 - Pbl))
    Wc = Lc / (p1 * (1 - Pbl))

    print_results(q, A, Potk, Pbl, Lo, Lc, Wo, Wc, K1, K2)


def simulate_practice_part():
    iterations_times = 10_000_000

    p1 = 0
    p2 = 0
    p3 = 0

    P1_v = 0.75
    P2_v = 0.8
    P3_v = 0.5

    Q1_v = 1 - P1_v
    Q2_v = 1 - P2_v
    Q3_v = 1 - P2_v

    state = "0000"  # P1

    P0000 = 0
    P0010 = 0
    P0011 = 0
    P0001 = 0
    P0111 = 0
    P0211 = 0
    P1211 = 0

    A = 0
    K1 = 0
    K2 = 0
    Lc = 0
    Lo = 0
    Potk = 0
    Q = 0
    Pbl = 0

    A_f = 0
    K1_f = 0
    K2_f = 0
    Lc_f = 0
    Lo_f = 0
    Potk_f = 0
    Q_f = 0
    Pbl_f = 0
    Wc_f = 0
    Wo_f = 0

    gen = 0

    for i in range(iterations_times):
        p1 = random.uniform(0.0, 1)
        p2 = random.uniform(0.0, 1)
        p3 = random.uniform(0.0, 1)

        if (state[0] == '0' and p1 >= P1_v):
            gen += 1

        if (state[0] == '1'):
            Lc += 1
            Pbl += 1

        if (state[1] == '1'):
            Lc += 1
            Lo += 1

        if (state[1] == '2'):
            Lc += 2
            Lo += 2

        if (state[2] == '1'):
            Lc += 1
            K1 += 1
            if (p2 >= P2_v):
                A += 1

        if (state[3] == '1'):
            Lc += 1
            K2 += 1
            if (p3 >= P3_v):
                A += 1

        # P1
        if (state == "0000"):
            P0000 += 1
            if (p1 >= P1_v):  # p1
                state = "0010"
            if (p1 < P1_v):  # q1
                state = "0000"
            continue

        # P2
        if (state == "0010"):
            P0010 += 1
            if (p1 >= P1_v and p2 >= P2_v):  # p1*p2
                state = "0010"
            if (p1 >= P1_v and p2 < P2_v):  # p1*q2
                state = "0011"
            if (p1 < P1_v and p2 >= P2_v):  # q1*p2
                state = "0000"
            if (p1 < P1_v and p2 < P2_v):  # q1*q2
                state = "0010"
            continue

        # P3
        if (state == "0011"):
            P0011 += 1
            if (p1 >= P1_v and p2 >= P2_v and p3 >= P3_v):  # p1*p2*p3
                state = "0010"
            if (p1 >= P1_v and p2 >= P2_v and p3 < P3_v):  # p1*p2*q3
                state = "0011"
            if (p1 >= P1_v and p2 < P2_v and p3 >= P3_v):  # p1*q2*p3
                state = "0011"
            if (p1 >= P1_v and p2 < P2_v and p3 < P3_v):  # p1*q2*q3
                state = "0111"

            if (p1 < P1_v and p2 >= P2_v and p3 >= P3_v):  # q1*p2*p3
                state = "0000"
            if (p1 < P1_v and p2 >= P2_v and p3 < P3_v):  # q1*p2*q3
                state = "0001"
            if (p1 < P1_v and p2 < P2_v and p3 >= P3_v):  # q1*q2*p3
                state = "0010"
            if (p1 < P1_v and p2 < P2_v and p3 < P3_v):  # q1*q2*q3
                state = "0011"
            continue

        # P4
        if (state == "0001"):
            P0001 += 1
            if (p1 >= P1_v and p3 >= P3_v):  # p1*p3
                state = "0010"
            if (p1 >= P1_v and p3 < P3_v):  # p1*q3
                state = "0011"
            if (p1 < P1_v and p3 >= P3_v):  # q1*p3
                state = "0000"
            if (p1 < P1_v and p3 < P3_v):  # q1*q3
                state = "0001"
            continue

        # P5
        if (state == "0111"):
            P0111 += 1
            if (p1 >= P1_v and p2 >= P2_v and p3 >= P3_v):  # p1*p2*p3
                state = "0011"
            if (p1 >= P1_v and p2 >= P2_v and p3 < P3_v):  # p1*p2*q3
                state = "0111"
            if (p1 >= P1_v and p2 < P2_v and p3 >= P3_v):  # p1*q2*p3
                state = "0111"
            if (p1 >= P1_v and p2 < P2_v and p3 < P3_v):  # p1*q2*q3
                state = "0211"

            if (p1 < P1_v and p2 >= P2_v and p3 >= P3_v):  # q1*p2*p3
                state = "0010"
            if (p1 < P1_v and p2 >= P2_v and p3 < P3_v):  # q1*p2*q3
                state = "0011"
            if (p1 < P1_v and p2 < P2_v and p3 >= P3_v):  # q1*q2*p3
                state = "0011"
            if (p1 < P1_v and p2 < P2_v and p3 < P3_v):  # q1*q2*q3
                state = "0111"
            continue

        # P6
        if (state == "0211"):
            P0211 += 1
            if (p1 >= P1_v and p2 >= P2_v and p3 >= P3_v):  # p1*p2*p3
                state = "0111"
            if (p1 >= P1_v and p2 >= P2_v and p3 < P3_v):  # p1*p2*q3
                state = "0211"
            if (p1 >= P1_v and p2 < P2_v and p3 >= P3_v):  # p1*q2*p3
                state = "0211"
            if (p1 >= P1_v and p2 < P2_v and p3 < P3_v):  # p1*q2*q3
                gen += 1
                state = "1211"

            if (p1 < P1_v and p2 >= P2_v and p3 >= P3_v):  # q1*p2*p3
                state = "0011"
            if (p1 < P1_v and p2 >= P2_v and p3 < P3_v):  # q1*p2*q3
                state = "0111"
            if (p1 < P1_v and p2 < P2_v and p3 >= P3_v):  # q1*q2*p3
                state = "0111"
            if (p1 < P1_v and p2 < P2_v and p3 < P3_v):  # q1*q2*q3
                state = "0211"
            continue

        # P7
        if (state == "1211"):
            P1211 += 1
            if (p2 >= P2_v and p3 >= P3_v):  # p2*p3
                state = "0111"
            if (p2 >= P2_v and p3 < P3_v):  # p2*q3
                state = "0211"
            if (p2 < P2_v and p3 >= P3_v):  # q2*p3
                state = "0211"
            if (p2 < P2_v and p3 < P3_v):  # q2*q3
                state = "1211"
            continue

    P1 = P0000 / iterations_times
    P2 = P0010 / iterations_times
    P3 = P0011 / iterations_times
    P4 = P0001 / iterations_times
    P5 = P0111 / iterations_times
    P6 = P0211 / iterations_times
    P7 = P1211 / iterations_times

    print_p([P1, P2, P3, P4, P5, P6, P7])

    # print("P0000: ", P1)
    # print("P0010: ", P2)
    # print("P0011: ", P3)
    # print("P0001: ", P4)
    # print("P0111: ", P5)
    # print("P0211: ", P6)
    # print("P1211: ", P7)

    _Pbl = (Pbl / iterations_times)
    _K1 = (K1 / iterations_times)
    _K2 = (K2 / iterations_times)
    _A = (A / iterations_times)
    _Q = 1
    _Potk = 0
    _Lo = (Lo / iterations_times)
    _Lc = (Lc / iterations_times)
    _Wo = (Lo / (gen - Pbl))
    _Wc = (Lc / (gen - Pbl))

    print_results(_Q, _A, _Potk, _Pbl, _Lo, _Lc, _Wo, _Wc, _K1, _K2)


    # print("Pbl: ", (Pbl / iterations_times))
    # Pbl_f = P7
    # print("Pbl_formula: ", Pbl_f)
    # #
    # print("K1: ", K1 / iterations_times)
    # K1_f = (P2 + P3 + P5 + P6 + P7)
    # print("K1_formula: ", K1_f)
    # #
    # print("K2: ", K2 / iterations_times)
    # K2_f = (P3 + P4 + P5 + P6 + P7)
    # print("K2_formula: ", K2_f)
    # #
    # print("A: ", (A / iterations_times))
    # A_f = P2_v * K1_f + P3_v * K2_f
    # print("A_formula: ", A_f)
    # #
    # print("Q: ", 1)
    # Q_f = 1
    # print("Q_formula: ", Q_f)
    # #
    # print("Potk: ", 0)
    # Potk_f = 0
    # print("Potk_formula: ", Potk_f)
    # #
    # print("Lo: ", (Lo / iterations_times))
    # Lo_f = (P5 + 2 * P6 + 2 * P7)
    # print("Lo_formula: ", Lo_f)
    # #
    # print("Lc: ", (Lc / iterations_times))
    # Lc_f = (P2 + 2 * P3 + P4 + 3 * P5 + 4 * P6 + 5 * P7)
    # print("Lc_formula: ", Lc_f)
    # #
    # print("Wo: ", (Lo / (gen - Pbl)))  # mul by 2 cause 2 parallel channels, empirically
    # Wo_f = Lo_f / (Q1_v * (1 - Pbl_f))
    # print("Wo_formula: ", Wo_f)
    #
    # print("Wc: ", (Lc / (gen - Pbl)))  # mul by 2 cause 2 parallel channels, empirically
    # Wc_f = Lc_f / (Q1_v * (1 - Pbl_f))
    # print("Wc_formula: ", Wc_f)


def main():
    print('Theory part calculation ... \n')
    simulate_theory_part()
    print('\nTheory part calculated successfully!\n')

    print('Practice part simulation ...\n')
    simulate_practice_part()
    print('\nPractice part simulated successfully!\n')


if __name__ == '__main__':
    main()
