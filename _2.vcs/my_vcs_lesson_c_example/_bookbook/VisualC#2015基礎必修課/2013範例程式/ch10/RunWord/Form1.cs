using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RunWord
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool move_d = true;   //記錄跑馬燈文字移動方向
        
        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            timer1.Interval = 100;
            toolStripTextBox1.Text = "船過水無痕";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (move_d == true)      //true 由左向右移
            {
                lblMsg.Left += 10;
                if (lblMsg.Left >= this.Width) lblMsg.Left = -lblMsg.Width;
            }
            else                     //false 由左向右移
            {
                lblMsg.Left -= 10;
                if (lblMsg.Left <= -lblMsg.Width) lblMsg.Left = this.Width;
            }
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            move_d = false;
        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            move_d = true;
        }

        private void toolStripTextBox1_TextChanged(object sender, EventArgs e)
        {
            lblMsg.Text = toolStripTextBox1.Text;
        }
    }
}
