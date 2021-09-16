using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_1_2_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listBox1.Items.AddRange(
                new object[] { 
                    "電冰箱：1300W", 
                    "電鍋：800W", 
                    "微波爐：1200W", 
                    "冷氣機：900W", 
                    "吹風機：800W" 
                });
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (textBox1.Text.ToString()=="") return;

            double hrs = double.Parse(textBox1.Text.ToString());
            switch (listBox1.SelectedIndex)
            {
                case 0:
                    label3.Text = "耗用度數：" + (1300 * hrs / 1000).ToString();
                    break;
                case 1:
                    label3.Text = "耗用度數：" + (800 * hrs / 1000).ToString();
                    break;
                case 2:
                    label3.Text = "耗用度數：" + (1200 * hrs / 1000).ToString();
                    break;
                case 3:
                    label3.Text = "耗用度數：" + (900 * hrs / 1000).ToString();
                    break;
                case 4:
                    label3.Text = "耗用度數：" +(800 * hrs / 1000).ToString();
                    break;
            }
        }
    }
}
