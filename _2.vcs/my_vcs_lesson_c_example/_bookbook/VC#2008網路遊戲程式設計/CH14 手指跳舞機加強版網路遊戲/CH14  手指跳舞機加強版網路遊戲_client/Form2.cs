using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 手指跳舞機網路遊戲_client
{
    public partial class Form2 : System.Windows.Forms.Form
    {
        public Form2()
        {
            InitializeComponent();

        }
        int v1, v2;
        int r_out;
        int score = 0, miss = 0;
        int i, j, time = 0;
        static string Number;
        public string NUMBER
        {

            set { Number = value; }


            get { return Number; }

        }
        private void Form2_Load(object sender, EventArgs e)
        {
            timer3.Enabled = true;
            for (int i = 0; i < 10; ++i) listBox1.Items.Add("");
        }
        private void button5_Click(object sender, EventArgs e)
        {
            i = 0;
            j = 0;
            score = 0;
            miss = 0;
            button5.Enabled = false;
            timer1.Enabled = true;
            label1.Visible = true;
            label2.Visible = true;
            label3.Visible = true;
        }
        private void checkpoint()
        {
            Form1 f1 = new Form1();
            if (v1 == r_out)
            {
                score = score + 1;
                label3.Text = "成績積分" + score.ToString();
                label1.Text = "目前遊戲總得分:" + score.ToString();
                f1.UPDATE = score.ToString();
            }
            else
            {
                if (v2 == r_out)
                {
                    score = score + 1;
                    label3.Text = "成績積分" + score.ToString();
                    label1.Text = "目前遊戲總得分:" + score.ToString();
                    f1.UPDATE = score.ToString();
                }
                else
                {
                    miss += 1;
                    label3.Text = "沒分";
                    label2.Text = "目前失誤總次數:" + miss.ToString();
                    if (miss == 10)
                    {
                        i = 0;
                        j = 0;
                        score = 0;
                        miss = 0;
                        label1.Text = "目前遊戲總得分:";
                        label2.Text = "目前失誤總次數:";
                        label2.Visible = false;
                        button5.Enabled = true;
                        timer1.Enabled = false;
                        timer2.Enabled = false;
                        label1.Visible = false;
                        label2.Visible = false;
                        label3.Visible = false;
                      //  pictureBox1.Image = imageList1.Images[5];
                        f1.LOSE = "lose";
                        MessageBox.Show("您輸了，請重新來過吧！", "Game Over", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);//利用MessageBox來show出東西
                    }
                }
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            Random rndObj = new Random(); //亂數宣告指令一
            int rndNum = rndObj.Next(); //亂數宣告指令二
            j++; 
            if (j <= 7)
            {
                v2 = rndObj.Next(8);
                pictureBox1.Image = imageList1.Images[v2];
            }
            else
            {
                if (j > 7)
                {
                    timer1.Enabled = true;
                    timer2.Enabled = false;
                    j = 0;
                    i = 0;
                }
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Random rndObj = new Random(); //亂數宣告指令一
            int rndNum = rndObj.Next(); //亂數宣告指令二
            i++; 
            if (i <= 7)
            {
                v1 = rndObj.Next(8);
                pictureBox1.Image = imageList1.Images[v1];
            }
            else
            {
                if (i > 7)
                {
                    timer1.Enabled = false;
                    timer2.Enabled = true;
                    j = 0;
                    i = 0;
                }
            }
        }

        private void Form2_KeyDown(object sender, System.Windows.Forms.KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.A:
                    r_out = 7;
                    checkpoint();
                    break;
                case Keys.W:
                    r_out = 4;
                    checkpoint();
                    break;
                case Keys.D:
                    r_out = 6;
                    checkpoint();
                    break;
                case Keys.X:
                    r_out = 5;
                    checkpoint();
                    break;
                case Keys.Up:
                    r_out = 2;
                    checkpoint();
                    break;

                case Keys.Down:
                    r_out = 3;
                    checkpoint();
                    break;

                case Keys.Left:
                    r_out = 0;
                    checkpoint();
                    break;

                case Keys.Right:
                    r_out = 1;
                    checkpoint();
                    break;
                
                case Keys.Escape:
                    timer1.Enabled = false;
                    timer2.Enabled = false;
                    DialogResult result = MessageBox.Show("您確定要中斷遊戲嗎?", "警告", MessageBoxButtons.OKCancel, MessageBoxIcon.Exclamation);//利用MessageBox來show出東西，並選擇OK Cancel
                    if (result == DialogResult.OK)
                    {
                        i = 0;
                        j = 0;
                        score = 0;
                        miss = 0;
                        // pictureBox1.Image = imageList1.Images[5];
                        label1.Text = "目前遊戲總得分:";
                        label2.Text = "目前失誤總次數:";
                        label2.Visible = false;
                        button5.Enabled = true;
                        timer1.Enabled = false;
                        timer2.Enabled = false;
                        label1.Visible = false;
                        label2.Visible = false;
                        label3.Visible = false;
                    }
                    else
                    {
                        timer1.Enabled = true;
                    }
                    break;
                case Keys.Space:
                    if (time == 0)
                    {
                        timer1.Enabled = false;
                        timer2.Enabled = false;
                        pictureBox1.Image = imageList1.Images[4];
                        MessageBox.Show("目前遊戲暫停中，如果您要恢復遊戲請載按一次空白鍵。", "遊戲暫停", MessageBoxButtons.OK, MessageBoxIcon.Information);//利用MessageBox來show出東西
                        time++;
                    }
                    else
                    {
                        timer1.Enabled = true;
                        time = 0;
                    }
                    break;

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
