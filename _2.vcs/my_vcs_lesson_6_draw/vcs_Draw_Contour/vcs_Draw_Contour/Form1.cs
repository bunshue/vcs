using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Contour
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }


        int COLUMN = 360 + 1 + 360;
        int ROW = 360 + 1 + 360;

        private void button1_Click(object sender, EventArgs e)
        {
            int i, j;
            //                    R   C
            //int[,] gray = new int[ROW, COLUMN];    //Row = 19, Column = 8
            double[,] brightness = new double[ROW, COLUMN];    //Row = 19, Column = 8
            int[,] brightness2 = new int[ROW, COLUMN];    //Row = 19, Column = 8

            //richTextBox1.Text += "assign value\n";

            double stepx = 360.0 / ((COLUMN - 1) / 2);
            double stepy = 360.0 / ((ROW - 1) / 2);

            double max = 0;
            double min = 100;
            double vv = 0;

            richTextBox1.Text += "stepx = " + stepx.ToString() + "\n";
            richTextBox1.Text += "stepy = " + stepy.ToString() + "\n";

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    //gray[j, i] = (i - COLUMN / 2) * 10 + (j - ROW / 2) * 10;

                    //vv = cosd((i - COLUMN / 2) * stepx) + cosd((j - ROW / 2) * stepy);
                    vv = cosd((i - 360) * 1) + cosd((j - 360) * 1);

                    brightness[j, i] = vv;
                    if (vv > max)
                        max = vv;
                    else if (vv < min)
                        min = vv;

                    //對應到0~255
                    brightness2[j, i] = (int)((vv + 2.0) * 64);
                    if (brightness2[j, i] == 256)
                        brightness2[j, i] = 255;
                    brightness2[j, i] = (brightness2[j, i] / 5) * 5;
                }
            }

            richTextBox1.Text += "max = " + max.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";






            /*
            richTextBox1.Text += "print value\n";
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    richTextBox1.Text += gray[j, i].ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            /*
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    //richTextBox1.Text += brightness[j, i].ToString("D2") + "\t";
                    //richTextBox1.Text += brightness[j, i].ToString() + "\t";
                    richTextBox1.Text += ((int)(brightness[j, i] * 100)).ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            //richTextBox1.Text += "二維陣列內容\n";
            //PrintArray(gray);

            //逐點製作圖檔

            Bitmap bitmap1 = new Bitmap(COLUMN, ROW);

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COLUMN; i++)
                {
                    //bitmap1.SetPixel(i, j, Color.FromArgb(255, (byte)(brightness[j, i] * 100), (byte)(brightness[j, i] * 100), (byte)(brightness[j, i] * 100)));
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, (byte)(brightness2[j, i]), (byte)(brightness2[j, i]), (byte)(brightness2[j, i])));
                }
            }

            /*
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p = new Pen(Color.Red, 5);
            Point point1a = new Point(0, 360);
            Point point2a = new Point(720, 360);
            g.DrawLine(p, point1a, point2a);

            point1a = new Point(360, 0);
            point2a = new Point(360, 720);
            g.DrawLine(p, point1a, point2a);
            */

            pictureBox1.Image = bitmap1;
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void PrintArray<T>(T[,] arr)
        {
            richTextBox1.Text += "Rank = " + arr.Rank.ToString() + "\n";

            int ROW = arr.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = arr.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = arr.Length;//獲取整個二維陣列的長度，即所有元 的個數
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";

            richTextBox1.Text += "L0 = " + arr.GetLength(0).ToString() + "\n";  //第0維的長度
            richTextBox1.Text += "L1 = " + arr.GetLength(1).ToString() + "\n";  //第1維的長度

            richTextBox1.Text += "t1 = " + arr.GetLowerBound(0).ToString() + "\n";  //第0維的下限 0
            richTextBox1.Text += "t2 = " + arr.GetLowerBound(1).ToString() + "\n";  //第1維的下限 0
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(0).ToString() + "\n";  //第0維的上限
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(1).ToString() + "\n";  //第1維的上限


            for (int r = arr.GetLowerBound(0); r <= arr.GetUpperBound(0); r++)
            {
                for (int c = arr.GetLowerBound(1); c <= arr.GetUpperBound(1); c++)
                {
                    richTextBox1.Text += arr[r, c].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void PrintArray<T>(T[, ,] arr)
        {
            int i;
            int rank = arr.Rank;

            richTextBox1.Text += "維度 rank = " + rank.ToString() + "\n";

            for (i = 0; i < rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + arr.GetLength(i).ToString() + "\n";
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + (arr.GetUpperBound(i) + 1).ToString() + "\n";
            }

            /*
            int ROW = arr.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = arr.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = arr.Length;//獲取整個二維陣列的長度，即所有元 的個數
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";

            richTextBox1.Text += "t1 = " + arr.GetLowerBound(0).ToString() + "\n";  //第0維的下限 0
            richTextBox1.Text += "t2 = " + arr.GetLowerBound(1).ToString() + "\n";  //第1維的下限 0
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(0).ToString() + "\n";  //第0維的上限
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(1).ToString() + "\n";  //第1維的上限
            */

            for (int r = arr.GetLowerBound(0); r <= arr.GetUpperBound(0); r++)
            {
                for (int c = arr.GetLowerBound(1); c <= arr.GetUpperBound(1); c++)
                {
                    //richTextBox1.Text += arr[r, c].ToString() + "\t";
                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
        }

    }
}
