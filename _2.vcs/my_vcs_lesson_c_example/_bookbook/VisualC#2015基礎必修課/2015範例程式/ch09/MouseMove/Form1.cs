using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MouseMove
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool move = false;//紀錄圖片是否隨滑鼠移動

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("../../cat1.gif");//載入cat1.gif
        }
        //在表單上按一下左鍵時
        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            pictureBox1.Image = Image.FromFile("../../cat2.gif");//載入cat2.gif
            move = true;//設圖片隨滑鼠移動
        }
        //滑鼠在表單上移動時
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (move == true)//若move == true
            {
                pictureBox1.Left = e.X + 2;//pictureBox1的Left = 滑鼠的X + 2
                pictureBox1.Top = e.Y + 2;//pictureBox1的Top = 滑鼠的Y + 2
            }
        }
        //在表單上快按兩下左鍵時
        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            pictureBox1.Image = Image.FromFile("../../cat1.gif");//載入cat1.gif
            move = false;//設圖片不隨滑鼠移動
        }
    }
}
