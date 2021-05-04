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
            picCat.Image = Image.FromFile("cat1.gif");//載入cat1.gif
        }
        //滑鼠游標移入picCat時
        private void picCat_MouseEnter(object sender, EventArgs e)
        {
            picCat.Image = Image.FromFile("cat3.gif");//載入cat3.gif
        }
        //滑鼠游標移出picCat時
        private void picCat_MouseLeave(object sender, EventArgs e)
        {
            picCat.Image = Image.FromFile("cat1.gif");//載入cat1.gif
        }
        //在picCat內按下滑鼠左鍵時
        private void picCat_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)//若是按滑鼠左鍵
            {
                picCat.Image = Image.FromFile("cat4.gif");//載入cat4.gif
                drag = true;//設drag=true，表可拖曳
            }
        }
        //滑鼠游標在picCat內移動時
        private void picCat_MouseMove(object sender, MouseEventArgs e)
        {
            if (drag)//若設drag=true
            {   //將目前滑鼠的座標設為picCat的座標
                picCat.Left += e.X;
                picCat.Top += e.Y;
            }
        }
        //在picCat內放開滑鼠左鍵時
        private void picCat_MouseUp(object sender, MouseEventArgs e)
        {
            picCat.Image = Image.FromFile("cat1.gif");//載入cat1.gif
            drag = false;//設drag=false，表不可拖曳
        }
    }
}
