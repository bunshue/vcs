using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using CCWin.SkinControl;


namespace KenMusicPlayer
{

    public partial class KenRichTextBox : RichTextBox
    {

       /* public KenRichTextBox()
        {
            ControlStyles styles = ControlStyles.SupportsTransparentBackColor | ControlStyles.OptimizedDoubleBuffer;
            SetStyle(ControlStyles.SupportsTransparentBackColor, true);//使允许透明背景透明  
            SetStyle(ControlStyles.OptimizedDoubleBuffer, true);//使用双缓存
            base.CreateControl();
            InitializeComponent();
            base.BackColor = Color.Transparent;  //背景设透明色
        }*/

        //让背景透明
        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        private static extern IntPtr LoadLibrary(string lpFileName);
        protected override CreateParams CreateParams
        {
            get
            {
                CreateParams prams = base.CreateParams;
                if (LoadLibrary("msftedit.dll") != IntPtr.Zero)
                {
                    prams.ExStyle |= 0x020;
                    prams.ClassName = "RICHEDIT50W";
                }
                return prams;
            }
        }


        public KenRichTextBox()
        {
            InitializeComponent();
            this.GetType().GetProperty("DoubleBuffered", System.Reflection.BindingFlags.Instance | System.Reflection.BindingFlags.NonPublic).SetValue(this, true, null);
        }


        protected override void WndProc(ref Message m)
        {
            if (m.Msg == 0x7 || m.Msg == 0x201 || m.Msg == 0x202 || m.Msg == 0x203 || m.Msg == 0x204 || m.Msg == 0x205 || m.Msg == 0x206 || m.Msg == 0x0100 || m.Msg == 0x0101)
            {
                return;
            }
            base.WndProc(ref m);
        }

    }
}
