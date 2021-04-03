using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 打地鼠網路遊戲_client
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            timer3.Enabled = true;
            for (int i = 0; i < 10; ++i) listBox1.Items.Add("");
        }
        int play_count, score = 0, x1; //play_count-遊戲時間,score-分數計算,x1-地鼠用
        static string Number;
        public string NUMBER
        {

            set { Number = value; }


            get { return Number; }

        }
        private void button1_Click(object sender, EventArgs e)
        {
            button1.Enabled = false;
            button1.Text = "打地鼠中";
            lblPlaytime.ForeColor = Color.Black;
            timer1.Enabled = true;
            timer2.Enabled = true;
            lblPlaytime.Text = "30秒";
            play_count = 30;
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            play_count--;
            lblPlaytime.Text = play_count.ToString() + "秒";

            if (play_count <= 10)
            {
                lblPlaytime.ForeColor = Color.Red;
            }
            if (play_count == 0)
            {
                timer1.Enabled = false;
                x1 = 0;
                pictureBox1.Image = imageList1.Images[0];
                pictureBox2.Image = imageList1.Images[0];
                pictureBox3.Image = imageList1.Images[0];
                pictureBox4.Image = imageList1.Images[0];
                pictureBox5.Image = imageList1.Images[0];
                pictureBox6.Image = imageList1.Images[0];
                pictureBox7.Image = imageList1.Images[0];
                pictureBox8.Image = imageList1.Images[0];
                pictureBox9.Image = imageList1.Images[0];
                timer2.Enabled = false;
                button1.Enabled = true;
                button1.Text = "開始遊戲";
                
                    switch (lblLevel.Text)
                    {
                        case "L.v 1":
                            if (score >= 25)
                            {
                                MessageBox.Show("分數:" + score + "\n晉級L.v 2 !!\n請按開始遊戲挑戰新等級!", "等級提升", MessageBoxButtons.OK);
                                lblLevel.Text = "L.v 2";
                                lblLvSe.Text = "50分";
                                lblSpeed.Text = "0.7秒";
                                timer1.Interval = 700; //設定時間
                                f1.UPDATE = score.ToString();
                            }
                            else if (score < 25)
                            {
                                MessageBox.Show("闖關失敗!" + "得" +  score + "分"  , "Game Over", MessageBoxButtons.OK);
                                lblLevel.Text = "L.v 1";
                                lblLvSe.Text = "25分";
                              //  score = 0;
                                f1.UPDATE = score.ToString();
                            }
                            break;
                        case "L.v 2":
                            if (score >= 50)
                            {
                                MessageBox.Show("分數:" + score + "\n晉級L.v 3 !!\n請按開始遊戲挑戰新等級!", "等級提升", MessageBoxButtons.OK);
                                lblLevel.Text = "L.v 3";
                                lblLvSe.Text = "75分";
                                timer1.Interval = 600; //設定時間
                                f1.UPDATE = score.ToString();
                                lblSpeed.Text = "0.6秒";
                            }
                            else if (score < 50)
                            {
                                MessageBox.Show("闖關失敗!" + score, "Game Over", MessageBoxButtons.OK);
                                lblLevel.Text = "L.v 1";
                                lblLvSe.Text = "25分";
                                f1.UPDATE = score.ToString();
                                score = 0;
                            }
                            break;
                        case "L.v 3":
                            if (score >= 75)
                            {
                                MessageBox.Show("恭喜您闖關成功~!!\n分數:" + score, "贏了", MessageBoxButtons.OK);
                                f1.UPDATE = score.ToString();
                            }
                            else if (score < 75)
                            {
                                MessageBox.Show("闖關失敗!" + score, "Game Over", MessageBoxButtons.OK);
                                lblLevel.Text = "L.v 1";
                                lblLvSe.Text = "25分";
                                f1.UPDATE = score.ToString();
                                score = 0;
                            }
                            break;
                    }
                            
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Random rndObj1 = new Random();
            int rndNum1 = rndObj1.Next();
            x1 = 1 + rndObj1.Next(9);  //取出亂碼,範圍1~9
            switch (x1)
            {
                case 1:
                    pictureBox1.Image = imageList1.Images[8]; //地鼠
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 2:
                    pictureBox1.Image = imageList1.Images[7];
                    pictureBox2.Image = imageList1.Images[8]; //地鼠
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 3:
                    pictureBox1.Image = imageList1.Images[6];
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[8]; //地鼠
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 4:
                    pictureBox1.Image = imageList1.Images[5];
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[8]; //地鼠
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 5:
                    pictureBox1.Image = imageList1.Images[4];
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[8]; //地鼠
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 6:
                    pictureBox1.Image = imageList1.Images[3];
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[8]; //地鼠
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 7:
                    pictureBox1.Image = imageList1.Images[2];
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[8]; //地鼠
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 8:
                    pictureBox1.Image = imageList1.Images[1];
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[8]; //地鼠
                    pictureBox9.Image = imageList1.Images[0];
                    break;
                case 9:
                    pictureBox1.Image = imageList1.Images[0];
                    pictureBox2.Image = imageList1.Images[7];
                    pictureBox3.Image = imageList1.Images[6];
                    pictureBox4.Image = imageList1.Images[5];
                    pictureBox5.Image = imageList1.Images[4];
                    pictureBox6.Image = imageList1.Images[3];
                    pictureBox7.Image = imageList1.Images[2];
                    pictureBox8.Image = imageList1.Images[1];
                    pictureBox9.Image = imageList1.Images[8]; //地鼠
                    break;
            }                        
        }

        private void Form2_MouseLeave(object sender, EventArgs e)
        {
            pictureBox1.Cursor = new Cursor("1.ico");
            pictureBox2.Cursor = new Cursor("1.ico");
            pictureBox3.Cursor = new Cursor("1.ico");
            pictureBox4.Cursor = new Cursor("1.ico");
            pictureBox5.Cursor = new Cursor("1.ico");
            pictureBox6.Cursor = new Cursor("1.ico");
            pictureBox7.Cursor = new Cursor("1.ico");
            pictureBox8.Cursor = new Cursor("1.ico");
            pictureBox9.Cursor = new Cursor("1.ico");
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox1.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox2.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox3.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox4.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox5.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox6_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox6.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox7_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox7.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox8_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox8.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox9_MouseDown(object sender, MouseEventArgs e)
        {
            if (button1.Text == "打地鼠中")
            {
                pictureBox9.Cursor = new Cursor("2.ico");
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            if (x1 == 1)
            {
                pictureBox1.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            if (x1 == 2)
            {
                pictureBox2.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            if (x1 == 3)
            {
                pictureBox3.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox4_Click(object sender, EventArgs e)
        {
            if (x1 == 4)
            {
                pictureBox4.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {
            if (x1 == 5)
            {
                pictureBox5.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {
            if (x1 == 6)
            {
                pictureBox6.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox7_Click(object sender, EventArgs e)
        {
            if (x1 == 7)
            {
                pictureBox7.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox8_Click(object sender, EventArgs e)
        {
            if (x1 == 8)
            {
                pictureBox8.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void pictureBox9_Click(object sender, EventArgs e)
        {
            if (x1 == 9)
            {
                pictureBox9.Image = imageList1.Images[9]; //顯示打到地鼠的畫面
                score = score + 1; //分數加1
                lblScore.Text = score.ToString(); //顯示分數
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
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
