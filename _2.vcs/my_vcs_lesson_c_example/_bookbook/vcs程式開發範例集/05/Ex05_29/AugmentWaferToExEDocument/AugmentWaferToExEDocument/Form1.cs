using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace AugmentWaferToExEDocument
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            this.label1.Text = "共有：" + this.imageList1.Images.Count.ToString() + " 幅图片";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.textBox1.Text != "")
            {
                try
                {
                    if (Convert.ToInt16(this.textBox1.Text) > Convert.ToInt16(this.imageList1.Images.Count.ToString()) || Convert.ToInt16(this.textBox1.Text) <= 0)
                    {
                        MessageBox.Show("信息有误");
                    }
                    else
                    {

                        this.pictureBox1.Image = this.imageList1.Images[Convert.ToInt16(this.textBox1.Text) - 1];
                    }
                }
                catch
                {
                    MessageBox.Show("请输入数字");
                }
            }
            else
            {
                MessageBox.Show("请输入数字");
            }
        }
    }
}