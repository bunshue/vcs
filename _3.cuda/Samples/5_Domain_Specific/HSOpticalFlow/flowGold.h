#ifndef FLOW_GOLD_H
#define FLOW_GOLD_H

void ComputeFlowGold(
    const float* I0,  // source frame
    const float* I1,  // tracked frame
    int width,        // frame width
    int height,       // frame height
    int stride,       // row access stride
    float alpha,      // smoothness coefficient
    int nLevels,      // number of levels in pyramid
    int nWarpIters,   // number of warping iterations per pyramid level
    int nIters,       // number of solver iterations (for linear system)
    float* u,         // output horizontal flow
    float* v);        // output vertical flow

#endif
