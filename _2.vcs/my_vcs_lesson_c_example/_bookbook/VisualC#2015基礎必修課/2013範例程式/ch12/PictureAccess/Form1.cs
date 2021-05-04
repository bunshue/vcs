using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PictureAccess
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Bitmap bmp;
        Pen p;
        float x, y;
        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            bmp = new Bitmap(345, 270);
            picDraw.BackColor = Color.White;
            p = new Pen(Color.Black, 2);  //指定畫筆的顏色與粗細
        }
        //在picDraw按上滑鼠鍵時執行
        private void picDraw_MouseDown(object sender, MouseEventArgs e)
        {
            x = e.X;
            y = e.Y;
        }
        //在picDraw上移動滑鼠游標時執行
        private void picDraw_MouseMove(object sender, MouseEventArgs e)
        {
            //宣告畫布的來源是bmp圖案物件
            Graphics g = Graphics.FromImage(bmp);
            //如果按下滑鼠左鍵時
            if (e.Button == MouseButtons.Left)
            {
                //隨指標移動不斷在畫布上(圖案物件)畫短點直線
                g.DrawLine(p, x, y, e.X, e.Y);
                //用圖片方塊picDraw來顯示畫布(圖案物件)的內容
                picDraw.Image = bmp;
                x = e.X;
                y = e.Y;
            }
        }
        //按 [開檔] 鈕時執行
        private void btnOpen_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "點陣圖 (*.bmp)|*.bmp|JPEG (*.JPG)|*.JPG|" + "GIF(*.GIF)|*.GIF|All File (*.*)|*.*";
            //執行openFileDialog1.ShowDialog()，選取圖形檔並指定給圖案物件，再用圖片方塊
            //picDraw顯示畫布(圖案物件)的內容。
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                System.IO.FileStream fs = new System.IO.FileStream(openFileDialog1.FileName, System.IO.FileMode.Open);
                bmp = new Bitmap(fs);
                fs.Close();
                picDraw.Image = bmp;
            }
        }
        //按 [存檔] 鈕時執行
        private void btnSave_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Filter = "點陣圖 (*.bmp)|*.bmp|JPEG (*.JPG)|*.JPG|" + "GIF(*.GIF)| *. GIF|All File (*.*)|*.*";
            // 執行saveFileDialog1.ShowDialog()，將圖案物件的內容儲存到指定的檔案內
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                bmp.Save(saveFileDialog1.FileName);
            }
        }
        //按 [清圖] 鈕時執行
        private void btnCls_Click(object sender, EventArgs e)
        {
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);    // 清除畫布，背景為白色
            picDraw.Image = bmp;
        }
        //按 [結束] 鈕時執行
        private void btnEnd_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
