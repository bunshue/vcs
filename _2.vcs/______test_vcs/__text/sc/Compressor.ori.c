        if (!Compress.Status.bit.WayValveOn)
        {
            Compress.Status.bit.WayValveOn = 1;
            //����EEPROM��־λTYPE_HARD_W.Bit0ѡ����������ʽ
            if (eepParam.member.typeHardWDrive & 0x01)
            {
                GpioDataRegs.AIOSET.bit.AIO6 = 1;
            }
            else
    }
}
// 500ms loop in main.c
// ��ͨ������
/***
void WayValveCtrl(void)
{
}
***/

/***************
// ���ʹ��� 500ms loop
void f_RtnOil(void)
{
        else
        {
            if (Compress.Status.bit.ReturnOil)      // ����
            {
                Compress.Status.bit.ReturnOil = 0;
                Compress.ReturnOilTime = Eep.E2RtnOilCycle*6*MIN_UINT;
            }
            else        // ���ͼ��
            {

// 100ms loop
// ѹ��������
void CompressCtrl(void)
{
#if COMPRESSOR_AUTO     // ��������
    if (Flag_Motor_Run)
    {

    return;
}

#define DELAY_FIRST_STARTUP 10000           // �״��ϵ���ʱʱ��
Uint16 Delay_PowerUp=0;
Uint16 Flag_PowerUp=0;
Uint16 Count_100ms = 0;
Uint16 Count_500_pc = 0;
// 1ms loop
void SlowTimer(void)
{
    if(Delay_PowerUp<DELAY_FIRST_STARTUP)       // �ϵ���ʱ
    {
                    SetWayValve(fourWayValevState);
                    break;
                case 4:
                    //f_RtnOil();       // ����
                    break;
            }           
        }


