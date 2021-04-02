using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace FadeImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";//設定文件名為空
            openFileDialog1.Filter = "*.bmp|*.BMP";//設定文件的類型
            if (openFileDialog1.ShowDialog() == DialogResult.OK)//開啟文件對話框
                textBox1.Text = openFileDialog1.FileName;//取得選取文件的路徑
        }

        public void UpDownConnect(string Str, Panel panel)
        {
            Bitmap tem_Bitmap = new Bitmap(Str);
            Bitmap Var_Bitmap = new Bitmap(tem_Bitmap, panel.Width, panel.Height);

            int Var_W = Var_Bitmap.Width; //圖片寬度 
            int Var_H = Var_Bitmap.Height; //圖片高度 
            Graphics g = panel.CreateGraphics();//實例化Graphics類
            g.Clear(Color.Gray);//清空panel控制元件
            Bitmap Tem_bmp = new Bitmap(Var_W, Var_H);//透過圖片大小實例化Bitmap類
            int n = 0;
            //搜尋圖片中的各象素
            while (n <= Var_H / 2)
            {
                for (int i = 0; i <= Var_W - 1; i++)//取得上半張圖片的象素
                {
                    Tem_bmp.SetPixel(i, n, Var_Bitmap.GetPixel(i, n));//根據象素取得目前象的顏色，並記錄在Bitmap類中
                }
                for (int i = 0; i <= Var_W - 1; i++)//取得下半張圖片的象素
                {
                    //根據象素取得目前象的顏色，並記錄在Bitmap類中
                    Tem_bmp.SetPixel(i, Var_H - n - 1, Var_Bitmap.GetPixel(i, Var_H - n - 1));
                }
                n++;
                panel.Refresh();//設定工作區無效
                g.DrawImage(Tem_bmp, 0, 0);//繪製圖片
                System.Threading.Thread.Sleep(5);//掛掉線程
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length > 0)
                UpDownConnect(textBox1.Text.Trim(), panel1);//呼叫自定義方法
            else
                MessageBox.Show("請選擇圖片的路徑。");
        }
    }
}
