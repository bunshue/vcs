using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 樂透網路遊戲設計_client
{
    public partial class Form2 : System.Windows.Forms.Form
    {
        public int[] Value = new int[5]; //存取亂數
        int[] choose = new int[5];
        string[] PE = new string[5]; //玩家的樂透號碼,共5個
        string[] PC = new string[5]; //電腦的樂透號碼,共5個
        string[] number = new string[5]; //存放中獎號碼
        int count_rand = 0 , i = 0 , count = 0;
        int ssec = 9, ssec2 = 5, mmin = 0;
        //選號倒數的: ssec-秒的個位數,ssec2-秒的十位數,mmin-分
        int sec = 0, sec2 = 0, min = 0, min2 = 0;
        //經過時間的: sec-秒的個位數,sec2-秒的十位數,min-分的個位數,min2-分的十位數
        Form1 f1 = new Form1();
        public Form2()
        {
            InitializeComponent();
            picShow.Image = imageList1.Images[0]; //動畫圖片為第1張
            lbla.Text = (1).ToString(); //選號倒數的分
            timer5.Enabled = true;
            timer6.Enabled = true;
            for (int i = 0; i < 10; ++i) listBox1.Items.Add("");
        }
        public static string rand;
        public string RANDNUM
        {

            set { rand = value; }


            get { return rand; }

        }
        public static string finish;
        public string FINISH
        {

            set { finish = value; }


            get { return finish; }

        }
        static string Number;
        public string NUMBER
        {

            set { Number = value; }


            get { return Number; }

        }
        private void Game_Random() //遊戲選擇.共同指令與亂數選取的方法
        {
            
            int c, d, pe, re = 0;
            try
            {
                if (rdbPlay1.Checked == true) //玩法1(5/20樂透)被選取
                {
                    PE[0] = txt1.Text;
                    PE[1] = txt2.Text;
                    PE[2] = txt3.Text;
                    PE[3] = txt4.Text;
                    PE[4] = txt5.Text;

                    for (c = 0; c <= 4; c++)
                    {
                        pe = int.Parse(PE[c]);

                        if (pe > 20 || pe == 0) //判斷輸入數字是否大於20或等於0
                        {
                            re++;
                        }
                        for (d = 0; d < c; d++)
                        {
                            if (pe == int.Parse(PE[d])) //判斷輸入數字是否有重覆
                            {
                                re++;
                            }
                        }
                    }
                    if (re > 0) //如果有錯誤
                    {
                        MessageBox.Show("輸入有錯喔!"); //顯示錯誤訊息
                    }
                    else //沒錯誤
                    {
                        btnStart.Text = "遊戲進行中..";
                        btnStart.Enabled = false;
                        lblShow.Text = "祝您好運~!";
                        timer1.Enabled = true; //5/20樂透計時器開啟
                        txt1.Enabled = false;
                        txt2.Enabled = false;
                        txt3.Enabled = false;
                        txt4.Enabled = false;
                        txt5.Enabled = false;
                    }
                }
            }
            catch
            {
                MessageBox.Show("數字還沒選");
            }

           
            if (rdbPlay2.Checked == true) //玩法2(一分鐘賓果)被選取
            {
                if (rdb1.Checked == true) //當選1個選取核被選取
                {
                    PE[0] = txta.Text;
                    PE[1] = (-1).ToString(); //給不會影響任何比對程式的值
                    PE[2] = (-2).ToString(); //給不會影響任何比對程式的值
                    PE[3] = (-3).ToString(); //給不會影響任何比對程式的值
                    PE[4] = (-4).ToString(); //給不會影響任何比對程式的值

                }
                else if (rdb2.Checked == true) //當選2個選取核被選取
                {
                    PE[0] = txta.Text;
                    PE[1] = txtb.Text;
                    PE[2] = (-1).ToString(); //給不會影響任何比對程式的值
                    PE[3] = (-2).ToString(); //給不會影響任何比對程式的值
                    PE[4] = (-3).ToString(); //給不會影響任何比對程式的值

                }
                else if (rdb3.Checked == true) //當選3個選取核被選取
                {
                    PE[0] = txta.Text;
                    PE[1] = txtb.Text;
                    PE[2] = txtc.Text;
                    PE[3] = (-1).ToString(); //給不會影響任何比對程式的值
                    PE[4] = (-2).ToString(); //給不會影響任何比對程式的值
                }
                else if (rdb4.Checked == true) //當選4個選取核被選取
                {
                    PE[0] = txta.Text;
                    PE[1] = txtb.Text;
                    PE[2] = txtc.Text;
                    PE[3] = txtd.Text;
                    PE[4] = (-1).ToString(); //給不會影響任何比對程式的值
                }
                else if (rdb5.Checked == true) //當選5個選取核被選取
                {
                    PE[0] = txta.Text;
                    PE[1] = txtb.Text;
                    PE[2] = txtc.Text;
                    PE[3] = txtd.Text;
                    PE[4] = txte.Text;
                }

                for (c = 0; c <= 4; c++)
                {
                    pe = int.Parse(PE[c]);

                    if (pe > 20 || pe == 0) //判斷輸入數字是否大於20或等於0
                    {
                        re++;
                    }

                    for (d = 0; d < c; d++)
                    {
                        if (pe == int.Parse(PE[d]))//判斷輸入數字是否有重覆
                        {
                            re++;
                        }
                    }
                }
                if (re > 0) //有錯誤時
                {
                    MessageBox.Show("輸入有錯喔!"); //顯示錯誤訊息
                    btnStart.Text = "繼續遊戲";
                    timer2.Enabled = false;
                    timer4.Enabled = false;
                }
                else //沒錯誤
                {
                    btnStart.Text = "遊戲進行中..";
                    btnStart.Enabled = false;
                    lblShow.Text = "祝您好運~!";
                    timer2.Enabled = true;
                    timer4.Enabled = true; //動畫開啟
                    txta.Enabled = false;
                    txtb.Enabled = false;
                    txtc.Enabled = false;
                    txtd.Enabled = false;
                    txte.Enabled = false;
                }
            }
           

        }
        private void NumberIn(KeyPressEventArgs e) //判斷是否輸入正確數字的方法
        {
            //以下判斷是否輸入正確數字
            if ((e.KeyChar.ToString().ToLower() == "0") || (e.KeyChar.ToString().ToLower() == "1") || (e.KeyChar.ToString().ToLower() == "2") || (e.KeyChar.ToString().ToLower() == "3") ||
               (e.KeyChar.ToString().ToLower() == "4") || (e.KeyChar.ToString().ToLower() == "5") || (e.KeyChar.ToString().ToLower() == "6") || (e.KeyChar.ToString().ToLower() == "7") ||
                 (e.KeyChar.ToString().ToLower() == "8") || (e.KeyChar.ToString().ToLower() == "9") || (e.KeyChar == Convert.ToChar(Keys.Back)))
            {
                btnStart.Enabled = true; //避免使用者未輸入任何數字
            }
            else //如果不是
                MessageBox.Show("是輸入數字喔!"); //顯示錯誤訊息
        }

        private void Get() //判斷有無中獎的方法
        {
            
            int get = 0;
            for (int a = 0; a <= 4; a++)
            {
                for (int b = 0; b <= 4; b++)
                {
                    if (PE[a] == PC[b])
                    {
                        number[a] = PC[b];
                        get++;
                    }
                }
            }
            if (get > 0) //有中獎時
            {
                lblShow.Text = number[0] + " " + number[1] + " " + number[2] + " " + number[3] + " " + number[4] + " ";
              //  f1.UPDATE = "update";
                f1.NUMBER = get.ToString();
                finish = null;
                for (int i = 0; i < 5; ++i) Value[i] = 0;
            }
            else if (get == 0) //沒中獎時
            {
                lblShow.Text = "沒中獎! 請再接再厲~!";
             //   f1.UPDATE = "update";
                f1.NUMBER = get.ToString();
                finish = null;
                for (int i = 0; i < 5; ++i) Value[i] = 0;
            }
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            i++;
            count++;
            picShow.Image = imageList1.Images[i]; //樂透動畫
            if (i == 6) //有Images[0]~Images[6],7張動畫圖
            {
                i = 0; //到第7張時i歸零,再重第1張開始
            }

            if (count == 15)
            {
                pic1.Image = imageList2.Images[Value[0]]; //顯示第1顆球
                PC[0] = (Value[0] + 1).ToString();
            }
            if (count == 20)
            {
                pic2.Image = imageList2.Images[Value[1]]; //顯示第2顆球
                PC[1] = (Value[1] + 1).ToString();
            }
            if (count == 25)
            {
                pic3.Image = imageList2.Images[Value[2]]; //顯示第3顆球
                PC[2] = (Value[2] + 1).ToString();
            }
            if (count == 30)
            {
                pic4.Image = imageList2.Images[Value[3]]; //顯示第4顆球
                PC[3] = (Value[3] + 1).ToString();
            }
            if (count == 35)
            {
                pic5.Image = imageList2.Images[Value[4]]; //顯示第5顆球
                PC[4] = (Value[4] + 1).ToString();
                timer1.Enabled = false; //計時停止
                btnStart.Enabled = true;
                btnStart.Text = "開始遊戲";
                picShow.Image = imageList1.Images[0];
                txt1.Enabled = true;
                txt2.Enabled = true;
                txt3.Enabled = true;
                txt4.Enabled = true;
                txt5.Enabled = true;
                count = 0;
                Get(); //判斷有無中獎的方法               
            }
        }

        private void timer4_Tick(object sender, EventArgs e)
        {
            btnStart.Text = "遊戲進行中..";
            i++;
            picShow.Image = imageList1.Images[i]; //樂透動畫
            if (i == 6) //有Images[0]~Images[6],7張動畫圖
            {
                i = 0; //到第7張時i歸零,再重第1張開始
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            ssec--;
            lbla.Text = mmin.ToString(); //分
            lblb.Text = ssec2.ToString(); //秒的十位數
            lblc.Text = ssec.ToString(); //秒的個位數

            if (ssec == 0)
            {
                if (ssec == 0 && ssec2 == 0)
                {
                    timer4.Enabled = true; //動畫開啟
                    lblShow.Text = "祝您好運~!";
                    pic1.Image = imageList2.Images[20];
                    pic2.Image = imageList2.Images[20];
                    pic3.Image = imageList2.Images[20];
                    pic4.Image = imageList2.Images[20];
                    pic5.Image = imageList2.Images[20];
                    number[0] = " "; //中獎記錄清空
                    number[1] = " "; //中獎記錄清空
                    number[2] = " "; //中獎記錄清空
                    number[3] = " "; //中獎記錄清空
                    number[4] = " "; //中獎記錄清空
                    timer3.Enabled = false; //選號倒數關閉
                    ssec = 9;
                    ssec2 = 5;
                    mmin = 0;
                    lbla.Text = (1).ToString();
                    Game_Random(); //遊戲選擇.共同指令與亂數選取的方法
                }
                ssec2--;
                ssec = 10;
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
             count++;
            /*執行計時啟動*/
            sec++;
            lbl4.Text = sec.ToString(); //秒的個位數
            if (sec == 10) //滿10秒時
            {
                sec2++; //進位
                lbl3.Text = sec2.ToString(); //秒的十位數
                sec = 0; //秒的個位數歸零
                lbl4.Text = sec.ToString();

                if (sec2 == 6) //滿60秒時
                {
                    min++; //進位
                    lbl2.Text = min.ToString(); //分的個位數
                    sec2 = 0; //秒的十位數歸零
                    lbl3.Text = sec2.ToString();

                    if (min == 10) //滿10分鐘時
                    {
                        min2++; //進位
                        lbl1.Text = min2.ToString(); //分的十位數
                        min = 0; //分的個位數歸零
                        lbl2.Text = min.ToString();

                        if (min2 == 6) //滿1小時時
                        {
                            min2 = 0; //分的十位數歸零
                            lbl1.Text = min2.ToString();
                            timer2.Enabled = false; //timer2計時停止
                            MessageBox.Show("玩1小時囉~,休息一下吧!\n遊戲停止!"); //顯示訊息
                            sec = 0; //歸零
                            sec2 = 0; //歸零
                            min = 0; //歸零
                        }
                    }
                }
            }
        }

        private void btnStart_Click(object sender, EventArgs e)
        {
            if (finish == "finishRand")
            {
                pic1.Image = imageList2.Images[20];
                pic2.Image = imageList2.Images[20];
                pic3.Image = imageList2.Images[20];
                pic4.Image = imageList2.Images[20];
                pic5.Image = imageList2.Images[20];
                number[0] = " "; //中獎記錄清空
                number[1] = " "; //中獎記錄清空
                number[2] = " "; //中獎記錄清空
                number[3] = " "; //中獎記錄清空
                number[4] = " "; //中獎記錄清空

                if (rdbPlay2.Checked == true) //當一分鐘賓果在進行時,使用者不小心按到該按鈕的措施
                {
                    timer3.Enabled = false; //倒數關閉
                    ssec = 9;
                    ssec2 = 5;
                    mmin = 0;
                    lbla.Text = (1).ToString();
                    lblb.Text = (0).ToString();
                    lblc.Text = (0).ToString();
                }


                Game_Random(); //遊戲選擇.共同指令與亂數選取的方法
              
            }
            else
            {
                MessageBox.Show("還沒開獎");
            }
        }

        private void timer5_Tick(object sender, EventArgs e)
        {
 
            if ((rand != null) && (count_rand < 5))
            {
               
                Value[count_rand] = int.Parse(rand);

                ++count_rand;
                rand = null;
                
            }
            else if (finish == "finishRand")
            {
                
                count_rand = 0;
                rand = null;
            }
        }

        private void timer6_Tick(object sender, EventArgs e)
        {
            int found = 0;
            string tempP;
            if (Number != null)
            {
                found = Number.IndexOf("|");
                if (found >= 0)
                {
                    tempP = Number.Substring(0, found);
                    Number = Number.Substring(found + 1);

                    listBox1.Items[int.Parse(tempP)] = Number;

                    Number = null;
                }
            }
        }
    }
}
