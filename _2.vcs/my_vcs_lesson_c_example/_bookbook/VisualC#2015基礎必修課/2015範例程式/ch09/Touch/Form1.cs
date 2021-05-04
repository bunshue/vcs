using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Touch
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool drag = false;//記錄是否可拖曳，預設不可拖曳
        int sX, sY;       //記錄滑鼠按下時的座標值

        private void Form1_Load(object sender, EventArgs e)
        {
            this.MouseWheel += new MouseEventHandler(lbl_Zoom);
        }

        private void lbl_Zoom(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0)
            { lblTouch.Width += 5; lblTouch.Height += 5; }
            else
            { lblTouch.Width -= 5; lblTouch.Height -= 5; }
        }

        private void lblTouch_Click(object sender, EventArgs e)
        {
            lblTouch.Text = "點按";
        }

        private void lblTouch_DoubleClick(object sender, EventArgs e)
        {
            lblTouch.Text = "快按兩下";
        }

        private void lblTouch_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
                lblTouch.Text = "長按";
            else
                lblTouch.Text = "點按";
        }

        private void lblTouch_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)  //若是按滑鼠左鍵
            {
                drag = true;//設drag=true，表可拖曳
                sX = e.X;sY = e.Y;  //記錄滑鼠的座標值
            }
        }

        private void lblTouch_MouseMove(object sender, MouseEventArgs e)
        {
            if (drag)      //若設drag=true
            {
                lblTouch.Left += e.X-sX;
                lblTouch.Top += e.Y-sY;
            }
        }

        private void lblTouch_MouseUp(object sender, MouseEventArgs e)
        {
            drag = false; //設drag=false，表不可拖曳
        }
    }
}
