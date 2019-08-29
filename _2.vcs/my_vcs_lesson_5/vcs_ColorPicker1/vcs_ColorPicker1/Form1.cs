using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;   //for dll

namespace vcs_ColorPicker1
{
    public partial class Form1 : Form
    {
        bool flag_small_mode = true;

        Graphics g;
        Font f;
        Bitmap bmp;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.TopMost = true;

            if (flag_small_mode == true)
            {
                checkBox1.Visible = false;
                panel1.Visible = false;
                label1.Visible = false;
                label2.Visible = false;
                label3.Visible = false;
                txtColor.Visible = false;
                txtPoint.Visible = false;
                txtRGB.Visible = false;

                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                //this.Location = new System.Drawing.Point(x_st, y_st);
                this.Location = new System.Drawing.Point(1200, 0);

                this.FormBorderStyle = FormBorderStyle.None;
                
                this.Size = new Size(240, 55);

                g = this.CreateGraphics();
                


            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                this.TopMost = true;
            }
            else
            {
                this.TopMost = false;
            }

        }

        [DllImport("gdi32.dll")]
        static public extern uint GetPixel(IntPtr hDC, int XPos, int YPos);
        [DllImport("gdi32.dll")]
        static public extern IntPtr CreateDC(string driverName, string deviceName, string output, IntPtr lpinitData);
        [DllImport("gdi32.dll")]
        static public extern bool DeleteDC(IntPtr DC);
        static public byte GetRValue(uint color)
        {
            return (byte)color;
        }
        static public byte GetGValue(uint color)
        {
            return ((byte)(((short)(color)) >> 8));
        }
        static public byte GetBValue(uint color)
        {
            return ((byte)((color) >> 16));
        }
        static public byte GetAValue(uint color)
        {
            return ((byte)((color) >> 24));
        }
        public Color GetColor(Point screenPoint)
        {
            IntPtr displayDC = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint colorref = GetPixel(displayDC, screenPoint.X, screenPoint.Y);
            DeleteDC(displayDC);
            byte Red = GetRValue(colorref);
            byte Green = GetGValue(colorref);
            byte Blue = GetBValue(colorref);
            return Color.FromArgb(Red, Green, Blue);
        }

        int cnt = 0;
        Brush b = new SolidBrush(Color.White);
        Color cl_old;

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_small_mode == true)
            {
                Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                Color cl = GetColor(pt);
                if (cl_old != cl)
                {
                    cnt = 0;
                    g.Clear(BackColor);

                    g.DrawString(cl.R.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5, 5));
                    g.DrawString(cl.G.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Green), new PointF(5 + 75, 5));
                    g.DrawString(cl.B.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 150, 5));

                    cl_old = cl;
                }
                else
                {
                    cnt++;
                    if ((cnt > 25) && (cnt % 5) == 0)
                    {
                        g.Clear(BackColor);
                        g.DrawString(DateTime.Now.ToString("HH:mm:ss"), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(20, 5));
                    }

                }

            }
            else
            {
                txtPoint.Text = Control.MousePosition.X.ToString() + "," + Control.MousePosition.Y.ToString();
                Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                Color cl = GetColor(pt);
                panel1.BackColor = cl;
                txtRGB.Text = cl.R + "," + cl.G + "," + cl.B;
                txtColor.Text = ColorTranslator.ToHtml(cl).ToString();
            }
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************

        #region 移動無邊框Form
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }

        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }

        }
        #endregion
    }
}
