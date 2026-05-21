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
            show_item_location();

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "Max : " + toolStripProgressBar1.Maximum + "\n";
            richTextBox1.Text += "min : " + toolStripProgressBar1.Minimum + "\n";
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_StatusStrip";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        //------------------------------------------------------------  # 60個

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


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


