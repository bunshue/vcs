        if (!Compress.Status.bit.WayValveOn)
        {
            Compress.Status.bit.WayValveOn = 1;
            //�ھ�EEPROM�лx��TYPE_HARD_W.Bit0��ܥ��V�ʧ@�Φ�
            if (eepParam.member.typeHardWDrive & 0x01)
            {
                GpioDataRegs.AIOSET.bit.AIO6 = 1;
            }
            else
    }
}
// 500ms loop in main.c
// �|�q�ֱ���
/***
void WayValveCtrl(void)
{
}
***/

/***************
// �^�o�B�z 500ms loop
void f_RtnOil(void)
{
        else
        {
            if (Compress.Status.bit.ReturnOil)      // �^�o
            {
                Compress.Status.bit.ReturnOil = 0;
                Compress.ReturnOilTime = Eep.E2RtnOilCycle*6*MIN_UINT;
            }
            else        // �^�o���j
            {

// 100ms loop
// ���Y������
void CompressCtrl(void)
{
#if COMPRESSOR_AUTO     // ���`�B��
    if (Flag_Motor_Run)
    {

    return;
}

#define DELAY_FIRST_STARTUP 10000           // �����W�q���ɮɶ�
Uint16 Delay_PowerUp=0;
Uint16 Flag_PowerUp=0;
Uint16 Count_100ms = 0;
Uint16 Count_500_pc = 0;
// 1ms loop
void SlowTimer(void)
{
    if(Delay_PowerUp<DELAY_FIRST_STARTUP)       // �W�q����
    {
                    SetWayValve(fourWayValevState);
                    break;
                case 4:
                    //f_RtnOil();       // �^�o
                    break;
            }
        }


