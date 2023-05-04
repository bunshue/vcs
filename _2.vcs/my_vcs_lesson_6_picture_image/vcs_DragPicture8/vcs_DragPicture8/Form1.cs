using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_DragPicture8
{
    public partial class vcs_DragPicture8 : Form
    {
        public vcs_DragPicture8()
        {
            InitializeComponent();
        }
        /// <summary>
        /// 本实例需设置窗体的FormBorderStyle属性为None、设置ContextMenuStrip属性为当前添加的实例
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>

        #region 本程序中用到的API函数
        [DllImport("user32.dll")]
        public static extern bool ReleaseCapture();  //用来释放被当前线程中某个窗口捕获的光标

        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwdn,int wMsg,int mParam,int lParam);//向指定的窗体发送Windows消息
        #endregion

        #region 本程序中需要声明的变量
        public const int WM_SYSCOMMAND = 0x0112;
        public const int SC_MOVE = 0xF010;
        public const int HTCAPTION = 0x0002;
        #endregion


        private void ExitContext_Click(object sender, EventArgs e)
        {
            Application.Exit();   //退出本程序
        }

        private void vcs_DragPicture8_MouseDown(object sender, MouseEventArgs e)
        {
            ReleaseCapture();
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0);
        }

        private void vcs_DragPicture8_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\picture1.jpg";
            this.BackgroundImage = Image.FromFile(filename);//设置窗体的背景图片
            this.Size = this.BackgroundImage.Size;
        }
    }
}
