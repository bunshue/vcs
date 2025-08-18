using OpenCvSharp;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

/*
工具/NuGet套件管理員/管理方案的NuGet套件/
瀏覽安裝
OpenCvSharp4

OpenCvSharp4
OpenCvSharp4.Extensions
OpenCvSharp4.runtime.win
OpenCvSharp4.windows
*/

namespace OpenCvSharp4a
{
    public partial class Form1 : Form
    {
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
            dx = 140;
            dy = 70;

            button1.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 0);
            button2.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 1);
            button3.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 2);
        }


        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            //例1
            Mat src = new Mat(filename, ImreadModes.Grayscale);
            Mat dst = new Mat();

            Cv2.Canny(src, dst, 50, 200);
            Cv2.ImShow("src image", src);
            Cv2.ImShow("dst image", dst);
            Cv2.WaitKey(0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //例2 创建一张大小为400*600颜色为白色背景的三通道彩色图像
            int d = 100;
            Mat img = new Mat(400, 600, MatType.CV_8UC3, new Scalar(255, 255, 255));

            Cv2.Line(img, 250, 100, 50, 200, new Scalar(0, 255, 0), 2);
            Cv2.Rectangle(img, new Rect(50, 50, d, d + 100), new Scalar(0, 0, 255), -1);
            Cv2.Circle(img, new OpenCvSharp.Point(50, 50), 25, new Scalar(255, 255, 0), -1);

            Cv2.PutText(img, "OpenCV", new OpenCvSharp.Point(220, 100), HersheyFonts.HersheyComplex, 3, Scalar.Blue, 15);
            Cv2.PutText(img, "OpenCV", new OpenCvSharp.Point(220, 100), HersheyFonts.HersheyComplex, 3, Scalar.Yellow, 5);

            ////显示图像
            Cv2.ImShow("img", img);
            ////延时等待按键按下
            Cv2.WaitKey(0);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery\taitung1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery\taitung2.jpg";

            Mat img1 = new Mat(filename1, ImreadModes.Grayscale);
            Mat img2 = new Mat(filename2, ImreadModes.Grayscale);

            //確定ROI區域
            Rect roi = new Rect(100, 100, 500, 500);

            //提取ROI區域
            Mat roiImg1 = new Mat(img1, roi);
            Mat roiImg2 = new Mat(img2, roi);

            //圖像融合
            Mat dst = new Mat();
            Cv2.AddWeighted(roiImg1, 0.5, roiImg2, 0.5, 0, dst);

            //將融合後的圖像複製回原圖
            dst.CopyTo(img1[roi]);

            //顯示結果
            Cv2.ImShow("Image Fusion", img1);
            Cv2.WaitKey(0);
            Cv2.DestroyAllWindows();
        }
    }
}
