using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Puzzle3
{
    public partial class Form1 : Form
    {
        #region 定義字段
        List<Image> imagelist;
        /// <summary>
        /// 定義屬性
        /// </summary>
        public List<Image> ImgList
        {
            get { return imagelist; }
            set
            {
                imagelist = new List<Image>();
                imagelist.Add(pictureBox1.BackgroundImage);
                imagelist.Add(pictureBox2.BackgroundImage);
                imagelist.Add(pictureBox3.BackgroundImage);
                imagelist.Add(pictureBox4.BackgroundImage);
                imagelist.Add(pictureBox5.BackgroundImage);
                imagelist.Add(pictureBox6.BackgroundImage);
            }
        }
        #endregion

        public Form1()
        {
            InitializeComponent();
            ImgList = null;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


        private void button1_Click(object sender, EventArgs e)
        {
            //隨機6個不同的數
            Random rd = new Random();
            int[] x = new int[6];
            for (int i = 0; i < 6; i++)
            {
                x[i] = rd.Next(0, 6);
                for (int j = 0; j < i; j++)
                {
                    if (x[i] == x[j])
                    {
                        i--;
                        break;
                    }
                }
            }
            //重新設置圖像
            pictureBox1.BackgroundImage = ImgList[x[0]];
            pictureBox2.BackgroundImage = ImgList[x[1]];
            pictureBox3.BackgroundImage = ImgList[x[2]];
            pictureBox4.BackgroundImage = ImgList[x[3]];
            pictureBox5.BackgroundImage = ImgList[x[4]];
            pictureBox6.BackgroundImage = ImgList[x[5]];
            //倒計時開始，並允許玩家操作
            time = 5;
            label1.Text = "5";
            timer1.Start();
            pictureBox1.Enabled = true;
            pictureBox2.Enabled = true;
            pictureBox3.Enabled = true;
            pictureBox4.Enabled = true;
            pictureBox5.Enabled = true;
            pictureBox6.Enabled = true;

        }

        #region 玩家操作
        //定義匹配變量
        int match = 0;
        //存儲上一張圖片
        PictureBox lpb = new PictureBox();
        //響應用戶操作
        private void pictureBox_Click(object sender, EventArgs e)
        {
            PictureBox pb = sender as PictureBox;
            //截取Name的最後一位作為唯一標識
            int n = int.Parse(pb.Name.Substring(10, 1));
            //判斷是否已經正確歸位，如果沒有正確歸位
            if (pb.BackgroundImage != ImgList[n - 1])
            {
                //重置參數
                if (match == 2)
                {
                    match = 0;
                }
                //交換背景圖片
                if (match == 1)
                {
                    Image img = pb.BackgroundImage;
                    pb.BackgroundImage = lpb.BackgroundImage;
                    lpb.BackgroundImage = img;
                    //判斷是否全部歸位
                    if (pictureBox1.BackgroundImage == ImgList[0] && pictureBox2.BackgroundImage == ImgList[1] && pictureBox3.BackgroundImage == ImgList[2] && pictureBox4.BackgroundImage == ImgList[3] && pictureBox5.BackgroundImage == ImgList[4] && pictureBox6.BackgroundImage == ImgList[5])
                    {
                        timer1.Stop();
                        MessageBox.Show("恭喜您，順利過關！");
                    }
                }
                lpb = pb;
                match++;
            }

        }
        #endregion
        #region 計時功能
        int time = 5;

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (time > 0)
            {
                time--;
                label1.Text = time.ToString();
            }
            else
            {
                //停止計時，並禁止玩家操作
                timer1.Stop();
                pictureBox1.Enabled = false;
                pictureBox2.Enabled = false;
                pictureBox3.Enabled = false;
                pictureBox4.Enabled = false;
                pictureBox5.Enabled = false;
                pictureBox6.Enabled = false;
                MessageBox.Show("很遺憾，游戲失敗！");
            }
        }
        #endregion
    }
}
