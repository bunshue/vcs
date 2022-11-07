#ifndef PARTICLES_KERNEL_H
#define PARTICLES_KERNEL_H

#include "vector_types.h"
typedef unsigned int uint;

// simulation parameters
struct SimParams {
	float3 colliderPos;
	float colliderRadius;

	float3 gravity;
	float globalDamping;
	float particleRadius;

	uint3 gridSize;
	uint numCells;
	float3 worldOrigin;
	float3 cellSize;

	uint numBodies;
	uint maxParticlesPerCell;

	float spring;
	float damping;
	float shear;
	float attraction;
	float boundaryDamping;
};

#endif
