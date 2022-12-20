using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using CCWin.SkinClass;
using vcs_PLC_Communication1.PLC_protocol.mitsubishi;

namespace vcs_PLC_Communication1.PLC_protocol
{
    /// <summary>
    /// 本类是共用类 
    /// </summary>
    public class PLC_public_Class: Mitsubishi_message
    {
        /// <summary>
        /// 指示着其他用户正在访问
        /// </summary>
        public static bool PLC_busy;//指示着其他用户正在访问

        /// <summary>
        /// 解析Y点线圈状态
        /// </summary>
        /// <param name="Data"></param>
        /// <param name="address"></param>
        /// <returns></returns>
        public bool Analysis(byte[] Data, int address)
        {
            int len = 0;//Y点读取位置
            int inx = 0;//尾部位置
            switch (address.ToString().Length)
            {
                case 1:
                    len = 1;
                    inx = address;
                    break;
                case 2:
                    len = Convert.ToInt32(address.ToString().Remove(1, 1)) % 2 > 0 ? 2 : 1;
                    inx = Convert.ToInt32(address.ToString().Remove(0, 1));
                    break;
                case 3:
                    len = Convert.ToInt32(address.ToString().Remove(2, 2)) % 2 > 0 ? 2 : 1;
                    inx = Convert.ToInt32(address.ToString().Remove(0, 2));
                    break;
            }
            if (len > 1)
            {
                int a = 15 + (inx / 2);
                return Y_ysis(Data[15 + (inx / 2)], inx);
            }
            return Y_ysis(Data[11 + (inx / 2)], inx);
        }
        private bool Y_ysis(byte Data, int inx)
        {
            switch (Data)
            {
                case 1:
                    if (inx % 2 == 1)
                        return true;
                    else
                        return false;
                case 16:
                    if (inx % 2 == 1)
                        return false;
                    else
                        return true;
                case 17:
                    if (inx % 2 == 1)
                        return true;
                    else
                        return true;
                case 0:
                    if (inx % 2 == 1)
                        return false;
                    else
                        return false;
            }
            return false;
        }
    }
}
