using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace OpenUpOrClosureClamourDevice
{
    public partial class Form1 : Form
    {
        [DllImport("winmm.dll", EntryPoint = "mciSendString")]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, System.UInt16 uReturnLength, System.IntPtr HwndCallback);
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        private void button1_Click(object sender, EventArgs e)
        {
            int i = mciSendString("Set cdaudio door open wait", "", 0, this.Handle);

            if (i == 0)
            {
                MessageBox.Show("CD_ROM打開");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i = mciSendString("Set cdaudio door Closed wait", "", 0, this.Handle);
            if (i == 0)
            {
                MessageBox.Show("CD_ROM關閉");
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}