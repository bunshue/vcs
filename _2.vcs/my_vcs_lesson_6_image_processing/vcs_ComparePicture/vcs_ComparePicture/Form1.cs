using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
CIE76：簡單，計算快，但不符合人眼感知。
CIE76：適合快速、粗略的影像比對，計算簡單。
CIEDE2000：更精準，尤其在低飽和度或高亮度的顏色下，人眼感知差異更貼近。
CIEDE2000：適合需要精準度的場合，例如印刷品顏色一致性檢測、醫學影像分析、專業攝影後製。
*/

namespace vcs_ComparePicture
{
    public partial class Form1 : Form
    {
        string filename1 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_f_mix_new\vcs_ComparePicture\vcs_ComparePicture\image1.bmp";
        string filename2 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_f_mix_new\vcs_ComparePicture\vcs_ComparePicture\image2.bmp";
        string filename3 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_f_mix_new\vcs_ComparePicture\vcs_ComparePicture\image3.bmp";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            pictureBox1.Size = new Size(640, 480);
            pictureBox2.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 6 + 70);

            richTextBox1.Size = new Size(200, 400);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 1050);
            this.Text = "vcs_ComparePicture";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // 定義 LAB 結構
        public struct LabColor
        {
            public double L;
            public double A;
            public double B;

            public LabColor(double l, double a, double b)
            {
                this.L = l;
                this.A = a;
                this.B = b;
            }
        }

        // RGB → LAB 轉換
        static LabColor RgbToLab(Color c)
        {
            double r = c.R / 255.0;
            double g = c.G / 255.0;
            double b = c.B / 255.0;

            r = (r > 0.04045) ? Math.Pow((r + 0.055) / 1.055, 2.4) : r / 12.92;
            g = (g > 0.04045) ? Math.Pow((g + 0.055) / 1.055, 2.4) : g / 12.92;
            b = (b > 0.04045) ? Math.Pow((b + 0.055) / 1.055, 2.4) : b / 12.92;

            double x = r * 0.4124 + g * 0.3576 + b * 0.1805;
            double y = r * 0.2126 + g * 0.7152 + b * 0.0722;
            double z = r * 0.0193 + g * 0.1192 + b * 0.9505;

            x /= 0.95047;
            y /= 1.00000;
            z /= 1.08883;

            Func<double, double> f = t => (t > 0.008856) ? Math.Pow(t, 1.0 / 3.0) : (7.787 * t + 16.0 / 116.0);

            double fx = f(x);
            double fy = f(y);
            double fz = f(z);

            double L = (116 * fy) - 16;
            double A = 500 * (fx - fy);
            double B = 200 * (fy - fz);

            return new LabColor(L, A, B);
        }

        void compare_picture(string file1, string file2)
        {
            Bitmap img1 = new Bitmap(file1);
            Bitmap img2 = new Bitmap(file2);
            pictureBox1.Image = img1;
            pictureBox2.Image = img2;

            Application.DoEvents();

            double totalDiff1 = 0;
            double totalDiff2 = 0;
            int width = Math.Min(img1.Width, img2.Width);
            int height = Math.Min(img1.Height, img2.Height);

            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    Color c1 = img1.GetPixel(x, y);
                    Color c2 = img2.GetPixel(x, y);

                    LabColor lab1 = RgbToLab(c1);
                    LabColor lab2 = RgbToLab(c2);

                    //使用 CIE76
                    double dL = lab1.L - lab2.L;
                    double dA = lab1.A - lab2.A;
                    double dB = lab1.B - lab2.B;
                    totalDiff1 += dL * dL + dA * dA + dB * dB;

                    //使用 CIEDE2000
                    double deltaE = Ciede2000(lab1, lab2);
                    totalDiff2 += deltaE * deltaE; // 累加平方差
                }
            }

            richTextBox1.Text += "CIE76     差值 : " + totalDiff1.ToString() + "\n";
            richTextBox1.Text += "CIEDE2000 差值 : " + totalDiff2.ToString() + "\n";
        }

        // CIEDE2000 ΔE 計算
        static double Ciede2000(LabColor lab1, LabColor lab2)
        {
            double L1 = lab1.L, a1 = lab1.A, b1 = lab1.B;
            double L2 = lab2.L, a2 = lab2.A, b2 = lab2.B;

            double avgLp = (L1 + L2) / 2.0;
            double C1 = Math.Sqrt(a1 * a1 + b1 * b1);
            double C2 = Math.Sqrt(a2 * a2 + b2 * b2);
            double avgC = (C1 + C2) / 2.0;

            double G = 0.5 * (1 - Math.Sqrt(Math.Pow(avgC, 7) / (Math.Pow(avgC, 7) + Math.Pow(25.0, 7))));
            double a1p = (1 + G) * a1;
            double a2p = (1 + G) * a2;
            double C1p = Math.Sqrt(a1p * a1p + b1 * b1);
            double C2p = Math.Sqrt(a2p * a2p + b2 * b2);
            double avgCp = (C1p + C2p) / 2.0;

            double h1p = Math.Atan2(b1, a1p);
            if (h1p < 0) h1p += 2 * Math.PI;
            double h2p = Math.Atan2(b2, a2p);
            if (h2p < 0) h2p += 2 * Math.PI;

            double avgHp;
            if (Math.Abs(h1p - h2p) > Math.PI)
                avgHp = (h1p + h2p + 2 * Math.PI) / 2.0;
            else
                avgHp = (h1p + h2p) / 2.0;

            double T = 1 - 0.17 * Math.Cos(avgHp - Math.PI / 6)
                         + 0.24 * Math.Cos(2 * avgHp)
                         + 0.32 * Math.Cos(3 * avgHp + Math.PI / 30)
                         - 0.20 * Math.Cos(4 * avgHp - 21 * Math.PI / 60);

            double dLp = L2 - L1;
            double dCp = C2p - C1p;

            double dhp;
            if (Math.Abs(h2p - h1p) <= Math.PI)
                dhp = h2p - h1p;
            else if (h2p <= h1p)
                dhp = h2p - h1p + 2 * Math.PI;
            else
                dhp = h2p - h1p - 2 * Math.PI;

            double dHp = 2 * Math.Sqrt(C1p * C2p) * Math.Sin(dhp / 2.0);

            double SL = 1 + (0.015 * Math.Pow(avgLp - 50, 2)) / Math.Sqrt(20 + Math.Pow(avgLp - 50, 2));
            double SC = 1 + 0.045 * avgCp;
            double SH = 1 + 0.015 * avgCp * T;

            double deltaTheta = 30 * Math.Exp(-Math.Pow((avgHp * 180 / Math.PI - 275) / 25, 2));
            double RC = 2 * Math.Sqrt(Math.Pow(avgCp, 7) / (Math.Pow(avgCp, 7) + Math.Pow(25.0, 7)));
            double RT = -RC * Math.Sin(2 * deltaTheta * Math.PI / 180);

            double dE = Math.Sqrt(
                Math.Pow(dLp / SL, 2) +
                Math.Pow(dCp / SC, 2) +
                Math.Pow(dHp / SH, 2) +
                RT * (dCp / SC) * (dHp / SH)
            );
            return dE;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            compare_picture(filename1, filename2);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            compare_picture(filename2, filename3);
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}
