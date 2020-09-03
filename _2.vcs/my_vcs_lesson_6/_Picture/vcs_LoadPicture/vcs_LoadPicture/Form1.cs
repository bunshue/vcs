using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File, FileStream
using System.Drawing.Imaging;   //for PixelFormat

namespace vcs_LoadPicture
{
    public partial class Form1 : Form
    {
        int zoom_cnt = 0;
        int zoom_cnt_max = 15;
        int zoom_step = 40;
        int usb_camera_width = 640;
        int usb_camera_height = 480;

        int btn_down_up_cnt = 0;
        int btn_right_left_cnt = 0;

        int flag_zoom_operation_mode = MODE_RELEASE_STAGE0;
        private const int MODE_RELEASE_STAGE0 = 0x00;   //調整PictureBox大小
        private const int MODE_RELEASE_STAGE1 = 0x01;   //調整擷取影像大小
        private const int MODE_RELEASE_STAGE2 = 0x02;   //調整影像大小

        Image image1;

        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            pictureBox1.ClientSize = new Size(640, 480);    //設定pictureBox的大小
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.Cursor = Cursors.Cross;  //移到控件上，改變鼠標
            comboBox1.SelectedIndex = 0;

            image1 = Image.FromFile("C:\\______test_files\\ims_image.bmp");
            pictureBox1.Image = image1;
            richTextBox1.Text += "W = " + image1.Width.ToString() + ", H = " + image1.Height.ToString() + "\n";

            button17.BackgroundImage = vcs_LoadPicture.Properties.Resources.plus;
            button18.BackgroundImage = vcs_LoadPicture.Properties.Resources.minus;
            btnUp.BackgroundImage = vcs_LoadPicture.Properties.Resources.up;
            btnDown.BackgroundImage = vcs_LoadPicture.Properties.Resources.down;
            btnLeft.BackgroundImage = vcs_LoadPicture.Properties.Resources.left;
            btnRight.BackgroundImage = vcs_LoadPicture.Properties.Resources.right;
            btnCenter.BackgroundImage = vcs_LoadPicture.Properties.Resources.stop;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            image1 = Image.FromFile("C:\\______test_files\\_case1\\pic1.jpg");
            pictureBox1.Image = image1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            image1 = new Bitmap(@"C:\______test_files\_case1\\pic2.jpg", true);
            pictureBox1.Image = image1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //法一
            //ImageLocation	取得或設定路徑或影像 URL 中顯示 PictureBox
            //pictureBox1.ImageLocation = "C:\\______test_files\\_case1\\pic3.jpg";

            //法二
            //Load()		顯示所指定的影像 ImageLocation 屬性 PictureBox。
            //string ImageLocation = "C:\\______test_files\\_case1\\pic3.jpg";
            //pictureBox1.Load(ImageLocation);

            //法三
            //Load(String)	設定 ImageLocation 到指定的 URL，並顯示所指出的影像。
            pictureBox1.Load("C:\\______test_files\\_case1\\pic3.jpg");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.ImageLocation = "http://www.myson.com.tw/images/index/ad01.jpg";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            DateTime dt = DateTime.Now;
            int Minute;
            pictureBox1.ClientSize = new Size(800, 800);

            //加入這段語法忽略憑證
            System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

            for (i = 0; i < 5; i++)
            {
                Minute = (dt.Minute / 10) * 10;
                string mapURL = string.Format("https://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/s1p-{0}-{1}-{2}-{3}-{4}.jpg",
                    dt.Year,
                    dt.Month.ToString("00"),
                    dt.Day.ToString("00"),
                    dt.Hour.ToString("00"),
                    Minute.ToString("00"));
                //MessageBox.Show("path: " + mapURL);

                try
                {   //可能會產生錯誤的程式區段
                    pictureBox1.Load(mapURL);
                    break;
                }
                catch (Exception ex)
                {   //定義產生錯誤時的例外處理程式碼
                    richTextBox1.Text += "path: " + mapURL + "\n";
                    richTextBox1.Text += ex.Message + "\n";
                }
                finally
                {
                    //一定會被執行的程式區段
                    //MessageBox.Show("path: " + mapURL);
                }
                dt = dt.AddMinutes(-10);
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //圖片SizeMode
            int sizemode = comboBox1.SelectedIndex;
            switch (sizemode)
            {
                case 0:
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
                case 1:
                    pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                    break;
                case 2:
                    pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                    break;
                case 3:
                    pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
                    break;
                case 4:
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                    break;
                default:
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //錯誤的寫法, 可能會出現"記憶體不足"
            //pictureBox1.Image = Image.FromFile(@"c:\______test_files\bear.bmp");

            //正確的寫法
            FileStream fs = File.OpenRead(@"c:\______test_files\bear.bmp");
            pictureBox1.Image = Image.FromStream(fs);
            fs.Close();

        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                //調整PictureBox大小

            }
            else if (radioButton2.Checked == true)
            {
                //調整影像大小
            }


        }

