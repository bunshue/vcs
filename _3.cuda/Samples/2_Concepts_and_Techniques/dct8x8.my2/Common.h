/*
* \file Common.h
* \brief Common includes header.
*
* This file contains includes of all libraries used by the project.
*/

#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <cuda_runtime.h>
#include <helper_cuda.h>  // helper functions for CUDA timing and initialization
#include <helper_functions.h>  // helper functions for timing, string parsing

/**
*  The dimension of pixels block
*/
#define BLOCK_SIZE 8

/**
*  Square of dimension of pixels block
*/
#define BLOCK_SIZE2 64

/**
*  log_2{BLOCK_SIZE), used for quick multiplication or division by the
*  pixels block dimension via shifting
*/
#define BLOCK_SIZE_LOG2 3

/**
*  log_2{BLOCK_SIZE*BLOCK_SIZE), used for quick multiplication or division by
*  the square of pixels block via shifting
*/
#define BLOCK_SIZE2_LOG2 6

/**
*  This macro states that __mul24 operation is performed faster that traditional
*  multiplication for two integers on CUDA. Please undefine if it appears to be
*  wrong on your system
*/
#define __MUL24_FASTER_THAN_ASTERIX

/**
*  Wrapper to the fastest integer multiplication function on CUDA
*/
#ifdef __MUL24_FASTER_THAN_ASTERIX
#define FMUL(x, y) (__mul24(x, y))
#else
#define FMUL(x, y) ((x) * (y))
#endif

/**
*  This macro allows using aligned memory management
*/
//#define __ALLOW_ALIGNED_MEMORY_MANAGEMENT
