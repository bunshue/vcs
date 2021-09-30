using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DynamicAddRemoveControls8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Button[] btn = new Button[10];//Button 陣列

            richTextBox1.Text += "在 表單/panel/pictureBox/richtextBox 上動態建立10個按鈕控件\n";

            for (int i = 0; i < 10; i++)
            {
                btn[i] = new Button();//實體化Button

                btn[i].Size = new Size(70, 50);
                btn[i].Location = new Point(85 * i + 50, 50);
                btn[i].Text = i.ToString();

                btn[i].Click += new EventHandler(this.btnXO_Click);//事件

                //this.Controls.Add(btn[i]); //add 到 this 容器
                panel1.Controls.Add(btn[i]); //add 到 panel1 容器
                //pictureBox1.Controls.Add(btn[i]); //add 到 pictureBox1 容器
                //richTextBox1.Controls.Add(btn[i]); //add 到 richTextBox1 容器
            }
        }

        private void btnXO_Click(object sender, EventArgs e)//動態Button 的事件
        {
            richTextBox1.Text += "你按下: " + ((Button)(sender)).Text + "\t" +
            "索引值: " + ((Button)(sender)).TabIndex.ToString() + "\n";
        }
    }
}
