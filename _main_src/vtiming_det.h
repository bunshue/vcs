
#ifndef _VTIMING_DET_H_
#define _VTIMING_DET_H_

// *****************************************************
// Notes
// *****************************************************
//   - The purpose of this driver is to provide a layer
//     of abstraction over the Video Timing Controller
//     drivers when it is used in detect-only mode. It
//     assumes the caller has allocated and initialized
//     the XVtc instance to be used.

// *****************************************************
// Dependencies
// *****************************************************
#include "xvtc.h"

// *****************************************************
// Function status return values
// *****************************************************
#define VTIMING_DET_SUCCESS        0
#define VTIMING_DET_ERROR_UNKNOWN -1

// *****************************************************
// Public functions
// *****************************************************

// vtiming_det_run() - Set up and start VTC detector registers and enable.
//   - p_vtd_inst    - Pointer to object to work on
//   - return        - None
void vtiming_det_run
(
	XVtc* p_vtd_inst
);

// vtiming_det_stop() - Stop the VTC detector and reset it. This function
//                      is intended to be called when there will be a
//                      disruption on the incoming frame data. This function
//                      will cause the hardware to hold off partial frames
//                      until vtiming_det_run() is called again which will
//                      allow video to flow again.
//   - p_vtd_inst - Pointer to object to work on
//   - return     - None
void vtiming_det_stop
(
	XVtc* p_vtd_inst
);

#endif // _VTIMING_DET_H_

