        if (!Compress.Status.bit.WayValveOn)
        {
            Compress.Status.bit.WayValveOn = 1;
            //根據EEPROM標誌位TYPE_HARD_W.Bit0選擇正向動作形式
            if (eepParam.member.typeHardWDrive & 0x01)
            {
                GpioDataRegs.AIOSET.bit.AIO6 = 1;
            }
            else
    }
}
// 500ms loop in main.c
// 四通閥控制
/***
void WayValveCtrl(void)
{
}
***/

/***************
// 回油處理 500ms loop
void f_RtnOil(void)
{
        else
        {
            if (Compress.Status.bit.ReturnOil)      // 回油
            {
                Compress.Status.bit.ReturnOil = 0;
                Compress.ReturnOilTime = Eep.E2RtnOilCycle*6*MIN_UINT;
            }
            else        // 回油間隔
            {

// 100ms loop
// 壓縮機控制
void CompressCtrl(void)
{
#if COMPRESSOR_AUTO     // 正常運行
    if (Flag_Motor_Run)
    {

    return;
}

#define DELAY_FIRST_STARTUP 10000           // 首次上電延時時間
Uint16 Delay_PowerUp=0;
Uint16 Flag_PowerUp=0;
Uint16 Count_100ms = 0;
Uint16 Count_500_pc = 0;
// 1ms loop
void SlowTimer(void)
{
    if(Delay_PowerUp<DELAY_FIRST_STARTUP)       // 上電延時
    {
                    SetWayValve(fourWayValevState);
                    break;
                case 4:
                    //f_RtnOil();       // 回油
                    break;
            }
        }


