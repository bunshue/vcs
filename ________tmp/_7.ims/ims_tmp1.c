

david0829: ../src/gdisp/gdisp_fonts.c:gdispGetFontName(92) ST name : iskpota240 W= 40 H = 39
david0829: ../src/gdisp/gdisp_fonts.c:gdispGetFontName(92) ST name : iskpota232 W= 32 H = 31
david0829: ../src/gdisp/gdisp_fonts.c:gdispGetFontName(92) ST name : iskpota240 W= 40 H = 39
david0829: ../src/gdisp/gdisp_fonts.c:gdispGetFontName(92) ST name : iskpota240 W= 40 H = 39
david0829: ../src/gdisp/gdisp_fonts.c:gdispGetFontName(92) ST name : iskpota240 W= 40 H = 39
david0829: ../src/gdisp/gdisp_fonts.c:gdispGetFontName(92) ST name : iskpota240 W= 40 H = 39



USB Standard Device Descriptor (section 9.6.1, table 9-8)

/* - spec sec 9.3 (USB Device Requests)
 *   - table 9-2 (Format of Setup Data)
 *     - bmRequestType
 *
 * .-------------------------------------------------------.
 * |     D7     | D6 | D5 |     D4 | D3 | D2 | D1 | D0     |
 * |-------------------------------------------------------|
 * | direction  |  type   |           recipient            |
 * '-------------------------------------------------------'
 *
 * - direction: 0 => host to device
 *              1 => device to host
 *
 * - type: 0 => standard
 *         1 => class
 *         2 = vendor
 *         3 = reserved
 *
 * - recipient: 0 => device
 *              1 => interface
 *              2 => endpoint
 *              3 => other
 *              4..31 => reserved
 */
 
 /* - spec sec 9.3.4 (wIndex)
 *   - figure 9-2 (format when specifying an endpoint)
 *
 * .-------------------------------------------------------.
 * |    D7     |     D6 | D5 | D4      | D3 | D2 | D1 | D0 |
 * |-------------------------------------------------------|
 * | direction | reserved (reset to 0) |  endpoint number  |
 *  >-----------------------------------------------------<
 * |      D15 | D14 | D13 | D12 | D11 | D10 | D9 | D8      |
 * |-------------------------------------------------------|
 * |                 reserved (reset to 0)                 |
 * '-------------------------------------------------------'
 *
 * - direction: 0 => out (to device), 1 => in (to host)
 */

data: 12 01 00 02 09 00 01 40
data: 12 01 00 02 09 00 01 40


12
01
00
02

09
00
01
40




bmRequestType=128, bRequest=6, wValue=256, wIndex=0, wLength=8

CMD:
80
06
00
01
00
00
12
00


response
data: 12 01 00 02 09 00 01 40
data: 12 01 00 02 09 00 01 40

12	length of the descriptor
01	
00	usb spec release number
02	usb spec release number

09
00
01
40

david0824 really error = 0x0 addr = 0 len = 12	data: 12 01 00 02 09 00 01 40 E3 05 08 06





attach TD
semaphoirq: 4C089

hcd_isr int_status: 40000
re wait
sema no error: 4367
mutex release

a Keyboard device (address 3) is mounted
Assert at ../class/hid_host.c: hidh_open_subtask: 199: expected 5, actual 0
enumeration_body_subtask()
dongle plugged
all plugged
turn on
update remove picture
irq: 8C489
ulpi:8C489








		carrier		picoZed
USB_OTG_CPEN	JX3之pin70	USB_OTG_CPEN



[aries@ims]# uname
Linux
[aries@ims]# date
一  8月 20 20:27:49 CST 2018
[aries@ims]#
[aries@ims]#
[aries@ims]#
[aries@ims]#
[aries@ims]# history
   1 ll
   2 ifconfig
   3 shutdown -h now
   4 date
  ...
  46 history
[aries@ims]#



ULPI registers

Read ulpi registers
24  04  07  00  40  40  40  18
18  18  27  27  27  1F  1F  1F
1F  1F  1F  04  00  00  AA  AA
AA  00  00  00  00  00  00  00
00  00  00  00  00  00  00  00
00  00  00  00  00  00  00  00
00  00  00  00  FF  00  00  00
00  04  04  04  00  00  00  00



Read ulpi registers
 8002400   8010400   8020700   8030000   8044500   8054500   8064500   8070800   8080800   8090800   80A2700   80B2700   80C2700   80D1F00   80E1F00   80F1F00
 8101F00   8111F00   8121F00   8130400   8140000   8150000   8165500   8175500   8185500   8190000   81A0000   81B0000   81C0000   81D0000   81E0000   81F0000
 8200000   8210000   8220000   8230000   8240000   8250000   8260000   8270000   8280000   8290000   82A0000   82B0000   82C0000   82D0000   82E0000   82F0000
 8300000   8310000   8320000   8330000   834FF00   8350000   8360000   8370000   8380000   8390400   83A0400   83B0400   83C0000   83D0000   83E0000   83F0000



08 固定
00 addr
24 data received
00 固定




xil_printf("david0810: %s:%s(%d) sizeof(ehci_registers_t) = %d\r\n",__FILE__,__func__,__LINE__, sizeof(ehci_registers_t));


重新啟動USB
			case 'w':
				xil_printf("wwwwww\n\r");
				port_connect_status_change_isr(0);
				break;
讀USB暫存器
			case 'q':
				value = Xil_In32((0xF8000000U) + (u32)(0x00000210));
				xil_printf("value = 0x%x\n\r",value);
				break;
讀USB暫存器
			case 'r':
				/*
				xil_printf("reset 3\n\r");
				value = 3;
				Xil_Out32((0xF8000000U) + (u32)(0x00000210), value);
				*/
				  //ehci_registers_t* const regs = get_operational_register(hostid);

				xil_printf("read\n\r");

				  ehci_registers_t* regs = (ehci_registers_t*) (XPAR_XUSBPS_0_BASEADDR+XUSBPS_CMD_OFFSET);

				  xil_printf("value1 = 0x%x\n\r",regs->usb_cmd_bit);
				  xil_printf("value2 = 0x%x\n\r",regs->usb_cmd_bit.run_stop);

				//hal_interrupt_disable(0);
				break;



