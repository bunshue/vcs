using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PicShow
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 建立picName[1]~picName[4] 用來存放圖檔名稱，picName[0]省略不用
            string[] picName = new string[] { "", "天空", "水庫", "庭園", "雪景" };
            // 建立btn[1]~btn[4]用來代表button1~button4四個按鈕物件，btn[0]省略不用
            Button[] btn = new Button[picName.Length];
            btn[1] = button1;   // 設定btn[1]即代表button1
            btn[2] = button2;   // 設定btn[2]即代表button2
            btn[3] = button3;   // 設定btn[3]即代表button3
            btn[4] = button4;   // 設定btn[4]即代表button4
            // 使用for 迴圈設定button1~button4上的Text屬性與Click事件要執行的事MyClick
            for (int i = 1; i < picName.Length; i++)
            {
                btn[i].Text = picName[i];
                btn[i].Click += new EventHandler(MyClick);
            }
            // 指定pictureBox1顯示無尾態.jpg
            pictureBox1.Image = new Bitmap("../../" + picName[1] + ".jpg");
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
        }

        // 建立MyClick事件處理函式, 用來處理button1~button4的Click事件
        void MyClick(object sender, EventArgs e)
        {
            Button btnHit = (Button)sender;   // 將sender轉型成Button物件btnHit

            richTextBox1.Text += "你按了 " + btnHit.Name + "\t" + btnHit.Text + "\n";

            // pictrueBox1顯示btnHit.Text上的圖檔名稱
            pictureBox1.Image = new Bitmap("../../" + btnHit.Text + ".jpg");

        }
    }
}

