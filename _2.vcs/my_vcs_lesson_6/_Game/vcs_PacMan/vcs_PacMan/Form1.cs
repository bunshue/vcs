using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PacMan
{
    public partial class Form1 : Form
    {
        Graphics g;
        //Single x = 0, y = 0, angle = 0;
        //Single angle = 0;
        //Single mode = 1;
        Single radiox = 1, radioy = 1;
        int center_x = 200;
        int center_y = 200;
        float radius = 150;
        int pacman_start_angle = 320;

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            //int linewidth = (int)numericUpDown_linewidth2.Value;
            int linewidth = 5;
            // Create a Graphics object for the Control.
            //Graphics g = pictureBox1.CreateGraphics();

            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(bt_color2.BackColor);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(Color.Red, linewidth);

            // Draw the circle
            g.DrawEllipse(p, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            p.Dispose();
        }

        private void DrawPacman(int center_x, int center_y, float radius)
        {
            // Create a Graphics object for the Control.
            //Graphics g = this.CreateGraphics();

            // Create a new brush.
            Brush brush = new SolidBrush(Color.Blue);

            g.FillPie(brush, new Rectangle(center_x - (int)radius, center_y - (int)radius, (int)radius * 2, (int)radius * 2), pacman_start_angle, -280);
            label2.Text = "pacman_start_angle = " + pacman_start_angle.ToString();

            //Dispose of the brush.
            brush.Dispose();

            //Pacman's eye  TBD
            //DrawCircle(center_x + (int)(radius * 0.5 * Math.Cos(pacman_start_angle + 30)), (int)(center_y - radius * 0.5 * Math.Sin(pacman_start_angle + 30)), 5);
            //DrawCircle(center_x + (int)(radius * 0.5 * Math.Cos(pacman_start_angle - 30)), (int)(center_y - radius * 0.5 * Math.Sin(pacman_start_angle - 30)), 5);
        }

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new System.Drawing.Size(800, 600);
            label4.Text = "";
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            Brush brush = new SolidBrush(Color.Blue);
            DrawPacman(center_x, center_y, radius);
            label1.Text = "W = " + this.Size.Width.ToString() + " H = " + this.Size.Height.ToString() + " x = " + center_x.ToString() + " y = " + center_y.ToString() + " r = " + radius.ToString();
            //g.DrawRectangle(new Pen(Color.Black), new Rectangle(10, 10, this.Size.Width - 30, this.Size.Height - 50));
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(10, 10, this.ClientSize.Width - 20, this.ClientSize.Height - 20));
        }

        int step = 10;
        void check_boundary()
        {
            bool beep = false;
            int w = this.ClientSize.Width - 10;
            int h = this.ClientSize.Height - 10;
            //MessageBox.Show("W = " + this.Size.Width.ToString() + "H = " + this.Size.Height.ToString());

            if ((center_x + radius) > w)
            {
                center_x -= step;
                label4.Text = "好痛";
                beep = true;
            }
            if ((center_x - radius) < 10)
            {
                center_x += step;
                label4.Text = "好痛";
                beep = true;
            }
            if ((center_y + radius) > h)
            {
                center_y -= step;
                label4.Text = "好痛";
                beep = true;
            }
            if ((center_y - radius) < 10)
            {
                center_y += step;
                label4.Text = "好痛";
                beep = true;
            }
            if (beep == true)
                System.Media.SystemSounds.Beep.Play();
            else
            {
                System.Media.SystemSounds.Exclamation.Play();
                label4.Text = "";
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Up:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        //MessageBox.Show("+");
                        radiox *= 1.1F;
                        radioy *= 1.1F;
                        radius *= 1.1F;
                        if(radius > 200)
                            label4.Text = "長太胖了";
                        check_boundary();
                    }
                    else
                    {
                        //MessageBox.Show("上");
                        pacman_start_angle = 230;
                        center_x += 00;
                        center_y += -step;
                        check_boundary();
                    }
                    this.Refresh();
                    break;
                case Keys.Down:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        //MessageBox.Show("-");
                        radiox *= 0.9F;
                        radioy *= 0.9F;
                        radius *= 0.9F;
                        if (radius < 30)
                        {
                            label4.Text = "不能再小了";
                            radius = 30;
                        }
                        check_boundary();
                    }
                    else
                    {
                        //MessageBox.Show("下");
                        pacman_start_angle = 50;
                        center_x += 00;
                        center_y += step;
                        check_boundary();
                    }
                    this.Refresh();
                    break;
                case Keys.Left:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        pacman_start_angle -= 3;
                    }
                    else
                    {
                        //MessageBox.Show("左");
                        pacman_start_angle = 140;
                        center_x += -step;
                        center_y += 0;
                        check_boundary();
                    }
                    this.Refresh();
                    break;
                case Keys.Right:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        pacman_start_angle += 3;
                    }
                    else
                    {
                        //MessageBox.Show("右");
                        pacman_start_angle = 320;
                        center_x += step;
                        center_y += 0;
                        check_boundary();
                    }
                    this.Refresh();
                    break;
                case Keys.Add:
                    //MessageBox.Show("+");
                    radiox *= 1.1F;
                    radioy *= 1.1F;
                    radius *= 1.1F;
                    check_boundary();
                    if(radius > 200)
                        label4.Text = "長太胖了";
                    this.Refresh();
                    break;
                case Keys.Subtract:
                    //MessageBox.Show("-");
                    radiox *= 0.9F;
                    radioy *= 0.9F;
                    radius *= 0.9F;
                    check_boundary();
                    if (radius < 30)
                    {
                        label4.Text = "不能再小了";
                        radius = 30;
                    }
                    this.Refresh();
                    break;
                case Keys.X:
                    //MessageBox.Show("X");
                    Application.Exit();
                    break;
                case Keys.M:
                    pacman_start_angle += 3;
                    this.Refresh();
                    break;
                case Keys.N:
                    pacman_start_angle -= 3;
                    this.Refresh();
                    break;
                default:
                    //MessageBox.Show("x, KeyCode: " + e.KeyCode.ToString());
                    break;
            }
        }

    }
}
