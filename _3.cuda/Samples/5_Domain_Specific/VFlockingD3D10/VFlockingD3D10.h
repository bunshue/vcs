#ifndef VFLOCKING_D3D10_H
#define VFLOCKING_D3D10_H

#pragma once

// simulation parameters
struct Params {
	float alpha;
	float upwashX;
	float upwashY;
	float wingspan;
	float dX;
	float dY;
	float epsilon;
	float lambda;  // -0.1073f * wingspan ;
};

#endif
