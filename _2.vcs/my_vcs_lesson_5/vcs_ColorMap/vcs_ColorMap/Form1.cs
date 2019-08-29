using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ColorMap
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;

        int[,] rgb_array = new int[64, 3] {
{   0,   0, 143},
{   0,   0, 159},
{   0,   0, 175},
{   0,   0, 191},
{   0,   0, 207},
{   0,   0, 223},
{   0,   0, 239},
{   0,   0, 255},
{   0,  16, 255},
{   0,  32, 255},
{   0,  48, 255},
{   0,  64, 255},
{   0,  80, 255},
{   0,  96, 255},
{   0, 112, 255},
{   0, 128, 255},
{   0, 143, 255},
{   0, 159, 255},
{   0, 175, 255},
{   0, 191, 255},
{   0, 207, 255},
{   0, 223, 255},
{   0, 239, 255},
{   0, 255, 255},
{  16, 255, 239},
{  32, 255, 223},
{  48, 255, 207},
{  64, 255, 191},
{  80, 255, 175},
{  96, 255, 159},
{ 112, 255, 143},
{ 128, 255, 128},
{ 143, 255, 112},
{ 159, 255,  96},
{ 175, 255,  80},
{ 191, 255,  64},
{ 207, 255,  48},
{ 223, 255,  32},
{ 239, 255,  16},
{ 255, 255,   0},
{ 255, 239,   0},
{ 255, 223,   0},
{ 255, 207,   0},
{ 255, 191,   0},
{ 255, 175,   0},
{ 255, 159,   0},
{ 255, 143,   0},
{ 255, 128,   0},
{ 255, 112,   0},
{ 255,  96,   0},
{ 255,  80,   0},
{ 255,  64,   0},
{ 255,  48,   0},
{ 255,  32,   0},
{ 255,  16,   0},
{ 255,   0,   0},
{ 239,   0,   0},
{ 223,   0,   0},
{ 207,   0,   0},
{ 191,   0,   0},
{ 175,   0,   0},
{ 159,   0,   0},
{ 143,   0,   0},
{ 128,   0,   0}
};


        int[,] rgb_array2 = new int[12, 3] {
{0     ,0     ,0},
{255   ,255   ,255},
{255     ,0     ,0},
{0   ,255     ,0},
{0     ,0   ,255},
{255   ,255     ,0},
{255     ,0   ,255},
{0   ,255   ,255},
{128   ,128   ,128},
{128     ,0     ,0},
{255   ,158   ,102},
{125   ,255   ,212}
};

        string[] rgb_array2_name = new string[] {
"black（黑）","white（白）","red（紅）","green（綠）",
"blue（藍）","yellow（黃）","magenta（錳紫）","cyan（青藍）",
"gray（灰）","dark red（暗紅）","copper（銅色）","aquamarine（碧綠）"};



        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 6);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            g.Clear(Color.White);
            Brush b;
            int i;
            int N = rgb_array.Length / 3;
            int hh = 9;
            int border = 20;

            for (i = 0; i < N; i++)
            {
                b = new SolidBrush(Color.FromArgb(255, rgb_array[i, 0], rgb_array[i, 1], rgb_array[i, 2]));
                //rgb_array
                //g.FillRectangle(b, w / 10, i * hh + h/10, w / 10 * 8, hh);
                g.FillRectangle(b, border, i * hh + border, w - border * 2, hh);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            g.Clear(Color.White);
            Brush b;
            int i;
            int N = rgb_array2.Length / 3;
            int hh = 50;
            int border = 20;

            for (i = 0; i < N; i++)
            {
                b = new SolidBrush(Color.FromArgb(255, rgb_array2[i, 0], rgb_array2[i, 1], rgb_array2[i, 2]));
                //rgb_array
                //g.FillRectangle(b, 0, i * 50, 300, 50);
                g.FillRectangle(b, border, i * hh + border, w - border * 2, hh);
            }

        }

    }
}
