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

            label1.Text =
                "拉一個StatusStrip控件成statusStrip1\n" +
                "顯選statusStrip1, 有四種新增項目\n" +
                "1. 新增 StatusLabel 成 toolStripStatusLabel1, 改Text, Image加入圖片\n" +
                "2. 新增 ProgressBar 成 toolStripProgressBar1\n" +
                "3. 新增 DropDownButton\n" +
                "4. 新增 SplitButton\n\n" +
                "顯示系統時間, 使用 toolStripStatusLabel1\n" +
                "顯示進度條,   使用 toolStripProgressBar1\n\n" +
                "加timer程式";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "Max : " + toolStripProgressBar1.Maximum + "\n";
            richTextBox1.Text += "min : " + toolStripProgressBar1.Minimum + "\n";

            //------------------------------------------------------------  # 60個

            this.toolStripStatusLabel3.AutoSize = false;
            this.toolStripProgressBar3.Maximum = 200;
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

        //------------------------------------------------------------  # 60個

        int count = 0;
        private void toolStripStatusLabel3_Click(object sender, EventArgs e)
        {
            count = 0;
            timer3.Start();//開始計時
            toolStripStatusLabel3.Text = "移動圖片";
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            if (count < 200)
            {
                //從表單的左邊移動圖片
                count += 5;
                toolStripProgressBar3.Value = count;
                //顯示進度列目前進行的狀態
                toolStripStatusLabel3.Text = String.Concat(toolStripProgressBar3.Value / 3, " % 已經完成");
            }
            else
            {
                timer3.Stop();
                toolStripStatusLabel3.Text = "使命已達";
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/
