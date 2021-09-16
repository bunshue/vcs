using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic;
using Microsoft.VisualBasic.Devices;

namespace MDIMutilFormDemo
{
    public partial class frmMemory : Form
    {
        public frmMemory()
        {
            InitializeComponent();
        }

        //宣告n[0]~n[8]整數陣列，用來表示8個圖片方塊所表示的值
        //n[0]省略不用
        int[] n = new int[] { 0, 1, 2, 4, 3, 3, 1, 4, 2 };
        //宣告p[0]~p[8]圖片方塊控制項陣列，
        //p[0]省略不用，p[1]~p[8]用來代表pic1~pic8
        PictureBox[] p = new PictureBox[9];
        //宣告hitPic表示第一次翻牌的圖片方塊
        //hitPic2表示第二次翻牌的圖片方塊
        PictureBox hitPic1, hitPic2;
        //t1字串存放第一次翻牌圖片所取得的值
        //t2字串存放第二次翻牌圖片所取得的值
        string t1, t2;
        bool isFirst = true;  //isFirst表示第一次按下圖片的旗標
        int timer1Tot; //表示timer1計時器執行的次數
        int timer2Tot; //表示timer2計時器執行的次數
        int level;    //表示等級，2為高級,5為中級,10為初級
        int tot;         //答對的組數，若tot為4表示過關
        //建立Computer物件myComputer，用來播放指定的聲音檔
        Computer myComputer = new Computer();

        //Form1表單載入時，即觸發Form1_Load事件處理函式
        private void frmMemory_Load(object sender, EventArgs e)
        {
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            lblShow.Text = "請按 [開始] 鈕進行遊戲";
            lblTime.Text = "";
            //指定timer1每一秒執行timer1_Tick事件處理函式一次
            timer1.Interval = 1000;
            //指定timer2每一秒執行timer1_Tick事件處理函式一次
            timer2.Interval = 1000;
            //分別將pic1~pic8指定給p[1]~p[8]
            //表示p[1]~p[8]可以操作pic1~pic8控制項
            p[1] = pic1;
            p[2] = pic2;
            p[3] = pic3;
            p[4] = pic4;
            p[5] = pic5;
            p[6] = pic6;
            p[7] = pic7;
            p[8] = pic8;
            for (int i = 1; i <= n.GetUpperBound(0); i++)
            {
                p[i].Image = new Bitmap("memoryImg/q.jpg");//使pic1~pic8顯示q.jpg
                p[i].Tag = n[i];    //pic1~pic8的Tag屬性皆設為n[1]~n[8]
                //使圖片隨pic1~pic8的大小做縮放
                p[i].SizeMode = PictureBoxSizeMode.StretchImage;
                //使pic1~pic8的框線樣式以3D框線顯示
                p[i].BorderStyle = BorderStyle.Fixed3D;
                p[i].Enabled = false; //pic1~pic8失效
                //使pic1~pic8的Click事件被觸發時皆會執行PicClick事件處理函式
                p[i].Click += new EventHandler(PicClick);
            }
        }

        //定義PicClick事件處理函式，以提供給pic1~pic8的Click事件使用
        private void PicClick(object sender, EventArgs e)
        {
            //第一次翻牌
            if (isFirst)
            {
                //將第一次翻牌的圖片方塊指定給hitPic1
                hitPic1 = (PictureBox)sender;
                t1 = Convert.ToString(hitPic1.Tag); //將目前翻牌圖片的值指定給t1
                //顯示目前翻牌的圖示
                hitPic1.Image = new Bitmap("memoryImg/" + Convert.ToString(hitPic1.Tag) + ".jpg");
                isFirst = false;  //將isFirst設為false表示目前己結束第二次翻牌
            }
            else//第二次翻牌
            {
                //將第二次翻牌的圖片方塊指定給hitPic
                hitPic2 = (PictureBox)sender;
                t2 = Convert.ToString(hitPic2.Tag); //將目前翻牌圖片的值指定給t2
                //顯示目前翻牌的圖示
                hitPic2.Image = new Bitmap("memoryImg/" + Convert.ToString(hitPic2.Tag) + ".jpg");
                isFirst = true;  //將isFirst設為true表示目前已結束第二次翻牌
                //若t1等於t2，表示所翻牌兩個圖片的Tag屬性相同，即兩者的圖示相同
                if (t1 == t2)
                {
                    //使目前翻牌兩個圖片失效
                    hitPic1.Enabled = false;
                    hitPic2.Enabled = false;
                    tot += 1;   //答對組數加1
                    myComputer.Audio.Play("memoryImg/CHIMES.WAV", AudioPlayMode.Background);
                }
                //若t1不等於t2，表示所翻牌兩個圖片的Tag屬性不同，即兩者的圖示不相同
                if (t1 != t2)
                {
                    MessageBox.Show("答錯了^_|||");
                    //將第一次和第二次翻牌的圖示以q.jpg顯示
                    hitPic1.Image = new Bitmap("memoryImg/q.jpg");
                    hitPic2.Image = new Bitmap("memoryImg/q.jpg");
                }
                //若答對組數為4，即表示過關
                if (tot == 4)
                {
                    //btn1. btn2. btn3鈕啟用
                    btn1.Enabled = true;
                    btn2.Enabled = true;
                    btn3.Enabled = true;
                    timer1.Enabled = false;   //timer1計時器停止
                    timer2.Enabled = false;  //timer2計時器停止
                    if (level == 2)
                    {
                        MessageBox.Show("過關了...果然是記憶高手");
                    }
                    else if (level == 5)
                    {
                        MessageBox.Show("過關了...你的記憶力還不錯");
                    }
                    else if (level == 10)
                    {
                        MessageBox.Show("過關了...你的記憶力還馬馬乎乎");
                    }
                    //播放股掌聲
                    myComputer.Audio.Play("memoryImg/APPLAUSE.WAV", AudioPlayMode.Background);
                }
            }
        }

