using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

using System.Runtime.InteropServices;

namespace vcs_ScreenCapture0
{
    public partial class Form1 : Form
    {
        //button0 ST
        [System.Runtime.InteropServices.DllImportAttribute("gdi32.dll")]

        private static extern bool BitBlt(
        IntPtr hdcDest, //目標設備的句柄
        int nXDest, // 目標對象的左上角的X坐標
        int nYDest, // 目標對象的左上角的X坐標
        int nWidth, // 目標對象的矩形的寬度
        int nHeight, // 目標對象的矩形的長度
        IntPtr hdcSrc, // 源設備的句柄
        int nXSrc, // 源對象的左上角的X坐標
        int nYSrc, // 源對象的左上角的X坐標
        System.Int32 dwRop // 光柵的操作值
        );

        [System.Runtime.InteropServices.DllImportAttribute("gdi32.dll")]

        private static extern IntPtr CreateDC(
        string lpszDriver, // 驅動名稱
        string lpszDevice, // 設備名稱
        string lpszOutput, // 無用，可以設定位"NULL"
        IntPtr lpInitData // 任意的打印機數據
        );
        //button0 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(440, 640);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);

            this.Size = new Size(720, 700);
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //擷取全螢幕
            Bitmap bitmap1 = null;
            IntPtr dc1 = CreateDC("DISPLAY", null, null, (IntPtr)null);

            //創建顯示器的DC
            Graphics g1 = Graphics.FromHdc(dc1);

            //由一個指定設備的句柄創建一個新的Graphics對象
            bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height, g1);

            //根據屏幕大小創建一個與之相同大小的Bitmap對象
            Graphics g2 = Graphics.FromImage(bitmap1);

            //獲得屏幕的句柄
            IntPtr dc3 = g1.GetHdc();

            //獲得位圖的句柄
            IntPtr dc2 = g2.GetHdc();

            //把當前屏幕捕獲到位圖對象中
            BitBlt(dc2, 0, 0, Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height, dc3, 0, 0, 13369376);

            //把當前屏幕拷貝到位圖中
            g1.ReleaseHdc(dc3);

            //釋放屏幕句柄
            g2.ReleaseHdc(dc2);

            //釋放位圖句柄
            string filename = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            try
            {
                bitmap1.Save(filename, ImageFormat.Jpeg);
                //bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }


        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}
