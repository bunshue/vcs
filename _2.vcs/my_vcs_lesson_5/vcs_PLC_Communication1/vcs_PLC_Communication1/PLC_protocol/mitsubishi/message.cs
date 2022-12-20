using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace vcs_PLC_Communication1.PLC_protocol.mitsubishi
{
    /// <summary>
    /// 可访问设备的软元件-类型是bit位
    /// 请指定读取、写入数据的对象模块中存在的软元件
    /// </summary>
    public enum message_bit
    {
        /// <summary>
        /// 内部用户软元件
        /// 内部继电器
        /// </summary>
        M = 0x90,
        /// <summary>
        /// 系统软元件 
        /// 特殊继电器
        /// </summary>
        SM = 0x91,
        /// <summary>
        /// 内部用户软元件
        /// 输入
        /// </summary>
        X = 0x9C,
        /// <summary>
        /// 内部用户软元件
        /// 输出
        /// </summary>
        Y = 0x9D,
        /// <summary>
        /// 内部用户软元件
        /// 锁存继电器
        /// </summary>
        L = 0x92,
        /// <summary>
        /// 内部用户软元件
        /// 报警器
        /// </summary>
        F = 0x93,
        /// <summary>
        /// 内部用户软元件
        /// 变址继电器
        /// </summary>
        V = 0x94,
        /// <summary>
        /// 内部用户软元件
        /// 定时器-位触点
        /// </summary>
        TS = 0xC1,
        /// <summary>
        /// 内部用户软元件
        /// 定时器-线圈
        /// </summary>
        TC = 0xC2,
        /// <summary>
        /// 内部用户软元件
        /// 累计定时器-触点
        /// </summary>
        SS = 0xC7,
        /// <summary>
        /// 内部用户软元件
        /// 累计定时器-线圈
        /// </summary>
        SC = 0xC6,
        /// <summary>
        /// 内部用户软元件
        /// 计数器-触点
        /// </summary>
        CS = 0xC4,
        /// <summary>
        /// 内部用户软元件
        /// 计数器-线圈
        /// </summary>
        CC = 0xC3,
        /// <summary>
        /// 内部用户软元件
        /// 链接特殊继电器
        /// </summary>
        SB = 0xA1,
        /// <summary>
        /// 内部用户软元件
        /// 步继电器
        /// </summary>
        S = 0x98,
    }
}
