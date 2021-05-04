using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ScrollPic
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            picShow.SizeMode = PictureBoxSizeMode.StretchImage;
            picShow.Image = Image.FromFile("船.jpg");//載入圖檔
            picShow.Height = 90; picShow.Width = 90;//設定圖片高度和寬度
            vsbHeight.Maximum = 180;    //設定vsbHeight的最大值 = 180
            hsbWidth.Maximum = 180;     //設定hsbWidth的最大值 = 180
            vsbHeight.Value = picShow.Height;//vsbHeight的Value值=圖片高度
            hsbWidth.Value = picShow.Width;//hsbWidth的Value值=圖片寬度
            lblH.Text = "高度=90"; lblW.Text = "寬度=90";
            vsbHeight.LargeChange = 1;    //設定vsbHeight的快動值 = 1
            hsbWidth.LargeChange = 1;     //設定hsbWidth的快動值 = 1
        }
        // 捲動垂直捲軸時執行
        private void vsbHeight_Scroll(object sender, ScrollEventArgs e)
        {
            picShow.Height = vsbHeight.Value;//設圖片高度=vsbHeight的Value值
            lblH.Text = "高度=" + vsbHeight.Value.ToString();
        }
        // 捲動水平捲軸時執行
        private void hsbWidth_Scroll(object sender, ScrollEventArgs e)
        {
            picShow.Width = hsbWidth.Value;//設圖片寬度=hsbWidth的Value值
            lblW.Text = "寬度=" + hsbWidth.Value.ToString();
        }
    }
}
