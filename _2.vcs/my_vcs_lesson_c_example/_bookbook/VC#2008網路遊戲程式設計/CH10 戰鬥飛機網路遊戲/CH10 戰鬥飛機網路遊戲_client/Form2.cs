using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 戰鬥飛機網路遊戲_client
{
    public partial class Form2 : Form
    {
        int bom_cnt1;//第一個飛彈變數
        int bom_cnt2;//第二個飛彈變數
        int x, y;
        int found1, found2, found3, Bfound1, Bfound2, Bfound3;//拆解訊號時所用到的變數
        int PP;                      //拆解訊號時所用到的變數                            
        string co_top, co_left, cob_top, cob_left;//拆解訊號時所用到的變數
        string BB1, BB2;//拆解訊號時所用到的變數
        Form1 f1 = new Form1();
        public Form2()
        {
            InitializeComponent();
            button1.Enabled = true;
            button2.Enabled = true;
            button3.Enabled = true;
            button4.Enabled = true;
            button6.Visible = true;
            picact1.Visible = true;
            timer3.Enabled = true;
            timer2.Enabled = true;
            timer5.Enabled = true;
            timer6.Enabled = true;
        }
        static string p;
        public string P
        {

            set { p = value; }


            get { return p; }

        }
        static string co;//飛機座標
        public string CO
        {

            set { co = value; }


            get { return co; }

        }
        static string cob;//飛彈座標
        public string COB
        {

            set { cob = value; }


            get { return cob; }

        }
        static string lose;//飛彈座標
        public string LOSE
        {

            set { lose = value; }


            get { return lose; }

        }
        static string win;//飛彈座標
        public string WIN
        {

            set { win = value; }


            get { return win; }

        }
        private void button3_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            if (p == "2")
            {
                if (picact.Top > 0)
                {
                    picact.Top -= 10;
                    f1.CO = p + "|" + picact.Top.ToString() + "@" + picact.Left.ToString() + "#" + "co"; 
                    
               //     label1.Text = "目前 X  座標：" + picact.Top.ToString();
               //     label2.Text = "目前 Y  座標：" + picact.Left.ToString();
                }
                else
                {
                    if (picact.Top == 0)
                    {
                        picact.Visible = false;
                        MessageBox.Show("飛機已撞毀，玩家請重新來過。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose";
                      //  gamestart();
                    }
                }
            }
            else if (p == "1")
            {
                if (picact1.Top > 0)
                {
                   
                    picact1.Top -= 10;
                    f1.CO = p + "|" + picact1.Top.ToString() + "@" + picact1.Left.ToString() + "#" + "co"; 
                //    label1.Text = "目前 X  座標：" + picact1.Top.ToString();
                //    label2.Text = "目前 Y  座標：" + picact1.Left.ToString();
                }
                else
                {
                    if (picact1.Top == 0)
                    {
                        picact1.Visible = false;
                        MessageBox.Show("飛機已撞毀，玩家請重新來過。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose";
                      //  gamestart();
                    }
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (p == "2")
            {
                if (picact.Top < 130)
                {
                    
                    picact.Top += 10;
                    f1.CO = p + "|" + picact.Top.ToString() + "@" + picact.Left.ToString() + "#" + "co"; 
                }
                else
                {
                    if (picact.Top == 130)
                    {
                        picact.Visible = false;
                        MessageBox.Show("玩家1飛機已撞毀，玩家2贏了。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose";
                      //  gamestart();
                    }
                }
            }
            else if (p == "1")
            {
                if (picact1.Top < 130)
                {
                    

                    picact1.Top += 10;
                    f1.CO = p + "|" + picact1.Top.ToString() + "@" + picact1.Left.ToString() + "#" + "co"; 
                }
                else
                {
                    if (picact1.Top == 130)
                    {
                        picact1.Visible = false;
                        MessageBox.Show("玩家1飛機已撞毀，玩家2贏了。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose";
                       // gamestart();
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (p == "2")
            {
                if (picact.Left >= 140)
                {
                    picact.Left -= 10;
                    f1.CO = p + "|" + picact.Top.ToString() + "@" + picact.Left.ToString() + "#" + "co"; 
                //    label1.Text = "目前 X  座標：" + picact.Top.ToString();
                //    label2.Text = "目前 Y  座標：" + picact.Left.ToString();
                }
                else
                {
                    if (picact.Left < 150)
                    {
                        picact.Visible = false;
                        MessageBox.Show("飛機已與敵機自爆，玩家請重新來過。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose";
                       // gamestart();
                    }
                }
            }
            else if (p == "1")
            {

                if (picact1.Left >= 140)
                {
                    picact1.Left -= 10;
                    f1.CO = p + "|" + picact1.Top.ToString() + "@" + picact1.Left.ToString() + "#" + "co"; 
                //    label1.Text = "目前 X  座標：" + picact1.Top.ToString();
                //    label2.Text = "目前 Y  座標：" + picact1.Left.ToString();
                }
                else
                {
                    if (picact1.Left < 150)
                    {
                        picact1.Visible = false;
                        MessageBox.Show("飛機已與敵機自爆，玩家請重新來過。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose";
                       // gamestart();
                    }
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (p == "2")
            {
                if (picact.Left <= 580)
                {
                    picact.Left += 10;
                    f1.CO = p + "|" + picact.Top.ToString() + "@" + picact.Left.ToString() + "#" + "co"; 
               //     label1.Text = "目前 X  座標：" + picact.Top.ToString();
               //     label2.Text = "目前 Y  座標：" + picact.Left.ToString();
                }
                else
                {
                    if (picact.Left > 580)
                    {
                        picact.Visible = false;
                        MessageBox.Show("飛機已撞毀，玩家請重新來過。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose";
                       // gamestart();

                    }
                }
            }
            else if (p == "1")
            {
                if (picact1.Left <= 580)
                {
                    picact1.Left += 10;
                    f1.CO = p + "|" + picact1.Top.ToString() + "@" + picact1.Left.ToString() + "#" + "co"; 
               //     label1.Text = "目前 X  座標：" + picact1.Top.ToString();
               //     label2.Text = "目前 Y  座標：" + picact1.Left.ToString();
                }
                else
                {
                    if (picact1.Left > 580)
                    {
                        picact1.Visible = false;
                        MessageBox.Show("飛機已撞毀，玩家請重新來過。", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        f1.LOSE = "lose" + "|" + p;
                       // gamestart();

                    }
                }
            }
                
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();

            if (p == "2")
            {
                bom_cnt2 = 0;
                f1.COB = p + "|" + pictureBox2.Top.ToString() + "@" + pictureBox2.Left.ToString() + "#" + "cob";
                pictureBox2.Visible = true;
                timer1.Enabled = true;
            }
            else
            {
                bom_cnt1 = 0;
                f1.COB = p + "|" + pictureBox3.Top.ToString() + "@" + pictureBox3.Left.ToString() + "#" + "cob";
                pictureBox3.Visible = true;
                timer1.Enabled = true;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (p == "2")
            {
                bom_cnt2 = bom_cnt2 + 50;
                y = picact.Top;
                x = picact.Left;

                pictureBox2.Location = new Point(x - bom_cnt2, y);
                f1.COB = p + "|" + pictureBox2.Top.ToString() + "@" + pictureBox2.Left.ToString() + "#" + "cob";
                
            }
            else
            {
                bom_cnt1 = bom_cnt1 + 50;
                y = picact1.Top;
                x = picact1.Left;

                pictureBox3.Location = new Point(x + bom_cnt1, y);
                f1.COB = p + "|" + pictureBox3.Top.ToString() + "@" + pictureBox3.Left.ToString() + "#" + "cob";
            }
           
        }

        private void button5_Click(object sender, EventArgs e)
        {
            
               
            
        }
        public void gamestart() //遊戲開始時的設定
        {
            picact.Location = new Point(578, 0);
            picact1.Location = new Point(0, 0);
            picact.Visible = true;
            picact1.Visible = true;
        //    label1.Text = "X軸";
        //    label2.Text = "Y軸";

            button6.Visible = false;
            
    
      
        }

        private void timer6_Tick(object sender, EventArgs e)
        {
            
            
            if ((co != null))
            {
                found1 = co.IndexOf("|");
                found2 = co.IndexOf("@");
                found3 = co.IndexOf("#");
                if (found1 >= 0)
                {
                    PP = int.Parse(co.Substring(0 , found1));
                    co_top = co.Substring(found1 + 1 , found2 - found1 - 1);
                    co_left = co.Substring(found2 + 1 , found3 - found2 - 1);
                    BB1 = co.Substring(found3 + 1);
                    
                }
                if ((PP == 1) && (BB1 == "co"))
                {
                    picact1.Top = int.Parse(co_top);
                    picact1.Left = int.Parse(co_left); ;
                    label1.Text = "目前 X  座標：" + picact1.Top.ToString();
                    label2.Text = "目前 Y  座標：" + picact1.Left.ToString();
                   
                }
                if ((PP == 2) && (BB1 == "co"))
                {
                    picact.Top = int.Parse(co_top);
                    picact.Left = int.Parse(co_left); ;
                    label1.Text = "目前 X  座標：" + picact.Top.ToString();
                    label2.Text = "目前 Y  座標：" + picact.Left.ToString();
                   
                }
                co = null;
            }
        }

        private void timer5_Tick(object sender, EventArgs e)
        {
      
            if ((cob != null))
            {
                Bfound1 = cob.IndexOf("|");
                Bfound2 = cob.IndexOf("@");
                Bfound3 = cob.IndexOf("#");
                if (Bfound1 >= 0)
                {
                    PP = int.Parse(cob.Substring(0, Bfound1));
                    cob_top = cob.Substring(Bfound1 + 1, Bfound2 - Bfound1 - 1);
                    cob_left = cob.Substring(Bfound2 + 1 , Bfound3 - Bfound2 - 1);
                    BB2 = cob.Substring(Bfound3 + 1);
                    
                }
                if ((PP == 1) && (BB2 == "cob"))
                {
                    pictureBox3.Visible = true;
                    pictureBox3.Top = int.Parse(cob_top);
                    pictureBox3.Left = int.Parse(cob_left); ;
                   
                   
                   /*
                   if ((pictureBox3.Left > picact.Left) && (pictureBox3.Top < picact.Top)) //炸到敵機
                    if ((pictureBox3.Left < picact.Left + 136) && (picact1.Left > picact.Left - 136)) //炸到敵機                  
                   */

                    if ((pictureBox3.Top == picact.Top)) 
                        {
                           // timer1.Stop();
                            timer5.Stop();
                            f1.WIN = "win";
                            picact.Visible = false;
                            pictureBox3.Visible = false;
                           // timer5.Enabled = false;
                            MessageBox.Show("恭喜您，\n您獲勝了！", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Information);
                            
                            //Application.Exit();
                          //  gamestart();
                        }
                    
                    
                }
                if ((PP == 2) && (BB2 == "cob"))
                {
                    pictureBox2.Visible = true;
                    pictureBox2.Top = int.Parse(cob_top);
                    pictureBox2.Left = int.Parse(cob_left); 
                    
                    
                    /*
                    if ((pictureBox2.Left < picact1.Left) && (pictureBox2.Top > picact1.Top)) //炸到敵機
                        if ((pictureBox2.Left < picact1.Left + 136) && (picact.Left > picact1.Left - 136)) //炸到敵機
                   */

                    if ((pictureBox2.Top == picact1.Top)) 
                        {
                            
                              //  timer1.Stop();
                                timer5.Stop();
                                f1.WIN = "win";
                                picact1.Visible = false;
                                pictureBox2.Visible = false;
                               // timer5.Enabled = false;
                                MessageBox.Show("恭喜您，\n您獲勝了！", "遊戲結束", MessageBoxButtons.OK, MessageBoxIcon.Information);
                                
                            //  Application.Exit();
                            //    gamestart();
                            
                        }
                     
                }
                cob = null;
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        { 
            /*
            if (lose != null)
            {
                if (int.Parse(p) == 1)
                {
                    picact.Visible = false;
                }
                else
                {
                    picact1.Visible = false;
                }
                lose = null;
            }
           */
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            /*
            if (win != null)
            {
                if (int.Parse(p) == 1)
                {
                    picact1.Visible = false;
                }
                else
                {
                    picact.Visible = false;
                }
                win = null;
            }
            */
        }

    }
}
