#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test numeric.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

try:
    import user305_SXBsmszNiUxIeoV as codeskulptor_lib  # pytype: disable=import-error  # noqa

    import numeric  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor_lib as codeskulptor_lib  # type: ignore  # noqa

    import SimpleGUICS2Pygame.numeric as numeric  # type: ignore

    SIMPLEGUICS2PYGAME = True


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version

    try:
        from typing import List, Tuple, Union
    except ImportError:
        pass

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
else:
    PYTHON_VERSION = 'CodeSkulptor'  # https://py2.codeskulptor.org/ or https://py3.codeskulptor.org/  # noqa


def m_eq(a, b, exact=True):
    # type: (numeric.Matrix, numeric.Matrix, bool) -> bool
    """
    If each element of a == each element of b
    then return True,
    else return False.

    If exact
    then comparaison of each element must be exact,
    else the absolute difference must be <= 1e-5

    :param a: numeric.Matrix
    :param b: numeric.Matrix
    :param exact: bool
    """
    assert isinstance(a, numeric.Matrix), type(a)
    assert isinstance(b, numeric.Matrix), type(b)
    assert isinstance(exact, bool), type(exact)

    if a.shape() != b.shape():
        return False

    if exact:  # pylint: disable=no-else-return
        return m_to_l(a) == m_to_l(b)
    else:
        m, n = a.shape()

        for i in range(m):
            for j in range(n):
                if abs(a[i, j] - b[i, j]) > 1e-5:
                    return False

        return True


def m_to_l(m):  # type: (numeric.Matrix) -> List[List[float]]
    """
    Return the list of list corresponding to the matrix m.

    :param m: numeric.Matrix

    :return: list of list of float
    """
    assert isinstance(m, numeric.Matrix), type(m)

    return [[m[i, j] for j in range(m.shape()[1])]
            for i in range(m.shape()[0])]


