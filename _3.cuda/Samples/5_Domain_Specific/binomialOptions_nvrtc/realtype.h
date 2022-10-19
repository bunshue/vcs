#ifndef REALTYPE_H
#define REALTYPE_H

// To use double precision uncomment the macro DOUBLE_PRECISION below, default is single precision.
//#define DOUBLE_PRECISION

#ifndef DOUBLE_PRECISION
typedef float real;
#else
typedef double real;
#endif

#endif
