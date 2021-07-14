using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;



namespace KenMusicPlayer
{    
    public partial class TMFormWin : Form
    {
        private const int WM_NCHITTEST = 0x84;
        private const int HTCLIENT = 0x01;
        private const int HTCAPTION = 0x02;
        private const int WM_SYSCOMMAND = 0x112;
        private const int SC_MAXMIZE = 0xF030;
        private const int WM_NCLBUTTONDBLCLK = 0xA3;
        private const int WM_MOUSEMOVE = 0x200;

        /// <summary>
        /// 重写窗口消息处理函数，就是为了实现鼠标拖动窗体和禁止双击最大化
        /// </summary>
        /// <param name="m"></param>
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_MOUSEMOVE:
                    base.WndProc(ref m);
                    this.Focus();
                    break;
                case 0x4e:
                case 0xd:
                case 0xe:
                case 0x14:
                    base.WndProc(ref m);
                    break;
                case WM_NCHITTEST://鼠标点任意位置后可以拖动窗体
                    base.WndProc(ref m);
                    if (m.Result.ToInt32() == HTCLIENT)
                    {
                        m.Result = new IntPtr(HTCAPTION);
                        return;
                    }
                    break;
                case WM_NCLBUTTONDBLCLK://禁止双击最大化
                    //base.WndProc(ref m);
                    Console.WriteLine(this.WindowState);
                    return;
                    break;

                default:

                    base.WndProc(ref m);
                    break;
            }
        }

        public TMFormWin()
        {         
            InitializeComponent();            
        }

    }
}