#
# Main
######
def main():  # pylint: disable=too-many-locals,too-many-branches,too-many-statements  # noqa
    # type: () -> None
    """Perform succession of tests."""
    if SIMPLEGUICS2PYGAME:
        from sys import argv  # pylint: disable=import-outside-toplevel

        if len(argv) != 2:
            print('Test numeric.Matrix ...\n')
    else:
        print('Test numeric.Matrix ...\n')

    nb_errors = 0

    dz5_3 = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]  # type: List[List[Union[int, float]]]

    dz3_5 = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]  # type: List[List[Union[int, float]]]

    di1 = [[1]]  # type: List[List[Union[int, float]]]

    di5 = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]]  # type: List[List[Union[int, float]]]

    d5_3 = [[0, -1, 2],
            [-3, 4, -5],
            [6, -7, 8],
            [-9, 10, -11],
            [12, -13, 14]]  # type: List[List[Union[int, float]]]

    d5_3t = [[0, -3, 6, -9, 12],
             [-1, 4, -7, 10, -13],
             [2, -5, 8, -11, 14]]  # type: List[List[Union[int, float]]]

    d3_5 = [[0, -1, 2, -3, 4],
            [-5, 6, -7, 8, -9],
            [10, -11, 12, -13, 14]]  # type: List[List[Union[int, float]]]

    d3_5t = [[0, -5, 10],
             [-1, 6, -11],
             [2, -7, 12],
             [-3, 8, -13],
             [4, -9, 14]]  # type: List[List[Union[int, float]]]

    d2_2 = [[1, 2],
            [3, 4]]  # type: List[List[Union[int, float]]]

    d2_2i = [[-2, 1],
             [1.5, -0.5]]  # type: List[List[Union[int, float]]]

    d3_3 = [[2, -1, 0],
            [-1, 2, -1],
            [0, -1, 2]]  # type: List[List[Union[int, float]]]

    d3_3i = [[0.75, 0.5, 0.25],
             [0.5, 1, 0.5],
             [0.25, 0.5, 0.75]]  # type: List[List[Union[int, float]]]

    datas = (dz5_3, dz3_5,
             di1, di5,
             d5_3, d5_3t, d3_5, d3_5t,
             d2_2, d2_2i, d3_3, d3_3i)  # type: Tuple[List[List[Union[int, float]]], ...]  # noqa

    # Matrix(), shape()
    for data in datas:
        m = numeric.Matrix(data)
        if m.shape() != (len(data), len(data[0])):
            nb_errors += 1
            print('error: constructor size: %s' % data)
        if m_to_l(m) != data:
            nb_errors += 1
            print('error: constructor value: %s' % data)

    # indentity()
    mi1 = numeric.identity(1)
    if mi1.shape() != (1, 1):
        nb_errors += 1
        print('error: identity size')

    if m_to_l(mi1) != di1:
        nb_errors += 1
        print('error: identity value')

    mi5 = numeric.identity(5)
    if mi5.shape() != (5, 5):
        nb_errors += 1
        print('error: identity size')

    if m_to_l(mi5) != di5:
        nb_errors += 1
        print('error: identity value')

    # []
    for data in datas:
        m = numeric.Matrix(data)
        for i, row in enumerate(data):
            for j in range(len(data[0])):
                if m[i, j] != row[j]:
                    nb_errors += 1
                    print('error: [%i, %i]: %s' % (i, j, data))

    # set []
    for data in datas:
        m = numeric.Matrix(data)
        m2 = numeric.Matrix(data)  # pylint: disable=invalid-name
        for i in range(len(data)):
            for j in range(len(data[0])):
                m2[i, j] = 666
                if not isinstance(m2[i, j], float) or (m2[i, j] != 666):
                    nb_errors += 1
                    print('error: [%i, %i] = 666: %s' % (i, j, data))
                    print(m2)

                m2[i, j] = m[i, j]
                if not m_eq(m, m2):
                    nb_errors += 1
                    print('error: [%i, %i] = old: %s' % (i, j, data))
                    print(m2)

    # copy()
    for data in datas:
        m = numeric.Matrix(data)
        m2 = m.copy()  # pylint: disable=invalid-name

        if not m_eq(m, m2):
            nb_errors += 1
            print('error: [%i, %i] = old: %s' % (i, j, data))
            print(m)
            print(m2)

        m2[0, 0] = 666
        if m_eq(m, m2) or (m[0, 0] == 666):
            nb_errors += 1
            print('error: [%i, %i] = old: %s' % (i, j, data))
            print(m)
            print(m2)

    # getrow()
    for data in datas:
        m = numeric.Matrix(data)

        for i, good_row in enumerate(data):
            row = m_to_l(m.getrow(i))[0]

            if len(row) != len(data[0]):
                nb_errors += 1
                print('error: getrow size %i %s %s' % (i, row, good_row))

            if row != good_row:
                nb_errors += 1
                print('error: getrow %i %s %s' % (i, row, good_row))

            for j in range(len(data[0])):
                if row[j] != good_row[j]:
                    nb_errors += 1
                    print('error: getrow != [%i, %i]' % (i, j))

    # getcol()
    for data in datas:
        m = numeric.Matrix(data)

        for j in range(len(data[0])):
            col = m_to_l(m.getcol(j))[0]
            if len(col) != len(data):
                nb_errors += 1
                print('error: getcol size %i %s %s' % (i, col, data))

            for i, row in enumerate(data):
                if col[i] != row[j]:
                    nb_errors += 1
                    print('error: getcol != [%i, %i]' % (i, j))

    # scale(), +, -
    # (in CodeSkulptor3 method scale() doesn't exist
    #  and * is the operator to multiply by a scalar)
    for data in datas:
        m = numeric.Matrix(data)
        adds = numeric.Matrix(data)
        if codeskulptor_lib.codeskulptor_version() == 3:
            subs = numeric.Matrix(data) * -1
        else:
            subs = numeric.Matrix(data).scale(-1)
        for k in range(1, 10):
            if codeskulptor_lib.codeskulptor_version() == 3:
                ms = m * k  # pylint: disable=invalid-name
            else:
                ms = m.scale(k)  # pylint: disable=invalid-name
            if not m_eq(ms, adds):
                nb_errors += 1
                print('error: scale != +: %i %s' % (k, data))
                print(ms)
                print(adds)
            adds = adds + m

            if codeskulptor_lib.codeskulptor_version() == 3:
                ms = m * -k  # pylint: disable=invalid-name
            else:
                ms = m.scale(-k)  # pylint: disable=invalid-name
            if not m_eq(ms, subs):
                nb_errors += 1
                print('error: scale != -: %i %s' % (k, data))
                print(ms)
                print(subs)
            subs = subs - m

    if codeskulptor_lib.codeskulptor_version() != 3:
        # *
        # (in CodeSkulptor3 * is the operator to multiply by a scalar
        # add @ the operator to multiply two matrices)
        m = numeric.Matrix(d5_3) * numeric.Matrix(d3_5)
        if m_to_l(m) != [[25, -28, 31, -34, 37],
                         [-70, 82, -94, 106, -118],
                         [115, -136, 157, -178, 199],
                         [-160, 190, -220, 250, -280],
                         [205, -244, 283, -322, 361]]:
            nb_errors += 1
            print('error: (5, 3) * (3, 5)')
            print(m)

        m = numeric.Matrix(d3_5) * numeric.Matrix(d5_3)
        if m_to_l(m) != [[90, -100, 110],
                         [-240, 275, -310],
                         [390, -450, 510]]:
            nb_errors += 1
            print('error: (3, 5) * (5, 3)')
            print(m)

        for data in datas:
            m = numeric.Matrix(data)
            m2 = m * numeric.identity(len(data[0]))  # pylint: disable=invalid-name  # noqa
            if not m_eq(m, m2):
                nb_errors += 1
                print('error: *: %s' % data)
                print(m2)

            m2 = numeric.identity(len(data)) * m  # pylint: disable=invalid-name  # noqa
            if not m_eq(m, m2):
                nb_errors += 1
                print('error: *: %s' % data)
                print(m2)

        a = numeric.Matrix(d2_2)
        b = numeric.Matrix(d2_2i)
        if not m_eq(a * b, numeric.identity(2)):
            nb_errors += 1
            print('error: a * a^(-1)')
            print(a * b)
        if not m_eq(b * a, numeric.identity(2)):
            nb_errors += 1
            print('error: a^(-1) * a')
            print(b * a)

        a = numeric.Matrix(d3_3)
        b = numeric.Matrix(d3_3i)
        if not m_eq(a * b, numeric.identity(3)):
            nb_errors += 1
            print('error: a * a^(-1)')
            print(a * b)
        if not m_eq(b * a, numeric.identity(3)):
            nb_errors += 1
            print('error: a^(-1) * a')
            print(b * a)

    # summation()
    for k in range(1, 10):
        m = numeric.identity(k)
        if m.summation() != k:
            nb_errors += 1
            print('error: sum %i %f' % (k, m.summation()))

    m = numeric.Matrix(dz5_3)
    if m.summation() != 0:
        nb_errors += 1
        print('error: sum %f' % m.summation())

    m = numeric.Matrix(d5_3)
    if m.summation() != 7:
        nb_errors += 1
        print('error: sum %f' % m.summation())

    m = numeric.Matrix(d3_5)
    if m.summation() != 7:
        nb_errors += 1
        print('error: sum %f' % m.summation())

    # abs()
    m = numeric.Matrix(dz5_3).abs()
    if not m_eq(m, numeric.Matrix(dz5_3)):
        nb_errors += 1
        print('error: abs(0)')
        print(m)

    for k in range(1, 10):
        m = numeric.identity(k).abs()
        if not m_eq(m, numeric.identity(k)):
            print('error: abs(identity(%i))' % k)
            print(m)

    m = numeric.Matrix(d5_3).abs()
    if m.summation() != 105:
        nb_errors += 1
        print('error: abs')
        print(m)

    m = numeric.Matrix(d3_5).abs()
    if m.summation() != 105:
        nb_errors += 1
        print('error: abs')
        print(m)

    # transpose()
    m = numeric.Matrix(dz5_3).transpose()
    if not m_eq(m, numeric.Matrix(dz3_5)):
        nb_errors += 1
        print('error: transpose(0)')
        print(m)

    for k in range(1, 10):
        m = numeric.identity(k).transpose()
        if not m_eq(m, numeric.identity(k)):
            print('error: transpose(identity(%i))' % k)
            print(m)

    m = numeric.Matrix(d5_3).transpose()
    if not m_eq(m, numeric.Matrix(d5_3t)):
        nb_errors += 1
        print('error: transpose')
        print(numeric.Matrix(d5_3))
        print(m)

    m = numeric.Matrix(d3_5).transpose()
    if not m_eq(m, numeric.Matrix(d3_5t)):
        nb_errors += 1
        print('error: transpose')
        print(numeric.Matrix(d3_5))
        print(m)

    # inverse()
    for k in range(1, 10):
        m = numeric.identity(k).inverse()
        if not m_eq(m, numeric.identity(k)):
            print('error: inverse(identity(%i))' % k)
            print(m)

        if codeskulptor_lib.codeskulptor_version() == 3:
            m = numeric.identity(k) * 5
            m = m.inverse()
            if not m_eq(m, numeric.identity(k) * (1.0 / 5)):
                print('error: inverse(identity(%i)*5)' % k)
                print(m)
        else:
            m = numeric.identity(k).scale(5).inverse()
            if not m_eq(m, numeric.identity(k).scale(1.0 / 5)):
                print('error: inverse(identity(%i)*5)' % k)
                print(m)

        m = numeric.identity(k)
        m[0, 0] = 0
        try:
            m = m.inverse()
            print('error: not inversible first: %i' % k)
            print(m)
        except ValueError:
            pass

        m = numeric.identity(k)
        m[k - 1, k - 1] = 0
        try:
            m = m.inverse()
            print('error: not inversible last: %i' % k)
            print(m)
        except ValueError:
            pass

    mi = numeric.Matrix(d2_2).inverse()  # pylint: disable=invalid-name
    if not m_eq(mi, numeric.Matrix(d2_2i), False):
        print('error: inverse 1')
        print(mi)
        print(numeric.Matrix(d2_2i))

    mi = numeric.Matrix(d2_2i).inverse()  # pylint: disable=invalid-name
    if not m_eq(mi, numeric.Matrix(d2_2), False):
        print('error: inverse 2')
        print(mi)
        print(numeric.Matrix(d2_2))

    # Result
    if nb_errors == 0:
        if not SIMPLEGUICS2PYGAME or (len(argv) != 2):
            print('Ok')
    else:
        print('\n%i errors founded' % nb_errors)

        exit(nb_errors)  # pylint: disable=consider-using-sys-exit


if __name__ == '__main__':
    main()
