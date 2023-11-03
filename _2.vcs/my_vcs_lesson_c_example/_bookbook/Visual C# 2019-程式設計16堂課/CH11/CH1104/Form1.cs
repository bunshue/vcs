using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1104
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int a = 0, b = 0, sec = 0, min = 0;

        //清除按鈕 - 與碼表有關的設定值都歸零 
        private void btnClear_Click(object sender, EventArgs e)
        {
            //將所有的值都歸零
            min = 0; sec = 0; a = 0; b = 0;
            trackTime.Value = 0;   //將追踪列的值歸零
            txtTime.Text = $"{min}分 {sec}秒 {a}{b}";
        }

        //停止按鈕 - 以stop()方法停止計時器
        private void btnStop_Click(object sender, EventArgs e)
        {
            tmrCount.Stop();  //停止計時器
        }

        //開始按鈕 - start()方法開始計時
        private void btnStart_Click(object sender, EventArgs e)
        {
            tmrCount.Start();   //啟動計時器
        }

        private void tmrCount_Tick(object sender, EventArgs e)
        {
            //a, b為計時器為來顯示毫秒的十位數和個數
            b += 1;   //啟動Timer先自行累加
            if (b == 10) //當個數累加到10就向變數a進位
            {
                b = 0;
                a += 1;
                //當變數a為累加為10，秒數就遞增並移動trackTime刻度
                if (a == 10)
                {
                    a = 0;
                    sec += 1;
                    trackTime.Value += 1;
                    //以秒為刻度來移動
                    if (trackTime.Value == 60)
                    {
                        trackTime.Value = 0;
                        if (sec == 60)
                        {
                            sec = 0;//秒數歸零
                            min += 1;//分鐘累計
                        }
                    }
                }
            }
            txtTime.Text = $"{min}分 {sec}秒 {a}{b}";
        }
    }
}

