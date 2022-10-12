#ifndef _FDTD3D_H_
#define _FDTD3D_H_

// The values are set to give reasonable runtimes, they can
// be changed but note that running very large dimensions can
// take a very long time and you should avoid running on your
// primary display in this case.
#define k_dim_min 96
#define k_dim_max 376
#define k_dim_qa 248

// Note that the radius is defined here as exactly 4 since the
// kernel code uses a constant. If you want a different radius
// you must change the kernel accordingly.
#define k_radius_min 4
#define k_radius_max 4
#define k_radius_default 4

// The values are set to give reasonable runtimes, they can
// be changed but note that running a very large number of
// timesteps can take a very long time and you should avoid
// running on your primary display in this case.
#define k_timesteps_min 1
#define k_timesteps_max 10
#define k_timesteps_default 5

#endif
