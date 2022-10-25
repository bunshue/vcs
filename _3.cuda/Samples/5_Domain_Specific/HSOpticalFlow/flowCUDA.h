#ifndef FLOW_CUDA_H
#define FLOW_CUDA_H

void ComputeFlowCUDA(
    const float* I0,   // source frame
    const float* I1,   // tracked frame
    int width,         // frame width
    int height,        // frame height
    int stride,        // row access stride
    float alpha,       // smoothness coefficient
    int nLevels,       // number of levels in pyramid
    int nWarpIters,    // number of warping iterations per pyramid level
    int nSolverIters,  // number of solver iterations (for linear system)
    float* u,          // output horizontal flow
    float* v);         // output vertical flow
#endif
