using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 中國暗棋網路遊戲_client
{
    public partial class Form2 : Form
    {
        public int count_rand = 0;
        public static int[] Value = new int[32]; //存取亂數
        int[] TAG = new int[32];  //紀錄pictureBox中的象棋是否為紅色或黑色，１為黑色，２為紅色       
        int[] PRIORITY = new int[32];
        public Form2()
        {
            InitializeComponent();
            timer1.Enabled = true;
            timer2.Enabled = true;
            timer3.Enabled = true;
            for (int i = 0; i < 16; ++i) TAG[i] = 1;
            for (int i = 16; i < 31; ++i) TAG[i] = 2;
            for (int i = 0; i < 32; ++i)
            {
                PRIORITY[0] = PRIORITY[16] = 99;
                if ((i == 1) || (i == 2) || (i == 17) || (i == 18)) PRIORITY[i] = 98;
                else if ((i == 3) || (i == 4) || (i == 19) || (i == 20)) PRIORITY[i] = 97;
                else if ((i == 5) || (i == 6) || (i == 21) || (i == 22)) PRIORITY[i] = 96;
                else if ((i == 7) || (i == 8) || (i == 23) || (i == 24)) PRIORITY[i] = 95;
                else if ((i == 9) || (i == 10) || (i == 25) || (i == 26)) PRIORITY[i] = 99;
                else PRIORITY[i] = 1;
            }
            
        }
        public static string turn;
        public string TURN
        {

            set { turn = value; }


            get { return turn; }

        }
        public static string pri;
        public string PRI
        {

            set { pri = value; }


            get { return pri; }

        }
        public static string rand;
        public string RANDNUM
        {

            set { 
                rand = value;
                Value[count_rand] = int.Parse(rand);
                count_rand++;
            }


            get { return rand; }

        }
        public static string finish;//表亂數已經取完
        public string FINISH
        {

            set { finish = value; }


            get { return finish; }

        }
        public static string temp;
        public string TEMP
        {

            set { temp = value; }


            get { return temp; }

        }
        private void pictureBox1_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
          //  if (turn == pri)
         //   {
                if ((pictureBox1.Tag == null))
                {
                    pictureBox1.Tag = "IsClick";
                    pictureBox1.Image = imageList1.Images[Value[0]];
                    f1.POS = "[11]";//象棋位置
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }

                }
                else
                {
                    if ((TAG[Value[0]] == 1) && (pri.ToString() == "1")) //進入遊戲，第一個進來的是控制黑色，第二個進來是控制紅色
                    {

                        if ((pictureBox12.Tag != null) && (pictureBox12.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[1]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[1]] <= PRIORITY[Value[0]])
                                {
                                    pictureBox1.Image = null;
                                    pictureBox12.Image = imageList1.Images[Value[0]];
                                    pictureBox12.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }

                                }
                            }

                        }
                        else if ((pictureBox4.Tag != null) && (pictureBox4.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[3]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[0]])
                                {
                                    pictureBox1.Image = null;
                                    pictureBox4.Image = imageList1.Images[Value[0]];
                                    pictureBox4.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }

                                }
                            }

                        }

                    }
                    else if ((TAG[Value[0]] == 2) && (pri.ToString() == "2")) //進入遊戲，第一個進來的是控制黑色，第二個進來是控制紅色
                    {
                        if ((pictureBox12.Tag != null) && (pictureBox12.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[1]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[1]] <= PRIORITY[Value[0]])
                                {
                                    pictureBox1.Image = null;
                                    pictureBox12.Image = imageList1.Images[Value[0]];
                                    pictureBox12.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox4.Tag != null) && (pictureBox4.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[3]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[0]])
                                {
                                    pictureBox1.Image = null;
                                    pictureBox4.Image = imageList1.Images[Value[0]];
                                    pictureBox4.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox1.Tag = "State";

                }
                
         //   }
        }

        private void pictureBox12_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
          //  if (turn == pri)
         //   {
                if (pictureBox12.Tag == null)
                {
                    pictureBox12.Tag = "IsClick";
                    pictureBox12.Image = imageList1.Images[Value[1]];
                    f1.POS = "[12]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {

                    if (((TAG[Value[1]] == 1)) && (pri.ToString() == "1"))//控制黑色
                    {
                        if ((pictureBox1.Tag != null) && (pictureBox1.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[0]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[0]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox12.Image = null;
                                    pictureBox1.Image = imageList1.Images[Value[1]];
                                    pictureBox1.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox12.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[1]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox11.Tag != null) && (pictureBox11.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[10]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[10]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox12.Image = null;
                                    pictureBox11.Image = imageList1.Images[Value[1]];
                                    pictureBox11.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[1]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox1.Tag != null) && (pictureBox1.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[0]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[0]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox12.Image = null;
                                    pictureBox1.Image = imageList1.Images[Value[1]];
                                    pictureBox1.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 1) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox12.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[1]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox11.Tag != null) && (pictureBox11.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[10]] == 1) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[10]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox12.Image = null;
                                    pictureBox11.Image = imageList1.Images[Value[1]];
                                    pictureBox11.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox12.Tag = "State";
                }
                
         //   }
        }

        private void pictureBox11_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox11.Tag == null)
                {
                    pictureBox11.Tag = "IsClick";
                    pictureBox11.Image = imageList1.Images[Value[10]];
                    f1.POS = "[13]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[10]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox12.Tag != null) && (pictureBox12.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[11]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[11]] <= PRIORITY[Value[10]])
                                {
                                    pictureBox11.Image = null;
                                    pictureBox12.Image = imageList1.Images[Value[10]];
                                    pictureBox12.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[10]])
                                {
                                    pictureBox11.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[10]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[10]])
                                {
                                    pictureBox11.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[10]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[10]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox12.Tag != null) && (pictureBox12.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[11]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[11]] <= PRIORITY[Value[10]])
                                {
                                    pictureBox11.Image = null;
                                    pictureBox12.Image = imageList1.Images[Value[10]];
                                    pictureBox12.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[10]])
                                {
                                    pictureBox11.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[10]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[10]])
                                {
                                    pictureBox11.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[10]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox11.Tag = "State";
                }
                
        //    }
        }

        private void pictureBox10_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox10.Tag == null)
                {
                    pictureBox10.Tag = "IsClick";
                    pictureBox10.Image = imageList1.Images[Value[9]];
                    f1.POS = "[14]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[9]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox11.Tag != null) && (pictureBox11.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[10]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[10]] <= PRIORITY[Value[9]])
                                {
                                    pictureBox10.Image = null;
                                    pictureBox11.Image = imageList1.Images[Value[9]];
                                    pictureBox11.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox30.Tag != null) && (pictureBox30.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[29]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[29]] <= PRIORITY[Value[9]])
                                {
                                    pictureBox10.Image = null;
                                    pictureBox30.Image = imageList1.Images[Value[9]];
                                    pictureBox30.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox9.Tag != null) && (pictureBox9.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[8]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[8]] <= PRIORITY[Value[9]])
                                {
                                    pictureBox10.Image = null;
                                    pictureBox9.Image = imageList1.Images[Value[9]];
                                    pictureBox9.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[9]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox11.Tag != null) && (pictureBox11.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[10]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[10]] <= PRIORITY[Value[9]])
                                {
                                    pictureBox10.Image = null;
                                    pictureBox11.Image = imageList1.Images[Value[9]];
                                    pictureBox11.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox30.Tag != null) && (pictureBox30.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[29]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[29]] <= PRIORITY[Value[9]])
                                {
                                    pictureBox10.Image = null;
                                    pictureBox30.Image = imageList1.Images[Value[9]];
                                    pictureBox30.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox9.Tag != null) && (pictureBox9.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[8]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[8]] <= PRIORITY[Value[9]])
                                {
                                    pictureBox10.Image = null;
                                    pictureBox9.Image = imageList1.Images[Value[9]];
                                    pictureBox9.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }
                        }
                    }
                    else pictureBox10.Tag = "State";
                }
                
         //   }
        }

        private void pictureBox9_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
        //    {
                if (pictureBox9.Tag == null)
                {
                    pictureBox9.Tag = "IsClick";
                    pictureBox9.Image = imageList1.Images[Value[8]];
                    f1.POS = "[15]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[8]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[8]])
                                {
                                    pictureBox9.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[8]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[8]])
                                {
                                    pictureBox9.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[8]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox8.Tag != null) && (pictureBox8.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[7]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[7]] <= PRIORITY[Value[8]])
                                {
                                    pictureBox9.Image = null;
                                    pictureBox8.Image = imageList1.Images[Value[8]];
                                    pictureBox8.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[8]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox8.Tag != null) && (pictureBox8.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[8]])
                                {
                                    pictureBox9.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[8]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[8]])
                                {
                                    pictureBox9.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[8]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox8.Tag != null) && (pictureBox8.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[7]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[7]] <= PRIORITY[Value[8]])
                                {
                                    pictureBox9.Image = null;
                                    pictureBox8.Image = imageList1.Images[Value[8]];
                                    pictureBox8.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox9.Tag = "State";
                }
                
          //  }
        }

        private void pictureBox8_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
        //    {
                if (pictureBox8.Tag == null)
                {
                    pictureBox8.Tag = "IsClick";
                    pictureBox8.Image = imageList1.Images[Value[7]];
                    f1.POS = "[16]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[7]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox9.Tag != null) && (pictureBox9.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[8]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[8]] <= PRIORITY[Value[7]])
                                {
                                    pictureBox8.Image = null;
                                    pictureBox9.Image = imageList1.Images[Value[7]];
                                    pictureBox9.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox21.Tag != null) && (pictureBox21.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[20]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[20]] <= PRIORITY[Value[7]])
                                {
                                    pictureBox8.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[7]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox7.Tag != null) && (pictureBox7.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[6]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[6]] <= PRIORITY[Value[7]])
                                {
                                    pictureBox8.Image = null;
                                    pictureBox7.Image = imageList1.Images[Value[7]];
                                    pictureBox7.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[7]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox9.Tag != null) && (pictureBox9.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[8]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[8]] <= PRIORITY[Value[7]])
                                {
                                    pictureBox8.Image = null;
                                    pictureBox9.Image = imageList1.Images[Value[7]];
                                    pictureBox9.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox21.Tag != null) && (pictureBox21.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[20]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[20]] <= PRIORITY[Value[7]])
                                {
                                    pictureBox8.Image = null;
                                    pictureBox21.Image = imageList1.Images[Value[7]];
                                    pictureBox21.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox7.Tag != null) && (pictureBox7.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[6]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[6]] <= PRIORITY[Value[7]])
                                {
                                    pictureBox8.Image = null;
                                    pictureBox7.Image = imageList1.Images[Value[7]];
                                    pictureBox7.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox8.Tag = "State";
                }
                
          //  }
        }

        private void pictureBox7_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
       //     if (turn == pri)
      //      {
                if (pictureBox7.Tag == null)
                {
                    pictureBox7.Tag = "IsClick";
                    pictureBox7.Image = imageList1.Images[Value[6]];
                    f1.POS = "[17]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[6]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox8.Tag != null) && (pictureBox8.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[7]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[7]] <= PRIORITY[Value[6]])
                                {
                                    pictureBox7.Image = null;
                                    pictureBox8.Image = imageList1.Images[Value[6]];
                                    pictureBox8.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[22]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[22]] <= PRIORITY[Value[6]])
                                {
                                    pictureBox7.Image = null;
                                    pictureBox23.Image = imageList1.Images[Value[6]];
                                    pictureBox23.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox6.Tag != null) && (pictureBox6.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[5]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[5]] <= PRIORITY[Value[6]])
                                {
                                    pictureBox7.Image = null;
                                    pictureBox6.Image = imageList1.Images[Value[6]];
                                    pictureBox6.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[6]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox8.Tag != null) && (pictureBox8.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[7]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[7]] <= PRIORITY[Value[6]])
                                {
                                    pictureBox7.Image = null;
                                    pictureBox8.Image = imageList1.Images[Value[6]];
                                    pictureBox8.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[22]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[22]] <= PRIORITY[Value[6]])
                                {
                                    pictureBox7.Image = null;
                                    pictureBox23.Image = imageList1.Images[Value[6]];
                                    pictureBox23.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox6.Tag != null) && (pictureBox6.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[5]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[5]] <= PRIORITY[Value[6]])
                                {
                                    pictureBox7.Image = null;
                                    pictureBox6.Image = imageList1.Images[Value[6]];
                                    pictureBox6.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox7.Tag = "State";
                }
                
        //    }
        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox6.Tag == null)
                {
                    pictureBox6.Tag = "IsClick";
                    pictureBox6.Image = imageList1.Images[Value[5]];
                    f1.POS = "[18]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[5]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox7.Tag != null) && (pictureBox7.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[6]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[6]] <= PRIORITY[Value[5]])
                                {
                                    pictureBox6.Image = null;
                                    pictureBox7.Image = imageList1.Images[Value[5]];
                                    pictureBox7.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox25.Tag != null) && (pictureBox25.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[24]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[24]] <= PRIORITY[Value[5]])
                                {
                                    pictureBox6.Image = null;
                                    pictureBox25.Image = imageList1.Images[Value[5]];
                                    pictureBox25.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[5]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox7.Tag != null) && (pictureBox7.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[6]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[6]] <= PRIORITY[Value[5]])
                                {
                                    pictureBox6.Image = null;
                                    pictureBox7.Image = imageList1.Images[Value[5]];
                                    pictureBox7.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox25.Tag != null) && (pictureBox25.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[24]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[24]] <= PRIORITY[Value[5]])
                                {
                                    pictureBox6.Image = null;
                                    pictureBox25.Image = imageList1.Images[Value[5]];
                                    pictureBox25.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox6.Tag = "State";
                }
               
      //      }
        }

        private void pictureBox4_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
          //  if (turn == pri)
          //  {
                if (pictureBox4.Tag == null)
                {
                    pictureBox4.Tag = "IsClick";
                    pictureBox4.Image = imageList1.Images[Value[3]];
                    f1.POS = "[21]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[3]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox1.Tag != null) && (pictureBox1.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[0]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[0]] <= PRIORITY[Value[3]])
                                {
                                    pictureBox4.Image = null;
                                    pictureBox1.Image = imageList1.Images[Value[3]];
                                    pictureBox1.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox3.Tag != null) && (pictureBox3.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[2]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[2]] <= PRIORITY[Value[3]])
                                {
                                    pictureBox4.Image = null;
                                    pictureBox3.Image = imageList1.Images[Value[3]];
                                    pictureBox3.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[3]])
                                {
                                    pictureBox4.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[3]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }

                    }
                    else if (((TAG[Value[3]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox1.Tag != null) && (pictureBox1.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[0]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[0]] <= PRIORITY[Value[3]])
                                {
                                    pictureBox4.Image = null;
                                    pictureBox1.Image = imageList1.Images[Value[3]];
                                    pictureBox1.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox3.Tag != null) && (pictureBox3.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[2]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[2]] <= PRIORITY[Value[3]])
                                {
                                    pictureBox4.Image = null;
                                    pictureBox3.Image = imageList1.Images[Value[3]];
                                    pictureBox3.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[3]])
                                {
                                    pictureBox4.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[3]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox11.Tag = "State";
                }
               
       //     }
        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox5.Tag == null)
                {
                    pictureBox5.Tag = "IsClick";
                    pictureBox5.Image = imageList1.Images[Value[4]];
                    f1.POS = "[22]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[4]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox12.Tag != null) && (pictureBox12.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[11]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[11]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox12.Image = imageList1.Images[Value[4]];
                                    pictureBox12.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox4.Tag != null) && (pictureBox4.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[3]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox4.Image = imageList1.Images[Value[4]];
                                    pictureBox4.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[13]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[4]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[4]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[4]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox12.Tag != null) && (pictureBox12.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[11]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[11]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox12.Image = imageList1.Images[Value[4]];
                                    pictureBox12.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox4.Tag != null) && (pictureBox4.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[3]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox4.Image = imageList1.Images[Value[4]];
                                    pictureBox4.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[13]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[4]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[4]])
                                {
                                    pictureBox5.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[4]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox5.Tag = "State";
                }
                
      //      }
        }

        private void pictureBox27_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
           // if (turn == pri)
         //   {
                if (pictureBox27.Tag == null)
                {
                    pictureBox27.Tag = "IsClick";
                    pictureBox27.Image = imageList1.Images[Value[26]];
                    f1.POS = "[23]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[26]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[26]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox11.Tag != null) && (pictureBox11.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[10]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[10]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox11.Image = imageList1.Images[Value[26]];
                                    pictureBox11.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox30.Tag != null) && (pictureBox30.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[29]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[29]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox30.Image = imageList1.Images[Value[26]];
                                    pictureBox30.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[26]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[26]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[26]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox11.Tag != null) && (pictureBox11.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[10]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[10]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox11.Image = imageList1.Images[Value[26]];
                                    pictureBox11.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox30.Tag != null) && (pictureBox30.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[29]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[29]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox30.Image = imageList1.Images[Value[26]];
                                    pictureBox30.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[26]])
                                {
                                    pictureBox27.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[26]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox27.Tag = "State";
                }
                
        //    }
        }

        private void pictureBox30_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
          //  if (turn == pri)
          //  {
                if (pictureBox30.Tag == null)
                {
                    pictureBox30.Tag = "IsClick";
                    pictureBox30.Image = imageList1.Images[Value[29]];
                    f1.POS = "[24]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[29]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[29]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[29]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[29]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[29]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[29]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[29]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[29]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[29]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[29]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox30.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox29_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
        //    if (turn == pri)
        //    {
                if (pictureBox29.Tag == null)
                {
                    pictureBox29.Tag = "IsClick";
                    pictureBox29.Image = imageList1.Images[Value[28]];
                    f1.POS = "[25]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[28]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox30.Tag != null) && (pictureBox30.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[29]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[29]] <= PRIORITY[Value[28]])
                                {
                                    pictureBox29.Image = null;
                                    pictureBox30.Image = imageList1.Images[Value[28]];
                                    pictureBox30.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox9.Tag != null) && (pictureBox9.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[8]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[8]] <= PRIORITY[Value[28]])
                                {
                                    pictureBox29.Image = null;
                                    pictureBox9.Image = imageList1.Images[Value[28]];
                                    pictureBox9.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox21.Tag != null) && (pictureBox21.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[20]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[20]] <= PRIORITY[Value[28]])
                                {
                                    pictureBox29.Image = null;
                                    pictureBox21.Image = imageList1.Images[Value[28]];
                                    pictureBox21.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox31.Tag != null) && (pictureBox31.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[30]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[30]] <= PRIORITY[Value[28]])
                                {
                                    pictureBox29.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[28]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[28]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[29]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[29]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[29]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[29]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox29.Tag = "State";
                }
                
        //    }
        }

        private void pictureBox21_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
        //    {
                if (pictureBox21.Tag == null)
                {
                    pictureBox21.Tag = "IsClick";
                    pictureBox21.Image = imageList1.Images[Value[20]];
                    f1.POS = "[26]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[20]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[20]])
                                {
                                    pictureBox21.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[20]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox8.Tag != null) && (pictureBox8.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[7]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[7]] <= PRIORITY[Value[20]])
                                {
                                    pictureBox21.Image = null;
                                    pictureBox8.Image = imageList1.Images[Value[20]];
                                    pictureBox8.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[22]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[22]] <= PRIORITY[Value[20]])
                                {
                                    pictureBox21.Image = null;
                                    pictureBox23.Image = imageList1.Images[Value[20]];
                                    pictureBox23.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox32.Tag != null) && (pictureBox32.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[31]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[31]] <= PRIORITY[Value[20]])
                                {
                                    pictureBox21.Image = null;
                                    pictureBox32.Image = imageList1.Images[Value[20]];
                                    pictureBox32.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[20]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[29]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[29]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[29]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[29]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox21.Tag = "State";
                }
               
        //    }
        }

        private void pictureBox23_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
          //  if (turn == pri)
          //  {
                if (pictureBox23.Tag == null)
                {
                    pictureBox23.Tag = "IsClick";
                    pictureBox23.Image = imageList1.Images[Value[22]];
                    f1.POS = "[27]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[22]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[20]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[20]] <= PRIORITY[Value[22]])
                                {
                                    pictureBox23.Image = null;
                                    pictureBox21.Image = imageList1.Images[Value[22]];
                                    pictureBox21.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox7.Tag != null) && (pictureBox7.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[6]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[6]] <= PRIORITY[Value[22]])
                                {
                                    pictureBox23.Image = null;
                                    pictureBox7.Image = imageList1.Images[Value[22]];
                                    pictureBox7.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox25.Tag != null) && (pictureBox25.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[24]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[24]] <= PRIORITY[Value[22]])
                                {
                                    pictureBox23.Image = null;
                                    pictureBox25.Image = imageList1.Images[Value[22]];
                                    pictureBox25.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox22.Tag != null) && (pictureBox22.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[21]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[21]] <= PRIORITY[Value[22]])
                                {
                                    pictureBox23.Image = null;
                                    pictureBox22.Image = imageList1.Images[Value[22]];
                                    pictureBox22.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[22]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[29]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox10.Tag != null) && (pictureBox10.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[9]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[9]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox10.Image = imageList1.Images[Value[29]];
                                    pictureBox10.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[29]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State"))//隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[29]])
                                {
                                    pictureBox30.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[29]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox23.Tag = "State";
                }
                
         //   }
        }

        private void pictureBox25_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
        //    if (turn == pri)
       //     {
                if (pictureBox25.Tag == null)
                {
                    pictureBox25.Tag = "IsClick";
                    pictureBox25.Image = imageList1.Images[Value[24]];
                    f1.POS = "[28]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[24]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[22]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[22]] <= PRIORITY[Value[24]])
                                {
                                    pictureBox25.Image = null;
                                    pictureBox23.Image = imageList1.Images[Value[24]];
                                    pictureBox23.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox6.Tag != null) && (pictureBox6.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[5]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[5]] <= PRIORITY[Value[24]])
                                {
                                    pictureBox25.Image = null;
                                    pictureBox6.Image = imageList1.Images[Value[24]];
                                    pictureBox6.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox24.Tag != null) && (pictureBox24.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[23]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[23]] <= PRIORITY[Value[24]])
                                {
                                    pictureBox25.Image = null;
                                    pictureBox24.Image = imageList1.Images[Value[24]];
                                    pictureBox24.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }

                    }
                    else if (((TAG[Value[24]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[22]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[22]] <= PRIORITY[Value[24]])
                                {
                                    pictureBox25.Image = null;
                                    pictureBox23.Image = imageList1.Images[Value[24]];
                                    pictureBox23.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox6.Tag != null) && (pictureBox6.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[5]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[5]] <= PRIORITY[Value[24]])
                                {
                                    pictureBox25.Image = null;
                                    pictureBox6.Image = imageList1.Images[Value[24]];
                                    pictureBox6.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox24.Tag != null) && (pictureBox24.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[23]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[23]] <= PRIORITY[Value[24]])
                                {
                                    pictureBox25.Image = null;
                                    pictureBox24.Image = imageList1.Images[Value[24]];
                                    pictureBox24.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox25.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
        //    {
                if (pictureBox3.Tag == null)
                {
                    pictureBox3.Tag = "IsClick";
                    pictureBox3.Image = imageList1.Images[Value[2]];
                    f1.POS = "[31]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[2]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox4.Tag != null) && (pictureBox4.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[3]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[2]])
                                {
                                    pictureBox3.Image = null;
                                    pictureBox4.Image = imageList1.Images[Value[2]];
                                    pictureBox4.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[12]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[12]] <= PRIORITY[Value[2]])
                                {
                                    pictureBox3.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[2]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox2.Tag != null) && (pictureBox2.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[1]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[1]] <= PRIORITY[Value[2]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox2.Image = imageList1.Images[Value[2]];
                                    pictureBox2.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }

                    }
                    else if (((TAG[Value[2]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox4.Tag != null) && (pictureBox4.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[3]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[3]] <= PRIORITY[Value[2]])
                                {
                                    pictureBox3.Image = null;
                                    pictureBox4.Image = imageList1.Images[Value[2]];
                                    pictureBox4.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[12]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[12]] <= PRIORITY[Value[2]])
                                {
                                    pictureBox3.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[2]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox2.Tag != null) && (pictureBox2.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[1]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[1]] <= PRIORITY[Value[2]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox2.Image = imageList1.Images[Value[2]];
                                    pictureBox2.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox3.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox13_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
        //    {
                if (pictureBox13.Tag == null)
                {
                    pictureBox13.Tag = "IsClick";
                    pictureBox13.Image = imageList1.Images[Value[12]];
                    f1.POS = "[32]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[12]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox3.Tag != null) && (pictureBox3.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[2]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[2]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox3.Image = imageList1.Images[Value[12]];
                                    pictureBox3.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[12]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[12]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox20.Tag != null) && (pictureBox20.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[19]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[19]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox20.Image = imageList1.Images[Value[12]];
                                    pictureBox20.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }

                    }
                    else if (((TAG[Value[12]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox3.Tag != null) && (pictureBox3.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[2]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[2]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox3.Image = imageList1.Images[Value[12]];
                                    pictureBox3.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox5.Tag != null) && (pictureBox5.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[4]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[4]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox5.Image = imageList1.Images[Value[12]];
                                    pictureBox5.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[12]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox20.Tag != null) && (pictureBox20.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[19]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[19]] <= PRIORITY[Value[12]])
                                {
                                    pictureBox13.Image = null;
                                    pictureBox20.Image = imageList1.Images[Value[12]];
                                    pictureBox20.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox13.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox26_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox26.Tag == null)
                {
                    pictureBox26.Tag = "IsClick";
                    pictureBox26.Image = imageList1.Images[Value[25]];
                    f1.POS = "[33]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[25]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[12]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[12]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[25]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[25]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[25]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox19.Tag != null) && (pictureBox19.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[18]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[18]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox19.Image = imageList1.Images[Value[25]];
                                    pictureBox19.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[25]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[12]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[12]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[25]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox27.Tag != null) && (pictureBox27.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[26]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[26]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox27.Image = imageList1.Images[Value[25]];
                                    pictureBox27.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[25]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox19.Tag != null) && (pictureBox19.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[18]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[18]] <= PRIORITY[Value[25]])
                                {
                                    pictureBox26.Image = null;
                                    pictureBox19.Image = imageList1.Images[Value[25]];
                                    pictureBox19.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox26.Tag = "State";
                }
                
        //    }
        }

        private void pictureBox28_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
          //  if (turn == pri)
         //   {
                if (pictureBox28.Tag == null)
                {
                    pictureBox28.Tag = "IsClick";
                    pictureBox28.Image = imageList1.Images[Value[27]];
                    f1.POS = "[34]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[27]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[27]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox30.Tag != null) && (pictureBox30.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[29]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[29]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox30.Image = imageList1.Images[Value[27]];
                                    pictureBox30.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox31.Tag != null) && (pictureBox31.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[30]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[30]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[27]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox18.Tag != null) && (pictureBox18.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[17]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[17]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox18.Image = imageList1.Images[Value[27]];
                                    pictureBox18.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[27]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[27]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox30.Tag != null) && (pictureBox30.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[29]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[29]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox30.Image = imageList1.Images[Value[27]];
                                    pictureBox30.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox31.Tag != null) && (pictureBox31.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[30]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[30]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[27]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox18.Tag != null) && (pictureBox18.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[17]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[17]] <= PRIORITY[Value[27]])
                                {
                                    pictureBox28.Image = null;
                                    pictureBox18.Image = imageList1.Images[Value[27]];
                                    pictureBox18.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox28.Tag = "State";
                }
               
      //      }
        }

        private void pictureBox31_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
          //  if (turn == pri)
         //   {
                if (pictureBox31.Tag == null)
                {
                    pictureBox31.Tag = "IsClick";
                    pictureBox31.Image = imageList1.Images[Value[30]];
                    f1.POS = "[35]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[30]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[30]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[30]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox32.Tag != null) && (pictureBox32.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[31]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[31]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox32.Image = imageList1.Images[Value[30]];
                                    pictureBox32.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox17.Tag != null) && (pictureBox17.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[16]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[16]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox17.Image = imageList1.Images[Value[30]];
                                    pictureBox17.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[30]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[30]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox29.Tag != null) && (pictureBox29.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[28]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[28]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox29.Image = imageList1.Images[Value[30]];
                                    pictureBox29.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox32.Tag != null) && (pictureBox32.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[31]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[31]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox32.Image = imageList1.Images[Value[30]];
                                    pictureBox32.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox17.Tag != null) && (pictureBox17.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[16]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[16]] <= PRIORITY[Value[30]])
                                {
                                    pictureBox31.Image = null;
                                    pictureBox17.Image = imageList1.Images[Value[30]];
                                    pictureBox17.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox31.Tag = "State";
                }
                
        //    }
        }

        private void pictureBox32_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox32.Tag == null)
                {
                    pictureBox32.Tag = "IsClick";
                    pictureBox32.Image = imageList1.Images[Value[31]];
                    f1.POS = "[36]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[31]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox31.Tag != null) && (pictureBox31.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[30]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[30]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[31]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox21.Tag != null) && (pictureBox21.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[20]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[20]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox21.Image = imageList1.Images[Value[31]];
                                    pictureBox21.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox22.Tag != null) && (pictureBox22.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[21]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[21]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox22.Image = imageList1.Images[Value[31]];
                                    pictureBox22.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox16.Tag != null) && (pictureBox16.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[15]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[15]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox16.Image = imageList1.Images[Value[31]];
                                    pictureBox16.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[31]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox31.Tag != null) && (pictureBox31.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[30]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[30]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[31]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox21.Tag != null) && (pictureBox21.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[20]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[20]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox21.Image = imageList1.Images[Value[31]];
                                    pictureBox21.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox22.Tag != null) && (pictureBox22.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[21]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[21]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox22.Image = imageList1.Images[Value[31]];
                                    pictureBox22.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox16.Tag != null) && (pictureBox16.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[15]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[15]] <= PRIORITY[Value[31]])
                                {
                                    pictureBox32.Image = null;
                                    pictureBox16.Image = imageList1.Images[Value[31]];
                                    pictureBox16.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox32.Tag = "State";
                }
                
     //       }
        }

        private void pictureBox22_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
        //    {
                if (pictureBox22.Tag == null)
                {
                    pictureBox22.Tag = "IsClick";
                    pictureBox22.Image = imageList1.Images[Value[21]];
                    f1.POS = "[37]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[21]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox32.Tag != null) && (pictureBox32.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[31]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[31]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox32.Image = imageList1.Images[Value[21]];
                                    pictureBox32.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[22]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[22]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox23.Image = imageList1.Images[Value[21]];
                                    pictureBox23.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox24.Tag != null) && (pictureBox24.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[23]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[23]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox24.Image = imageList1.Images[Value[21]];
                                    pictureBox24.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox15.Tag != null) && (pictureBox15.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[14]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[14]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox15.Image = imageList1.Images[Value[21]];
                                    pictureBox15.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[21]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox32.Tag != null) && (pictureBox32.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[31]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[31]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox32.Image = imageList1.Images[Value[21]];
                                    pictureBox32.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox23.Tag != null) && (pictureBox23.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[22]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[22]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox23.Image = imageList1.Images[Value[21]];
                                    pictureBox23.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox24.Tag != null) && (pictureBox24.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[23]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[23]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox24.Image = imageList1.Images[Value[21]];
                                    pictureBox24.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox15.Tag != null) && (pictureBox15.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[14]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[14]] <= PRIORITY[Value[21]])
                                {
                                    pictureBox22.Image = null;
                                    pictureBox15.Image = imageList1.Images[Value[21]];
                                    pictureBox15.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox22.Tag = "State";
                }
               
      //      }
        }

        private void pictureBox24_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
        //    if (turn == pri)
        //    {
                if (pictureBox24.Tag == null)
                {
                    pictureBox24.Tag = "IsClick";
                    pictureBox24.Image = imageList1.Images[Value[23]];
                    f1.POS = "[38]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[23]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox25.Tag != null) && (pictureBox25.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[24]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[24]] <= PRIORITY[Value[23]])
                                {
                                    pictureBox24.Image = null;
                                    pictureBox25.Image = imageList1.Images[Value[23]];
                                    pictureBox25.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox22.Tag != null) && (pictureBox22.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[21]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[21]] <= PRIORITY[Value[23]])
                                {
                                    pictureBox24.Image = null;
                                    pictureBox22.Image = imageList1.Images[Value[23]];
                                    pictureBox22.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox14.Tag != null) && (pictureBox14.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[13]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[13]] <= PRIORITY[Value[23]])
                                {
                                    pictureBox24.Image = null;
                                    pictureBox14.Image = imageList1.Images[Value[23]];
                                    pictureBox14.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[23]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox25.Tag != null) && (pictureBox25.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[24]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[24]] <= PRIORITY[Value[23]])
                                {
                                    pictureBox24.Image = null;
                                    pictureBox25.Image = imageList1.Images[Value[23]];
                                    pictureBox25.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox22.Tag != null) && (pictureBox22.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[21]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[21]] <= PRIORITY[Value[23]])
                                {
                                    pictureBox24.Image = null;
                                    pictureBox22.Image = imageList1.Images[Value[23]];
                                    pictureBox22.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox14.Tag != null) && (pictureBox14.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[13]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[13]] <= PRIORITY[Value[23]])
                                {
                                    pictureBox24.Image = null;
                                    pictureBox14.Image = imageList1.Images[Value[23]];
                                    pictureBox14.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox24.Tag = "State";
                }
                
     //       }
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox2.Tag == null)
                {
                    pictureBox2.Tag = "IsClick";
                    pictureBox2.Image = imageList1.Images[Value[1]];
                    f1.POS = "[41]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[1]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox3.Tag != null) && (pictureBox3.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[2]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[2]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox2.Image = null;
                                    pictureBox3.Image = imageList1.Images[Value[1]];
                                    pictureBox3.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox20.Tag != null) && (pictureBox20.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[19]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[19]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox2.Image = null;
                                    pictureBox20.Image = imageList1.Images[Value[1]];
                                    pictureBox20.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[1]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox3.Tag != null) && (pictureBox3.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[2]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[2]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox2.Image = null;
                                    pictureBox3.Image = imageList1.Images[Value[1]];
                                    pictureBox3.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox20.Tag != null) && (pictureBox20.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[19]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[19]] <= PRIORITY[Value[1]])
                                {
                                    pictureBox2.Image = null;
                                    pictureBox20.Image = imageList1.Images[Value[1]];
                                    pictureBox20.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox2.Tag = "State";
                }
                
      //      }
        }

        private void pictureBox20_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
        ////    if (turn == pri)
        //    {
                if (pictureBox20.Tag == null)
                {
                    pictureBox20.Tag = "IsClick";
                    pictureBox20.Image = imageList1.Images[Value[19]];
                    f1.POS = "[42]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[19]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox2.Tag != null) && (pictureBox2.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[1]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[1]] <= PRIORITY[Value[19]])
                                {
                                    pictureBox20.Image = null;
                                    pictureBox2.Image = imageList1.Images[Value[19]];
                                    pictureBox2.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[12]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[12]] <= PRIORITY[Value[19]])
                                {
                                    pictureBox20.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[19]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox19.Tag != null) && (pictureBox19.Tag.ToString() == "State"))//隔壁的棋子被選取
                        {
                            if (TAG[Value[18]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[18]] <= PRIORITY[Value[19]])
                                {
                                    pictureBox20.Image = null;
                                    pictureBox19.Image = imageList1.Images[Value[19]];
                                    pictureBox19.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[19]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox2.Tag != null) && (pictureBox2.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[1]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[1]] <= PRIORITY[Value[19]])
                                {
                                    pictureBox20.Image = null;
                                    pictureBox2.Image = imageList1.Images[Value[19]];
                                    pictureBox2.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox13.Tag != null) && (pictureBox13.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[12]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[12]] <= PRIORITY[Value[19]])
                                {
                                    pictureBox20.Image = null;
                                    pictureBox13.Image = imageList1.Images[Value[19]];
                                    pictureBox13.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox19.Tag != null) && (pictureBox19.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[18]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[18]] <= PRIORITY[Value[19]])
                                {
                                    pictureBox20.Image = null;
                                    pictureBox19.Image = imageList1.Images[Value[19]];
                                    pictureBox19.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox20.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox19_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox19.Tag == null)
                {
                    pictureBox19.Tag = "IsClick";
                    pictureBox19.Image = imageList1.Images[Value[18]];
                    f1.POS = "[43]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[18]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox20.Tag != null) && (pictureBox20.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[19]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[19]] <= PRIORITY[Value[18]])
                                {
                                    pictureBox19.Image = null;
                                    pictureBox20.Image = imageList1.Images[Value[18]];
                                    pictureBox20.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[18]])
                                {
                                    pictureBox19.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[18]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox18.Tag != null) && (pictureBox18.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[17]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[17]] <= PRIORITY[Value[18]])
                                {
                                    pictureBox19.Image = null;
                                    pictureBox18.Image = imageList1.Images[Value[18]];
                                    pictureBox18.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[18]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox20.Tag != null) && (pictureBox20.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[19]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[19]] <= PRIORITY[Value[18]])
                                {
                                    pictureBox19.Image = null;
                                    pictureBox20.Image = imageList1.Images[Value[18]];
                                    pictureBox20.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox26.Tag != null) && (pictureBox26.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[25]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[25]] <= PRIORITY[Value[18]])
                                {
                                    pictureBox19.Image = null;
                                    pictureBox26.Image = imageList1.Images[Value[18]];
                                    pictureBox26.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox18.Tag != null) && (pictureBox18.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[17]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[17]] <= PRIORITY[Value[18]])
                                {
                                    pictureBox19.Image = null;
                                    pictureBox18.Image = imageList1.Images[Value[18]];
                                    pictureBox18.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox19.Tag = "State";
                }
               
       //     }
        }

        private void pictureBox18_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox18.Tag == null)
                {
                    pictureBox18.Tag = "IsClick";
                    pictureBox18.Image = imageList1.Images[Value[17]];
                    f1.POS = "[44]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[17]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox19.Tag != null) && (pictureBox19.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[18]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[18]] <= PRIORITY[Value[17]])
                                {
                                    pictureBox18.Image = null;
                                    pictureBox19.Image = imageList1.Images[Value[17]];
                                    pictureBox19.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[17]])
                                {
                                    pictureBox18.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[17]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox17.Tag != null) && (pictureBox17.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[16]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[16]] <= PRIORITY[Value[17]])
                                {
                                    pictureBox18.Image = null;
                                    pictureBox17.Image = imageList1.Images[Value[17]];
                                    pictureBox17.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[17]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox19.Tag != null) && (pictureBox19.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[18]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[18]] <= PRIORITY[Value[17]])
                                {
                                    pictureBox18.Image = null;
                                    pictureBox19.Image = imageList1.Images[Value[17]];
                                    pictureBox19.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox28.Tag != null) && (pictureBox28.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[27]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[27]] <= PRIORITY[Value[17]])
                                {
                                    pictureBox18.Image = null;
                                    pictureBox28.Image = imageList1.Images[Value[17]];
                                    pictureBox28.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox17.Tag != null) && (pictureBox17.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[16]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[16]] <= PRIORITY[Value[17]])
                                {
                                    pictureBox18.Image = null;
                                    pictureBox17.Image = imageList1.Images[Value[17]];
                                    pictureBox17.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox18.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox17_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
        //    {
                if (pictureBox17.Tag == null)
                {
                    pictureBox17.Tag = "IsClick";
                    pictureBox17.Image = imageList1.Images[Value[16]];
                    f1.POS = "[45]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[16]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox18.Tag != null) && (pictureBox18.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[17]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[17]] <= PRIORITY[Value[16]])
                                {
                                    pictureBox17.Image = null;
                                    pictureBox18.Image = imageList1.Images[Value[16]];
                                    pictureBox18.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox31.Tag != null) && (pictureBox31.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[30]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[30]] <= PRIORITY[Value[16]])
                                {
                                    pictureBox17.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[16]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox16.Tag != null) && (pictureBox16.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[15]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[15]] <= PRIORITY[Value[16]])
                                {
                                    pictureBox17.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[16]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[16]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox18.Tag != null) && (pictureBox18.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[17]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[17]] <= PRIORITY[Value[16]])
                                {
                                    pictureBox17.Image = null;
                                    pictureBox18.Image = imageList1.Images[Value[16]];
                                    pictureBox18.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox31.Tag != null) && (pictureBox31.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[30]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[30]] <= PRIORITY[Value[16]])
                                {
                                    pictureBox17.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[16]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox16.Tag != null) && (pictureBox16.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[15]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[15]] <= PRIORITY[Value[16]])
                                {
                                    pictureBox17.Image = null;
                                    pictureBox31.Image = imageList1.Images[Value[16]];
                                    pictureBox31.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox17.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox16_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox16.Tag == null)
                {
                    pictureBox16.Tag = "IsClick";
                    pictureBox16.Image = imageList1.Images[Value[15]];
                    f1.POS = "[46]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[15]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox17.Tag != null) && (pictureBox17.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[16]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[16]] <= PRIORITY[Value[15]])
                                {
                                    pictureBox16.Image = null;
                                    pictureBox17.Image = imageList1.Images[Value[15]];
                                    pictureBox17.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox32.Tag != null) && (pictureBox32.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[31]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[31]] <= PRIORITY[Value[15]])
                                {
                                    pictureBox16.Image = null;
                                    pictureBox32.Image = imageList1.Images[Value[15]];
                                    pictureBox32.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox15.Tag != null) && (pictureBox15.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[14]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[14]] <= PRIORITY[Value[15]])
                                {
                                    pictureBox16.Image = null;
                                    pictureBox15.Image = imageList1.Images[Value[15]];
                                    pictureBox15.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[15]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox17.Tag != null) && (pictureBox17.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[16]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[16]] <= PRIORITY[Value[15]])
                                {
                                    pictureBox16.Image = null;
                                    pictureBox17.Image = imageList1.Images[Value[15]];
                                    pictureBox17.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox32.Tag != null) && (pictureBox32.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[31]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[31]] <= PRIORITY[Value[15]])
                                {
                                    pictureBox16.Image = null;
                                    pictureBox32.Image = imageList1.Images[Value[15]];
                                    pictureBox32.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox15.Tag != null) && (pictureBox15.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[14]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[14]] <= PRIORITY[Value[15]])
                                {
                                    pictureBox16.Image = null;
                                    pictureBox15.Image = imageList1.Images[Value[15]];
                                    pictureBox15.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox16.Tag = "State";
                }
                
      //      }
        }

        private void pictureBox15_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
         //   if (turn == pri)
         //   {
                if (pictureBox15.Tag == null)
                {
                    pictureBox15.Tag = "IsClick";
                    pictureBox15.Image = imageList1.Images[Value[14]];
                    f1.POS = "[47]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[14]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox16.Tag != null) && (pictureBox16.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[15]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[15]] <= PRIORITY[Value[14]])
                                {
                                    pictureBox15.Image = null;
                                    pictureBox16.Image = imageList1.Images[Value[14]];
                                    pictureBox16.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox22.Tag != null) && (pictureBox22.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[21]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[21]] <= PRIORITY[Value[14]])
                                {
                                    pictureBox15.Image = null;
                                    pictureBox22.Image = imageList1.Images[Value[14]];
                                    pictureBox22.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox14.Tag != null) && (pictureBox14.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[13]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[13]] <= PRIORITY[Value[14]])
                                {
                                    pictureBox15.Image = null;
                                    pictureBox14.Image = imageList1.Images[Value[14]];
                                    pictureBox14.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else if (((TAG[Value[14]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox16.Tag != null) && (pictureBox16.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[15]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[15]] <= PRIORITY[Value[14]])
                                {
                                    pictureBox15.Image = null;
                                    pictureBox16.Image = imageList1.Images[Value[14]];
                                    pictureBox16.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox22.Tag != null) && (pictureBox22.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[21]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[21]] <= PRIORITY[Value[14]])
                                {
                                    pictureBox15.Image = null;
                                    pictureBox22.Image = imageList1.Images[Value[14]];
                                    pictureBox22.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox14.Tag != null) && (pictureBox14.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[13]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[13]] <= PRIORITY[Value[14]])
                                {
                                    pictureBox15.Image = null;
                                    pictureBox14.Image = imageList1.Images[Value[14]];
                                    pictureBox14.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox15.Tag = "State";
                }
                
       //     }
        }

        private void pictureBox14_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
        //    if (turn == pri)
         //   {
                if (pictureBox14.Tag == null)
                {
                    pictureBox14.Tag = "IsClick";
                    pictureBox14.Image = imageList1.Images[Value[13]];
                    f1.POS = "[48]";
                    if (turn == "1")
                    {
                        turn = "2";
                        f1.TURN = "2";
                    }
                    else
                    {
                        turn = "1";
                        f1.TURN = "1";
                    }
                }
                else
                {
                    if (((TAG[Value[13]] == 1)) && (pri.ToString() == "1"))
                    {
                        if ((pictureBox15.Tag != null) && (pictureBox15.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[14]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[14]] <= PRIORITY[Value[13]])
                                {
                                    pictureBox14.Image = null;
                                    pictureBox15.Image = imageList1.Images[Value[13]];
                                    pictureBox15.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox24.Tag != null) && (pictureBox24.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[23]] == 2) // 要被吃的棋子是紅色的
                            {
                                if (PRIORITY[Value[23]] <= PRIORITY[Value[13]])
                                {
                                    pictureBox14.Image = null;
                                    pictureBox24.Image = imageList1.Images[Value[13]];
                                    pictureBox24.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }

                    }
                    else if (((TAG[Value[13]] == 2)) && (pri.ToString() == "2"))
                    {
                        if ((pictureBox15.Tag != null) && (pictureBox15.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[14]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[14]] <= PRIORITY[Value[13]])
                                {
                                    pictureBox14.Image = null;
                                    pictureBox15.Image = imageList1.Images[Value[13]];
                                    pictureBox15.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                        else if ((pictureBox24.Tag != null) && (pictureBox24.Tag.ToString() == "State")) //隔壁的棋子被選取
                        {
                            if (TAG[Value[23]] == 1) // 要被吃的棋子是黑色的
                            {
                                if (PRIORITY[Value[23]] <= PRIORITY[Value[13]])
                                {
                                    pictureBox14.Image = null;
                                    pictureBox24.Image = imageList1.Images[Value[13]];
                                    pictureBox24.Tag = "IsClick";
                                    if (turn == "1")
                                    {
                                        turn = "2";
                                        f1.TURN = "2";
                                    }
                                    else
                                    {
                                        turn = "1";
                                        f1.TURN = "1";
                                    }
                                }
                            }

                        }
                    }
                    else pictureBox14.Tag = "State";
                }
                
        //    }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            
            if ((finish == "finishRand"))
            {

                count_rand = 0;
               // Init();
                finish = null;
                rand = null;

                turn = "1";
                pictureBox1.Image = imageList1.Images[32];
                pictureBox2.Image = imageList1.Images[32];
                pictureBox3.Image = imageList1.Images[32];
                pictureBox4.Image = imageList1.Images[32];
                pictureBox5.Image = imageList1.Images[32];
                pictureBox6.Image = imageList1.Images[32];
                pictureBox7.Image = imageList1.Images[32];
                pictureBox8.Image = imageList1.Images[32];
                pictureBox9.Image = imageList1.Images[32];
                pictureBox10.Image = imageList1.Images[32];
                pictureBox11.Image = imageList1.Images[32];
                pictureBox12.Image = imageList1.Images[32];
                pictureBox13.Image = imageList1.Images[32];
                pictureBox14.Image = imageList1.Images[32];
                pictureBox15.Image = imageList1.Images[32];
                pictureBox16.Image = imageList1.Images[32];
                pictureBox17.Image = imageList1.Images[32];
                pictureBox18.Image = imageList1.Images[32];
                pictureBox19.Image = imageList1.Images[32];
                pictureBox20.Image = imageList1.Images[32];
                pictureBox21.Image = imageList1.Images[32];
                pictureBox22.Image = imageList1.Images[32];
                pictureBox23.Image = imageList1.Images[32];
                pictureBox24.Image = imageList1.Images[32];
                pictureBox25.Image = imageList1.Images[32];
                pictureBox26.Image = imageList1.Images[32];
                pictureBox27.Image = imageList1.Images[32];
                pictureBox28.Image = imageList1.Images[32];
                pictureBox29.Image = imageList1.Images[32];
                pictureBox30.Image = imageList1.Images[32];
                pictureBox31.Image = imageList1.Images[32];
                pictureBox32.Image = imageList1.Images[32];
            }
        }
        private void Init() //洗好的棋子翻面
        {
            
          //  PRIORITY[] = {99 , 98 , 98 , 97 , 97 , 96 , 96 , 95 , 95 , 99 , 99 , 1 , 1 , 1 , 1 , 1 , 99 , 98 , 98 , 97 , 97 , 96 , 96 , 95 , 95 , 99 , 99 , 1 , 1 , 1 , 1 , 1 };
           
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (temp != null)
            {
                if (temp == "[11]")
                {
                    pictureBox1.Image = imageList1.Images[Value[0]];
                    temp = null;
                }
                else if (temp == "[12]")
                {
                    pictureBox12.Image = imageList1.Images[Value[1]];
                    temp = null;
                }
                else if (temp == "[13]")
                {
                    pictureBox11.Image = imageList1.Images[Value[10]];
                    temp = null;
                }
                else if (temp == "[14]")
                {
                    pictureBox10.Image = imageList1.Images[Value[9]];
                    temp = null;
                }
                else if (temp == "[15]")
                {
                    pictureBox9.Image = imageList1.Images[Value[8]];
                    temp = null;
                }
                else if (temp == "[16]")
                {
                    pictureBox8.Image = imageList1.Images[Value[7]];
                    temp = null;
                }
                else if (temp == "[17]")
                {
                    pictureBox7.Image = imageList1.Images[Value[6]];
                    temp = null;
                }
                else if (temp == "[18]")
                {
                    pictureBox6.Image = imageList1.Images[Value[5]];
                    temp = null;
                }
                else if (temp == "[21]")
                {
                    pictureBox4.Image = imageList1.Images[Value[3]];
                    temp = null;
                }
                else if (temp == "[22]")
                {
                    pictureBox5.Image = imageList1.Images[Value[4]];
                    temp = null;
                }
                else if (temp == "[23]")
                {
                    pictureBox27.Image = imageList1.Images[Value[26]];
                    temp = null;
                }
                else if (temp == "[24]")
                {
                    pictureBox30.Image = imageList1.Images[Value[29]];
                    temp = null;
                }
                else if (temp == "[25]")
                {
                    pictureBox29.Image = imageList1.Images[Value[28]];
                    temp = null;
                }
                else if (temp == "[26]")
                {
                    pictureBox21.Image = imageList1.Images[Value[20]];
                    temp = null;
                }
                else if (temp == "[27]")
                {
                    pictureBox23.Image = imageList1.Images[Value[22]];
                    temp = null;
                }
                else if (temp == "[28]")
                {
                    pictureBox25.Image = imageList1.Images[Value[24]];
                    temp = null;
                }
                else if (temp == "[31]")
                {
                    pictureBox3.Image = imageList1.Images[Value[2]];
                    temp = null;
                }
                else if (temp == "[32]")
                {
                    pictureBox13.Image = imageList1.Images[Value[12]];
                    temp = null;
                }
                else if (temp == "[33]")
                {
                    pictureBox26.Image = imageList1.Images[Value[25]];
                    temp = null;
                }
                else if (temp == "[34]")
                {
                    pictureBox28.Image = imageList1.Images[Value[27]];
                    temp = null;
                }
                else if (temp == "[35]")
                {
                    pictureBox31.Image = imageList1.Images[Value[30]];
                    temp = null;
                }
                else if (temp == "[36]")
                {
                    pictureBox32.Image = imageList1.Images[Value[31]];
                    temp = null;
                }
                else if (temp == "[37]")
                {
                    pictureBox22.Image = imageList1.Images[Value[21]];
                    temp = null;
                }
                else if (temp == "[38]")
                {
                    pictureBox24.Image = imageList1.Images[Value[23]];
                    temp = null;
                }
                else if (temp == "[41]")
                {
                    pictureBox2.Image = imageList1.Images[Value[1]];
                    temp = null;
                }
                else if (temp == "[42]")
                {
                    pictureBox20.Image = imageList1.Images[Value[19]];
                    temp = null;
                }
                else if (temp == "[43]")
                {
                    pictureBox19.Image = imageList1.Images[Value[18]];
                    temp = null;
                }
                else if (temp == "[44]")
                {
                    pictureBox18.Image = imageList1.Images[Value[17]];
                    temp = null;
                }
                else if (temp == "[45]")
                {
                    pictureBox17.Image = imageList1.Images[Value[16]];
                    temp = null;
                }
                else if (temp == "[46]")
                {
                    pictureBox16.Image = imageList1.Images[Value[15]];
                    temp = null;
                }
                else if (temp == "[47]")
                {
                    pictureBox15.Image = imageList1.Images[Value[14]];
                    temp = null;
                }
                else if (temp == "[48]")
                {
                    pictureBox14.Image = imageList1.Images[Value[13]];
                    temp = null;
                }
            }
        }

    }
}
