#ifndef __USB_ULPI_H
#define __USB_ULPI_H

// USB3320 USB PHY

/*
 * Register Map
 */
#define ULPI_VENDOR_ID_LOW			0x00
#define ULPI_VENDOR_ID_HIGH			0x01
#define ULPI_PRODUCT_ID_LOW			0x02
#define ULPI_PRODUCT_ID_HIGH		0x03
#define ULPI_FC_CTRL				0x04
#define ULPI_IFC_CTRL				0x07
#define ULPI_OTG_CTRL				0x0a
#define ULPI_USB_INT_EN_RISE		0x0d
#define ULPI_USB_INT_EN_FALL		0x10
#define ULPI_USB_INT_STS			0x13
#define ULPI_USB_INT_LATCH			0x14
#define ULPI_DEBUG					0x15
#define ULPI_SCRATCH				0x16
/* Optional Carkit Registers */
#define ULPI_CARKIT_CTRL			0x19
#define ULPI_CARKIT_INT_EN			0x1d
#define ULPI_CARKIT_INT_STS			0x20
#define ULPI_CARKIT_INT_LATCH		0x21
/* Vendor Specific */
#define ULPI_HS_TX_BOOST			0x31
#define ULPI_HEADSET_AUDIO_MODE		0x33
#define ULPI_VENDOR_RID_CONVERSION	0x36
#define ULPI_USB_IO_POWER_MAN		0x39

/*
 * ULPI Flags
 */

// ULPI_FC_CTRL						0x04
#define ULPI_FC_XCVRSEL				(1 << 0)
#define ULPI_FC_XCVRSEL_MASK		(0x3 << 3)
#define ULPI_FC_XCVRSEL_HS			(0x0 << 3)
#define ULPI_FC_XCVRSEL_FS			(0x1 << 3)
#define ULPI_FC_XCVRSEL_LS			(0x2 << 3)
#define ULPI_FC_XCVRSEL_FS4LS		(0x3 << 3) 
#define ULPI_FC_TERMSEL				(1 << 2)
#define ULPI_FC_OPMODE				(1 << 3)
#define ULPI_FC_OPMODE_MASK			(0x3 << 3)
#define ULPI_FC_OPMODE_NORMAL		(0x0 << 3)
#define ULPI_FC_OPMODE_NONDRIVING	(0x1 << 3)
#define ULPI_FC_OPMODE_DISABLE_NRZI	(0x2 << 3)
#define ULPI_FC_OPMODE_RESERVED		(0x3 << 3)
#define ULPI_FC_RESET				(1 << 5)
#define ULPI_FC_SUSPENDM			(1 << 6) 
 
// ULPI_IFC_CTRL					0x07 
#define ULPI_IFC_6PIN_SERIAL		(1 << 0)
#define ULPI_IFC_3PIN_SERIAL		(1 << 1)
#define ULPI_IFC_CARKIT				(1 << 2)
#define ULPI_IFC_CLKSUSPM			(1 << 3)
#define ULPI_IFC_AUTORESUME			(1 << 4)
#define ULPI_IFC_EXTVBUS_INDINV		(1 << 5)
#define ULPI_IFC_IND_PASSTHRU		(1 << 6)
#define ULPI_IFC_PROTECT_DIS		(1 << 7)

// ULPI_OTG_CTRL					0x0a 
#define ULPI_OTG_ID_PULLUP			(1 << 0)
#define ULPI_OTG_DP_PULLDOWN		(1 << 1)
#define ULPI_OTG_DM_PULLDOWN		(1 << 2)
#define ULPI_OTG_DISCHRGVBUS		(1 << 3)
#define ULPI_OTG_CHRGVBUS			(1 << 4)
#define ULPI_OTG_DRVVBUS			(1 << 5)
#define ULPI_OTG_DRVVBUS_EXT		(1 << 6)
#define ULPI_OTG_EXTVBUSIND			(1 << 7)

// ULPI_USB_INT_EN_RISE				0x0d
// ULPI_USB_INT_EN_FALL				0x10
// ULPI_USB_INT_STS					0x13
// ULPI_USB_INT_LATCH				0x14
#define ULPI_INT_HOST_DISCONNECT	(1 << 0)
#define ULPI_INT_VBUS_VALID			(1 << 1)
#define ULPI_INT_SESS_VALID			(1 << 2)
#define ULPI_INT_SESS_END			(1 << 3)
#define ULPI_INT_IDGRD				(1 << 4)

// ULPI_DEBUG						0x15
#define ULPI_DEBUG_LINESTATE0		(1 << 0)
#define ULPI_DEBUG_LINESTATE1		(1 << 1)

// ULPI_CARKIT_CTRL						0x19
#define ULPI_CARKIT_CTRL_CARKITPWR		(1 << 0)
#define ULPI_CARKIT_CTRL_IDGNDDRV		(1 << 1)
#define ULPI_CARKIT_CTRL_TXDEN			(1 << 2)
#define ULPI_CARKIT_CTRL_RXDEN			(1 << 3)
#define ULPI_CARKIT_CTRL_SPKLEFTEN		(1 << 4)
#define ULPI_CARKIT_CTRL_SPKRIGHTEN		(1 << 5)
#define ULPI_CARKIT_CTRL_MICEN			(1 << 6)

// ULPI_CARKIT_INT_EN					0x1d
#define ULPI_CARKIT_INT_EN_IDFLOAT_RISE	(1 << 0)
#define ULPI_CARKIT_INT_EN_IDFLOAT_FALL	(1 << 1)
#define ULPI_CARKIT_INT_EN_CARINTDET	(1 << 2)
#define ULPI_CARKIT_INT_EN_DP_RISE		(1 << 3)
#define ULPI_CARKIT_INT_EN_DP_FALL		(1 << 4)
#define ULPI_CARKIT_INT_EN_RID_INT		(1 << 5)

// ULPI_CARKIT_INT_STS					0x20
// ULPI_CARKIT_INT_LATCH				0x21
#define ULPI_CARKIT_INT_IDFLOAT			(1 << 0)
#define ULPI_CARKIT_INT_CARINTDET		(1 << 1)
#define ULPI_CARKIT_INT_DP				(1 << 2)
#define ULPI_CARKIT_INT_RIDVAL			(1 << 3)
#define ULPI_CARKIT_INT_RIDVAL_MASK		(0x7 << 3)
#define ULPI_CARKIT_INT_RIDVAL_0		(0x0 << 3)
#define ULPI_CARKIT_INT_RIDVAL_75		(0x1 << 3)
#define ULPI_CARKIT_INT_RIDVAL_102K		(0x2 << 3)
#define ULPI_CARKIT_INT_RIDVAL_200K		(0x3 << 3)
#define ULPI_CARKIT_INT_RIDVAL_440K		(0x4 << 3)
#define ULPI_CARKIT_INT_RIDVAL_FLOAT	(0x5 << 3)
#define ULPI_CARKIT_INT_RIDVAL_ERROR	(0x7 << 3)
#define ULPI_CARKIT_INT_RID_DONE		(1 << 6)

/*
 * Macros for Set and Clear
 * See ULPI 1.1 specification to find the registers with Set and Clear offsets
 */
#define ULPI_SET(a)				(a + 1)
#define ULPI_CLR(a)				(a + 2)


#endif /* __USB_ULPI_H */


