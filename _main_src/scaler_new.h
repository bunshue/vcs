
#ifndef _SCALER_NEW_H_
#define _SCALER_NEW_H_

// *****************************************************
// Notes
// *****************************************************
//   - The purpose of this driver is to provide a layer
//     of abstraction over the VPSS v1.0 based scaler
//     drivers. It assumes the caller has allocated and
//     initialized the XVprocSs instance to be used.

// *****************************************************
// Dependencies
// *****************************************************
#include "xvprocss.h"

// *****************************************************
// Function status return values
// *****************************************************
#define SCALER_NEW_SUCCESS        0
#define SCALER_NEW_ERROR_UNKNOWN -1

// *****************************************************
// Public functions
// *****************************************************

// scaler_new_set_input_size() - Set up the new scaler input size. This
//                               function causes a hardware reset to upstream
//                               modules (to avoid partial frame issues).
//   - p_scaler_new_inst_inst - Pointer to object to work on
//   - hsize                  - Horizontal input frame size (pixels per line)
//   - vsize                  - Vertical input frame size (lines per frame)
//   - print_config           - Print VPSS configuration
//   - return                 - Function status return value (see above)
unsigned int scaler_new_set_size
(
	XVprocSs*    p_scaler_new_inst,
	unsigned int in_hsize,
	unsigned int in_vsize,
	unsigned int in_color_format,
	unsigned int out_hsize,
	unsigned int out_vsize,
	unsigned int out_color_format,
	unsigned int print_config
);

// scaler_new_set_input_color_format() - Set up the new scaler input color format. This
//                               function causes a hardware reset to upstream
//                               modules (to avoid partial frame issues).
//   - p_scaler_new_inst_inst - Pointer to object to work on
//   - color_format           - Input frame color format
//   - print_config           - Print VPSS configuration
//   - return                 - Function status return value (see above)
unsigned int scaler_new_set_input_color_format
(
	XVprocSs*    p_scaler_new_inst,
	unsigned int color_format,
	unsigned int print_config
);

// scaler_new_set_output_size() - Set up the new scaler output size. This
//                               function causes a hardware reset to upstream
//                               modules (to avoid partial frame issues).
//   - p_scaler_new_inst_inst - Pointer to object to work on
//   - hsize                  - Horizontal input frame size (pixels per line)
//   - vsize                  - Vertical input frame size (lines per frame)
//   - print_config           - Print VPSS configuration
//   - return                 - Function status return value (see above)
unsigned int scaler_new_set_output_size
(
	XVprocSs*    p_scaler_new_inst,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int print_config
);

#endif // _SCALER_NEW_H_
