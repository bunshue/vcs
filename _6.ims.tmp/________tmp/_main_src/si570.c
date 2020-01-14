
// *****************************************************
// Dependencies
// *****************************************************
#include "si570.h"

// *****************************************************
// Globals
// *****************************************************

// Note: This frequency look-up table is based on the
//       following initial register values for the 
//       SI570:
//         Register 7  = 0x01
//         Register 8  = 0xC2
//         Register 9  = 0xBC
//         Register 10 = 0x00
//         Register 11 = 0xD4
//         Register 12 = 0x3B
//
//       If you have something different for initial
//       register values, these frequencies likely won't
//       work and you won't see anything on the screen
//       because the pixel frequency will be wrong. If
//       you have different register values, the
//       following calculation is used to set them:
//         1) Use the si5750_print_regs() function to
//            report the power-on value of registers 7
//            through 12 (in hex)
//         2) Extract RFREQ by concatenating the bits
//            of the registers as follows:
//              RFREQ = {reg8[5:0], reg9[7:0], reg10[7:0], reg11[7:0], reg12[4:0]}
//              RFREQ (example) = {6'h02, 8'hBC, 8'h00, 8'hD4, 8'h3B} = 38'h02BC00D43B
//         3) Convert RFREQ to decimal (38'h02BC00D43B = 11744105531)
//         4) Divide this number by 2^28 (11744105531/2^28 = 43.750202398747206)
//         5) Extract HS_DIV from reg7[7:5] (3'h0)
//         6) Use register mapping for SI570 to get final
//            HS_DIV value from this register value (3'h corresponds to value of 4)
//         7) Extract N1 by concatenating the bits of
//            the registers as follows:
//              N1 = {reg7[4:0], reg8[7:6]}
//              N1 (example) = {5'h01, 2'h3} = 7'h07
//         8) Convert N1 to decimal (7'h07 = 7)
//         9) Add 1 to N1 (N1 = 7+1 = 8)
//         10) Using Fout = 156.25 (pre-programmed
//             initial power up value for ZC702),
//             compute fXTAL from the following equation:
//               fXTAL = (Fout*HSDIV*N1)/RFREQ
//               fXTAL (example) = (156.25*4*8)/43.750202398747206 = 114.2851855730655
//         11) All remaining steps are performed in
//             SiLabs Programmable Oscillator Calculator
//             software utility.
//         12) Selec Options -> Advanced and input the
//             value of fXTAL calculated in step 10
//             (114.2851855730655) and click "OK."
//         13) Enter the start-up frequency of 156.25
//             and click "Apply Definition."
//         14) Select a new output frequency you wish
//             to use. For example, we'll calculate
//             74.25 MHz for 720p60 pixel clock. Enter
//             this value into the "New Frequency"
//             field and click "Create Example."
//         15) New register values will be displayed
//             in the "Procedure" tab. Use register
//             values 7 through 12 in the freq_reg_vals
//             array. For our example, 74.25MHz
//             corresponds to the following new register
//             values:
//               Register 7  = 0xE1
//               Register 8  = 0x42
//               Register 9  = 0xAE
//               Register 10 = 0x12
//               Register 11 = 0xBB
//               Register 12 = 0x5B
//             You can see these values used in the
//             corresponding entry in the array for
//             74.25MHz
//        
static const unsigned char freq_reg_vals[SI570_NUM_FREQS][6] =  // 6 registers in SI570 set the frequency
{
	{0x66, 0xC2, 0xB2, 0xCE, 0x21, 0x25}, //  25.175 MHz
	{0xA4, 0xC2, 0xA8, 0x67, 0x34, 0x85}, //  27.000 MHz
	{0xA3, 0x42, 0xC1, 0x9A, 0x6F, 0x5B}, //  40.000 MHz
	{0x23, 0xC2, 0xD8, 0x00, 0xDC, 0x8A}, //  65.000 MHz
	{0xE1, 0x42, 0xAE, 0x12, 0xBB, 0x5B}, //  74.250 MHz
	{0x41, 0xC2, 0xE3, 0x34, 0x13, 0x22}, // 110.000 MHz
	{0xA0, 0xC2, 0xEC, 0x71, 0x86, 0x92}, // 148.500 MHz
	{0x21, 0x42, 0xA8, 0x67, 0x34, 0x85}  // 162.000 MHz
};

// *****************************************************
// Private data
// *****************************************************

// Subcore instantiations
static XIicPs si570_iic_inst;

// *****************************************************
// Private functions
// *****************************************************

// i2c_mux_init() - Initialize the I2C mux to send
//                  commands and data to the Si570.
//   - p_si570_iic_inst - Pointer to the PS I2C controller
//   - return           - None
static void i2c_mux_init
(
	XIicPs* p_si570_iic_inst
)
{
	// Local variables
	unsigned char wr_buf = 0x1;
	unsigned char rd_buf = 0;

	// Deassert reset on MUX via GPIO
	Xil_Out32(0xe000a204, 0x2000);
 	Xil_Out32(0xe000a208, 0x2000);
 	Xil_Out32(0xe000a040, 0x2000);

	// Select SI570
	wr_buf = 0x01;
	XIicPs_MasterSendPolled(p_si570_iic_inst, &wr_buf, 1, I2C_MUX_CHIP_ADDR);
	while (XIicPs_BusIsBusy(p_si570_iic_inst)); // Wait until bus is idle to start another transfer

	XIicPs_MasterRecvPolled(p_si570_iic_inst, &rd_buf, 1, I2C_MUX_CHIP_ADDR);
	while (XIicPs_BusIsBusy(p_si570_iic_inst)); // Wait until bus is idle to start another transfer
}

