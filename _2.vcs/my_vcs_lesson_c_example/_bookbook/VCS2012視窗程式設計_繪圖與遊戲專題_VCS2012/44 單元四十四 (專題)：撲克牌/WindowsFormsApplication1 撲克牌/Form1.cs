using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        bool Dragging = false; // 玩家 是否進行 拖拉中
        int x0, y0;  // 開始進行 拖拉 時的 滑鼠位置

        PictureBox[] ComputerPB = new PictureBox[7];  // 電腦的 PictureBox
        PictureBox[] MyPB = new PictureBox[7];        // 玩家的 PictureBox

        int[] ComputerScore = new int[7]; // 電腦相對牌卡的牌序
        int[] MyScore = new int[7];       // 玩家相對牌卡的牌序

        int ComputerPB_Index = 0; // 電腦的 PictureBox 的索引 進行到第幾張
        int MyPB_index = 0;       // 玩家的 PictureBox 的索引 進行到第幾張

        bool ComputerPB_Active = true; // 電腦是否持續要牌
        bool MyPB_Active = true;       // 玩家是否持續要牌

        bool MyTurn = false; // 玩家時間

        int DW, DH; // 判斷是否托拉到位 的容忍值
        int[] CardSeq = new int[52]; // 紀錄 52 張牌序
        // 牌卡的點數
        int[] weight = new int[52] {1,2,3,4,5,6,7,8,9,10,10,10,10,
                                    1,2,3,4,5,6,7,8,9,10,10,10,10,
                                    1,2,3,4,5,6,7,8,9,10,10,10,10,
                                    1,2,3,4,5,6,7,8,9,10,10,10,10};
        Random rd = new Random();
        int Card_No = 0;      // 發牌序 目前發到第幾張
        int Card_Washing = 0; // 洗牌序 目前洗牌效果呈現第幾張

        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            if (MyTurn)
            {
                Dragging = true; // (玩家要牌)開始拖拉
                x0 = e.X; // 紀錄游標位置 拖拉時要計算出偏移値
                y0 = e.Y;
            }
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            int d1, d2;

            if (Dragging)
            {
                d1 = Math.Abs(MyPB[MyPB_index].Location.X - pictureBox2.Location.X);
                d2 = Math.Abs(MyPB[MyPB_index].Location.Y - pictureBox2.Location.Y);

                if (d1 <= DW && d2 <= DH)  // 是否已經拖曳到定位了
                {
                    MyScore[MyPB_index] = CardSeq[Card_No];
                    MyPB[MyPB_index].Image = imageList1.Images[CardSeq[Card_No++]];
                    pictureBox2.Location = new Point(pictureBox1.Location.X + 10, pictureBox1.Location.Y - 10);

                    // 決定 是否 玩家暴掉了
                    int sum = 0;
                    for (int i = 0; i <= MyPB_index; i++)
                        sum = sum + weight[MyScore[i]];

                    if (sum > 21)
                    {
                        MyPB_index++;
                        MessageBox.Show("玩家爆了！ 電腦贏！");
                        ComputerPB_Active = false;
                        MyPB_Active = false;
                        return;
                    }

                    Dragging = false;
                    if (MyPB_Active) // 如果玩家 還未 叫停
                    {
                        if (MyPB_index < MyPB.Length - 1) MyPB_index++;
                    }

                    if (ComputerPB_Active)  // 如果 電腦 尚未 叫停
                    {
                        MyTurn = false; // 電腦時間
                        if (ComputerPB_Index < ComputerPB.Length - 1) // 還有空間
                        {
                            ComputerPB_Index++;
                            timer2.Enabled = true;  // 讓電腦跑一次
                        }
                    }
                    else if (MyPB_Active) // 電腦 已經叫停  玩家 還未 叫停
                        MyTurn = true; // 開始 玩家時間
                }
                else  // 尚未到位 就放開滑鼠  只好歸回原位
                {
                    pictureBox2.Location = new Point(pictureBox1.Location.X + 10, pictureBox1.Location.Y - 10);
                    Dragging = false;
                }
            }

        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            int dx, dy;

            if (Dragging)
            {
                dx = (e.X - x0) + pictureBox2.Location.X; // 托拉偏移値 + 原來的位置
                dy = (e.Y - y0) + pictureBox2.Location.Y;
                pictureBox2.Location = new Point(dx, dy);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int t1, t2, temp;

            ComputerPB[0] = pictureBox3;
            ComputerPB[1] = pictureBox4;
            ComputerPB[2] = pictureBox5;
            ComputerPB[3] = pictureBox6;
            ComputerPB[4] = pictureBox7;
            ComputerPB[5] = pictureBox8;
            ComputerPB[6] = pictureBox9;

            MyPB[0] = pictureBox10;
            MyPB[1] = pictureBox11;
            MyPB[2] = pictureBox12;
            MyPB[3] = pictureBox13;
            MyPB[4] = pictureBox14;
            MyPB[5] = pictureBox15;
            MyPB[6] = pictureBox16;

            DW = pictureBox3.Width / 2; // 判斷是否托拉到位 的容忍值
            DH = pictureBox3.Height / 2;

            for (int i = 0; i <= 51; i++)
            {
                CardSeq[i] = i;
            }

            for (int i = 0; i < 100; i++) // 兩兩交換 洗牌
            {
                t1 = rd.Next(52);
                t2 = rd.Next(52);
                temp = CardSeq[t1];
                CardSeq[t1] = CardSeq[t2];
                CardSeq[t2] = temp;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 製造洗牌效果
            if (Card_Washing > 48)  // 洗好了 通通翻面
            {
                pictureBox0.Image = Properties.Resources.cardback_blue_lace;
                pictureBox1.Image = Properties.Resources.cardback_blue_lace;
                pictureBox2.Image = Properties.Resources.cardback_blue_lace;
                timer1.Enabled = false;
                timer2.Enabled = true;  // 讓電腦跑一張
            }
            else  // 製造洗牌效果
            {
                pictureBox0.Image = imageList1.Images[CardSeq[Card_Washing++]];
                pictureBox1.Image = imageList1.Images[CardSeq[Card_Washing++]];
                pictureBox2.Image = imageList1.Images[CardSeq[Card_Washing++]];
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            // 電腦跑一張 到位了
            if (ComputerPB[ComputerPB_Index].Location.X - pictureBox2.Location.X < 10)
            {
                timer2.Enabled = false; // 電腦一次只跑一張
                ComputerScore[ComputerPB_Index] = CardSeq[Card_No];
                // 將目標牌 秀出
                if (ComputerPB_Index == 0) // 電腦第一張不翻牌
                {
                    ComputerPB[ComputerPB_Index].Image = Properties.Resources.cardback_blue_lace;
                    Card_No++; // 發牌序 加一
                }
                else
                {
                    ComputerPB[ComputerPB_Index].Image = imageList1.Images[CardSeq[Card_No]];
                    Card_No++; // 發牌序 加一
                }
                pictureBox2.Location = new Point(pictureBox1.Location.X + 10, pictureBox1.Location.Y - 10);  // 瞬間將發牌 移回 原處 障眼法


                // 要決定 是否 電腦要叫停
                int sum = 0;
                int aces = 0;
                for (int i = 0; i <= ComputerPB_Index; i++)
                {
                    sum = sum + weight[ComputerScore[i]]; // 全部加總 Ace 算 1 分
                    if (weight[ComputerScore[i]] == 1) aces++; // 有幾張 Ace 
                }
                if (sum > 16) ComputerPB_Active = false; // 電腦 不再 要牌
                else if (aces >= 1 && sum > 7) ComputerPB_Active = false;
                else if (aces >= 2 && sum == 3) ComputerPB_Active = false;

                if (sum > 21)
                {
                    MessageBox.Show("電腦爆了！ 玩家贏！");
                    ComputerPB_Active = false;
                    MyPB_Active = false;
                    return;
                }

                if (MyPB_Active) // 如果玩家 還未 叫停
                    MyTurn = true; // 開始 玩家時間
                else if (ComputerPB_Active) // 否則  玩家已經叫停 且 電腦 尚未叫停
                {
                    if (ComputerPB_Index < ComputerPB.Length - 1) // 還有空間
                    {
                        ComputerPB_Index++;
                        timer2.Enabled = true;  // 讓電腦再跑一張
                    }
                }
            }
            else // 持續移動
            {
                pictureBox2.Location = new Point(pictureBox2.Location.X + 10, pictureBox2.Location.Y);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int t1, t2, temp;

            for (int i = 0; i < ComputerPB.Length; i++)
                ComputerPB[i].Image = null;  // 電腦的 PictureBox

            for (int i = 0; i < MyPB.Length; i++)
                MyPB[i].Image = null;         // 玩家的 PictureBox

            for (int i = 0; i <= 51; i++)  // 先依序排好
                CardSeq[i] = i;

            for (int i = 0; i < 100; i++)  // 再兩兩洗牌
            {
                t1 = rd.Next(52);
                t2 = rd.Next(52);
                temp = CardSeq[t1];
                CardSeq[t1] = CardSeq[t2];
                CardSeq[t2] = temp;
            }

            ComputerPB_Index = 0; // 電腦的 PictureBox 的索引
            MyPB_index = 0;       // 玩家的 PictureBox 的索引

            ComputerPB_Active = true; // 電腦是否持續要牌
            MyPB_Active = true;       // 玩家是否持續要牌

            MyTurn = false; // 玩家時間

            Card_No = 0;  // 發牌序 從頭開始

            Card_Washing = 0;  // 洗牌序 只是為了呈現效果
            timer1.Enabled = true;
        }

        // 玩家叫停
        private void button2_Click(object sender, EventArgs e)
        {
            MyPB_Active = false;

            if (MyTurn == true) // 玩家時間
            {
                if (ComputerPB_Active) // 玩家已經叫停 且 電腦 尚未叫停
                {
                    if (ComputerPB_Index < ComputerPB.Length - 1) // 還有空間
                    {
                        ComputerPB_Index++;
                        timer2.Enabled = true;  // 讓電腦跑一次
                    }
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int sum1 = 0;
            int aces1 = 0;
            int k;

            int sum2 = 0;
            int aces2 = 0;

            if (ComputerPB_Active == false) // 如果電腦已經叫停 
            {
                ComputerPB[0].Image = imageList1.Images[CardSeq[0]]; // 電腦第一張翻牌

                // 計算 電腦的最高得分
                for (int i = 0; i <= ComputerPB_Index; i++)
                {
                    sum1 = sum1 + weight[ComputerScore[i]];
                    if (weight[ComputerScore[i]] == 1) aces1++; // 電腦有幾張 Ace 
                }
                if (aces1 >= 1)
                {
                    k = sum1 + 9;
                    if (k <= 21) sum1 = k;
                }
                if (aces1 >= 2)  // 最多只會有2張Ace當作10 否則會爆掉
                {
                    k = sum1 + 9;
                    if (k <= 21) sum1 = k;
                }

                // 計算 玩家的最高得分
                for (int i = 0; i < MyPB_index; i++)
                {
                    sum2 = sum2 + weight[MyScore[i]];
                    if (weight[MyScore[i]] == 1) aces2++; // 玩家有幾張 Ace
                }
                if (aces2 >= 1)
                {
                    k = sum2 + 9;
                    if (k <= 21) sum2 = k;
                }
                if (aces2 >= 2)
                {
                    k = sum2 + 9;
                    if (k <= 21) sum2 = k;
                }

                if (sum1 > 21)
                    MessageBox.Show("電腦爆了！ 玩家贏！" + Convert.ToString(sum1) + " : " + Convert.ToString(sum2));
                else if (sum2 > 21)
                    MessageBox.Show("玩家爆了！ 電腦贏！" + Convert.ToString(sum1) + " : " + Convert.ToString(sum2));
                else if (sum1 > sum2)
                    MessageBox.Show("電腦贏！" + Convert.ToString(sum1) + " : " + Convert.ToString(sum2));
                else if (sum1 < sum2)
                    MessageBox.Show("玩家贏！" + Convert.ToString(sum1) + " : " + Convert.ToString(sum2));
                else if (sum1 == sum2)
                    MessageBox.Show("平手" + Convert.ToString(sum1) + " : " + Convert.ToString(sum2));
            }
        }

    }
}