#ifndef __CS8963_I2C_H__
#define __CS8963_I2C_H__

void send_I2C_data(BYTE length);
void get_I2C_data();
void mIIC_P21P20_Initial(void);
void sIIC_P21P20_Initial(unsigned char slaveADD3,unsigned char slaveADD1);

/*
void Initial_I2CM(unsigned char pin_scl, unsigned char pin_sda);
void Initial_I2CS1(unsigned char pin_scl, unsigned char pin_sda);
void Initial_I2CS2(unsigned char pin_scl, unsigned char pin_sda);
void mIIC_Send_1byte(unsigned char slaveADD, unsigned char DAT);
unsigned char mIIC_Receive_1byte(unsigned char slaveADD);
void test_send_i2c_command();
*/

#endif