寫在osal_none.h裡

 void tick_get(void);
 void tick_set(uint32_t tick);


寫在main.c下

void tick_get(void)
{
	xil_printf("t=%d\n\r", g_ms_tick);
}

void tick_set(uint32_t tick)
{
	g_ms_tick = tick;
}




設定字型:
1.	gwinSetDefaultFont(gdispOpenFont("iskpota232"));

2.
	font_t  font1, font2;
	font1 = gdispOpenFont("UI2");
	font2 = gdispOpenFont("DejaVu Sans 48");
	gwinSetDefaultFont(font2);
3.
	font2 = gdispOpenFont("DejaVu Sans 24");
	gwinSetDefaultFont(font2);




int test_gpio(periphs_t*   p_periphs_inst)
{
	XGpioPs *Gpio = p_periphs_inst->p_ps_gpio_inst;

	xil_printf("LED test ST\r\n");

	XGpioPs_WritePin(Gpio, GPIO_LED_1, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_2, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_4, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_5, 0);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

	xil_printf("LED 1\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_1, 1);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

	xil_printf("LED 2\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_1, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_2, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("LED 3\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_2, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 1);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

    xil_printf("LED 4\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_4, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

    xil_printf("LED 5\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_4, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_5, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("LED 3\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_5, 0);
	XGpioPs_WritePin(Gpio, GPIO_LED_3, 1);
	usleep(200000);
    usleep(200000);
	usleep(200000);
    usleep(200000);

	xil_printf("RED LED ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_RED, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("RED LED OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_RED, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);


	xil_printf("GPIO_LED_AUTO OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AUTO, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_CEN ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_CEN, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_CEN OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_CEN, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_AVG ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AVG, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_AVG OFF\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AVG, 0);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

	xil_printf("GPIO_LED_AUTO ON\r\n");
	XGpioPs_WritePin(Gpio, GPIO_LED_AUTO, 1);
	usleep(200000);
	usleep(200000);
    usleep(200000);
    usleep(200000);

    xil_printf("LED test SP\r\n");
    return 0;
}

UART修改
xuartps_hw.c

u8 XUartPs_RecvByte(u32 BaseAddress)
{
	u32 RecievedByte;
	/* Wait until there is data */
	/*
	while (!XUartPs_IsReceiveData(BaseAddress)) {
		;
	}
	*/
	if (!XUartPs_IsReceiveData(BaseAddress))
		return 0;

	RecievedByte = XUartPs_ReadReg(BaseAddress, XUARTPS_FIFO_OFFSET);
	/* Return the byte received */
	return (u8)RecievedByte;
}




scutimer每2ms發一個中斷
void scutimer_IntrHandler(void *CallbackRef)
{
	g_ms_tick++;
}

測試:
	while(1)
	{
	    usleep(200000);
	    usleep(200000);
	    usleep(200000);
	    usleep(200000);
	    usleep(200000);
	    g_ms_tick_old = g_ms_tick;
	    sleep(1);
	    g_ms_tick_diff = g_ms_tick - g_ms_tick_old;
	    usleep(200000);
	    usleep(200000);
	    xil_printf("g_ms_tick_diff = %d\n\r", g_ms_tick_diff);
	    g_ms_tick_diff = 0;
	}


	xil_printf("\n\rg_ms_tick = %d\n\r\n\r", g_ms_tick);




已經有效的程式:

讓timer動起來  需要搭配SCUGIC

int main()
{
	testXScuTimer(&periphs_inst, XPAR_PS7_SCUGIC_0_DEVICE_ID, XPAR_PS7_SCUTIMER_0_DEVICE_ID);
	
	while(1)
	{
		il_printf("\tg_ms_tick = %d\n\r", g_ms_tick);
	    	usleep(200000);usleep(200000);usleep(200000);usleep(200000);usleep(200000);usleep(200000);usleep(200000);
	}
}

void testXScuTimer
(
	periphs_t*   p_periphs_inst,
	unsigned int scugic_device_id,
	unsigned int scutimer_device_id
)
{
	// Local variables
	int              status         = 0;
	XScuGic_Config*  p_scugic_cfg;
	XScuTimer_Config* p_scutimer_cfg;

	p_periphs_inst->p_scugic_inst				= &scugic_inst;
	p_periphs_inst->p_scutimer_inst				= &scutimer_inst;


	xil_printf("\n\r---interrupt controller 0xF8F00100-----------------------------------------\n\r");
	// Initialize the interrupt controller
	p_scugic_cfg = XScuGic_LookupConfig(scugic_device_id);
	if (NULL == p_scugic_cfg)
	{
		xil_printf("ERROR! Failed to find scugic.\n\r");
		return XST_FAILURE;
	}

	status = XScuGic_CfgInitialize(p_periphs_inst->p_scugic_inst, p_scugic_cfg, p_scugic_cfg->CpuBaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize scugic.\n\r");
		return XST_FAILURE;
	}
	xil_printf("david0704: %s:%s(%d) XScuGic base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_scugic_cfg->CpuBaseAddress);

	xil_printf("\n\r---CPU private timer SCUTimer 0xF8F00600-----------------------------------------\n\r");
	// Initialize the CPU private timer
	p_scutimer_cfg = XScuTimer_LookupConfig(scutimer_device_id);	//0
	if (NULL == p_scutimer_cfg) {
		xil_printf("ERROR! Failed to find scutimer.\n\r");
		return XST_FAILURE;
	}

	status = XScuTimer_CfgInitialize(p_periphs_inst->p_scutimer_inst, p_scutimer_cfg, p_scutimer_cfg->BaseAddr);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize scutimer.\n\r");
		return XST_FAILURE;
	}
	xil_printf("david0704: %s:%s(%d) XScuTimer base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_scutimer_cfg->BaseAddr);



	// Connect the interrupt controller interrupt handler to the hardware interrupt handling logic in the processor.
	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_INT,
				(Xil_ExceptionHandler)XScuGic_InterruptHandler,
				p_periphs_inst->p_scugic_inst);

	// SCUTIMER - Connect the device driver handler that will be called when an interrupt for the device occurs
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_SCUTIMER_INTR,
				(Xil_ExceptionHandler)scutimer_IntrHandler, p_periphs_inst->p_scutimer_inst);
	if (status != XST_SUCCESS) {
		xil_printf("failed to connect scutimer\r\n");
		return status;
	}


	// Reset/Stop scutimer
	xil_printf("\n\r\n\rReset/Stop scutimer\n\r");
	xil_printf("david0712: %s:%s(%d) timer\r\n",__FILE__,__func__,__LINE__);
	XScuTimer_Stop(p_periphs_inst->p_scutimer_inst);
	XScuTimer_DisableInterrupt(p_periphs_inst->p_scutimer_inst);
	XScuTimer_ClearInterruptStatus(p_periphs_inst->p_scutimer_inst);

	// Load scutimer values
	XScuTimer_LoadTimer(p_periphs_inst->p_scutimer_inst, COUNTS_PER_MILLI_SECOND);
	XScuTimer_RestartTimer(p_periphs_inst->p_scutimer_inst);
	XScuTimer_SetPrescaler(p_periphs_inst->p_scutimer_inst, 1);
	XScuTimer_EnableAutoReload(p_periphs_inst->p_scutimer_inst);
	XScuTimer_EnableInterrupt(p_periphs_inst->p_scutimer_inst);
	XScuTimer_Start(p_periphs_inst->p_scutimer_inst);

	xil_printf("david0806: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);

	// Enable the scugic interrupt for the scutimer.
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPAR_SCUTIMER_INTR);

	/* Enable System wide interrupts in the Processor. */
	Xil_ExceptionEnable();

	xil_printf("david0724: %s:%s(%d) SP\r\n",__FILE__,__func__,__LINE__);
}


必要的修改:
UART收命令
改成每1秒檢查一次dongle
UART收命令部份另外寫



	




typedef volatile struct {
  union {
    uint32_t usb_cmd                  ; ///< The Command Register indicates the command to be executed by the serial bus host controller. Writing to the register causes a command to be executed
    struct {
      uint32_t run_stop               : 1 ; ///< Default 0b. 1=Run. 0=Stop. When set to a 1, the Host Controller proceeds with execution of the schedule. The Host Controller continues execution as long as this bit is set to a 1. When this bit is set to 0, the Host Controller completes the current and any actively pipelined transactions on the USB and then halts. The Host Controller must halt within 16 micro-frames after software clears the Run bit. The HC Halted bit in the status register indicates when the Host Controller has finished its pending pipelined transactions and has entered the stopped state. Software must not write a one to this field unless the host controller is in the Halted state (i.e. HCHaltedin the USBSTS register is a one). Doing so will yield undefined results.
      uint32_t reset                  : 1 ; ///< his control bit is used by software to reset the host controller. The effects of this on Root Hub registers are similar to a Chip Hardware Reset. When software writes a one to this bit, the Host Controller resets its internal pipelines, timers, counters, state machines, etc. to their initial value. Any transaction currently in progress on USB is immediately terminated. A USB reset is not driven on downstream ports.This bit is set to zero by the Host Controller when the reset process is complete. Software cannot terminate the reset process early by writing a zero to this register. Software should not set this bit to a one when the HCHaltedbit in the USBSTS register is a zero. Attempting to reset an actively running host controller will result in undefined behavior.
      uint32_t framelist_size         : 2 ; ///< This field is R/W only if Programmable Frame List Flagin the HCCPARAMS registers is set to a one. This field specifies the size of the frame list.00b  1024 elements (4096 bytes) Default value 01b  512 elements (2048 bytes) 10b 256 elements (1024 bytes)
      uint32_t periodic_enable        : 1 ; ///< This bit controls whether the host controller skips processing the Periodic Schedule. Values mean: 0b Do not process the Periodic Schedule 1b Use the PERIODICLISTBASE register to access the Periodic Schedule.
      uint32_t async_enable           : 1 ; ///< This bit controls whether the host controller skips processing the Asynchronous Schedule. Values mean: 0b Do not process the Asynchronous Schedule 1b Use the ASYNCLISTADDR register to access the Asynchronous Schedule.
      uint32_t advacne_async          : 1 ; ///< This bit is used as a doorbell by software to tell the host controller to issue an interrupt the next time it advances asynchronous schedule. Software must write a 1 to this bit to ringthe doorbell. When the host controller has evicted all appropriate cached schedule state, it sets the Interrupt on Async Advancestatus bit in the USBSTS register. If the Interrupt on Async Advance Enablebit in the USBINTR register is a one then the host controller will assert an interrupt at the next interrupt threshold. See Section 4.8.2 for operational details. The host controller sets this bit to a zero after it has set the Interrupt on Async Advance status bit in the USBSTS register to a one. Software should not write a one to this bit when the asynchronous schedule is disabled. Doing so will yield undefined results.
      uint32_t light_reset            : 1 ; ///< This control bit is not required. If implemented, it allows the driver to reset the EHCI controller without affecting the state of the ports or the relationship to the companion host controllers. For example, the PORSTC registers should not be reset to their default values and the CF bit setting should not go to zero (retaining port ownership relationships). A host software read of this bit as zero indicates the Light Host Controller Reset has completed and it is safe for host software to re-initialize the host controller. A host software read of this bit as a one indicates the Light Host Controller Reset has not yet completed.
      uint32_t async_park             : 2 ; ///< It contains a count of the number of successive transactions the host controller is allowed to execute from a high-speed queue head on the Asynchronous schedule before continuing traversal of the Asynchronous schedule. See Section 4.10.3.2 for full operational details. Valid values are 1h to 3h. Software must not write a zero to this bit when Park Mode Enableis a one as this will result in undefined behavior.
      uint32_t                        : 1 ; ///< reserved
      uint32_t async_park_enable      : 1 ; ///< Software uses this bit to enable or disable Park mode. When this bit is one, Park mode is enabled. When this bit is a zero, Park mode is disabled.
      uint32_t                        : 3 ; ///< reserved
      uint32_t nxp_framelist_size_msb : 1 ; ///< NXP customized : Bit 2 of the Frame List Size bits \n 011b: 128 elements \n 100b: 64 elements \n 101b: 32 elements \n 110b: 16 elements \n 111b: 8 elements
      uint32_t int_threshold          : 8 ; ///< Default 08h. This field is used by system software to select the maximum rate at which the host controller will issue interrupts. The only valid values are defined below. If software writes an invalid value to this register, the results are undefined. Value Maximum Interrupt Interval 00h Reserved 01h 1 micro-frame 02h 2 micro-frames 04h 4 micro-frames 08h 8 micro-frames (default, equates to 1 ms) 10h 16 micro-frames (2 ms) 20h 32 micro-frames (4 ms) 40h 64 micro-frames (8 ms) Refer to Section 4.15 for interrupts affected by this register. Any other value in this register yields undefined results. Software modifications to this bit while HCHalted bit is equal to zero results in undefined behavior.
      uint32_t                        : 0 ; // padding to the boundary of storage unit
    }usb_cmd_bit;
  };

  union {
    uint32_t usb_sts            ; ///< This register indicates pending interrupts and various states of the Host Controller. The status resulting from a transaction on the serial bus is not indicated in this register. Software sets a bit to 0 in this register by writing a 1 to it. See Section 4.15 for additional information concerning USB interrupt conditions.
    struct {
      uint32_t usb                    : 1  ; ///< R/WC The Host Controller sets this bit to 1 on the completion of a USB transaction, which results in the retirement of a Transfer Descriptor that had its IOC bit set. \n The Host Controller also sets this bit to 1 when a short packet is detected (actual number of bytes received was less than the expected number of bytes).
      uint32_t usb_error              : 1  ; ///< R/WC The Host Controller sets this bit to 1 when completion of a USB transaction results in an error condition (e.g., error counter underflow). If the TD on which the error interrupt occurred also had its IOC bit set, both this bit and USBINT bit are set. See Section 4.15.1 for a list of the USB errors that will result in this bit being set to a one.
      uint32_t port_change_detect     : 1  ; ///< R/WC The Host Controller sets this bit to a one when any port for which the Port Ownerbit is set to zero (see Section 2.3.9) has a change bit transition from a zero to a one or a Force Port Resumebit transition from a zero to a one as a result of a J-K transition detected on a suspended port.
      uint32_t framelist_rollover     : 1  ; ///< R/WC The Host Controller sets this bit to a one when the Frame List Index(see Section 2.3.4) rolls over from its maximum value to zero. The exact value at which the rollover occurs depends on the frame list size. For example, if the frame list size (as programmed in the Frame List Sizefield of the USBCMD register) is 1024, the Frame Index Registerrolls over every time FRINDEX[13] toggles. Similarly, if the size is 512, the Host Controller sets this bit to a one every time FRINDEX[12] toggles.
      uint32_t pci_host_system_error  : 1  ; ///< R/WC (not used by NXP) The Host Controller sets this bit to 1 when a serious error occurs during a host system access involving the Host Controller module. In a PCI system, conditions that set this bit to 1 include PCI Parity error, PCI Master Abort, and PCI Target Abort. When this error occurs, the Host Controller clears the Run/Stop bit in the Command register to prevent further execution of the scheduled TDs.
      uint32_t async_advance          : 1  ; ///< R/WC 0=Default. System software can force the host controller to issue an interrupt the next time the host controller advances the asynchronous schedule by writing a one to the Interrupt on Async Advance Doorbell bit in the USBCMD register. This status bit indicates the assertion of that interrupt source.
      uint32_t                        : 1  ; ///< These bits are reserved and should be set to zero.
      uint32_t nxp_int_sof            : 1  ; ///< R/WC NXP customized:  this bit will be set every 125us and can be used by host controller driver as a time base.
      uint32_t                        : 4  ; ///< These bits are reserved and should be set to zero.
      uint32_t hc_halted              : 1  ; ///< Read-Only 1=Default. This bit is a zero whenever the Run/Stop bit is a one. The Host Controller sets this bit to one after it has stopped executing as a result of the Run/Stop bit being set to 0, either by software or by the Host Controller hardware (e.g. internal error).
      uint32_t reclamation            : 1  ; ///< Read-Only 0=Default. This is a read-only status bit, which is used to detect an empty asynchronous schedule. The operational model of empty schedule detection is described in Section 4.8.3. The valid transitions for this bit are described in Section 4.8.6.
      uint32_t period_schedule_status : 1  ; ///< Read-Only The bit reports the current real status of the Periodic Schedule. If this bit is a zero then the status of the Periodic Schedule is disabled. If this bit is a one then the status of the Periodic Schedule is enabled
      uint32_t async_schedule_status  : 1  ; ///< Read-Only 0=Default. The bit reports the current real status of the Asynchronous Schedule. If this bit is a zero then the status of the Asynchronous Schedule is disabled. If this bit is a one then the status of the Asynchronous Schedule is enabled.
      uint32_t                        : 2  ; ///< reseved
      uint32_t nxp_int_async          : 1  ; ///< R/WC NXP customized: This bit is set by the Host Controller when the cause of an interrupt is a completion of a USB transaction where the Transfer Descriptor (TD) has an interrupt on complete (IOC) bit set andthe TD was from the asynchronous schedule. This bit is also set by the Host when a short packet is detected andthe packet is on the asynchronous schedule.
      uint32_t nxp_int_period         : 1  ; ///< R/WC NXP customized: This bit is set by the Host Controller when the cause of an interrupt is a completion of a USB transaction where the Transfer Descriptor (TD) has an interrupt on complete (IOC) bit set andthe TD was from the periodic schedule.
      uint32_t                        : 12 ; ///< reserved
      uint32_t                        : 0  ; // padding to the boundary of storage unit
    }usb_sts_bit;
  };

  union{
    uint32_t usb_int_enable     ; ///< This register enables and disables reporting of the corresponding interrupt to the software. When a bit is set and the corresponding interrupt is active, an interrupt is generated to the host. Interrupt sources that are disabled in this register still appear in the USBSTS to allow the software to poll for events.
    struct {
      uint32_t usb                   : 1  ; ///< When this bit is a one, and the USBINT bit in the USBSTS register is a one, the host controller will issue an interrupt at the next interrupt threshold. The interrupt is acknowledged by software clearing the USBINTbit.
      uint32_t usb_error             : 1  ; ///< When this bit is a one, and the USBERRINT bit in the USBSTS register is a one, the host controller will issue an interrupt at the next interrupt threshold. The interrupt is acknowledged by software clearing the USBERRINTbit.
      uint32_t port_change_detect    : 1  ; ///< When this bit is a one, and the Port Change Detect bit in the USBSTS register is a one, the host controller will issue an interrupt. The interrupt is acknowledged by software clearing the Port Change Detectbit.
      uint32_t framelist_rollover    : 1  ; ///< When this bit is a one, and the Frame List Rolloverbit in the USBSTS register is a one, the host controller will issue an interrupt. The interrupt is acknowledged by software clearing the Frame List Rollover bit.
      uint32_t pci_host_system_error : 1  ; ///< (not used by NXP) When this bit is a one, and the Host System Error Statusbit in the USBSTS register is a one, the host controller will issue an interrupt. The interrupt is acknowledged by software clearing the Host System Error bit.
      uint32_t async_advance         : 1  ; ///< When this bit is a one, and the Interrupt on Async Advancebit in the USBSTS register is a one, the host controller will issue an interrupt at the next interrupt threshold. The interrupt is acknowledged by software clearing the Interrupt on Async Advancebit.
      uint32_t                       : 1  ; ///< reserved
      uint32_t nxp_int_sof           : 1  ; ///< NXP customized: if this bit is one and the SRI bit in the USBSTS register is one, the host controller will issue an interrupt. In host mode, the SRI bit will be set every 125 micro sec and can be used by the host controller as a time base. The interrupt is acknowledged by software clearing the SRI bit in the USBSTS register.
      uint32_t                       : 10 ; ///< reserved
      uint32_t nxp_int_async         : 1  ; ///< NXP customized: When this bit is a one, and the USBHSTASYNCINT bit in the USBSTS register is a one, the host controller will issue an interrupt at the next interrupt threshold. The interrupt is acknowledged by software clearing the USBHSTASYNCINT bit.
      uint32_t nxp_int_period        : 1  ; ///< NXP customized: When this bit is a one, and the USBHSTPERINT bit in the USBSTS register is a one, the host controller will issue an interrupt at the next interrupt threshold. The interrupt is acknowledged by software clearing the USBHSTPERINT bit.
      uint32_t                       : 12 ; ///< reserved
      uint32_t                       : 0  ; // padding to the boundary of storage unit
    }usb_int_enable_bit;
  };

  /*
  uint32_t frame_index        ; ///< This register is used by the host controller to index into the periodic frame list. The register updates every 125 microseconds (once each micro-frame). Bits [N:3] are used to select a particular entry in the Periodic Frame List during periodic schedule execution. The number of bits used for the index depends on the size of the frame list as set by system software in the Frame List Sizefield in the USBCMD register
  uint32_t ctrl_ds_seg        ; ///< (not used by NXP) This 32-bit register corresponds to the most significant address bits [63:32] for all EHCI data structures. If the 64-bit Addressing Capabilityfield in HCCPARAMS is a zero, then this register is not used
  uint32_t periodic_list_base ; ///< This 32-bit register contains the beginning address of the Periodic Frame List in the system memory. System software loads this register prior to starting the schedule execution by the Host Controller (see 4.1). The memory structure referenced by this physical memory pointer is assumed to be 4-Kbyte aligned. The contents of this register are combined with the Frame Index Register (FRINDEX) to enable the Host Controller to step through the Periodic Frame List in sequence.
  uint32_t async_list_base    ; ///< This 32-bit register contains the address of the next asynchronous queue head to be executed. Bits [4:0] of this register cannot be modified by system software and will always return a zero when read. The memory structure referenced by this physical memory pointer is assumed to be 32-byte (cache line) aligned
  uint32_t tt_control         ; ///< nxp embedded transaction translator (reserved by EHCI specs)
  uint32_t reserved[8]        ; ///< reserved by EHCI specs
  uint32_t config_flag        ; ///< (not used by NXP) configured flag register
  */

  union {
    uint32_t portsc             ; ///< port status and control
    struct {
      uint32_t current_connect_status      : 1; ///< RO 1=Device is present on port. 0=No device is present. Default = 0. This value reflects the current state of the port, and may not correspond directly to the event that caused the Connect Status Change bit (Bit 1) to be set. This field is zero if Port Power is zero.
      uint32_t connect_status_change       : 1; ///< R/WC 1=Change in Current Connect Status. 0=No change. Default = 0. Indicates a change has occurred in the port's Current Connect Status. The host controller sets this bit for all changes to the port device connect status, even if system software has not cleared an existing connect status change. For example, the insertion status changes twice before system software has cleared the changed condition, hub hardware will be "setting" an already-set bit (i.e., the bit will remain set). Software sets this bit to 0 by writing a 1 to it. This field is zero if Port Power is zero.
      uint32_t port_enable                 : 1; ///< 1=Enable. 0=Disable. Default = 0. Ports can only be enabled by the host controller as a part of the reset and enable. Software cannot enable a port by writing a one to this field. The host controller will only set this bit to a one when the reset sequence determines that the attached device is a high-speed device. Ports can be disabled by either a fault condition (disconnect event or other fault condition) or by host software. Note that the bit status does not change until the port state actually changes.
      uint32_t port_enable_change          : 1; ///< R/WC 1=Port enabled/disabled status has changed. 0=No change. Default = 0. For the root hub, this bit gets set to a one only when a port is disabled due to the appropriate conditions existing at the EOF2 point (See Chapter 11 of the USB Specification for the definition of a Port Error). Software clears this bit by writing a 1 to it. This field is zero if Port Power is zero.
      uint32_t over_current_active         : 1; ///< RO Default = 0. 1=This port currently has an over-current condition. 0=This port does not have an over-current condition. This bit will automatically transition from a one to a zero when the over current condition is removed.
      uint32_t over_current_change         : 1; ///< R/WC Default = 0. 1=This bit gets set to a one when there is a change to Over-current Active. Software clears this bit by writing a one to this bit position.
      uint32_t force_port_resume           : 1; ///< 1= Resume detected/driven on port. 0=No resume (K-state) detected/driven on port. Default = 0. This functionality defined for manipulating this bit depends on the value of the Suspendbit. For example, if the port is not suspended (Suspendand Enabledbits are a one) and software transitions this bit to a one, then the effects on the bus are undefined. Software sets this bit to a 1 to drive resume signaling. The Host Controller sets this bit to a 1 if a J-to-K transition is detected while the port is in the Suspend state. When this bit transitions to a one because a J-to-K transition is detected, the Port Change Detectbit in the USBSTS register is also set to a one. If software sets this bit to a one, the host controller must not set the Port Change Detectbit.
      uint32_t suspend                     : 1; ///< 1=Port in suspend state. 0=Port not in suspend state. Default = 0. Port Enabled Bit and Suspend bit of this register define the port states as follows: Bits [Port Enabled, Suspend] Port State 0X Disable 10 Enable 11 Suspend When in suspend state, downstream propagation of data is blocked on this port, except for port reset. The blocking occurs at the end of the current transaction, if a transaction was in progress when this bit was written to 1. In the suspend state, the port is sensitive to resume detection. Note that the bit status does not change until the port is suspended and that there may be a delay in suspending a port if there is a transaction currently in progress on the USB. A write of zero to this bit is ignored by the host controller. The host controller will unconditionally set this bit to a zero when: Software sets the Force Port Resumebit to a zero (from a one). Software sets the Port Resetbit to a one (from a zero).
      uint32_t port_reset                  : 1; ///< 1=Port is in Reset. 0=Port is not in Reset. Default = 0. When software writes a one to this bit (from a zero)
      uint32_t nxp_highspeed_status        : 1; ///< NXP customized: 0=connected to the port is not in High-speed mode, 1=connected to the port is in High-speed mode
      uint32_t line_status                 : 2; ///< hese bits reflect the current logical levels of the D+ (bit 11) and D- (bit 10) signal lines. These bits are used for detection of low-speed USB devices prior to the port reset and enable sequence. This field is valid only when the port enable bit is zero and the current connect status bit is set to a one. The encoding of the bits are: 00b SE0, 10b J-state, 01b K-state, 11b undefined
      uint32_t port_power                  : 1; ///< 0= power off, 1= power on, Host/OTG controller requires port power control switches. This bit represents the current setting of the switch (0=off, 1=on). When power is not available on a port (i.e. PP equals a 0), the port is non-functional and will not report attaches, detaches, etc. When an over-current condition is detected on a powered port and PPC is a one, the PP bit in each affected port may be transitioned by the host controller driver from a one to a zero (removing power from the port).
      uint32_t port_owner                  : 1; ///< (not used by NXP)
      uint32_t port_indicator_control      : 2; ///< Writing to this field effects the value of the pins USB0_IND1 and USB0_IND0. 00b: Port indication is off, 01b: Amber, 10b: green, 11b: undefined
      uint32_t port_test_control           : 4; ///< When this field is zero, the port is NOT operating in a test mode. A non-zero value indicates that it is operating in test mode
      uint32_t wake_on_connect_enable      : 1; ///< Default = 0b. Writing this bit to a one enables the port to be sensitive to device connects as wake-up events. See Section 4.3 for effects of this bit on resume event behavior. Refer to Section 4.3.1 for operational model.
      uint32_t wake_on_disconnect_enable   : 1; ///<  Default = 0b. Writing this bit to a one enables the port to be sensitive to device disconnects as wake-up events. See Section 4.3 for effects of this bit on resume event behavior. Refer to Section 4.3.1 for operational model.
      uint32_t wake_on_over_current_enable : 1; ///< Default = 0b. Writing this bit to a one enables the port to be sensitive to over-current conditions as wake-up events. See Section 4.3 for effects of this bit on resume event behavior. Refer to Section 4.3.1 for operational model.
      uint32_t nxp_phy_clock_disable       : 1; ///< NXP customized: the PHY can be put into Low Power Suspend Clock Disable when the downstream device has been put into suspend mode or when no downstream device is connected. Low power suspend is completely under the control of software. 0: enable PHY clock, 1: disable PHY clock
      uint32_t nxp_port_force_fullspeed    : 1; ///< NXP customized: Writing this bit to a 1 will force the port to only connect at Full Speed. It disables the chirp sequence that allowsthe port to identify itself as High Speed. This is useful for testing FS configurations with a HS host, hub or device.
      uint32_t                             : 1;
      uint32_t nxp_port_speed              : 2; ///< NXP customized: This register field indicates the speed atwhich the port is operating. For HS mode operation in the host controllerand HS/FS operation in the device controller the port routing steers data to the Protocol engine. For FS and LS mode operation in the host controller, the port routing steers data to the Protocol Engine w/ Embedded Transaction Translator. 0x0: Fullspeed, 0x1: Lowspeed, 0x2: Highspeed
      uint32_t                             : 0; // padding to the boundary of storage unit
    }portsc_bit;
  };
}ehci_registers_ta;

INLINE_ ehci_registers_ta* get_operational_registera(void)
{
  //xil_printf("ehci get_operation_register\r\n");
  return (ehci_registers_ta*) (XPAR_XUSBPS_0_BASEADDR+XUSBPS_CMD_OFFSET);
}







void read_usb_status(void)
{
	xil_printf("\n\rRead usb status\n\r");

	bool ret1;
	bool ret2;
	bool ret3;
	ret1 = get_operational_registera()->portsc_bit.current_connect_status;
	ret2 = get_operational_registera()->portsc_bit.connect_status_change;
	ret3 = get_operational_registera()->portsc_bit.port_enable;

	//ret = get_operational_registera();
	xil_printf("david0824: %s:%s(%d) ret1 = %d ret2 = %d ret3 = %d\r\n",__FILE__,__func__,__LINE__,ret1, ret2, ret3);

	u32 value;

	value = Xil_In32(XPAR_XUSBPS_0_BASEADDR + 0);
	xil_printf("david0824: %s:%s(%d) register 0 value = 0x%08X\r\n",__FILE__,__func__,__LINE__,value);

	value = Xil_In32(XPAR_XUSBPS_0_BASEADDR + 4);
	xil_printf("david0824: %s:%s(%d) register 4 value = 0x%08X\r\n",__FILE__,__func__,__LINE__,value);

	value = Xil_In32(XPAR_XUSBPS_0_BASEADDR + 8);
	xil_printf("david0824: %s:%s(%d) register 8 value = 0x%08X\r\n",__FILE__,__func__,__LINE__,value);

	value = Xil_In32(XPAR_XUSBPS_0_BASEADDR + 0xC);
	xil_printf("david0824: %s:%s(%d) register 0xC value = 0x%08X\r\n",__FILE__,__func__,__LINE__,value);

	value = Xil_In32(XPAR_XUSBPS_0_BASEADDR + 0x10);
	xil_printf("david0824: %s:%s(%d) register 0x10 value = 0x%08X\r\n",__FILE__,__func__,__LINE__,value);

	value = Xil_In32(XPAR_XUSBPS_0_BASEADDR + 0x14);
	xil_printf("david0824: %s:%s(%d) register 0x14 value = 0x%08X\r\n",__FILE__,__func__,__LINE__,value);

	xil_printf("david0824: %s:%s(%d) sizeof(ehci_registers_ta) = %d\r\n",__FILE__,__func__,__LINE__,sizeof(ehci_registers_ta));
	xil_printf("david0824: %s:%s(%d) sizeof(uint32_t) = %d\r\n",__FILE__,__func__,__LINE__,sizeof(uint32_t));

	value = Xil_In32(XPAR_XUSBPS_0_BASEADDR + XUSBPS_CMD_OFFSET);
	xil_printf("david0824: %s:%s(%d) register value = 0x%08X\r\n",__FILE__,__func__,__LINE__,value);

	/*
	ret1 = get_operational_registera()->portsc_bit.current_connect_status;
	ret2 = get_operational_registera()->portsc_bit.connect_status_change;
	ret3 = get_operational_registera()->portsc_bit.port_enable;
	*/

	xil_printf("usb_cmd\trun_stop = %d\r\n", get_operational_registera()->usb_cmd_bit.run_stop );
	xil_printf("usb_cmd\treset = %d\r\n", get_operational_registera()->usb_cmd_bit.reset );
	xil_printf("usb_cmd\tframelist_size = %d\r\n", get_operational_registera()->usb_cmd_bit.framelist_size );
	xil_printf("usb_cmd\tperiodic_enable = %d\r\n", get_operational_registera()->usb_cmd_bit.periodic_enable );
	xil_printf("usb_cmd\tasync_enable = %d\r\n", get_operational_registera()->usb_cmd_bit.async_enable );
	xil_printf("usb_cmd\tadvacne_async = %d\r\n", get_operational_registera()->usb_cmd_bit.advacne_async );
	xil_printf("usb_cmd\tlight_reset = %d\r\n", get_operational_registera()->usb_cmd_bit.light_reset );
	xil_printf("usb_cmd\tasync_park = %d\r\n", get_operational_registera()->usb_cmd_bit.async_park );
	xil_printf("usb_cmd\tasync_park_enable = %d\r\n", get_operational_registera()->usb_cmd_bit.async_park_enable );
	xil_printf("usb_cmd\tnxp_framelist_size_msb = %d\r\n", get_operational_registera()->usb_cmd_bit.nxp_framelist_size_msb );
	xil_printf("usb_cmd\tint_threshold = %d\r\n", get_operational_registera()->usb_cmd_bit.int_threshold );

	xil_printf("usb_sts\tusb = %d\r\n", get_operational_registera()->usb_sts_bit.usb );
	xil_printf("usb_sts\tusb_error = %d\r\n", get_operational_registera()->usb_sts_bit.usb_error );
	xil_printf("usb_sts\tport_change_detect = %d\r\n", get_operational_registera()->usb_sts_bit.port_change_detect );
	xil_printf("usb_sts\tframelist_rollover = %d\r\n", get_operational_registera()->usb_sts_bit.framelist_rollover );
	xil_printf("usb_sts\tpci_host_system_error = %d\r\n", get_operational_registera()->usb_sts_bit.pci_host_system_error );
	xil_printf("usb_sts\tasync_advance = %d\r\n", get_operational_registera()->usb_sts_bit.async_advance );
	xil_printf("usb_sts\tnxp_int_sof = %d\r\n", get_operational_registera()->usb_sts_bit.nxp_int_sof );
	xil_printf("usb_sts\thc_halted = %d\r\n", get_operational_registera()->usb_sts_bit.hc_halted );
	xil_printf("usb_sts\treclamation = %d\r\n", get_operational_registera()->usb_sts_bit.reclamation );
	xil_printf("usb_sts\tperiod_schedule_status = %d\r\n", get_operational_registera()->usb_sts_bit.period_schedule_status );
	xil_printf("usb_sts\tasync_schedule_status = %d\r\n", get_operational_registera()->usb_sts_bit.async_schedule_status );
	xil_printf("usb_sts\tnxp_int_async = %d\r\n", get_operational_registera()->usb_sts_bit.nxp_int_async );
	xil_printf("usb_sts\tnxp_int_period = %d\r\n", get_operational_registera()->usb_sts_bit.nxp_int_period );

	xil_printf("usb_int\tusb = %d\r\n", get_operational_registera()->usb_int_enable_bit.usb );
	xil_printf("usb_int\tusb_error = %d\r\n", get_operational_registera()->usb_int_enable_bit.usb_error );
	xil_printf("usb_int\tport_change_detect = %d\r\n", get_operational_registera()->usb_int_enable_bit.port_change_detect );
	xil_printf("usb_int\tframelist_rollover = %d\r\n", get_operational_registera()->usb_int_enable_bit.framelist_rollover );
	xil_printf("usb_int\tpci_host_system_error = %d\r\n", get_operational_registera()->usb_int_enable_bit.pci_host_system_error );
	xil_printf("usb_int\tasync_advance = %d\r\n", get_operational_registera()->usb_int_enable_bit.async_advance );
	xil_printf("usb_int\tnxp_int_sof = %d\r\n", get_operational_registera()->usb_int_enable_bit.nxp_int_sof );
	xil_printf("usb_int\tnxp_int_async = %d\r\n", get_operational_registera()->usb_int_enable_bit.nxp_int_async );
	xil_printf("usb_int\tnxp_int_period = %d\r\n", get_operational_registera()->usb_int_enable_bit.nxp_int_period );


	xil_printf("portsc\tcurrent_connect_status = %d\r\n", get_operational_registera()->portsc_bit.current_connect_status);
	xil_printf("portsc\tconnect_status_change = %d\r\n", get_operational_registera()->portsc_bit.connect_status_change);
	xil_printf("portsc\tport_enable = %d\r\n", get_operational_registera()->portsc_bit.port_enable);
	xil_printf("portsc\tport_enable_change = %d\r\n", get_operational_registera()->portsc_bit.port_enable_change);
	xil_printf("portsc\tover_current_active = %d\r\n", get_operational_registera()->portsc_bit.over_current_active);
	xil_printf("portsc\tover_current_change = %d\r\n", get_operational_registera()->portsc_bit.over_current_change);
	xil_printf("portsc\tforce_port_resume = %d\r\n", get_operational_registera()->portsc_bit.force_port_resume);
	xil_printf("portsc\tsuspend = %d\r\n", get_operational_registera()->portsc_bit.suspend);
	xil_printf("portsc\tport_reset = %d\r\n", get_operational_registera()->portsc_bit.port_reset);
	xil_printf("portsc\tnxp_highspeed_status = %d\r\n", get_operational_registera()->portsc_bit.nxp_highspeed_status);
	xil_printf("portsc\tline_status = %d\r\n", get_operational_registera()->portsc_bit.line_status);
	xil_printf("portsc\tport_power = %d\r\n", get_operational_registera()->portsc_bit.port_power);
	xil_printf("portsc\tport_owner = %d\r\n", get_operational_registera()->portsc_bit.port_owner);
	xil_printf("portsc\tport_indicator_control = %d\r\n", get_operational_registera()->portsc_bit.port_indicator_control);
	xil_printf("portsc\tport_test_control = %d\r\n", get_operational_registera()->portsc_bit.port_test_control);
	xil_printf("portsc\twake_on_connect_enable = %d\r\n", get_operational_registera()->portsc_bit.wake_on_connect_enable);
	xil_printf("portsc\twake_on_disconnect_enable = %d\r\n", get_operational_registera()->portsc_bit.wake_on_disconnect_enable);
	xil_printf("portsc\twake_on_over_current_enable = %d\r\n", get_operational_registera()->portsc_bit.wake_on_over_current_enable);
	xil_printf("portsc\tnxp_phy_clock_disable = %d\r\n", get_operational_registera()->portsc_bit.nxp_phy_clock_disable);
	xil_printf("portsc\tnxp_port_force_fullspeed = %d\r\n", get_operational_registera()->portsc_bit.nxp_port_force_fullspeed);
	xil_printf("portsc\tnxp_port_speed = %d\r\n", get_operational_registera()->portsc_bit.nxp_port_speed);





}




  xil_printf("david0823: %s:%s(%d) dev_addr=%d, bmRequestType=0x%02x, bRequest=0x%02x, wValue=%d, wIndex=%d, wLength=%d\r\n",__FILE__,__func__,__LINE__,
		  dev_addr, bmRequestType, bRequest, wValue, wIndex, wLength);

  switch(bRequest)
  {
  case TUSB_REQUEST_GET_STATUS:		xil_printf("1 usbh_control_xfer_subtask : TUSB_REQUEST_GET_STATUS\n\r");break;
  case TUSB_REQUEST_CLEAR_FEATURE:	xil_printf("2 usbh_control_xfer_subtask : TUSB_REQUEST_CLEAR_FEATURE\n\r");break;
  case TUSB_REQUEST_RESERVED:		xil_printf("3 usbh_control_xfer_subtask : TUSB_REQUEST_RESERVED\n\r");break;
  case TUSB_REQUEST_SET_FEATURE:	xil_printf("4 usbh_control_xfer_subtask : TUSB_REQUEST_SET_FEATURE\n\r");break;
  case TUSB_REQUEST_RESERVED2:		xil_printf("5 usbh_control_xfer_subtask : TUSB_REQUEST_RESERVED2\n\r");break;
  case TUSB_REQUEST_SET_ADDRESS:	xil_printf("6 usbh_control_xfer_subtask : TUSB_REQUEST_SET_ADDRESS\n\r");break;
  case TUSB_REQUEST_GET_DESCRIPTOR:	xil_printf("7 usbh_control_xfer_subtask : TUSB_REQUEST_GET_DESCRIPTOR\n\r");break;
  case TUSB_REQUEST_SET_DESCRIPTOR:	xil_printf("8 usbh_control_xfer_subtask : TUSB_REQUEST_SET_DESCRIPTOR\n\r");break;
  case TUSB_REQUEST_GET_CONFIGURATION:	xil_printf("9 usbh_control_xfer_subtask : TUSB_REQUEST_GET_CONFIGURATION\n\r");break;
  case TUSB_REQUEST_SET_CONFIGURATION:	xil_printf("10 usbh_control_xfer_subtask : TUSB_REQUEST_SET_CONFIGURATION\n\r");break;
  case TUSB_REQUEST_GET_INTERFACE:	xil_printf("11 usbh_control_xfer_subtask : TUSB_REQUEST_GET_INTERFACE\n\r");break;
  case TUSB_REQUEST_SET_INTERFACE:	xil_printf("12 usbh_control_xfer_subtask : TUSB_REQUEST_SET_INTERFACE\n\r");break;
  case TUSB_REQUEST_SYNCH_FRAME:	xil_printf("13 usbh_control_xfer_subtask : TUSB_REQUEST_SYNCH_FRAME\n\r");break;
  default:	xil_printf("14 usbh_control_xfer_subtask : XXXXXXXXXX\n\r");break;
  }

  xil_printf("s\r\n");
  
  
  