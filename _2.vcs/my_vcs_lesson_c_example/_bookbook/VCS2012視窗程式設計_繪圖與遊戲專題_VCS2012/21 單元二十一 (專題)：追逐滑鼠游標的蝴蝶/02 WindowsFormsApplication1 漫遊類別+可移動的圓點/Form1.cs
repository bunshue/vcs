using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        GC_2D_Wander gc; // 宣告一個物件
        GC_2D_MovableCircle cir;

        public Form1()
        {
            InitializeComponent();
            gc = new GC_2D_Wander(Properties.Resources.png_0729);
            cir = new GC_2D_MovableCircle(20, new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2));
            gc.Update();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            gc.Wander_Center = cir.pos;
            gc.Update();
            this.Invalidate();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.ResetTransform();
            cir.Draw(e.Graphics);
            gc.Draw(e.Graphics);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            cir.CheckSelected(e.X, e.Y);
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            cir.dragging = false;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            cir.Update(e.X, e.Y);
        }
    }
}
