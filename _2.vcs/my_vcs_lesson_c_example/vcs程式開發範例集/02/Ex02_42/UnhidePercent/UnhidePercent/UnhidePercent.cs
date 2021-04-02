using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace UnhidePercent
{
    public partial class UnhidePercent : Form
    {
        public UnhidePercent()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (this.progressBar1.Value == this.progressBar1.Maximum)//當進度條的當前值等於最大值時
            {
                this.progressBar1.Value = this.progressBar1.Minimum;//設置進度條的當前值為最小值
            }
            else //當進度條的當前值小於最大值時
            {
                this.progressBar1.PerformStep();//按指定的增量增加進度條中的進度塊
            }
            int percentValue = 100 * (this.progressBar1.Value - this.progressBar1.Minimum) / (this.progressBar1.Maximum - this.progressBar1.Minimum);//將當前進度轉化為百分比的形式
            label1.Text = percentValue.ToString() + "%";//在Label中顯示百分比的值                                                                                               
        }

        private void StartOrStop_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled)//當Timer處於可用狀態時
            {
                timer1.Enabled = false;//設置Timer為不可用狀態
                StartOrStop.Text = "開始";//設置「開始」按鈕上的文本內容為「開始」
            }
            else//當Timer處於不可用狀態時
            {
                timer1.Enabled = true;//設置Timer為可用狀態
                StartOrStop.Text = "停止";//設置「停止」按鈕上的文本內容為「停止」
            }
        }

        private void UnhidePercent_Load(object sender, EventArgs e)
        {

        }
    }
}
