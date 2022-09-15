#include <curand.h>
#include <string>

// RNGs
class RNG
{
public:
    enum RngType { Pseudo, Quasi, ScrambledQuasi };
    RNG(unsigned long prngSeed, unsigned int qrngDimensions, unsigned int nSamples);
    virtual ~RNG();

    float getNextU01(void);
    void getInfoString(std::string& msg);
    void selectRng(RngType type);
    void resetSeed(void);
    void resetDimensions(void);
    void incrementDimensions(void);

private:
    // Generators
    curandGenerator_t* m_pCurrent;
    curandGenerator_t m_prng;
    curandGenerator_t m_qrng;
    curandGenerator_t m_sqrng;

    // Parameters
    unsigned long m_prngSeed;
    unsigned int  m_qrngDimensions;

    // Batches
    const unsigned int m_nSamplesBatchTarget;
    unsigned int       m_nSamplesBatchActual;
    unsigned int       m_nSamplesRemaining;
    void generateBatch(void);

    // Helpers
    void updateDimensions(void);
    void setBatchSize(void);

    // Buffers
    float* m_h_samples;
    float* m_d_samples;

    static const unsigned int s_maxQrngDimensions;
};
