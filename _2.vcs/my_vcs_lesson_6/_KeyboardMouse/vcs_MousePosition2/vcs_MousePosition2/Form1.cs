using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_MousePosition2
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll")]
        public static extern bool GetCursorPos(out POINT lpPoint);

        [StructLayout(LayoutKind.Sequential)]
        public struct POINT
        {
            public int X;
            public int Y;
            public POINT(int x, int y)
            {
                this.X = x;
                this.Y = y;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            POINT pt = new POINT();
            GetCursorPos(out pt);
            //label1.Text = "滑鼠位置 : (" + pt.X.ToString() + ", " + pt.Y.ToString() + ")";    same
            label1.Text = "滑鼠位置 : (" + string.Format("X:{0}, Y:{1}", pt.X, pt.Y) + ")";

        }
    }
}

