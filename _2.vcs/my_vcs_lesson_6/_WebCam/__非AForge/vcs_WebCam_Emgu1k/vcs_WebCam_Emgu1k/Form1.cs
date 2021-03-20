using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using Emgu.CV;
using Emgu.CV.Structure;

namespace vcs_WebCam_Emgu1k
{
    public partial class Form1 : Form
    {
        private Capture cap = null;
        string _phtoDirectory = @"c:\______test_files\photos\";
        string _fileName;

        public Form1()
        {
            InitializeComponent();
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> frame = cap.QueryFrame();
            pictureBox1.Image = frame.ToBitmap();
        
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            cap = new Capture(0);
            //cap = new Capture("C:\\______test_files\\aaaa.mp4");
            Application.Idle += new EventHandler(Application_Idle);
            double width;
            double height;
            double frame_count;
            double fps;
            width = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            height = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "width = " + width.ToString() + " height = " + height.ToString() + "\n";
            richTextBox1.Text += "frame_count = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "fps = " + fps.ToString() + "\n";
        }

        /// <summary>
        /// 開啟攝影機
        /// </summary>
        private void openWebCam()
        {
            //如果webcam沒啟動
            if (cap == null)
            {
                try
                {
                    //打開預設的webcam
                    cap = new Capture();
                }
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //openWebCam();

            // Query 攝影機的畫面
            Image<Bgr, Byte> phtoFrame = cap.QueryFrame();

            //儲存路徑
            _fileName = string.Format("{0}{1}{2}", _phtoDirectory, DateTime.Now.ToString("yyyyMMddHmmss"), ".JPG");

            //儲存影像
            phtoFrame.Save(_fileName);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // Query 攝影機的畫面
            Image<Bgr, Byte> phtoFrame = cap.QueryFrame();

            //儲存路徑
            _fileName = string.Format("{0}{1}{2}", _phtoDirectory, DateTime.Now.ToString("yyyyMMddHmmss"), ".JPG");

            //儲存影像
            phtoFrame.Save(_fileName);


            System.Drawing.Bitmap bitmap = null;
            //宣告 QRCode Reader 物件
            ZXing.IBarcodeReader reader = new ZXing.BarcodeReader();

            //讀取要解碼的圖片
            FileStream fs = new FileStream(_fileName, FileMode.Open);
            Byte[] data = new Byte[fs.Length];
            // 把檔案讀取到位元組陣列
            fs.Read(data, 0, data.Length);
            fs.Close();
            // 實例化一個記憶體資料流 MemoryStream，將位元組陣列放入
            MemoryStream ms = new MemoryStream(data);
            // 將記憶體資料流的資料放到 BitMap的物件中
            bitmap = (Bitmap)Image.FromStream(ms);

            //將圖片顯示於 PictureBox 中
            //pictureBox2.Image = bitmap;
            //進行解碼的動作
            ZXing.Result result = reader.Decode(bitmap);

            if (result != null)
            {   //如果有成功解讀，則顯示文字
                richTextBox2.Text = result.Text;
            }
            else
            {
                richTextBox2.Text = "解不出來";
            
            }


        }
    }
}
