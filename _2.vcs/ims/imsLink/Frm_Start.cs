using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace imsLink
{
    public partial class Frm_Start : Form
    {
        public Frm_Start()
        {
            InitializeComponent();
        }

        private void Frm_Start_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;    //把視窗其他按鈕拿掉
            this.BackgroundImage = Image.FromFile("logo-720x480.bmp");     //載入圖片放在：/bin/Debug下
            this.BackgroundImageLayout = ImageLayout.Stretch;   //填滿圖片
            this.timer1.Start();            //啟動計時器
            this.timer1.Interval = 1000;    //過5秒消失
        }

        private void Frm_Start_FormClosed(object sender, FormClosedEventArgs e)
        {
            this.timer1.Stop();  //關閉計時器
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Close();  //時間到關閉視窗
        }
    }
}
