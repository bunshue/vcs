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
        PictureBox[] picArray = new PictureBox[16];
        int[] imageId = new int[16];
        int firstPicPos = -1; //尚未有任何翻開的圖片
        int counter = 0;
        DateTime start;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            picArray[0] = pictureBox1;
            picArray[1] = pictureBox2;
            picArray[2] = pictureBox3;
            picArray[3] = pictureBox4;
            picArray[4] = pictureBox5;
            picArray[5] = pictureBox6;
            picArray[6] = pictureBox7;
            picArray[7] = pictureBox8;
            picArray[8] = pictureBox9;
            picArray[9] = pictureBox10;
            picArray[10] = pictureBox11;
            picArray[11] = pictureBox12;
            picArray[12] = pictureBox13;
            picArray[13] = pictureBox14;
            picArray[14] = pictureBox15;
            picArray[15] = pictureBox16;
            // 顯示背面圖像
            for (int i = 0; i < 16; i++)
                picArray[i].Image = imageList1.Images[8];
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
                picArray[i].Image = imageList1.Images[id];
            }*/

            start = DateTime.Now;


        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            PictureBox s = (PictureBox)sender;

            int picPos = 0;
            // 取得目前被按的PictureBox，將其位置記錄在picPos
            for (int i = 0; i < 16; i++)
                if (s == picArray[i])
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
                picArray[picPos].Image = imageList1.Images[id];
                firstPicPos = picPos;
            }
            else
            {
                //已有打開的圖片
                if (picPos == firstPicPos) return;// 相同位置
                // 這是第二張, 打開此圖片
                picArray[picPos].Image = imageList1.Images[id];
                // 強制更新, 再延遲0.5秒
                picArray[picPos].Refresh();
                //for (long i = 0; i <= 100000000; i++) ;
                Thread.Sleep(500);

                if (id == imageId[firstPicPos])
                {
                    // 相同圖像, 取走此兩張牌
                    picArray[picPos].Image = null;
                    picArray[firstPicPos].Image = null;

                    imageId[firstPicPos] = -1;
                    imageId[picPos] = -1;

                    counter += 2;

                    if (counter == 16)
                    {   // 計算所花的時間
                        DateTime end = DateTime.Now;

                        TimeSpan t = end - start;
                        int ts = (int)t.TotalSeconds;
                        MessageBox.Show("完成! 共花了" + ts + "秒",
                                        "記憶遊戲",
                                        MessageBoxButtons.OK,
                                        MessageBoxIcon.Information);
                    }

                }
                else
                {   // 圖像不相同, 蓋上此兩張牌
                    picArray[firstPicPos].Image = imageList1.Images[8];
                    picArray[picPos].Image = imageList1.Images[8];

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
                picArray[i].Image = imageList1.Images[id];
                picArray[i].Refresh();
            }

            Thread.Sleep(2000);

            for (int i = 0; i < 16; i++)
            {
                if (imageId[i] != -1)
                    picArray[i].Image = imageList1.Images[8];
            }
        }
    }
}
