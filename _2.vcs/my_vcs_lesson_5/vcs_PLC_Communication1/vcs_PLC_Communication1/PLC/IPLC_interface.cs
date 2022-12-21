using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;

namespace vcs_PLC_Communication1.PLC_Communication
{
    /// <summary>
    /// PLC實現接口--規範定義的方法名稱Mitsubishi_realize
    /// </summary>
    public interface IPLC_interface//規範定義的方法名稱
    {
        /// <summary>
        /// PLC IP與端口
        /// </summary>
        IPEndPoint IPEndPoint { get; set; }
        /// <summary>
        /// PLC準備好
        /// </summary>
        bool PLC_ready { get; }//PLC準備好
        /// <summary>
        /// 打開PLC
        /// </summary>
        /// <returns></returns>
        string PLC_open();//打開PLC
        /// <summary>
        /// 讀取--位
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <returns></returns>
        List<bool> PLC_read_M_bit(string Name, string id);//讀取--位
        /// <summary>
        /// /寫入--位
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="button_State"></param>
        /// <returns></returns>
        List<bool> PLC_write_M_bit(string Name, string id, Button_state button_State);//寫入--位
        /// <summary>
        /// /讀取--字
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="format"></param>
        /// <returns></returns>
        string PLC_read_D_register(string Name, string id, numerical_format format);//讀取--字
        /// <summary>
        /// 讀寫--字
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="content"></param>
        /// <param name="format"></param>
        /// <returns></returns>
        string PLC_write_D_register(string Name, string id, string content, numerical_format format);//讀寫--字
    }
}
