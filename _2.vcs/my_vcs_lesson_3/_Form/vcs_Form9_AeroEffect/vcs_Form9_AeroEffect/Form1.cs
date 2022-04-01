using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//C#實現具有Aero效果的窗體

using System.Runtime.InteropServices;

namespace vcs_Form9_AeroEffect
{
    public partial class Form1 : Form
    {
        [DllImport("dwmapi.dll")]
        public static extern int DwmExtendFrameIntoClientArea(IntPtr hWnd, ref MARGINS pMarinset);
        [StructLayout(LayoutKind.Sequential)]
        public struct MARGINS
        {
            public int Right;
            public int left;
            public int Top;
            public int Bottom;
        }  

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackgroundImage = null;
            MARGINS margins = new MARGINS();
            margins.left = 20;
            margins.Right = 20;
            margins.Top = 20;
            margins.Bottom = 20;
            IntPtr hwnd = Handle;
            int result = DwmExtendFrameIntoClientArea(hwnd, ref margins);
            this.BackColor = Color.Black;
            this.label1.BackColor = Color.Transparent;
            this.label1.ForeColor = Color.White;  
        }
    }
}