// si570_i2c_write_reg() - Perform a I2C register write to the
//                         Si570 device. Assumes the I2C mux has
//                         already been set appropriately.
//   - p_si570_iic_inst - Pointer to the PS I2C controller
//   - reg_addr         - Register address to write to
//   - reg_val          - Data to write to the register
//   - return           - None
static void si570_i2c_write_reg
(
	XIicPs*       p_si570_iic_inst,
	unsigned char reg_addr,
	unsigned char reg_val
)
{
	// Local variables
	unsigned char wr_buf[2] = {0, 0};
	
	// Put the reg address on the bus
	wr_buf[0] = reg_addr;
	wr_buf[1] = reg_val;
	XIicPs_MasterSendPolled(p_si570_iic_inst, wr_buf, 2, SI570_I2C_CHIP_ADDR);
	while (XIicPs_BusIsBusy(p_si570_iic_inst));
	usleep(100);
}

// si570_i2c_read_reg() - Perform a I2C register read from the
//                        Si570 device. Assumes the I2C mux has
//                        already been set appropriately.
//   - p_si570_iic_inst - Pointer to the PS I2C controller
//   - reg_addr         - Register address to read from
//   - return           - Data read from the register
static unsigned char si570_i2c_read_reg
(
	XIicPs*        p_si570_iic_inst,
	unsigned char  reg_addr
)
{
	// Local variables
	unsigned char wr_buf[2] = {0, 0};
	unsigned char reg[2]    = {0, 0};
	
	// Put the reg address on the bus
	wr_buf[0] = reg_addr;
	XIicPs_MasterSendPolled(p_si570_iic_inst, wr_buf, 1, SI570_I2C_CHIP_ADDR);
	while (XIicPs_BusIsBusy(p_si570_iic_inst));
	usleep(100);
	
	// Get the reg data from the bus
	XIicPs_MasterRecvPolled(p_si570_iic_inst, &reg[0], 2, SI570_I2C_CHIP_ADDR);
	while (XIicPs_BusIsBusy(p_si570_iic_inst));
	
	return reg[0];
}

// *****************************************************
// Public functions
// *****************************************************
int si570_init
(
	si570_t*     p_si570_inst,
	unsigned int si570_iic_device_id
)
{
	// Local variables
	int status               = 0;
	XIicPs_Config  iic_cfg;
	XIicPs_Config* p_iic_cfg = &iic_cfg;
	
	// Attach subcore instances to object
	p_si570_inst->p_si570_iic_inst = &si570_iic_inst;
	
	// Initialize PS IIC drivers
	p_iic_cfg = XIicPs_LookupConfig(si570_iic_device_id);
	if (p_iic_cfg == NULL)
	{
		xil_printf("ERROR! Failed to find SI570 IIC driver.\n\r");
		return SI570_ERR_UNKNOWN;
	}

	status = XIicPs_CfgInitialize(p_si570_inst->p_si570_iic_inst, p_iic_cfg, p_iic_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize SI570 IIC driver.\n\r");
		return SI570_ERR_UNKNOWN;
	}
	
	// Set IIC serial clock rate
	XIicPs_SetSClk(p_si570_inst->p_si570_iic_inst, 100000);
	
	// Initialize the I2C MUX
	i2c_mux_init(p_si570_inst->p_si570_iic_inst);
	
	// Initialize the clock to 74.25 MHz
	si570_set_freq(p_si570_inst, SI570_FREQ_74_250_000);
	
	return SI570_SUCCESS;
}

void si570_set_freq
(
	si570_t*        p_si570_inst,
	si570_freq_id_t freq_id
)
{	
	unsigned int ii = 0;

	i2c_mux_init(p_si570_inst->p_si570_iic_inst);
	
	// Set back to known powerup state and freq
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 137, 0x10);
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 135, 0x01);
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 137, 0x00);
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 135, 0x40);
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 137, 0x10);
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 137, 0x10);
	
	// Set new freq
	for (ii = 0; ii < 6; ii++)
	{
		si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 7+ii, freq_reg_vals[freq_id][ii]);
	}
	
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 137, 0x00);
	si570_i2c_write_reg(p_si570_inst->p_si570_iic_inst, 135, 0x40);
	usleep(1000); // Not sure why this is needed, but it hangs without it.
}

void si5750_print_regs
(
	si570_t* p_si570_inst
)
{
	unsigned int ii = 0;
	
	for (ii = 0; ii < 6; ii++)
	{
		xil_printf("SI570 reg offset %d = 0x%02X\n\r", 7+ii, si570_i2c_read_reg(p_si570_inst->p_si570_iic_inst, 7+ii));
	}
}

