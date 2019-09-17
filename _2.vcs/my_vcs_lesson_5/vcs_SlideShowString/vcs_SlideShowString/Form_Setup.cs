using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SlideShowString
{
    public partial class Form_Setup : Form
    {
        public Form_Setup()
        {
            InitializeComponent();


            int x_st = 100;
            int y_st = 100;
            int dy = 60;
            label0.Location = new Point(x_st, y_st + dy * 0);
            label1.Location = new Point(x_st, y_st + dy * 1);
            label2.Location = new Point(x_st, y_st + dy * 2);
            label3.Location = new Point(x_st, y_st + dy * 3);
            label4.Location = new Point(x_st, y_st + dy * 4);
            label5.Location = new Point(x_st, y_st + dy * 5);
            label6.Location = new Point(x_st, y_st + dy * 6);
            label7.Location = new Point(x_st, y_st + dy * 7);
            label0.Text = "對齊方向：";
            label1.Text = "播放順序：";
            label2.Text = "字型：";
            label3.Text = "自訂字型大小：";
            label4.Text = "播放速度：";
            label5.Text = "最上層顯示：";
            label6.Text = "螢幕佔寬比：";
            label7.Text = "螢幕佔高比：";

            int dx = 200;
            label22.Location = new Point(x_st + dx, y_st + dy * 2);
            button2.Location = new Point(x_st + dx + dx, y_st + dy * 2);
            comboBox0.Location = new Point(x_st + dx, y_st + dy * 0);
            comboBox1.Location = new Point(x_st + dx, y_st + dy * 1);
            comboBox5.Location = new Point(x_st + dx, y_st + dy * 5);

            numericUpDown3.Location = new Point(x_st + dx, y_st + dy * 3);
            numericUpDown4.Location = new Point(x_st + dx, y_st + dy * 4);
            numericUpDown6.Location = new Point(x_st + dx, y_st + dy * 6);
            numericUpDown7.Location = new Point(x_st + dx, y_st + dy * 7);



        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
