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

namespace vcs_PicPick4
{
    public partial class Form1 : Form
    {
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


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
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

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            try
            {
                bitmap1.Save(filename, ImageFormat.Jpeg);
                //bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }
    }
}

