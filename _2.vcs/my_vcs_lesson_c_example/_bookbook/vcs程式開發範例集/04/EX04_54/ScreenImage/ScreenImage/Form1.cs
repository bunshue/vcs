using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Threading;

namespace ScreenImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Hook.KeyUp += new KeyEventHandler(Hook_KeyUp);//加載鍵盤的放開事件
            comboBox1.SelectedIndex = 0;//設定圖片的類型
        }


        //聲明一個API函數
        [System.Runtime.InteropServices.DllImportAttribute("gdi32.dll")]
        private static extern bool BitBlt(IntPtr hdcDest, int nXDest, int nYDest, int nWidth, int nHeight, IntPtr hdcSrc, int nXSrc, int nYSrc, System.Int32 dwRop);

        public void SnatchScreen(Form Frm, string FilePath, string Style)
        {
            Point Var_Loc = Frm.Location;//取得目前視窗的位置
            int Frm_left = -Var_Loc.X;
            int Frm_right = -Var_Loc.Y;

            Rectangle Var_rect = new Rectangle();//實例化Rectangle類
            Var_rect = Screen.GetWorkingArea(Frm);//獲得目前螢幕的大小
            Graphics g = Frm.CreateGraphics();//建立一個以目前螢幕為模板的圖片
            Image Var_Image = new Bitmap(Var_rect.Width, Var_rect.Height, g);//建立以螢幕大小為標準的位圖 
            Graphics Var_G_Image = Graphics.FromImage(Var_Image);//根據圖片實例化Graphics類
            IntPtr Screen_dc = g.GetHdc();//得到螢幕的句柄
            IntPtr Bitmap_dc = Var_G_Image.GetHdc();//得到Bitmap的句柄
            BitBlt(Bitmap_dc, 0, 0, Var_rect.Width, Var_rect.Height, Screen_dc, Frm_left, Frm_right, 13369376);//呼叫此API函數，完成螢幕擷取
            g.ReleaseHdc(Screen_dc);//釋放掉螢幕的句柄
            Var_G_Image.ReleaseHdc(Bitmap_dc);//釋放掉Bitmap的句柄
            ImageFormat ImageF = ImageFormat.Jpeg;//實例化ImageFormat類
            switch (Style)
            {
                //設定文件的類型
                case "JPG": ImageF = ImageFormat.Jpeg; break;
                case "BMP": ImageF = ImageFormat.Bmp; break;
                case "GIF": ImageF = ImageFormat.Gif; break;
                case "PNG": ImageF = ImageFormat.Png; break;
                case "WMF": ImageF = ImageFormat.Wmf; break;
            }
            Var_Image.Save(FilePath, ImageF);//以指定的文件格式來保存
        }

        HOOK Hook = new HOOK();
        private void button1_Click(object sender, EventArgs e)
        {
            Hook.Stop();//卸載掛鉤
            Hook.Start();//安裝掛鉤
        }

        void Hook_KeyUp(object sender, KeyEventArgs e)
        {
            this.Text = "AAAA";
            if (e.KeyCode.ToString() == "F10")//如是目前按下的是F10鍵
            {
                //如果沒有對螢幕螢幕截圖進行設定
                if (textBox1.Text.Length == 0 || textBox2.Text.Length == 0 || comboBox1.Text.Length == 0)
                {
                    MessageBox.Show("請設定抓取圖片的存放位置及圖片類型。");//彈出提示文字框
                    HOOK.pp = 1;//標識，不進行F10鍵的正常操作
                    return;//退出本次操作
                }
                //執行螢幕截圖的操作
                SnatchScreen(this, textBox1.Text + "\\" + textBox2.Text + "." + comboBox1.Text, comboBox1.Text);
                HOOK.pp = 1;//標識，不進行F10鍵的正常操作
            }
            else
                HOOK.pp = 0;//標識，執行F10鍵的正常操作
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)//開啟文件對話框
                textBox1.Text = folderBrowserDialog1.SelectedPath;//取得圖片儲存的路徑
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Hook.Stop();//卸載掛鉤
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Hook.Stop();//卸載掛鉤
        }
    }
}