        void reload_picturebox()
        {
            int w = usb_camera_width;
            int h = usb_camera_height;
            //int x_st = zoom_step * zoom_cnt / 2;
            //int y_st = zoom_step * zoom_cnt / 2 * 3 / 4;
            int x_st = zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2;
            int y_st = (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;

            int W = w - zoom_step * zoom_cnt;
            int H = h - zoom_step * zoom_cnt * 3 / 4;
            richTextBox1.Text += "zoom_cnt = " + zoom_cnt.ToString() + "\tx_st = " + x_st.ToString() + "\ty_st = " + y_st.ToString() + "\tW = " + W.ToString() + "\tH = " + H.ToString() + "\n";

            Bitmap bm = new Bitmap(@"C:\______test_files\ims_image.bmp", true);

            /*
            RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2,
                                             (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4,
                                             w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
            */


            RectangleF rect = new RectangleF(x_st, y_st, W, H);
            richTextBox1.Text += "x_st = " + x_st.ToString() + "\ty_st = " + y_st.ToString() + "\tW = " + W.ToString() + "\tH = " + H.ToString() + "\n";

            try
            {
                //將處理之後的圖片貼出來
                pictureBox1.Image = bm.Clone(rect, PixelFormat.Format32bppArgb);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息p : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源





        }

        private void button17_Click(object sender, EventArgs e)
        {
            if (zoom_cnt < zoom_cnt_max)
            {
                zoom_cnt++;

                int w = usb_camera_width;
                float ratio;
                ratio = 640 / (float)(w - zoom_step * zoom_cnt);
                lb_zoom.Text = ratio.ToString("#0.00") + " X";

                reload_picturebox();
            }
            else
                richTextBox1.Text += "已達最大放大倍率\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            if (zoom_cnt > 0)
            {
                int w = usb_camera_width;
                int h = usb_camera_height;
                int x_st = zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2;
                int y_st = (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                int W = w - zoom_step * zoom_cnt;
                int H = h - zoom_step * zoom_cnt * 3 / 4;
                //richTextBox1.Text += "原抓取位置 x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + " W = " + W.ToString() + " H = " + H.ToString() + "\n";

                int x_st_next = zoom_step * (zoom_cnt - 1) / 2 + zoom_step * btn_right_left_cnt / 2;
                int y_st_next = (zoom_step * (zoom_cnt - 1) / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                int W2 = w - zoom_step * (zoom_cnt - 1) + x_st_next;
                int H2 = h - zoom_step * (zoom_cnt - 1) * 3 / 4 + y_st_next;

                //richTextBox1.Text += "x_st_next = " + x_st_next.ToString() + " y_st_next = " + y_st_next.ToString() + "\n";

                bool flag_need_to_reload_picturebox = true;
                if (x_st_next < 0)
                {
                    richTextBox1.Text += "已到左邊界, 不動作left, 回走, 向右一步\n";
                    btn_right_left_cnt++;
                    flag_need_to_reload_picturebox = false;
                }
                if (y_st_next < 0)
                {
                    richTextBox1.Text += "已到上邊界, 不動作up, 回走, 向下一步\n";
                    btn_down_up_cnt++;
                    flag_need_to_reload_picturebox = false;
                }
                if (W2 > 640)
                {
                    richTextBox1.Text += "已到右邊界, 不動作right, 回走, 向左一步\n";
                    btn_right_left_cnt--;
                    flag_need_to_reload_picturebox = false;
                }
                if (H2 > 480)
                {
                    richTextBox1.Text += "已到下邊界, 不動作down, 回走, 向上一步\n";
                    btn_down_up_cnt--;
                    flag_need_to_reload_picturebox = false;
                }

                if (flag_need_to_reload_picturebox == true)
                {
                    zoom_cnt--;
                    x_st = zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2;
                    y_st = (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                    W = w - zoom_step * zoom_cnt;
                    H = h - zoom_step * zoom_cnt * 3 / 4;

                    reload_picturebox();

                    float ratio;
                    ratio = 640 / (float)(w - zoom_step * zoom_cnt);
                    lb_zoom.Text = ratio.ToString("#0.00") + " X";
                }
            }
            else
                richTextBox1.Text += "已達最小放大倍率\n";
        }

        private void btnLeft_Click(object sender, EventArgs e)
        {
            if (btn_right_left_cnt > -zoom_cnt)
            {
                btn_right_left_cnt--;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
                reload_picturebox();
            }
            else
                richTextBox1.Text += "已達邊界最左\n";
        }

        private void btnRight_Click(object sender, EventArgs e)
        {
            if (btn_right_left_cnt < zoom_cnt)
            {
                btn_right_left_cnt++;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
                reload_picturebox();
            }
            else
                richTextBox1.Text += "已達邊界最右\n";
        }

        private void btnUp_Click(object sender, EventArgs e)
        {
            if (btn_down_up_cnt > -zoom_cnt)
            {
                btn_down_up_cnt--;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
                reload_picturebox();
            }
            else
                richTextBox1.Text += "已達邊界最上\n";
        }

        private void btnDown_Click(object sender, EventArgs e)
        {
            if (btn_down_up_cnt < zoom_cnt)
            {
                btn_down_up_cnt++;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
                reload_picturebox();
            }
            else
                richTextBox1.Text += "已達邊界最下\n";
        }

        private void btnCenter_Click(object sender, EventArgs e)
        {
            zoom_cnt = 0;
            btn_down_up_cnt = 0;
            btn_right_left_cnt = 0;
            lb_zoom.Text = "1.00 X";
            richTextBox1.Text += "恢復置中\n";
            reload_picturebox();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            flag_zoom_operation_mode = MODE_RELEASE_STAGE0;
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            flag_zoom_operation_mode = MODE_RELEASE_STAGE1;
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            flag_zoom_operation_mode = MODE_RELEASE_STAGE2;
        }

    }
}
