using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

 // 本例需要使用檔案物件來存取圖片，因此請引用System.IO命名空間
 using System.IO;  

namespace WinMouseEvent
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Bitmap bmp;    		// 宣告圖形物件
        int oldX, oldY; 	// 記錄滑鼠指標X、Y座標
        int PenPoint;  	 	// 宣告PenPoint表示畫筆粗細
        Color PenColor;  	// 宣告PenColor表示畫筆顏色

        // === 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            bmp = new Bitmap(320, 210);  //建立圖形物件大小320*210
            Graphics g = Graphics.FromImage(bmp);  // 建立畫布物件g
            PenColor = Color.Black;
            PenPoint = 3;
            g.Clear(Color.White);   // 將畫布清為白色
            pictureBox1.Image = bmp;// 畫布貼到pictureBox1圖片方塊控制項上
            pictureBox1.Refresh();  // 更新pictureBox1圖片方塊控制項
        }
        // ===  執行 [檔案/開檔] 指令執行
        private void 開檔ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                FileStream f = new FileStream("myPic.jpg", FileMode.Open);
                bmp = new Bitmap(f);
                f.Close();   
                pictureBox1.Image = bmp;
            }
            catch (Exception ex)
            {
                MessageBox.Show("目前專案無圖檔，請先繪圖後再存檔");
            }
        }
        // ===   執行 [檔案/存檔] 指令執行
        private void 存檔ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            bmp.Save("myPic.jpg");
        }
        // ===  執行 [檔案/清除] 指令執行
        private void 清除ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Graphics g = Graphics.FromImage(bmp);  // 建立畫布物件g
            g.Clear(Color.White);                  // 將畫布清為白色
            pictureBox1.Image = bmp;   
         }
        
        // ===  執行 [檔案/結束] 指令執行
        private void 結束ToolStripMenuItem_Click(object sender, EventArgs e)
        {
         Application.Exit();
        }
        // ===  在pictureBox圖片方塊上按滑鼠鍵
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            oldX = e.X;
            oldY = e.Y;
        }
        // ===  在pictureBox圖片方塊移動滑鼠會執行
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            //  判斷是否按下滑鼠左鍵
            if (e.Button == MouseButtons.Left)
            {
                Graphics g = Graphics.FromImage(bmp);
                Pen p = new Pen(PenColor, PenPoint);
                g.DrawLine(p, oldX, oldY, e.X, e.Y);//在bmp畫布上畫一條直線
                pictureBox1.Image=bmp;// 畫布貼到pictureBox1圖片方塊控制項上
                oldX = e.X;           // 將目前畫筆座標當作下次畫筆的起點
                oldY = e.Y;
            }
       }
        // ===  設定畫筆粗細為 1 pt 時執行
        private void pixelsToolStripMenuItem_Click(object sender, EventArgs e)
        {
           PenPoint = 1;
        }
        // ===  設定畫筆粗細為 3 pt 時執行
        private void pixelsToolStripMenuItem1_Click(object sender, EventArgs e)
        {
           PenPoint = 3;
        }
        // ===  設定畫筆粗細為 5 pt 時執行
        private void pixelsToolStripMenuItem2_Click(object sender, EventArgs e)
        {
           PenPoint = 5;
        }
        // ===  設定畫筆顏色為黑色
        private void 黑ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PenColor = Color.Black;
        }
        // ===  設定畫筆顏色為紅色
        private void 紅ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PenColor = Color.Red;
        }
         // ===  設定畫筆顏色為綠色
        private void 綠ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PenColor = Color.Green;
        }
        // ===  設定畫筆顏色為藍色
        private void 藍ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PenColor= Color.Blue;
        }
    }
}
