using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh8_5_1_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        BindingManagerBase myBindingManagerBase;
        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: 這行程式碼會將資料載入 '北風DataSet.員工' 資料表。您可以視需要進行移動或移除。
            this.員工TableAdapter.Fill(this.北風DataSet.員工);

            comboBox1.DataSource = 北風DataSet;
            comboBox1.DisplayMember = "員工.識別碼";

            textBox1.DataBindings.Add(new Binding("Text", 北風DataSet, "員工.名字"));
            textBox2.DataBindings.Add(new Binding("Text", 北風DataSet, "員工.職稱"));
            textBox3.DataBindings.Add("Text", 北風DataSet, "員工.電子郵件地址");

            myBindingManagerBase = this.BindingContext[北風DataSet, "員工"];
            ShowPosition();
        }

        private void ShowPosition()
        {
            label5.Text = "目前位置是：" + (myBindingManagerBase.Position + 1).ToString();
            label5.Text += "，總記錄數是：" + myBindingManagerBase.Count;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            myBindingManagerBase.Position = 0;
            ShowPosition();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (myBindingManagerBase.Position > 0)
            {
                myBindingManagerBase.Position -= 1;
                ShowPosition();
            }
            else
                MessageBox.Show("目前已是第一筆，無法往前取得資料");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (myBindingManagerBase.Position < myBindingManagerBase.Count - 1)
            {
                myBindingManagerBase.Position += 1;
                ShowPosition();
            }
            else
                MessageBox.Show("目前已是最後一筆，無法往下取得資料");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            myBindingManagerBase.Position = myBindingManagerBase.Count - 1;
            ShowPosition();
        }
    }
}
