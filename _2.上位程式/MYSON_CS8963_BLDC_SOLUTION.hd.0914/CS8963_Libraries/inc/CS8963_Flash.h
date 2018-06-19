#ifndef __CS8963_FLASH_H__
#define __CS8963_FLASH_H__

void Unlock_Flash(void);
void Lock_Flash(void);
void IFB_Writ_1Byte(unsigned char ADD,unsigned char DAT);
void Flash_Read_Write_Test(void);
void Erase_Page(bit highADD, unsigned char pageADD);
void Erase_All(void);
void Program_Flash_1Byte(bit highADD, unsigned char midADD, unsigned char lowADD, unsigned char writeDAT);
unsigned char MainFlash_Read_1BYTE(bit highADD, unsigned char midADD, unsigned char lowADD);
unsigned char IFB_Read_1Byte(unsigned char ADD);
#ifdef SAVE_FACTORY_DATA
void save_factory_data_time(void);
void save_factory_data_time_222(void);
#endif
#endif


