using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace mouse_event
{
    public partial class Form1 : Form
    {
        [DllImport("User32")]
        internal extern static bool GetCursorPos(out MousePoint point);

        internal struct MousePoint
        {
            public int x;
            public int y;
        };

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MousePoint point;
            GetCursorPos(out point);
            richTextBox1.Text += point.x.ToString() + ", " + point.y.ToString() + "\n";
        }
    }
}
