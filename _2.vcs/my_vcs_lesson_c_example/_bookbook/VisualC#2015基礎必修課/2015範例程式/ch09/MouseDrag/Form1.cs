using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MouseDrag
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool drag = false;//紀錄是否可拖曳，預設不可拖曳
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("../../cat1.gif");//載入cat1.gif
        }
        //滑鼠游標移入pictureBox1時
        private void pictureBox1_MouseEnter(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("../../cat3.gif");//載入cat3.gif
        }
        //滑鼠游標移出pictureBox1時
        private void pictureBox1_MouseLeave(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("../../cat1.gif");//載入cat1.gif
        }
        //在pictureBox1內按下滑鼠左鍵時
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)//若是按滑鼠左鍵
            {
                pictureBox1.Image = Image.FromFile("../../cat4.gif");//載入cat4.gif
                drag = true;//設drag=true，表可拖曳
            }
        }
        //滑鼠游標在pictureBox1內移動時
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (drag)//若設drag=true
            {   //將目前滑鼠的座標設為pictureBox1的座標
                pictureBox1.Left += e.X;
                pictureBox1.Top += e.Y;
            }
        }
        //在pictureBox1內放開滑鼠左鍵時
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            pictureBox1.Image = Image.FromFile("../../cat1.gif");//載入cat1.gif
            drag = false;//設drag=false，表不可拖曳
        }
    }
}
