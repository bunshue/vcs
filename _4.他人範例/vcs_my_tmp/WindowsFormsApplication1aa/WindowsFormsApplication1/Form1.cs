using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//using System.Net.NetworkInformation;
//using System.Net.Sockets;
//using System.Net;

using System.Runtime.InteropServices;   //for dll

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("wininet.dll", EntryPoint = "InternetGetConnectedState")]
        public extern static bool InternetGetConnectedState(out int conState, int reder);

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = "當前滑鼠位置為(" + e.X + "，" + e.Y + ")";
        }

        public bool IsConnectedToInternet()
        {
            int Desc = 0;
            return InternetGetConnectedState(out  Desc, 0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (IsConnectedToInternet())
                MessageBox.Show("網路OK", "AAAA");
            else
                MessageBox.Show("無網路", "BBBB");

        }

        private void button4_Click(object sender, EventArgs e)
        {
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值

            Graphics g = this.CreateGraphics();

            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);
                Pen p = new Pen(SBrush, 1);
                g.DrawLine(p, 400, 50 + i, 500, 50 + i);


            }

        }

    }
}
