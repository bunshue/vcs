using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_1_1_11
{
    public partial class Form1 : Form
    {
        private System.Windows.Forms.Button Button1;
        private System.Windows.Forms.Button Button2;
        private System.Windows.Forms.Button Button3;
        private System.Windows.Forms.Button Button4;
        private System.Windows.Forms.Button Button5;
        private System.Windows.Forms.Button Button6;
        private System.Windows.Forms.Button Button7;
        private System.Windows.Forms.Button Button8;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Button1 = new System.Windows.Forms.Button();
            Button2 = new System.Windows.Forms.Button();
            Button3 = new System.Windows.Forms.Button();
            Button4 = new System.Windows.Forms.Button();
            Button5 = new System.Windows.Forms.Button();
            Button6 = new System.Windows.Forms.Button();
            Button7 = new System.Windows.Forms.Button();
            Button8 = new System.Windows.Forms.Button();
            Button1.Name = "Button11";
            Button2.Name = "Button22";
            Button3.Name = "Button33";
            Button4.Name = "Button44";
            Button5.Name = "Button55";
            Button6.Name = "Button66";
            Button7.Name = "Button77";
            Button8.Name = "Button88";
            Button1.Text = "1.張三峰";
            Button2.Text = "2.張無忌";
            Button3.Text = "3.趙敏";
            Button4.Text = "4.黃蓉";
            Button5.Text = "5.郭靖";
            Button6.Text = "6.小龍女";
            Button7.Text = "7.楊過";
            Button8.Text = "8.虛竹";

            flowLayoutPanel1.Controls.Add(Button1);
            flowLayoutPanel1.Controls.Add(Button2);
            flowLayoutPanel1.Controls.Add(Button3);
            flowLayoutPanel1.Controls.Add(Button4);
            flowLayoutPanel1.Controls.Add(Button5);
            flowLayoutPanel1.Controls.Add(Button6);
            flowLayoutPanel1.Controls.Add(Button7);
            flowLayoutPanel1.Controls.Add(Button8);

            flowLayoutPanel1.Name = "FlowLayoutPanel1";
            flowLayoutPanel1.BorderStyle = BorderStyle.Fixed3D;
            flowLayoutPanel1.FlowDirection = FlowDirection.RightToLeft;
            flowLayoutPanel1.WrapContents = false;
            flowLayoutPanel1.AutoScroll = false;
            flowLayoutPanel1.BackColor = Color.Pink;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                richTextBox1.Text += "FlowDirection = LeftToRight 左到右\n";
                flowLayoutPanel1.FlowDirection = FlowDirection.LeftToRight;
            }
            else
            {
                richTextBox1.Text += "FlowDirection = RightToLeft 右到左\n";
                flowLayoutPanel1.FlowDirection = FlowDirection.RightToLeft;
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked)
            {
                richTextBox1.Text += "WrapContents = true\n";
                flowLayoutPanel1.WrapContents = true;
            }
            else
            {
                richTextBox1.Text += "WrapContents = false\n";
                flowLayoutPanel1.WrapContents = false;
            }
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox3.Checked)
            {
                richTextBox1.Text += "AutoScroll = true\n";
                flowLayoutPanel1.AutoScroll = true;
            }
            else
            {
                richTextBox1.Text += "AutoScroll = false\n";
                flowLayoutPanel1.AutoScroll = false;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "11111111\n";
            flowLayoutPanel1.AutoSize = true;
            flowLayoutPanel1.AutoSizeMode = AutoSizeMode.GrowAndShrink;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "2222222222\n";
            flowLayoutPanel1.AutoSize = true;
            flowLayoutPanel1.AutoSizeMode = AutoSizeMode.GrowOnly;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "FlowDirection : " + flowLayoutPanel1.FlowDirection + "\n";
            richTextBox1.Text += "WrapContents : " + flowLayoutPanel1.WrapContents + "\n";
            richTextBox1.Text += "AutoScroll : " + flowLayoutPanel1.AutoScroll + "\n";
        }
    }
}