        //進行遊戲的GameStart()事件處理函式
        private void GameStart()
        {
            myComputer.Audio.Stop();  //停止播放聲音
            level = timer1Tot;
            btn1.Enabled = false;       //btn1鈕失效
            btn2.Enabled = false;        //btn2鈕失效
            btn3.Enabled = false;        //btn3鈕失效
            timer1.Enabled = true;          //啟動timer1計時器
            timer2Tot = 0;                       //timer2Tot的計時遊戲時間
            t1 = "";                 //將t1第一次翻牌圖片所取得的值設為空白
            t2 = "";                //將t2第二次翻牌圖片所取得的值設為空白
            tot = 0;                //將答對的組數設為0，若tot為4表示過關
            hitPic1 = null; //將hitPic1第一次翻牌的圖片方塊設為null
            hitPic2 = null; //'將hitPic2第一次翻牌的圖片方塊設為null
            lblShow.Text = "你可以檢視的時間還有 " + Convert.ToString(timer1Tot) + "秒";
            lblTime.Text = "";
            //使pic1~pic8顯示1~4.jpg四個圖示
            for (int i = 1; i <= n.GetUpperBound(0); i++)
            {
                p[i].Image = new Bitmap("memoryImg/"+ Convert.ToString(n[i]) + ".jpg");
            }
        }

        private void btn1_Click(object sender, EventArgs e)
        {
            timer1Tot = 2;   //設定timer1Tot的倒數時間為2秒
            GameStart();
        }

        private void btn2_Click(object sender, EventArgs e)
        {
            timer1Tot = 5;                    //設定timer1Tot的倒數時間為5秒
            GameStart();
        }

        private void btn3_Click(object sender, EventArgs e)
        {
            timer1Tot = 10;           //設定timer1Tot的倒數時間為10秒
            GameStart();
        }

        //timer1計時器啟動時會觸發timer1_Tick事件
        private void timer1_Tick(object sender, EventArgs e)
        {
            timer1Tot -= 1;   //timer1Tot減1即倒數秒數
            lblShow.Text = "你可以檢視的時間還有 " + Convert.ToString(timer1Tot) + "秒";
            //若timer1Tot倒數秒數為0則執行下面敘述
            if (timer1Tot == 0)
            {
                timer1.Enabled = false; //timer1失效
                lblShow.Text = "";
                timer2.Enabled = true;  //timer2啟動
                for (int i = 1; i <= n.GetUpperBound(0); i++)
                {
                    p[i].Image = new Bitmap("memoryImg/q.jpg");  //pic1~pic8顯示q.jpg
                    //pic1~pic8圖片啟用
                    p[i].Enabled = true;
                }
            }
        }

        //timer2計時器啟動時會觸發timer2_Tick事件
        private void timer2_Tick(object sender, EventArgs e)
        {
            timer2Tot += 1;   //timer2Tot加1即遊戲時間加1
            lblTime.Text = "遊戲時間：" + Convert.ToString(timer2Tot) + " 秒";
            //timer2Tot遊戲時間到30時，即執行下面敘述馬上停止遊戲
            if (timer2Tot == 30)
            {
                timer2.Enabled = false; //timer2失效 
                //btn1, btn2, btm3啟用
                btn1.Enabled = true;
                btn2.Enabled = true;
                btn3.Enabled = true;
                MessageBox.Show("時間到，闖關失敗");
                lblShow.Text = "請按 [開始] 鈕進行遊戲";
                lblTime.Text = "";
                for (int i = 1; i <= n.GetUpperBound(0); i++)
                {
                    p[i].Image = new Bitmap("memoryImg/q.jpg"); //pic1~pic8顯示q.jpg
                    p[i].Enabled = false;  //pic1~pic8圖片失效
                }
            }
        }
    }
}

