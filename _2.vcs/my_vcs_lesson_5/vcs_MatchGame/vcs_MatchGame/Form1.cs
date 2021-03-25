using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_MatchGame
{
    public partial class Form1 : Form
    {
        int[] imageId = new int[16];
        int firstPicPos = -1; //尚未有任何翻開的圖片
        int counter = 0;
        DateTime start;
        PictureBox[] pbx = new PictureBox[16];

        public Form1()
        {
            InitializeComponent();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int w = 102;
            int h = 76;

            x_st = 50;
            y_st = 50;
            dx = w * 12 / 10;
            dy = h * 12 / 10;
            int i;
            for (i = 0; i < pbx.Length; i++)
            {
                pbx[i] = new PictureBox();
                pbx[i].AutoSize = false;
                pbx[i].Name = "pbx" + i.ToString();
                pbx[i].Text = (i + 1).ToString();
                pbx[i].Click += pbx_Click;
                pbx[i].Location = new Point(x_st + dx * (i % 4), y_st + dy * (i / 4));
                pbx[i].Size = new Size(w, h);
                pbx[i].Tag = "pbx : " + i.ToString();
                pbx[i].BackColor = Color.Gray;
                this.Controls.Add(pbx[i]);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            for (int i = 0; i < pbx.Length; i++)
            {
                pbx[i] = pbx[i];
            }

            // 顯示背面圖像
            for (int i = 0; i < 16; i++)
                pbx[i].Image = imageList1.Images[8];
            // 產生隨機打散的圖像資料
            for (int i = 0; i < 8; i++)
            {
                imageId[i * 2] = i;
                imageId[i * 2 + 1] = i;
            }

            Random rd = new Random();

            for (int i = 0; i < 16; i++)
            {
                int t = rd.Next(0, 16);
                int temp = imageId[i];
                imageId[i] = imageId[t];
                imageId[t] = temp;
            }

            /*for (int i = 0; i < 16; i++)
            {
                int id = imageId[i];
                pbx[i].Image = imageList1.Images[id];
            }*/

            start = DateTime.Now;
        }

        private void pbx_Click(object sender, EventArgs e)
        {
            PictureBox s = (PictureBox)sender;

            int picPos = 0;
            // 取得目前被按的PictureBox，將其位置記錄在picPos
            for (int i = 0; i < 16; i++)
                if (s == pbx[i])
                {
                    picPos = i;
                    break;
                }
            // 取得目前的圖像Id
            int id = imageId[picPos];
            if (id == -1) return; //已取走圖片

            // 是否為第一張?
            if (firstPicPos == -1)
            {   //此是第一張, 記錄其位置並打開圖片
                pbx[picPos].Image = imageList1.Images[id];
                firstPicPos = picPos;
            }
            else
            {
                //已有打開的圖片
                if (picPos == firstPicPos) return;// 相同位置
                // 這是第二張, 打開此圖片
                pbx[picPos].Image = imageList1.Images[id];
                // 強制更新, 再延遲0.5秒
                pbx[picPos].Refresh();
                //for (long i = 0; i <= 100000000; i++) ;
                Thread.Sleep(500);

                if (id == imageId[firstPicPos])
                {
                    // 相同圖像, 取走此兩張牌
                    pbx[picPos].Image = null;
                    pbx[firstPicPos].Image = null;

                    imageId[firstPicPos] = -1;
                    imageId[picPos] = -1;

                    counter += 2;

                    if (counter == 16)
                    {   // 計算所花的時間
                        DateTime end = DateTime.Now;

                        TimeSpan t = end - start;
                        int ts = (int)t.TotalSeconds;
                        MessageBox.Show("完成! 共花了" + ts + "秒", "記憶遊戲", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
                else
                {   // 圖像不相同, 蓋上此兩張牌
                    pbx[firstPicPos].Image = imageList1.Images[8];
                    pbx[picPos].Image = imageList1.Images[8];
                }
                firstPicPos = -1;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < 16; i++)
            {
                int id = imageId[i];
                if (id == -1) continue;
                pbx[i].Image = imageList1.Images[id];
                pbx[i].Refresh();
            }

            Thread.Sleep(2000);

            for (int i = 0; i < 16; i++)
            {
                if (imageId[i] != -1)
                {
                    pbx[i].Image = imageList1.Images[8];
                }
            }
        }
    }
}