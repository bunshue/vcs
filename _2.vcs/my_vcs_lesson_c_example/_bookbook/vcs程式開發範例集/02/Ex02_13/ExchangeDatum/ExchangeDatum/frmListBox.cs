using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ExchangeDatum
{
    public partial class frmListBox : Form
    {
        public frmListBox()
        {
            InitializeComponent();
        }

        private void frmListBox_Load(object sender, EventArgs e)
        {
            string[] name = { "小明", "小1", "小2", "小3", "小4", "小5", "小6", "小7", "小8", "小9", "小10", "小11" };
            //lbSocure.DataSource = name;   //list用了DataSource, 內容不可改變
            foreach (string n in name)
            {
                lbSocure.Items.Add(n);
            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)//全部添加到選擇的項中
        {
            for (int i = 0; i < lbSocure.Items.Count; i++)
            {
                lbSocure.SelectedIndex = i;
                lbChoose.Items.Add(lbSocure.SelectedItem.ToString());
            }
            lbSocure.Items.Clear();
        }

        private void button3_Click(object sender, EventArgs e)//全部添加到數據源中
        {
            for (int i = 0; i < lbChoose.Items.Count; i++)
            {
                lbChoose.SelectedIndex = i;
                lbSocure.Items.Add(lbChoose.SelectedItem.ToString());
            }
            lbChoose.Items.Clear();
        }

        private void button1_Click(object sender, EventArgs e)//單個添加到選擇的項中
        {
            if (lbSocure.SelectedIndex != -1)
            {
                this.lbChoose.Items.Add(this.lbSocure.SelectedItem.ToString());
                this.lbSocure.Items.Remove(this.lbSocure.SelectedItem);
            }
        }

        private void button4_Click(object sender, EventArgs e)//單個添加到數據源中
        {
            if (lbChoose.SelectedIndex != -1)
            {
                this.lbSocure.Items.Add(this.lbChoose.SelectedItem.ToString());
                this.lbChoose.Items.Remove(this.lbChoose.SelectedItem);
            }
        }
    }
}
