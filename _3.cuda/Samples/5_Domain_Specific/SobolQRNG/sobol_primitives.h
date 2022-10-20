/*
 * Sobol Quasi-random Number Generator example
 *
 * Based on CUDA code submitted by Mike Giles, Oxford University, United Kingdom
 * http://people.maths.ox.ac.uk/~gilesm/
 *
 * and C code developed by Stephen Joe, University of Waikato, New Zealand
 * and Frances Kuo, University of New South Wales, Australia
 * http://web.maths.unsw.edu.au/~fkuo/sobol/
 *
 * For theoretical background see:
 *
 * P. Bratley and B.L. Fox.
 * Implementing Sobol's quasirandom sequence generator
 * http://portal.acm.org/citation.cfm?id=42288
 * ACM Trans. on Math. Software, 14(1):88-100, 1988
 *
 * S. Joe and F. Kuo.
 * Remark on algorithm 659: implementing Sobol's quasirandom sequence generator.
 * http://portal.acm.org/citation.cfm?id=641879
 * ACM Trans. on Math. Software, 29(1):49-57, 2003
 */

#ifndef SOBOL_PRIMITIVES_H
#define SOBOL_PRIMITIVES_H

#define max_m 17

 // Each primitive is stored as a struct where
 //  dimension is the dimension number of the polynomial (unused)
 //  degree is the degree of the polynomial
 //  a is a binary word representing the coefficients
 //  m is the array of m values
struct primitive {
	unsigned int dimension;
	unsigned int degree;
	unsigned int a;
	unsigned int m[max_m];
};

extern const struct primitive sobol_primitives[];

#endif
