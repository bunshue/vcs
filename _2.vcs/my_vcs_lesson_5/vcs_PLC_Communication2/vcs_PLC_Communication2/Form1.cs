using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;       //for Process, Stopwatch
using System.Drawing.Imaging;

using vcs_PLC_Communication2.PLC_Communication;

namespace vcs_PLC_Communication2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.plC_Open_Time1.MitsubishiIP = "192.168.3.39";
            this.plC_Open_Time1.Interval = 500;
            this.plC_Open_Time1.Enabled = true;
            this.plC_Open_Time1.Mitsubishi_Open = true;
            this.plC_Open_Time1.Start();

            add_automation_controls();
            show_item_location();
        }

        void show_item_location()
        {
            this.Size = new Size(PLC_PANEL_WIDTH + BORDER * 4, PLC_PANEL_HEIGHT + 0 + BORDER * 6);
            //this.Size = new Size(PLC_PANEL_WIDTH + BORDER * 4, PLC_PANEL_HEIGHT + groupBox1.Height + BORDER * 6);
            //groupBox1.Location = new Point(BORDER, PLC_PANEL_HEIGHT + BORDER * 1);

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(10, 10);

            // C# 設定視窗載入位置 
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        void save_image_to_drive() //用時間檔名存檔 不檢查序號
        {
            show_plc_main_message1("存檔中...", S_OK, 10);
            delay(10);

            Bitmap bitmap1 = (Bitmap)pictureBox_plc_status.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                g.ReleaseHdc();
                g.Dispose();

                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);

                    richTextBox_plc.Text += "存檔成功\n";
                    richTextBox_plc.Text += "已存檔 : " + filename + "\n";
                    show_plc_main_message1("已存檔BMP", S_OK, 30);
                }
                catch (Exception ex)
                {
                    richTextBox_plc.Text += "xxx錯誤訊息e39 : " + ex.Message + "\n";
                    show_plc_main_message1("存檔失敗", S_OK, 30);
                    //show_plc_main_message1("存檔失敗 : " + ex.Message, S_OK, 30);
                }
            }
            else
            {
                richTextBox_plc.Text += "無圖可存\n";
                show_plc_main_message1("無圖可存a", S_FALSE, 30);
                show_plc_main_message1("無圖可存a", S_FALSE, 30);
            }
            return;
        }
    }
}
