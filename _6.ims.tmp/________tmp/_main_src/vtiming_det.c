
// *****************************************************
// Dependencies
// *****************************************************
#include "vtiming_det.h"

// *****************************************************
// Public functions
// *****************************************************
void vtiming_det_run
(
	XVtc* p_vtd_inst
)
{
	XVtc_EnableDetector(p_vtd_inst);
	XVtc_RegUpdateEnable(p_vtd_inst);
}

void vtiming_det_stop
(
	XVtc* p_vtd_inst
)
{
	XVtc_Reset(p_vtd_inst);
}
