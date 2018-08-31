
// *****************************************************
// Dependencies
// *****************************************************
#include "psusb0.h"
#include "periphs.h"
#include "sleep.h"
#include "ulpi.h"

//volatile int TotalReceivedCount = 0;
//volatile int TotalSentCount = 0;
//int TotalErrorCount = 0;

//static u8 SendBuffer[PSUSB0_BUFFER_SIZE];	/* Buffer for Transmitting Data */
//static u8 RecvBuffer[PSUSB0_BUFFER_SIZE];	/* Buffer for Receiving Data */

// *****************************************************
// Private functions
// *****************************************************

/****************************************************************************
psuart0 interrupt handler
******************************************************************************/
void psusb0_IntrHandler(void *CallBackRef)
{
	uint32_t n, IrqMask;
	//xil_printf("\r\nEnter ISR\r\n");
	XUsbPs *psusb0 = (XUsbPs *)CallBackRef;
	IrqMask = XUsbPs_ReadReg(periphs_inst.p_psusb0_inst->Config.BaseAddress, XUSBPS_ISR_OFFSET);
	xil_printf("irq: %x\r\n", IrqMask);
	// Handle ULPI
	if(IrqMask & XUSBPS_IXR_ULPI_MASK) {
		// ULPI Interrupt Triggered
n = XUsbPs_ReadReg(periphs_inst.p_psusb0_inst->Config.BaseAddress, XUSBPS_ISR_OFFSET);
xil_printf("ulpi:%x\r\n",n);
	}

	// Handle USB Related Interrupts
	tusb_isr(0);
	//n = XUsbPs_ReadReg(periphs_inst.p_psusb0_inst->Config.BaseAddress, XUSBPS_ISR_OFFSET);
	//xil_printf("exit ISR\r\n",n);
	//Xil_DCacheFlush();

}

void psusb0_hal_interrupt_enable(uint8_t coreid)
{
	if(coreid != 0)
		return;
	xil_printf("hal_interrupt enable\r\n");

	// Enable the psusb0 interrupt
	XScuGic_Enable(periphs_inst.p_scugic_inst, XPAR_XUSBPS_0_INTR);
}

void psusb0_hal_interrupt_disable(uint8_t coreid)
{
	if(coreid != 0)
		return;
	xil_printf("hal_interrupt disable\r\n");
	XScuGic_Disable(periphs_inst.p_scugic_inst, XPAR_XUSBPS_0_INTR);
}

int psusb0_hal_controller_reset(uint8_t coreid)
{
	int ret;
	if(coreid != 0)
		return XST_FAILURE;

	xil_printf("psusb0_hal_controller_reset\r\n");
	ret = XUsbPs_Reset(periphs_inst.p_psusb0_inst);
	if(ret) {
		xil_printf("psusb0 reset failure\r\n");
		return XST_FAILURE;
	}
	xil_printf("psusb0 reset success\r\n");
	return XST_SUCCESS;
}

int32_t ulpi_init()
{
	int i, ret; //,vid, pid;
	//u32 ulpi_id = 0;

	xil_printf("ulpi_init()\r\n");
//	for (i = 0; i < 4; i++) {
//		ret = usb_phy_io_read(phy, ULPI_PRODUCT_ID_HIGH - i);
//		if (ret < 0)
//			return ret;
//		ulpi_id = (ulpi_id << 8) | ret;
//	}
//	vid = ulpi_id & 0xffff;
//	pid = ulpi_id >> 16;
//
//	pr_info("ULPI transceiver vendor/product ID 0x%04x/0x%04x\n", vid, pid);
//
//	for (i = 0; i < ARRAY_SIZE(ulpi_ids); i++) {
//		if (ulpi_ids[i].id == ULPI_ID(vid, pid)) {
//			pr_info("Found %s ULPI transceiver.\n",
//				ulpi_ids[i].name);
//			break;
//		}
//	}

	ret = ulpi_check_integrity();
	if (ret)
		return ret;

	//return XST_SUCCESS;
	return ulpi_set_flags();
}


//int32_t ulpi_set_host(struct usb_otg *otg, struct usb_bus *host)
//{
//	struct usb_phy *phy = otg->usb_phy;
//	unsigned int flags = usb_phy_io_read(phy, ULPI_IFC_CTRL);
//
//	if (!host) {
//		otg->host = NULL;
//		return 0;
//	}
//
//	otg->host = host;
//
//	flags &= ~(ULPI_IFC_CTRL_6_PIN_SERIAL_MODE |
//		   ULPI_IFC_CTRL_3_PIN_SERIAL_MODE |
//		   ULPI_IFC_CTRL_CARKITMODE);
//
//	if (phy->flags & ULPI_IC_6PIN_SERIAL)
//		flags |= ULPI_IFC_CTRL_6_PIN_SERIAL_MODE;
//	else if (phy->flags & ULPI_IC_3PIN_SERIAL)
//		flags |= ULPI_IFC_CTRL_3_PIN_SERIAL_MODE;
//	else if (phy->flags & ULPI_IC_CARKIT)
//		flags |= ULPI_IFC_CTRL_CARKITMODE;
//
//	return usb_phy_io_write(phy, flags, ULPI_IFC_CTRL);
//}







