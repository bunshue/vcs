using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 保齡球網路遊戲設計_client
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            timer3.Enabled = true;
            timer4.Enabled = true;
            timer5.Enabled = true;
            pic_ball.Left = 0;  //初始狀態pic_ball的X座標0
            pic_ball.Top = 590;//初始狀態pic_ball的Y座標590
            for (int i = 0; i < 10; ++i) listBox1.Items.Add("");
        }
        int b, a1;        //宣告b,a1為整數(b為球的行進距離；a1為trackBar2的位置)
        int a = 1;           //宣告a為整數(a為球的行進的最小單位)
        int score = 0 , num = 0;
        Form1 f1 = new Form1();

        static string score1;
        public string SCORE
        {

            set { score1 = value; }


            get { return score1; }

        }
        static string Pri;
        public string PRI
        {

            set { Pri = value; }


            get { return Pri; }

        }
        static string temp;
        public string TEMP
        {

            set { temp = value; }


            get { return temp; }

        }
        private void button5_Click(object sender, EventArgs e)
        {
            
            b = 0;      //將b為設0
            timer1.Enabled = true;//timer1開啟
            timer2.Enabled = true;//timer2開啟
            trackBar1.Enabled = false; ;//trackBar1關閉
            trackBar2.Enabled = false;//trackBar2關閉
         //   button5.Enabled = false;//button5關閉
         //   button6.Enabled = false;//button6關閉
            
        }

        private void button6_Click(object sender, EventArgs e)
        {
            a = 1;                  //將a設為1
            
            label6.Text = "分數：";//label6顯示"分數："
            trackBar1.Value = 0;//trackBar1位置設為0
            trackBar2.Value = 0;//trackBar2位置設為0
            trackBar1.Enabled = true;//trackBar1開啟
            trackBar2.Enabled = true;//trackBar2開啟
            pic_ball.Visible = true;//pic_ball顯示
            pic_ball.Left = 0;  //初始狀態pic_ball的X座標0
            pic_ball.Top = 590;//初始狀態pic_ball的Y座標590
            pictureBox2.Visible = true;//將瓶子全部顯示
            pictureBox4.Visible = true;
            pictureBox5.Visible = true;
            pictureBox6.Visible = true;
            pictureBox7.Visible = true;
            pictureBox8.Visible = true;
            pictureBox9.Visible = true;
            pictureBox10.Visible = true;
            pictureBox11.Visible = true;
            pictureBox12.Visible = true;
            label2.Text = "Y 座標：" + pic_ball.Top.ToString();//顯示球的X座標位置
            label1.Text = "X 座標：" + pic_ball.Left.ToString();//顯示球的X座標位置
            num = 0;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            if (trackBar1.Value == 0)  //判斷trackBar1指標的位置
                a = 1;
            else
                if (trackBar1.Value == 1)
                    a = 2;
                else
                    if (trackBar1.Value == 2)
                        a = 3;
                    else
                        if (trackBar1.Value == 3)
                            a = 4;
                        else
                            if (trackBar1.Value == 4)
                                a = 5;
                            else
                                if (trackBar1.Value == 5)
                                    a = 6;
                                else
                                    if (trackBar1.Value == 6)
                                        a = 7;
                                    else
                                        if (trackBar1.Value == 7)
                                            a = 8;
                                        else
                                            if (trackBar1.Value == 8)
                                                a = 9;
                                            else
                                                if (trackBar1.Value == 9)
                                                    a = 10;
                                                else
                                                    if (trackBar1.Value == 10)
                                                        a = 11;

        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            a1 = trackBar2.Value;//將trackBar2的位置傳給a1
            switch (a1)//用SWITCH判斷a1的值
            {
                case 0:
                    pic_ball.Left = 0;//求的X座標為0
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();//顯示球的X座標位置
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();//顯示球的X座標位置
                    break;
                case 1:
                    pic_ball.Left = 19;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 2:
                    pic_ball.Left = 37;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 3:
                    pic_ball.Left = 55;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 4:
                    pic_ball.Left = 73;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 5:
                    pic_ball.Left = 91;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 6:
                    pic_ball.Left = 109;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 7:
                    pic_ball.Left = 127;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 8:
                    pic_ball.Left = 145;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 9:
                    pic_ball.Left = 163;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 10:
                    pic_ball.Left = 181;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 11:
                    pic_ball.Left = 199;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 12:
                    pic_ball.Left = 217;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;
                case 13:
                    pic_ball.Left = 235;
                    label2.Text = "Y 座標：" + pic_ball.Top.ToString();
                    label1.Text = "X 座標：" + pic_ball.Left.ToString();
                    break;

            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            b = b + a;
            pic_ball.Top -= b;            //將球的位置減去行近距離
            if (pic_ball.Top < -10)       //判斷求的位置小於-10
            {
                pic_ball.Visible = false;//pic_ball隱藏
                timer1.Enabled = false;//timer1關閉
                timer2.Enabled = false;//timer2關閉
                trackBar1.Enabled = false;//trackBar1關閉
                num = 0;
                f1.COUNT = Pri;
            }
            else
            {
                if ((pic_ball.Top <= 155) && (pic_ball.Left == 109))
                {
                   
                    pictureBox2.Visible = false;//將被擊倒瓶子隱藏起來
                    pictureBox4.Visible = false;
                    pictureBox5.Visible = false;
                    pictureBox6.Visible = false;
                    pictureBox7.Visible = false;
                    pictureBox8.Visible = false;
                    pictureBox9.Visible = false;
                    pictureBox10.Visible = false;
                    pictureBox11.Visible = false;
                    pictureBox12.Visible = false;
                    
                        score += 10;
                        f1.SCORE = score.ToString();
                        label11.Text = score.ToString();
                        label6.Text = "分數：恭喜!全倒";//顯示分數
                    
                   
                }
                else
                {
                    if ((pic_ball.Top <= 140) && (pic_ball.Left == 127))
                    {
                        
                        pictureBox4.Visible = false;
                        pictureBox5.Visible = false;
                        pictureBox6.Visible = false;
                        pictureBox7.Visible = false;
                        pictureBox8.Visible = false;
                        pictureBox9.Visible = false;
                        pictureBox10.Visible = false;
                        pictureBox11.Visible = false;
                        pictureBox12.Visible = false;
                        
                            score += 9;
                            f1.SCORE = score.ToString();
                            label11.Text = score.ToString();
                            label6.Text = "分數：9瓶";//顯示分數
                        
                        
                    }
                }
                if ((pic_ball.Top <= 140) && (pic_ball.Left == 91))
                {
                    
                    pictureBox2.Visible = false;
                    pictureBox4.Visible = false;
                    pictureBox5.Visible = false;
                    pictureBox7.Visible = false;
                    pictureBox8.Visible = false;
                    pictureBox9.Visible = false;
                    pictureBox10.Visible = false;
                    pictureBox11.Visible = false;
                    pictureBox12.Visible = false;
                    
                        score += 9;
                        f1.SCORE = score.ToString();
                        label11.Text = score.ToString();
                        label6.Text = "分數：9瓶";//顯示分數
                    
                   
                }
                else
                {
                    if ((pic_ball.Top <= 125) && (pic_ball.Left == 145))
                    {
                        
                        pictureBox4.Visible = false;
                        pictureBox5.Visible = false;
                        pictureBox6.Visible = false;
                        pictureBox8.Visible = false;
                        pictureBox9.Visible = false;
                        pictureBox11.Visible = false;
                        pictureBox12.Visible = false;
                        
                            score += 7;
                            f1.SCORE = score.ToString();
                            label11.Text = score.ToString();
                            label6.Text = "分數：7瓶";//顯示分數
                        
                        
                    }
                    else
                        if ((pic_ball.Top <= 125) && (pic_ball.Left == 73))
                        {
                            
                            pictureBox2.Visible = false;
                            pictureBox4.Visible = false;
                            pictureBox5.Visible = false;
                            pictureBox7.Visible = false;
                            pictureBox8.Visible = false;
                            pictureBox10.Visible = false;
                            pictureBox12.Visible = false;
                            
                                score += 7;
                                f1.SCORE = score.ToString();
                                label11.Text = score.ToString();
                                label6.Text = "分數：7瓶";//顯示分數
                            
                           
                        }
                        else
                            if ((pic_ball.Top <= 110) && (pic_ball.Left == 163))
                            {
                                
                                pictureBox5.Visible = false;
                                pictureBox6.Visible = false;
                                pictureBox8.Visible = false;
                                pictureBox9.Visible = false;
                                pictureBox11.Visible = false;
                                pictureBox12.Visible = false;
                                
                                    score += 6;
                                    f1.SCORE = score.ToString();
                                    label11.Text = score.ToString();
                                    label6.Text = "分數：6瓶";//顯示分數
                                
                                
                            }

                            else
                                if ((pic_ball.Top <= 110) && (pic_ball.Left == 55))
                                {
                                    
                                    pictureBox2.Visible = false;
                                    pictureBox4.Visible = false;
                                    pictureBox7.Visible = false;
                                    pictureBox8.Visible = false;
                                    pictureBox10.Visible = false;
                                    pictureBox12.Visible = false;
                                   
                                        score += 6;
                                        f1.SCORE = score.ToString();
                                        label11.Text = score.ToString();
                                        label6.Text = "分數：6瓶";//顯示分數
                                    
                                    
                                }
                                else
                                    if ((pic_ball.Top <= 95) && (pic_ball.Left == 181))
                                    {
                                        
                                        pictureBox5.Visible = false;
                                        pictureBox6.Visible = false;
                                        pictureBox9.Visible = false;
                                        pictureBox11.Visible = false;
                                        
                                            score += 4;
                                            f1.SCORE = score.ToString();
                                            label11.Text = score.ToString();
                                            label6.Text = "分數：4瓶";//顯示分數
                                        
                                       
                                    }
                                    else
                                        if ((pic_ball.Top <= 95) && (pic_ball.Left == 37))
                                        {
                                            
                                            pictureBox2.Visible = false;
                                            pictureBox4.Visible = false;
                                            pictureBox7.Visible = false;
                                            pictureBox10.Visible = false;
                                            
                                                score += 4;
                                                f1.SCORE = score.ToString();
                                                label11.Text = score.ToString();
                                                label6.Text = "分數：4瓶";//顯示分數
                                            
                                            
                                        }
                                        else
                                            if ((pic_ball.Top <= 80) && (pic_ball.Left == 199))
                                            {
                                                
                                                pictureBox9.Visible = false;
                                                pictureBox6.Visible = false;
                                                
                                                    score += 2;
                                                    f1.SCORE = score.ToString();
                                                    label11.Text = score.ToString();
                                                    label6.Text = "分數：2瓶";//顯示分數
                                                
                                               
                                            }

                                            else
                                                if ((pic_ball.Top <= 80) && (pic_ball.Left == 19))
                                                {
                                                    
                                                    pictureBox2.Visible = false;
                                                    pictureBox4.Visible = false;
                                                    
                                                        score += 2;
                                                        f1.SCORE = score.ToString();
                                                        label11.Text = score.ToString();
                                                        label6.Text = "分數：2瓶";//顯示分數
                                                    
                                                    
                                                }
                                                else
                                                    if ((pic_ball.Top <= 65) && (pic_ball.Left == 217))
                                                    {
                                                        
                                                        pictureBox6.Visible = false;
                                                        
                                                            score += 1;
                                                            f1.SCORE = score.ToString();
                                                            label11.Text = score.ToString();
                                                            label6.Text = "分數：1瓶";//顯示分數
                                                        
                                                        
                                                    }
                                                    else
                                                        if ((pic_ball.Top <= 190) && (pic_ball.Left == 0))
                                                        {
                                                            label6.Text = "分數：0瓶";
                                                        }
                                                        else
                                                            if ((pic_ball.Top <= 190) && (pic_ball.Left == 235))
                                                            {
                                                                label6.Text = "分數：0瓶";
                                                            }
                }
            }



            label2.Text = "Y 座標：" + pic_ball.Top.ToString();//顯示球的X座標位置
            label1.Text = "X 座標：" + pic_ball.Left.ToString();//顯示球的X座標位置
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            pic_ball.Image.RotateFlip(RotateFlipType.Rotate90FlipNone);//繞著中心旋轉90度   
            pic_ball.Refresh();//刷新顯示 
        }

        private void timer3_Tick(object sender, EventArgs e)//檢查是否有玩家得分
        {
            int found;
            string N, tempP;
            if (score1 != null)
            {
                found = score1.IndexOf("|");
                if (found >= 0)
                {
                    tempP = score1.Substring(0, found);

                    N = score1.Substring(found + 1);

                    listBox1.Items[int.Parse(tempP) - 1] = N;                  
                    
                }
                score1 = null;
                
            }
            
        }

        private void timer4_Tick(object sender, EventArgs e)//第一個玩家先開始
        {
            
                if (Pri == "1")
                {
                    button5.Enabled = true;
                    button6.Enabled = true;
                    timer4.Enabled = false;
                }
                
            
        }

        private void timer5_Tick(object sender, EventArgs e)//檢查玩家是否發完球，以便輪流
        {
            if (temp != null)
            {
                
             
                if (temp == "1")
                {
                    if (Pri == "2")
                    {
                        button5.Enabled = true;
                        button6.Enabled = true;
                        
                    }

                }
                else if (temp == "2")
                {
                    if (Pri == "3")
                    {
                        button5.Enabled = true;
                        button6.Enabled = true;
                       
                    }

                }
                else if (temp == "3")
                {
                    if (Pri == "1")
                    {
                        button5.Enabled = true;
                        button6.Enabled = true;
                    }

                }
                temp = null; 
            }
        }
    }
}
