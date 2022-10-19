#include <stdio.h>
#include <math.h>
#include "binomialOptions_common.h"
#include "realtype.h"

///////////////////////////////////////////////////////////////////////////////
// Polynomial approximation of cumulative normal distribution function
///////////////////////////////////////////////////////////////////////////////
static real CND(real d)
{
    const real A1 = (real)0.31938153;
    const real A2 = (real)-0.356563782;
    const real A3 = (real)1.781477937;
    const real A4 = (real)-1.821255978;
    const real A5 = (real)1.330274429;
    const real RSQRT2PI = (real)0.39894228040143267793994605993438;

    real K = (real)(1.0 / (1.0 + 0.2316419 * (real)fabs(d)));

    real cnd = (real)RSQRT2PI * (real)exp(-0.5 * d * d) * (K * (A1 + K * (A2 + K * (A3 + K * (A4 + K * A5)))));

    if (d > 0)
    {
        cnd = (real)1.0 - cnd;
    }

    return cnd;
}

extern "C" void BlackScholesCall(real & callResult, TOptionData optionData)
{
    real S = optionData.S;
    real X = optionData.X;
    real T = optionData.T;
    real R = optionData.R;
    real V = optionData.V;

    real sqrtT = (real)sqrt(T);
    real d1 = (real)(log(S / X) + (R + (real)0.5 * V * V) * T) / (V * sqrtT);
    real d2 = d1 - V * sqrtT;
    real CNDD1 = CND(d1);
    real CNDD2 = CND(d2);

    // Calculate Call and Put simultaneously
    real expRT = (real)exp(-R * T);
    callResult = (real)(S * CNDD1 - X * expRT * CNDD2);
}

////////////////////////////////////////////////////////////////////////////////
// Process an array of OptN options on CPU
// Note that CPU code is for correctness testing only and not for benchmarking.
////////////////////////////////////////////////////////////////////////////////
static real expiryCallValue(real S, real X, real vDt, int i)
{
    real d = S * (real)exp(vDt * (real)(2 * i - NUM_STEPS)) - X;
    return (d > (real)0) ? d : (real)0;
}

extern "C" void binomialOptionsCPU(real & callResult, TOptionData optionData)
{
    static real Call[NUM_STEPS + 1];

    const real S = optionData.S;
    const real X = optionData.X;
    const real T = optionData.T;
    const real R = optionData.R;
    const real V = optionData.V;

    const real dt = T / (real)NUM_STEPS;
    const real vDt = (real)V * (real)sqrt(dt);
    const real rDt = R * dt;
    // Per-step interest and discount factors
    const real If = (real)exp(rDt);
    const real Df = (real)exp(-rDt);
    // Values and pseudoprobabilities of upward and downward moves
    const real u = (real)exp(vDt);
    const real d = (real)exp(-vDt);
    const real pu = (If - d) / (u - d);
    const real pd = (real)1.0 - pu;
    const real puByDf = pu * Df;
    const real pdByDf = pd * Df;

    ///////////////////////////////////////////////////////////////////////
    // Compute values at expiration date:
    // call option value at period end is V(T) = S(T) - X
    // if S(T) is greater than X, or zero otherwise.
    // The computation is similar for put options.
    ///////////////////////////////////////////////////////////////////////
    for (int i = 0; i <= NUM_STEPS; i++)
    {
        Call[i] = expiryCallValue(S, X, vDt, i);
    }

    ////////////////////////////////////////////////////////////////////////
    // Walk backwards up binomial tree
    ////////////////////////////////////////////////////////////////////////
    for (int i = NUM_STEPS; i > 0; i--)
    {
        for (int j = 0; j <= i - 1; j++)
        {
            Call[j] = puByDf * Call[j + 1] + pdByDf * Call[j];
        }
    }

    callResult = (real)Call[0];
}
