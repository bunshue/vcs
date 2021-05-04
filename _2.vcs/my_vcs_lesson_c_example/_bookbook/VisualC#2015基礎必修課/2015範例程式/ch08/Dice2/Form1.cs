using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Dice2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 宣告arrPic為圖片控制項陣列，陣列元素arrPic[0]~arrPic[2]
        PictureBox[] arrPic = new PictureBox[3];
        // 宣告getPoint陣列用來存放亂數值，陣列元素getpoint[0]~getpoint[2]
        int[] getpoint = new int[3];
        int total = 0;        // total整數變數用來存放三個骰子的總點數
        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Interval = 50;  // 每0.05秒執行timer1_Tick事件處理函式一次
            arrPic[0] = pic1;      // 控制項陣列的第一個元素即為pic1圖片控制項
            arrPic[1] = pic2;
            arrPic[2] = pic3;
        }
        // 按 [開始] 鈕執行
        private void btnStart_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }
        //  當timer1啟動時，每0.05秒會執行timer1_Tick事件處理函式一次
        private void timer1_Tick(object sender, EventArgs e)
        {
            total = 0;
            Random rnd = new Random();
            for (int i = 0; i <= arrPic.GetUpperBound(0); i++)   // 控制產生亂數的次數
            {
                getpoint[i] = rnd.Next(0, 6);  // 產生0~5 間之亂數
                total += getpoint[i] + 1;      // 產生的點數累加到total變數
                // 將指定圖檔置入控制項陣列在表單對應的圖片控制項      
                arrPic[i].Image = imgDice.Images[getpoint[i]] ;
            }
        }
        // 按 [停止] 鈕執行
        private void btnStop_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
            lblMsg.Text = "共得到 " + Convert.ToString(total) + " 點 !!";
        }
    }
}
