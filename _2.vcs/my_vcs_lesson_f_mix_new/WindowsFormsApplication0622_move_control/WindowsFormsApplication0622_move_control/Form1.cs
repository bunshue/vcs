using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace WindowsFormsApplication0622_move_control
{
    public partial class Form1 : Form
    {
        [DllImportAttribute("user32.dll")]
        private extern static bool ReleaseCapture();
        [DllImportAttribute("user32.dll")]
        private extern static int SendMessage(IntPtr handle, int m, int p, int h);

        protected void MyBaseControl_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.Cursor = Cursors.SizeAll;
                ReleaseCapture();
                SendMessage(this.Handle, 0xA1, 0x2, 0);
                this.Cursor = Cursors.Default;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.MouseDown += new MouseEventHandler(MyBaseControl_MouseDown);
            this.button1.MouseDown += new MouseEventHandler(MyBaseControl_MouseDown);
            //this.pictureBox1.MouseDown += new MouseEventHandler(MyBaseControl_MouseDown);

        }
    }
}
