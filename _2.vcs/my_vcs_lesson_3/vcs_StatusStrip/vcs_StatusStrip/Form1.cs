using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_StatusStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "Max : " + toolStripProgressBar1.Maximum + "\n";
            richTextBox1.Text += "min : " + toolStripProgressBar1.Minimum + "\n";

        }

        //int i = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString();
            //statusStrip1.Items[0].Text = "日期:" + DateTime.Now.ToString();   //same

            if (toolStripProgressBar1.Value < toolStripProgressBar1.Maximum)
            {
                this.toolStripProgressBar1.PerformStep();   //走固定步伐, 設定在 Step 裏

                richTextBox1.Text += this.toolStripProgressBar1.Value.ToString() + " ";
            }
            else
            {
                toolStripProgressBar1.Value = 0;
            }

            /*
            i++;
            if (i > toolStripProgressBar1.Maximum)
            {
                i = 0;
            }
            toolStripProgressBar1.Value = i;
            richTextBox1.Text += i.ToString() + " ";
            */

        }

    }
}
