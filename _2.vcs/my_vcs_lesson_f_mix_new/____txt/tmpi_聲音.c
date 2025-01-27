C# 二種方法控制系統音量/麥克風大小，

C# 二種方法控制系統音量/麥克風大小，

場景:在做播放設備的時候需要控制音量的大小，下面幾種方法將滿足你的要求

方法一: 改變系統音量設置


[DllImport("user32.dll")]
static extern void keybd_event(byte bVk, byte bScan, UInt32 dwFlags, UInt32 dwExtraInfo);
 
[DllImport("user32.dll")]
static extern Byte MapVirtualKey(UInt32 uCode, UInt32 uMapType);
 
private const byte VK_VOLUME_MUTE = 0xAD;
private const byte VK_VOLUME_DOWN = 0xAE;
private const byte VK_VOLUME_UP = 0xAF;
private const UInt32 KEYEVENTF_EXTENDEDKEY = 0x0001;
private const UInt32 KEYEVENTF_KEYUP = 0x0002;
 
/// <summary>
/// 改变系统音量大小，增加
/// </summary>
public void VolumeUp()
{
    keybd_event(VK_VOLUME_UP, MapVirtualKey(VK_VOLUME_UP, 0), KEYEVENTF_EXTENDEDKEY, 0);
    keybd_event(VK_VOLUME_UP, MapVirtualKey(VK_VOLUME_UP, 0), KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0);
}
 
/// <summary>
/// 改变系统音量大小，减小
/// </summary>
public void VolumeDown()
{
    keybd_event(VK_VOLUME_DOWN, MapVirtualKey(VK_VOLUME_DOWN, 0), KEYEVENTF_EXTENDEDKEY, 0);
    keybd_event(VK_VOLUME_DOWN, MapVirtualKey(VK_VOLUME_DOWN, 0), KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0);
}
 
/// <summary>
/// 改变系统音量大小，静音
/// </summary>
public void Mute()
{
    keybd_event(VK_VOLUME_MUTE, MapVirtualKey(VK_VOLUME_MUTE, 0), KEYEVENTF_EXTENDEDKEY, 0);
    keybd_event(VK_VOLUME_MUTE, MapVirtualKey(VK_VOLUME_MUTE, 0), KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0);
}

 

方法二: 改變程序音量，但不改變系統音量設置

 


[DllImport("Winmm.dll")]
private static extern int waveOutSetVolume(int hwo, System.UInt32 pdwVolume);
 
[DllImport("Winmm.dll")]
private static extern uint waveOutGetVolume(int hwo, out    System.UInt32 pdwVolume);  
#region 
 
private int volumeMinScope = 0;
private int volumeMaxScope = 100;
private int volumeSize = 100;
 
/// <summary>
/// 音量控制，但不改变系统音量设置
/// </summary>
public int VolumeSize
{
    get { return volumeSize; }
    set { volumeSize = value; }
}
 
public void SetCurrentVolume()
{
    if (volumeSize < 0)
    {
        volumeSize = 0;
    }
 
    if (volumeSize > 100)
    {
        volumeSize = 100;
    }
    System.UInt32 Value = (System.UInt32)((double)0xffff * (double)volumeSize / (double)(volumeMaxScope - v           
 
              olumeMinScope));//先把trackbar的value值映射到0x0000～0xFFFF范围
 
 
    //限制value的取值范围
    if (Value < 0)
    {
        Value = 0;
    }
 
    if (Value > 0xffff)
    {
        Value = 0xffff;
    }
 
    System.UInt32 left = (System.UInt32)Value;//左声道音量
    System.UInt32 right = (System.UInt32)Value;//右
    waveOutSetVolume(0, left << 16 | right); //"<<"左移，“|”逻辑或运算
}



