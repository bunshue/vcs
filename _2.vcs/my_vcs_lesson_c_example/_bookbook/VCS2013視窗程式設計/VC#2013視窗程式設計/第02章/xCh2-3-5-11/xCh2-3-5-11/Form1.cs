using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_3_5_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建構１個GroupBox物件及3個TextBox物件
            GroupBox groupBox1 = new GroupBox();
            TextBox textBox1 = new TextBox();
            TextBox textBox2 = new TextBox();
            TextBox textBox3 = new TextBox();

           // 設定TextBox物件的屬性並加入GroupBox物件
            textBox1.BackColor = Color.Red;
            textBox2.BackColor = Color.BlueViolet;
            textBox3.BackColor = Color.Green;

            textBox1.Text = "文字方塊1";
            textBox2.Text = "文字方塊2";
            textBox3.Text = "文字方塊3";
            groupBox1.Controls.Add(textBox1);
            groupBox1.Controls.Add(textBox2);
            groupBox1.Controls.Add(textBox3);

            // 設定GroupBox物件屬性
            groupBox1.Text = "群組";
            groupBox1.Dock = DockStyle.Right;

            // 設定TextBox的Dock屬性
            textBox1.Dock = DockStyle.Right;
            textBox2.Dock = DockStyle.Top;
            textBox3.Dock = DockStyle.Bottom;

             // 將GroupBox物件加入Form1
            this.Controls.Add(groupBox1);
        }
    }
}
