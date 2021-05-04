using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Picture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int no;    //成員變數no紀錄照片編號供所有程序共用
        private void Form1_Load(object sender, EventArgs e)
        {
            no = 1; //預設照片編號為1
            lblNo.Text = "第" + no.ToString() + "張";
            picShow.Image = new Bitmap("pic" + no.ToString() + ".jpg");//載入圖檔
            //設隨控制項調整圖片大小
            picShow.SizeMode = PictureBoxSizeMode.StretchImage;
            btnP.Enabled = false;   //設上一張鈕不能使用
        }
        //按下一張鈕時
        private void btnN_Click(object sender, EventArgs e)
        {
            no++; //照片編號加1
            lblNo.Text = "第" + no.ToString() + "張"; //顯示照片編號
            btnP.Enabled = true;   //設上一張鈕可以使用
            if (no == 4) btnN.Enabled = false;   //若no = 4設下一張鈕不能使用
            picShow.Image = new Bitmap("pic" + no.ToString() + ".jpg");
            picShow.Size = new Size(250, 200);  //恢復成預設大小
        }
        //按上一張鈕時
        private void btnP_Click(object sender, EventArgs e)
        {
            no--; //照片編號減1
            lblNo.Text = "第" + no.ToString() + "張"; //顯示照片編號
            btnN.Enabled = true;   //設下一張鈕可以使用
            if (no == 1) btnP.Enabled = false;   //若no = 1設上一張鈕不能使用
            picShow.Image = new Bitmap("pic" + no.ToString() + ".jpg");
            picShow.Size = new Size(250, 200);  //恢復成預設大小
        }
        //按縮小鈕時
        private void btnS_Click(object sender, EventArgs e)
        {
            for (int w = 250; w >= 50; w -= 20)   //圖片寬度由250到50，間距為-20
            {
                picShow.Size = new Size(w, Convert.ToInt32(w * 0.8));//重設大小
                DateTime now = DateTime.Now;    //now紀錄目前時間
                do     //時間間隔 < 0.1秒
                {
                    Application.DoEvents(); //處理其他事件
                } while ((DateTime.Now - now).TotalSeconds < 0.1);
            }
        }
    }
}
