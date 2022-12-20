using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace vcs_PLC_Communication1
{
    /// <summary>
    ///  PLC--按钮状态
    /// </summary>
    public enum Button_state
    {
        Off, ON
    }
    /// <summary>
    /// 数值显示类型
    /// </summary>
    public enum numerical_format
    {
        BCD_16_Bit,     //0
        BCD_32_Bit,
        Hex_16_Bit,
        Hex_32_Bit,
        Binary_16_Bit,
        Binary_32_Bit,      //5
        Unsigned_16_Bit,
        Signed_16_Bit,
        Unsigned_32_Bit,
        Signed_32_Bit,
        Float_32_Bit,       //10
        String_32_Bit       //11
    }
}
