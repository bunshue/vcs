using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for SecurityProtocolType

namespace vcs_SatelliteImages
{
    public partial class Form1 : Form
    {
        int image_type = 0;
        public Form1()
        {
            InitializeComponent();
            //this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法

            //.Net 4.0 要強迫使用 TLS 1.2 抓資料
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件

            //表單不顯示在 Windows 工作列中
            //this.ShowInTaskbar = false;
            Load_SatelliteImages();
        }

        void Load_SatelliteImages()
        {
            int i;
            string mapURL = string.Empty;
            DateTime dt = DateTime.Now;
            int Minute;
            //pictureBox1.ClientSize = new Size(1200, 1200);
            pictureBox1.Location = new Point(0, 0);

            //加入這段語法忽略憑證
            System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

            for (i = 0; i < 5; i++)
            {
                Minute = (dt.Minute / 10) * 10;

                switch (image_type)
                {
                    case 0:
                        richTextBox1.Text += "000\n";
                        mapURL = string.Format("https://www.cwa.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    case 1:
                        richTextBox1.Text += "111\n";
                        mapURL = string.Format("https://www.cwa.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    case 2:
                        richTextBox1.Text += "222\n";
                        mapURL = string.Format("https://www.cwa.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    case 3:
                        richTextBox1.Text += "333\n";
                        mapURL = string.Format("https://www.cwa.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    default:
                        richTextBox1.Text += "xxxxx\n";
                        break;

                }




                richTextBox1.Text += "aaaa mapURL : " + mapURL + "\n";


                //MessageBox.Show("path: " + mapURL);

                try
                {   //可能會產生錯誤的程式區段
                    pictureBox1.Load(mapURL);
                    /*
                    richTextBox1.Text += "URL = " + mapURL + "\n";
                    richTextBox1.Text += "W = " + pictureBox1.Image.Size.Width.ToString() + "\n";
                    richTextBox1.Text += "H = " + pictureBox1.Image.Size.Height.ToString() + "\n";
                    */
                    break;
                }
                catch (Exception ex)
                {   //定義產生錯誤時的例外處理程式碼
                    //MessageBox.Show("path: " + mapURL);
                    //MessageBox.Show(ex.Message);
                }
                finally
                {
                    //一定會被執行的程式區段
                    //MessageBox.Show("path: " + mapURL);
                }
                dt = dt.AddMinutes(-10);
            }

        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            image_type++;
            if (image_type >= 4)
                image_type = 0;
            richTextBox1.Text += "image_type = " + image_type.ToString() + "\t";

            switch (image_type)
            {
                case 0 :
                    richTextBox1.Text += "台灣\n";
                    break;
                case 1:
                    richTextBox1.Text += "東亞\n";
                    break;
                case 2:
                    richTextBox1.Text += "全景\n";
                    break;
                case 3:
                    richTextBox1.Text += "真實色影像\n";
                    break;
                default:
                    richTextBox1.Text += "xxxxx\n";
                    break;

            }
            
            Load_SatelliteImages();
            //Application.Exit();
        }

        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += e.Delta.ToString() + " ";
            if (e.Delta < 0)
            {
                richTextBox1.Text += "圖變小\n";
            }
            else
            {
                richTextBox1.Text += "圖變大\n";
            }
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.X)
            {
                Application.Exit();
            }
            else if (e.KeyCode == Keys.F5)
            {
                richTextBox1.Text += "F5 : Refresh\n";
                Load_SatelliteImages();
            }
            else if (e.KeyCode == Keys.Add)
            {


            }
            else if (e.KeyCode == Keys.Subtract)
            {

            }
            else
            {
                richTextBox1.Text += "你按了" + e.KeyCode.ToString() + "\n";
            }
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************


        #region 移動無邊框Form
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
        #endregion



    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}
