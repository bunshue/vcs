#pragma once

#ifndef _RENDERCHECK_D3D9_H_
#define _RENDERCHECK_D3D9_H_

#include <assert.h>
#include <d3d9.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

class CheckRenderD3D9 {
public:
	CheckRenderD3D9() {}

	static HRESULT BackbufferToPPM(IDirect3DDevice9* pDevice, const char* zFileName);
	static HRESULT SurfaceToPPM(IDirect3DDevice9* pDevice, IDirect3DSurface9* pSurface, const char* zFileName);

	static bool PPMvsPPM(const char* src_file, const char* ref_file, const char* exec_path, const float epsilon, const float threshold = 0.0f);
};

#endif