using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1303
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void tsslMsg_Click(object sender, EventArgs e)
        {
            picSample.Left = 0;
            tmrAuto.Start();//開始計時
            tsslMsg.Text = "移動圖片";
        }

        private void tmrAuto_Tick(object sender, EventArgs e)
        {
            if (picSample.Left < 200)
            {
                //從表單的左邊移動圖片
                picSample.Left += 5;
                tsspShow.Value = picSample.Left;
                //顯示進度列目前進行的狀態
                tsslMsg.Text = String.Concat(
                   tsspShow.Value / 3, " % 已經完成");
            }
            else
            {
                tmrAuto.Stop();
                tsslMsg.Text = "使命已達";
            }
        }
    }
}
