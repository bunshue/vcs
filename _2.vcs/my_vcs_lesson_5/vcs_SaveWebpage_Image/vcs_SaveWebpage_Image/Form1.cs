using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_SaveWebpage_Image
{
    public partial class Form1 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lb_main_mesg.Text = "";

            //this.FormBorderStyle = FormBorderStyle.None;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            this.Location = new System.Drawing.Point(screenWidth - this.Width - 50, screenHeight - this.Height - 400);
            this.BackColor = Color.Gold;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "Clipboard內的影像顯示存檔\t全部\n";
            bool flag = Clipboard.ContainsImage();  //判斷Clipboard中是否包含圖片資料
            //richTextBox1.Text += "Clipboard 是否包含圖片資料 : " + flag.ToString() + "\n";

            if (flag == true)
            {
                Image img = Clipboard.GetImage();

                //pictureBox_clipboard.Image = img;

                String filename = "C:\\_git\\vcs\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

                Bitmap bitmap1 = (Bitmap)img;

                if (bitmap1 != null)
                {
                    try
                    {
                        //bitmap1.Save(@file1, ImageFormat.Jpeg);
                        bitmap1.Save(filename, ImageFormat.Bmp);
                        //bitmap1.Save(@file3, ImageFormat.Png);

                        //richTextBox1.Text += "存檔成功\n";
                        //richTextBox1.Text += "已存檔 : " + filename + "\n";
                        show_main_message("已存檔", S_OK, 30);
                    }
                    catch (Exception ex)
                    {
                        //richTextBox1.Text += "xxx錯誤訊息b2 : " + ex.Message + "\n";
                        show_main_message("存檔失敗", S_OK, 30);
                    }
                }
            }
            else
            {
                show_main_message("無圖可存", S_OK, 30);
            }
        }

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg.Text = "";
                }
            }
        }
    }
}
