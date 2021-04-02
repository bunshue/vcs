using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace BadgeImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public Image SetBadge(PictureBox Pict, String Str, Font font, int place)
        {
            Image Var_Image = Pict.Image;//根據圖片實例化Image類
            int Var_FontSize = (int)font.Size;//取得字體大小
            bool Var_isSetFont = false;//判斷目前文字是否超出圖片的大小
            int Var_W = Var_Image.Width;//取得圖片的寬度
            int Var_H = Var_Image.Height;//取得圖片的高度
            int Var_StrX = 0;//記錄文字的X位置
            int Var_StrY = 0;//記錄文字的Y位置

            Bitmap Var_bmp = new Bitmap(Var_W, Var_H);//實例化Image類
            Bitmap Var_SaveBmp = new Bitmap(Var_Image);//實例化Image類
            Graphics g = Graphics.FromImage(Var_bmp);//用指定的Bitmap實例化Graphics
            Graphics tem_Graphics = Graphics.FromImage(Var_Image);//用指定的Bitmap實例化Graphics
            SizeF Var_Size = new SizeF(Var_W, Var_H);//實例化SizeF類
            Font tem_Font = font;//取得文字的設定文字
            g.Clear(Color.White);//清空圖片
            while (Var_isSetFont == false)//如果文字超出圖片的大小
            {
                //設定文字的文字
                tem_Font = new Font(font.Name, Var_FontSize, font.Bold ? FontStyle.Bold : FontStyle.Regular);
                Var_Size = g.MeasureString(Str, tem_Font);//對文字進行測量
                if (Var_Size.Width < Var_bmp.Width - 10)//如果文字的寬度沒有超出圖片
                {
                    if (Var_Size.Height < Var_bmp.Height - 10)//如果文字的高度沒有超出圖片
                        Var_isSetFont = true;//不減小文字的大小
                }
                else
                    Var_FontSize = Var_FontSize - 1;//文字的字體大小減1
            }
            switch (place)//選擇文字的顯示位置
            {
                case 1://右下角
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width-3);//設定文字的X座標值
                        Var_StrY = (int)(Var_bmp.Height - Var_Size.Height);//設定文字的Y座標值
                        break;
                    }
                case 2://右上角
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width - 3);
                        Var_StrY = 1;
                        break;
                    }
                case 3://左下角
                    {
                        Var_StrX = 1;
                        Var_StrY = (int)(Var_bmp.Height - Var_Size.Height);
                        break;
                    }
                case 4://左上角
                    {
                        Var_StrX = 1;
                        Var_StrY = 1;
                        break;
                    }
                case 5://頂局中
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width-2)/2;
                        Var_StrY = 1;
                        break;
                    }
                case 6://底局中
                    {
                        Var_StrX = (int)(Var_bmp.Width - Var_Size.Width - 2) / 2;
                        Var_StrY = (int)(Var_bmp.Height - Var_Size.Height);
                        break;
                    }

            }
            g.DrawString(Str, tem_Font, new SolidBrush(Color.Black), Var_StrX, Var_StrY);//繪製前景色為黑色的文字
            int tem_Become = 40;//設定文字的變色深度
            //搜尋圖片的所有象素
            for (int x = 1; x < Var_bmp.Width; x++)
            {
                for (int y = 1; y < Var_bmp.Height; y++)
                {
                    int tem_a, tem_r, tem_g, tem_b, tem_r1, tem_g1, tem_b1;//定義變數
                    if (Var_bmp.GetPixel(x, y).ToArgb() == Color.Black.ToArgb())//如果目前象素的顏色為黑色
                    {
                        tem_a = Var_SaveBmp.GetPixel(x, y).A;//取得目前象素的alpha份量值
                        tem_r = Var_SaveBmp.GetPixel(x, y).R;//取得目前象素的R色值
                        tem_g = Var_SaveBmp.GetPixel(x, y).G;//取得目前象素的G色值
                        tem_b = Var_SaveBmp.GetPixel(x, y).B;//取得目前象素的B色值
                        tem_r1 = tem_r;//臨時儲存R色值
                        tem_g1 = tem_g;//臨時儲存G色值
                        tem_b1 = tem_b;//臨時儲存B色值
                        //根據加深後的圖片背景顯示文字
                        if (tem_b + tem_Become < 255)//如果B色值加上目前深度小於255
                            tem_b = tem_b + 255;//B色值加上深度值
                        if (tem_g + tem_Become < 255)
                            tem_g = tem_g + 255;
                        if (tem_r + tem_Become < 255)
                            tem_r = tem_r + 255;
                        if (tem_r1 - tem_Become > 0)//如果B色值加上目前深度大於0
                            tem_r1 = tem_r1 - tem_Become;//B色值減去深度值
                        if (tem_g1 - tem_Become > 0)
                            tem_g1 = tem_g1 - tem_Become;
                        if (tem_b1 - tem_Become > 0)
                            tem_b1 = tem_b1 - tem_Become;
                        tem_Graphics.DrawEllipse(new Pen(new SolidBrush(Color.Black)), x, y + 1, 3, 3);//繪製文字的陰影
                        //以深後的圖片背景顯示文字
                        tem_Graphics.DrawEllipse(new Pen(new SolidBrush(Color.FromArgb(tem_a, tem_r1, tem_g1, tem_b1))), x, y, 1, 1);
                    }
                }
            }
            return Var_Image;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            V_p = comboBox1.SelectedIndex + 1;//設定文字的顯示位置
            pictureBox1.Image = SetBadge(pictureBox1, "範例寶典升級版", V_font, V_p);//呼叫自定義方法
        }

        Font V_font;
        int V_p = 1;

        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.SelectedIndex = 0;
            V_font = new Font("細明體", 12, FontStyle.Bold);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (fontDialog1.ShowDialog() == DialogResult.OK)
                V_font = fontDialog1.Font;
        }
    }
}
