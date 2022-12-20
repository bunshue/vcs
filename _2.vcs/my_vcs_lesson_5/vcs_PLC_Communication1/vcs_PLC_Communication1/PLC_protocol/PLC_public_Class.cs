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
        /// 转换类型---shorot--list<int>根据需要读取个数返回泛型表--三菱专用
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="format"></param>
        /// <returns></returns>
        public List<int> Mitsubishi_to_Index_numerical(string Name,int id, numerical_format format,int Index,IPLC_interface pLC_Interface)//转换类型---shorot--string
        {
            List<int> data = new List<int>();//初始化数据表
            for (int i=0;i<Index+1;i++)
                switch (format)
                {
                    case numerical_format.BCD_16_Bit:
                    case numerical_format.Binary_16_Bit:
                    case numerical_format.Hex_16_Bit:
                    case numerical_format.Signed_16_Bit:
                    case numerical_format.Unsigned_16_Bit:
                        data.Add(pLC_Interface.PLC_read_D_register(Name, (id + i).ToString(), format).ToInt32());//获取读取到的数据添加到泛型表
                        break;
                    case numerical_format.Binary_32_Bit:
                    case numerical_format.Float_32_Bit:
                    case numerical_format.Hex_32_Bit:
                    case numerical_format.Signed_32_Bit:
                    case numerical_format.Unsigned_32_Bit:
                    case numerical_format.BCD_32_Bit:
                        data.Add(pLC_Interface.PLC_read_D_register(Name, (id + (i*2)).ToString(), format).ToInt32());//获取读取到的数据添加到泛型表
                        break;
                }
            return data;//返回数据
        }

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
