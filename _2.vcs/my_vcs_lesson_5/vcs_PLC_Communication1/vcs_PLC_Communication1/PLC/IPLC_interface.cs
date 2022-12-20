using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace vcs_PLC_Communication1.PLC_Communication
{
    /// <summary>
    /// PLC实现接口--规范定义的方法名称Mitsubishi_realize
    /// </summary>
    public interface IPLC_interface//规范定义的方法名称
    {
        /// <summary>
        /// PLC IP与端口
        /// </summary>
        IPEndPoint IPEndPoint { get; set; }
        /// <summary>
        /// PLC准备好
        /// </summary>
        bool PLC_ready { get; }//PLC准备好
        /// <summary>
        /// 打开PLC
        /// </summary>
        /// <returns></returns>
        string PLC_open();//打开PLC
        /// <summary>
        /// 读取--位
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <returns></returns>
        List<bool> PLC_read_M_bit(string Name, string id);//读取--位
        /// <summary>
        /// /写入--位
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="button_State"></param>
        /// <returns></returns>
        List<bool> PLC_write_M_bit(string Name, string id, Button_state button_State);//写入--位
        /// <summary>
        /// /读取--字
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="format"></param>
        /// <returns></returns>
        string PLC_read_D_register(string Name, string id, numerical_format format);//读取--字
        /// <summary>
        /// 读写--字
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="content"></param>
        /// <param name="format"></param>
        /// <returns></returns>
        string PLC_write_D_register(string Name, string id, string content, numerical_format format);//读写--字
    }
}
