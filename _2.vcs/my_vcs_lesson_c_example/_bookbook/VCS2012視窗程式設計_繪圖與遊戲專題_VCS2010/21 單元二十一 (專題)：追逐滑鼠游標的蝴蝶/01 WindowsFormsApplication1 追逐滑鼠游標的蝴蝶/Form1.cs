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
        NPC npc;
        Point MousePos = new Point();

        //Image 
        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(800, 600);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Rectangle rect = new Rectangle(0, 0, this.ClientSize.Width, this.ClientSize.Height);
            npc = new NPC(Properties.Resources.Butterfly);
            npc.SetLocation(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            npc.SetAngle(0, -90);
            npc.SetBoundary(rect); // 設定視窗客戶區的邊界
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            npc.Update(MousePos);

            //npc.Turn(1);
            npc.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Up)
            {
                npc.ChangeSpeed(1);
            }
            else if (e.KeyCode == Keys.Down)
            {
                npc.ChangeSpeed(-1);
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            MousePos.X = e.X;
            MousePos.Y = e.Y;
        }
    }
}