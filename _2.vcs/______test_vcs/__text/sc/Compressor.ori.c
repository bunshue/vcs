        if (!Compress.Status.bit.WayValveOn)
        {
            Compress.Status.bit.WayValveOn = 1;
            //根据EEPROM标志位TYPE_HARD_W.Bit0选择正向动作形式
            if (eepParam.member.typeHardWDrive & 0x01)
            {
                GpioDataRegs.AIOSET.bit.AIO6 = 1;
            }
            else
    }
}
// 500ms loop in main.c
// 四通阀控制
/***
void WayValveCtrl(void)
{
}
***/

/***************
// 回油处理 500ms loop
void f_RtnOil(void)
{
        else
        {
            if (Compress.Status.bit.ReturnOil)      // 回油
            {
                Compress.Status.bit.ReturnOil = 0;
                Compress.ReturnOilTime = Eep.E2RtnOilCycle*6*MIN_UINT;
            }
            else        // 回油间隔
            {

// 100ms loop
// 压缩机控制
void CompressCtrl(void)
{
#if COMPRESSOR_AUTO     // 正常运行
    if (Flag_Motor_Run)
    {

    return;
}

#define DELAY_FIRST_STARTUP 10000           // 首次上电延时时间
Uint16 Delay_PowerUp=0;
Uint16 Flag_PowerUp=0;
Uint16 Count_100ms = 0;
Uint16 Count_500_pc = 0;
// 1ms loop
void SlowTimer(void)
{
    if(Delay_PowerUp<DELAY_FIRST_STARTUP)       // 上电延时
    {
                    SetWayValve(fourWayValevState);
                    break;
                case 4:
                    //f_RtnOil();       // 回油
                    break;
            }           
        }


