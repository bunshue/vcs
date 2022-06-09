using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_Ladybug
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        //漫遊演算法 ST
        GC_2D_Wander gc; // 宣告一個物件
        //GC_2D_MovableCircle cir;
        //漫遊演算法 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //漫遊演算法 ST
            string filename2 = @"C:\______test_files\__RW\_png\ladybug.png";
            gc = new GC_2D_Wander(new Bitmap(filename2));
            //cir = new GC_2D_MovableCircle(20, new Point(this.pictureBox2.ClientSize.Width / 2, this.pictureBox2.ClientSize.Height / 2));
            gc.Update();
            //漫遊演算法 SP


            pictureBox2.Size = new Size(1920 / 2, 1080 / 2);
            pictureBox2.Location = new Point(0, 0);

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;


        }


        //漫遊演算法 ST
        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            //cir.CheckSelected(e.X, e.Y);
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            //cir.Update(e.X, e.Y);
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            //cir.dragging = false;
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.ResetTransform();
            //cir.Draw(e.Graphics);
            gc.Draw(e.Graphics);
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            //gc.Wander_Center = new PointF(1920 / 4, 1080 / 4);
            gc.Update();
            this.pictureBox2.Invalidate();
        }

        //漫遊演算法 SP


    }
}