int32_t ulpi_set_vbus(int32_t on)
{
	uint8_t flags;

	xil_printf("ulpl_set_vbus\r\n", flags);

	flags = ulpi_ReadReg(ULPI_OTG_CTRL);

	xil_printf("set_vbus flags initial: %x\r\n", flags);

	flags &= ~(ULPI_OTG_DRVVBUS | ULPI_OTG_DRVVBUS_EXT); // Reset DRVVBUS bit positions

	if (on) {
			flags |= ULPI_OTG_DRVVBUS;
//			flags |= ULPI_OTG_DRVVBUS_EXT;
	}

	return ulpi_WriteReg(flags, ULPI_OTG_CTRL);
}

int32_t ulpi_check_integrity()
{
	int ret, i;
	unsigned int val = 0x55;

	for (i = 0; i < 2; i++) {
		ret = ulpi_WriteReg(val, ULPI_SCRATCH);
		if (ret != 0) {
			return ret;
		}

		ret = ulpi_ReadReg(ULPI_SCRATCH);

		if (ret != val) {
			xil_printf("ULPI integrity check: failed!");
			return XST_FAILURE;
		}
		val = val << 1;
	}

	xil_printf("ULPI integrity check: passed.\r\n");

	return XST_SUCCESS;
}

int32_t ulpi_set_otg_flags(void)
{
	unsigned int flags = ULPI_OTG_DP_PULLDOWN | ULPI_OTG_DM_PULLDOWN;

	xil_printf("ulpi_set_otg_flags()\r\n");
	// Disable Pull up
//	if (phy->flags & ULPI_OTG_ID_PULLUP)
//		flags |= ULPI_OTG_CTRL_ID_PULLUP;

	/*
	 * ULPI Specification rev.1.1 default
	 * for Dp/DmPulldown is enabled.
	 */
//	if (phy->flags & ULPI_OTG_DP_PULLDOWN_DIS)
//		flags &= ~ULPI_OTG_CTRL_DP_PULLDOWN;
//
//	if (phy->flags & ULPI_OTG_DM_PULLDOWN_DIS)
//		flags &= ~ULPI_OTG_CTRL_DM_PULLDOWN;
//
//	if (phy->flags & ULPI_OTG_EXTVBUSIND)
//		flags |= ULPI_OTG_CTRL_EXTVBUSIND;
	return ulpi_WriteReg(flags, ULPI_OTG_CTRL);
}

int32_t ulpi_set_fc_flags(void)
{
	unsigned int flags = 0;

	xil_printf("ulpi_set_fc_flags()\r\n");

	/*
	 * ULPI Specification rev.1.1 default
	 * for XcvrSelect is Full Speed.
	 */
//	if (phy->flags & ULPI_FC_HS)
//		flags |= ULPI_FUNC_CTRL_HIGH_SPEED;
//	else if (phy->flags & ULPI_FC_LS)
//		flags |= ULPI_FUNC_CTRL_LOW_SPEED;
//	else if (phy->flags & ULPI_FC_FS4LS)
//		flags |= ULPI_FUNC_CTRL_FS4LS;
//	else
		//flags |= ULPI_FC_XCVRSEL_FS; // Enable Full Speed by default
		flags |= 0x01; // Enable Full Speed by default

	//if (phy->flags & ULPI_FC_TERMSEL)
		flags |= ULPI_FC_TERMSEL; // Termsel is enabled for full speed host mode

	/*
	 * ULPI Specification rev.1.1 default
	 * for OpMode is Normal Operation.
	 */
//	if (phy->flags & ULPI_FC_OP_NODRV)
//		flags |= ULPI_FUNC_CTRL_OPMODE_NONDRIVING;
//	else if (phy->flags & ULPI_FC_OP_DIS_NRZI)
//		flags |= ULPI_FUNC_CTRL_OPMODE_DISABLE_NRZI;
//	else if (phy->flags & ULPI_FC_OP_NSYNC_NEOP)
//		flags |= ULPI_FUNC_CTRL_OPMODE_NOSYNC_NOEOP;
//	else
		// flags |= ULPI_FC_OPMODE_NORMAL; // Normal Mode by default

	/*
	 * ULPI Specification rev.1.1 default
	 * for SuspendM is Powered.
	 */
	flags |= ULPI_FC_SUSPENDM;

	return ulpi_WriteReg(flags, ULPI_FC_CTRL);
}


