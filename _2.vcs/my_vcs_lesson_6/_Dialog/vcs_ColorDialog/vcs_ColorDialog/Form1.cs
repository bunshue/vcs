using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ColorDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //設定前景色, 使用自定義色彩
            // Use dark custom colors for the foreground dialog.
            int[] fg_colors = {
                0x808080, 0xFF0000, 0xFF8000, 0xFFFF00, 0x00FF00,
                0x00FFFF, 0x0000FF, 0xFF00FF, 0x000000, 0xC00000,
                0x804000, 0xC0C000, 0x008000, 0x00C0C0, 0x0000C0,
                0x800080 };
            colorDialog_forecolor.CustomColors = fg_colors;
            // Make the background dialog open with the custom colors displayed.
            colorDialog_forecolor.FullOpen = false;

            //設定背景色, 使用自定義色彩
            // Use light custom colors for the background dialog.
            int[] bg_colors = {
                0xFFFFFF, 0xFFC0C0, 0xFFE0C0, 0xFFFFC0, 0xC0FFC0,
                0xC0FFFF, 0xC0C0FF, 0xFFC0FF, 0xE0E0E0, 0xFF8080,
                0xFFC080, 0xFFFF80, 0x80FF80, 0x80FFFF, 0x8080FF,
                0xFF80FF
            };
            colorDialog_backcolor.CustomColors = bg_colors;
            // Make the background dialog open with the custom colors displayed.
            colorDialog_backcolor.FullOpen = true;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0+20);
            richTextBox1.Size = new Size(600, 400);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(860, 620);
            this.Text = "vcs_ColorDialog";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //色彩對話方塊 選擇背景色
            colorDialog1.Color = richTextBox1.BackColor;    //顏色對話框的預設顏色
            colorDialog1.AllowFullOpen = true;  //可以使用該對話框定義自定義顏色
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.BackColor = colorDialog1.Color;
                button1.BackColor = colorDialog1.Color;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //設定部分背景顏色
            colorDialog1.AllowFullOpen = true;  //可以使用該對話框定義自定義顏色
            colorDialog1.AnyColor = true;      			//顯示基本顏色集中可用的所有顏色
            colorDialog1.FullOpen = true;      //創建自定義顏色的控件在對話框打開時是可見的
            colorDialog1.SolidColorOnly = false;			//不限制只選擇純色
            if (colorDialog1.ShowDialog() == DialogResult.OK)   //彈出對話框
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //設定前景色, 使用自定義色彩
            colorDialog_forecolor.Color = this.ForeColor;

            if (colorDialog_forecolor.ShowDialog() == DialogResult.OK)
            {
                this.ForeColor = colorDialog_forecolor.Color;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //設定背景色, 使用自定義色彩
            colorDialog_backcolor.Color = this.BackColor;

            if (colorDialog_backcolor.ShowDialog() == DialogResult.OK)
            {
                this.BackColor = colorDialog_backcolor.Color;
                button3.BackColor = colorDialog_backcolor.Color;
                button4.BackColor = colorDialog_backcolor.Color;
            }
        }
    }
}
