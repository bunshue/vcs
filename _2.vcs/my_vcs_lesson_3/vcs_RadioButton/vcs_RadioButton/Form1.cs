using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RadioButton
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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            richTextBox1.Size = new Size(340, 500);
            //richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(620, 580);
            this.Text = "vcs_RadioButton";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            //RadioButton共用函數

            RadioButton radioButton = (RadioButton)sender;
            if (radioButton.Checked == false)
            {
                return;
            }

            richTextBox1.Text += "你選擇了 : ";

            // 顏色選項
            if (radioButton == rb_color1)
                richTextBox1.Text += "紅色\n";
            else if (radioButton == rb_color2)
                richTextBox1.Text += "綠色\n";
            else if (radioButton == rb_color3)
                richTextBox1.Text += "藍色\n";

            // 樣式選項
            else if (radioButton == rb_style1)
                richTextBox1.Text += "實線\n";
            else if (radioButton == rb_style2)
                richTextBox1.Text += "虛線\n";
            else if (radioButton == rb_style3)
                richTextBox1.Text += "點線\n";
        }

    }
}
