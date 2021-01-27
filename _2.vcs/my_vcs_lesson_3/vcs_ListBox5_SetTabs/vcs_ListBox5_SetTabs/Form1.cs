using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListBox5_SetTabs
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Set tabs.
            int[] tabs = { 75, 125, 175 };
            listBox1.SetTabs(tabs);

            int i;
            string txt = "";

            txt = "原數值" + "\t" + "平方項" + "\t" + "立方項";
            listBox1.Items.Add(txt);

            for (i = -5; i <= 5; i++)
            {
                txt = i.ToString() + "\t" + (i * i).ToString() + "\t" + (i * i * i).ToString();
                listBox1.Items.Add(txt);
            }

        }
    }
}
