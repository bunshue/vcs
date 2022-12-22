using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
//using System.Net.Sockets;
//using System.Threading;
using System.ComponentModel;

using vcs_PLC_Communication1.PLC_Communication;

namespace vcs_PLC_Communication1.SetupControls
{
    //==============================================================
    //  作者：BAtoDA
    //  文件名：PLC_Open_Time 
    //  說明： 實現後台打開與重鏈PLC控件
    //==============================================================
    /// <summary>
    /// PLC後台定時打開,刷新,重新鏈接控件
    /// </summary>
    public class PLC_Open_Time : Timer
    {
        //三菱PLC配置屬性
        public string MitsubishiIP
        {
            get
            {
                return Mitsubishi_ip.ToString();
            }
            set
            {
                Mitsubishi_ip = IPAddress.Parse("192.168.3.39");
            }
        }

        private IPAddress Mitsubishi_ip = IPAddress.Parse("192.168.3.39");
        public int MitsubishiPort { get; set; } = 4999;
        public bool Mitsubishi_Open { get; set; } = false;

        #region PLC通訊對象
        /// <summary>
        /// 三菱通訊對象
        /// </summary>
        static IPLC_interface Mitsubishi = new Mitsubishi_realize();
        /// <summary>
        /// 全局鎖 指示該控件只能添加一個 
        /// </summary>
        static bool Lock_control;
        /// <summary>
        /// 全局鎖異常標志位
        /// </summary>
        private bool lock_err;
        #endregion

        /// <summary>
        /// 構造函數
        /// </summary>
        public PLC_Open_Time()
        {
            if (Lock_control)
            {
                lock_err = true;
                //throw new Exception("該控件不能重復添加");
            }
            Lock_control = true;
            //配置該控件默認參數
            this.Enabled = false;
            this.Interval = 500;
            //mutex = new Mutex();
            //配置PLC參數
            Mitsubishi.IPEndPoint = new IPEndPoint(Mitsubishi_ip, MitsubishiPort);
        }
        protected override void OnTick(EventArgs e)//重寫定時器到達事件
        {
            lock (this)
            {
                //配置PLC參數
                if (Mitsubishi_Open & !Mitsubishi.PLC_ready)
                {
                    Mitsubishi.IPEndPoint.Address = Mitsubishi_ip;
                    Mitsubishi.IPEndPoint.Port = MitsubishiPort;
                    string result = Mitsubishi.PLC_open();
                    Console.WriteLine("開啟 PLC, IP : " + Mitsubishi.IPEndPoint.Address + ", port : "
                        + Mitsubishi.IPEndPoint.Port + "\t結果 : " + result);
                }
                else
                {
                    //Console.WriteLine("PLC 已開啟");

                }
            }
        }
        protected override void Dispose(bool disposing)//重寫釋放托管資源方法
        {
            base.Dispose(disposing);
            if (!lock_err)
            {
                Lock_control = false;
            }
            lock_err = false;
        }
    }
}
