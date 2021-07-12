using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace SetupPelsImage
{
    public partial class Form1 : Form
    {
        int Var_MouseX = 0;//記錄滑鼠游標的X座標的位置
        int Var_MouseY = 0;//記錄滑鼠游標的X座標的位置
        int W = 0;//記錄滑鼠游標拖曳矩形框的寬度
        int H = 0;//記錄滑鼠游標拖曳矩形框的高度

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Var_MouseX = e.X;//記錄滑鼠游標按下時的X座標值
            Var_MouseY = e.Y;//記錄滑鼠游標按下時的Y座標值
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            W = e.X - Var_MouseX;//取得滑鼠游標拖曳矩形框的寬度
            H = e.Y - Var_MouseY;//取得滑鼠游標拖曳矩形框的高度
            if (W == 0)//矩形框的寬度為0
            {
                W = 1;//設定寬度為1
            }
            if (H == 0)//矩形框的高度為0
            {
                H = 1;//設定高度為1
            }
            label_X.Text = Var_MouseX.ToString();//顯示X的座標值
            label_Y.Text = Var_MouseY.ToString();//顯示Y的座標值
            label_W.Text = W.ToString();//顯示寬度
            label_H.Text = H.ToString();//顯示高度
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)//開啟顏色對話框
            {
                panel1.BackColor = colorDialog1.Color;//顯示選擇的顏色
            }
        }

        public Image SetPels(PictureBox Pict, Panel panel, Color color, int x, int y, int w, int h)
        {
            Bitmap Var_Bmp = new Bitmap(w, h);//根據矩形框的大小實例化Bitmap類
            Bitmap Var_SaveBmp = (Bitmap)Pict.Image;//實例化Bitmap
            //搜尋矩形框內的各象素點
            for (int i = x; i < x + w; i++)
            {
                for (int j = y; j < y + h; j++)
                {
                    Var_SaveBmp.SetPixel(i, j, color);//設定目前象素點的顏色
                }
            }
            return Var_SaveBmp;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if ((W > 0) && (H > 0))
            {
                //呼叫自定義方法修改圖片的顏色
                pictureBox1.Image = SetPels(pictureBox1, panel1, panel1.BackColor, Var_MouseX, Var_MouseY, W, H);
            }
        }

    }
}