int32_t ulpi_set_ic_flags(void)
{
	unsigned int flags = ULPI_IFC_AUTORESUME; // Enable Auto-Resume for HOST Mode

	xil_printf("ulpi_set_ic_flags()\r\n");
//	if (phy->flags & ULPI_IC_AUTORESUME)
//		flags |= ULPI_IFC_CTRL_AUTORESUME;
//
//	if (phy->flags & ULPI_IC_EXTVBUS_INDINV)
//		flags |= ULPI_IFC_CTRL_EXTERNAL_VBUS;
//
//	if (phy->flags & ULPI_IC_IND_PASSTHRU)
//		flags |= ULPI_IFC_CTRL_PASSTHRU;
//
//	if (phy->flags & ULPI_IC_PROTECT_DIS)
//		flags |= ULPI_IFC_CTRL_PROTECT_IFC_DISABLE;
//

	return ulpi_WriteReg(flags, ULPI_IFC_CTRL);
}

int32_t ulpi_set_flags()
{
	int ret = 0;

	xil_printf("ulpi_set_flags()\r\n");
	ret = ulpi_set_otg_flags();
	if (ret)
		return ret;

	ret = ulpi_set_ic_flags();
	if (ret)
		return ret;

	return ulpi_set_fc_flags();
}

uint8_t ulpi_ReadReg(uint8_t reg)
{

	uint32_t data = 0;
	uint32_t i = 1000;

	//read = XUsbPs_ReadReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET);
	//xil_printf("read: %x\r\n", read);

	// Set up flags Operation
	data |= (1 << XUSBPS_ULPIVIEW_RUN_SHIFT) | (reg << XUSBPS_ULPIVIEW_ADDR_SHIFT);

	// Start Read operation and wait
	XUsbPs_WriteReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET, data);
	while(i > 0)
	{
		data = XUsbPs_ReadReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET); // Read back register
		if(data & XUSBPS_ULPIVIEW_RUN_MASK)
		{
//			if(i == 0) // Time out
//			{
//				xil_printf("ULPI Read timeout!\r\n");
//				return XST_FAILURE;
//			}
			continue;
		}
		else
		{
			break;
		}
		i--;
	}
	xil_printf("ulpi_read_data - reg: %x, data: %x\r\n", reg, (data >> XUSBPS_ULPIVIEW_DATRD_SHIFT) & 0xff);
	//xil_printf("i: %d\r\n", i);

	return (data >> XUSBPS_ULPIVIEW_DATRD_SHIFT) & 0xff;
}

int32_t ulpi_WriteReg(uint8_t flags, uint8_t reg)
{

	uint32_t data = 0;
	//uint32_t read = 0;
	uint32_t i = 1000;

	//read = XUsbPs_ReadReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET);
	//xil_printf("read: %x\r\n", read);

	// Set up flags Operation
	data |= (1 << XUSBPS_ULPIVIEW_RUN_SHIFT) | (1 << XUSBPS_ULPIVIEW_RW_SHIFT)
				| (reg << XUSBPS_ULPIVIEW_ADDR_SHIFT) | (flags);

	// Start Write operation and wait
	XUsbPs_WriteReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET, data);

	//data = XUsbPs_ReadReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET); // Read back register
	//xil_printf("1 data: %x\r\n", data);
	//data = XUsbPs_ReadReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET); // Read back register
	//xil_printf("2 data: %x\r\n", data);
	//data = XUsbPs_ReadReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET); // Read back register
	//xil_printf("3 data: %x\r\n", data);


	while(i > 0)
	{
		data = XUsbPs_ReadReg(XPAR_XUSBPS_0_BASEADDR, XUSBPS_ULPIVIEW_OFFSET); // Read back register
//		xil_printf("1 data: %x\r\n", data);
		if(data & XUSBPS_ULPIVIEW_RUN_MASK)
		{
//			if(i == 0) // Time out
//			{
//				xil_printf("ULPI Read timeout!\r\n");
//				return XST_FAILURE;
//			}
			continue;
		}
		else
		{
			break;
		}
		i--;
	}
	xil_printf("ulpi_write_data - reg: %x, data: %x\r\n", reg, (data >> XUSBPS_ULPIVIEW_DATWR_SHIFT) & 0xff);
	//xil_printf("i: %d\r\n", i);

	return XST_SUCCESS;
}

