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
        string filename1 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_image_processing\vcs_ComparePicture\vcs_ComparePicture\image1.bmp";
        string filename2 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_image_processing\vcs_ComparePicture\vcs_ComparePicture\image2.bmp";
        string filename3 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_image_processing\vcs_ComparePicture\vcs_ComparePicture\image3.bmp";

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
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            pictureBox1.Size = new Size(640, 480);
            pictureBox2.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 6 + 70);

            richTextBox1.Size = new Size(400, 800);
            richTextBox1.Location = new Point(x_st + dx * 4+30, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1300, 1050);
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

        //6060


        static float Gamma(float x)
        {
            return (float)(x > 0.04045f ? Math.Pow((x + 0.055f) / 1.055f, 2.4f) : x / 12.92f);
        }

        public static float[] rgb2lab(float var_R, float var_G, float var_B)
        {
            float[] arr = new float[3];
            float B = Gamma(var_B);
            float G = Gamma(var_G);
            float R = Gamma(var_R);
            float X = 0.412453f * R + 0.357580f * G + 0.180423f * B;
            float Y = 0.212671f * R + 0.715160f * G + 0.072169f * B;
            float Z = 0.019334f * R + 0.119193f * G + 0.950227f * B;

            X /= 0.95047f;
            Y /= 1.0f;
            Z /= 1.08883f;

            float FX = (float)(X > 0.008856f ? Math.Pow(X, 1.0f / 3.0f) : (7.787f * X + 0.137931f));
            float FY = (float)(Y > 0.008856f ? Math.Pow(Y, 1.0f / 3.0f) : (7.787f * Y + 0.137931f));
            float FZ = (float)(Z > 0.008856f ? Math.Pow(Z, 1.0f / 3.0f) : (7.787f * Z + 0.137931f));
            arr[0] = Y > 0.008856f ? (116.0f * FY - 16.0f) : (903.3f * Y);
            arr[1] = 500f * (FX - FY);
            arr[2] = 200f * (FY - FZ);
            return arr;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //RGB 轉 LAB

            //RGB 轉 LAB

            float var_R = 255;
            float var_G = 0;
            float var_B = 0;

            float[] cc = rgb2lab(var_R, var_G, var_B);

            richTextBox1.Text += cc + "\n";
            richTextBox1.Text += cc[0] + "\n";
            richTextBox1.Text += cc[1] + "\n";
            richTextBox1.Text += cc[2] + "\n";


            var_R = 0;
            var_G = 255;
            var_B = 0;

            cc = rgb2lab(var_R, var_G, var_B);

            richTextBox1.Text += cc + "\n";
            richTextBox1.Text += cc[0] + "\n";
            richTextBox1.Text += cc[1] + "\n";
            richTextBox1.Text += cc[2] + "\n";


            var_R = 0;
            var_G = 0;
            var_B = 255;

            cc = rgb2lab(var_R, var_G, var_B);

            richTextBox1.Text += cc + "\n";
            richTextBox1.Text += cc[0] + "\n";
            richTextBox1.Text += cc[1] + "\n";
            richTextBox1.Text += cc[2] + "\n";


        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Color Matrix的使用 1\n";
            //color_correction_matrix = 
            double[,] color_correction_matrix = new double[,] {
            { 1.36, -0.3, -0.06},
            { -0.20, 1.32, -0.12},
            { -0.04, -0.55, 1.59}
            };

            richTextBox1.Text += color_correction_matrix[0, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[0, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[0, 2].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[1, 2].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 0].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 1].ToString() + "\n";
            richTextBox1.Text += color_correction_matrix[2, 2].ToString() + "\n";

            double N16 = color_correction_matrix[0, 0];
            double O16 = color_correction_matrix[0, 1];
            double P16 = color_correction_matrix[0, 2];
            double N17 = color_correction_matrix[1, 0];
            double O17 = color_correction_matrix[1, 1];
            double P17 = color_correction_matrix[1, 2];
            double N18 = color_correction_matrix[2, 0];
            double O18 = color_correction_matrix[2, 1];
            double P18 = color_correction_matrix[2, 2];

            //保留給 RGB to YUV Conversion Matrix
            //double[] B = new double[] { 1, 2, 3, 4, 5 };
            double E12 = -0.31;
            double F12 = -0.59;
            double G12 = 0.89;
            double E13 = 0.69;
            double F13 = -0.59;
            double G13 = -0.11;
            double E17 = E12 * 0.563;
            double F17 = F12 * 0.563;
            double G17 = G12 * 0.563;
            double E18 = E13 * 0.713;
            double F18 = F13 * 0.713;
            double G18 = G13 * 0.713;

            double E22 = E17 * N16 + F17 * N17 + G17 * N18;	//MMULT(E17:G17,N16:N18)
            double F22 = E17 * O16 + F17 * O17 + G17 * O18;	//MMULT(E17:G17,O16:O18)
            double G22 = E17 * P16 + F17 * P17 + G17 * P18;	//MMULT(E17:G17,P16:P18)
            double E23 = E18 * N16 + F18 * N17 + G18 * N18;	//MMULT(E18:G18,N16:N18)
            double F23 = E18 * O16 + F18 * O17 + G18 * O18;	//MMULT(E18:G18,O16:O18)
            double G23 = E18 * P16 + F18 * P17 + G18 * P18;	//MMULT(E18:G18,P16:P18)

            richTextBox1.Text += "E22 = " + E22.ToString() + "\n";
            richTextBox1.Text += "F22 = " + F22.ToString() + "\n";
            richTextBox1.Text += "G22 = " + G22.ToString() + "\n";
            richTextBox1.Text += "E23 = " + E23.ToString() + "\n";
            richTextBox1.Text += "F23 = " + F23.ToString() + "\n";
            richTextBox1.Text += "G23 = " + G23.ToString() + "\n";

            double dMTX1 = E23 * 128;
            double dMTX2 = F23 * 128;
            double dMTX3 = G23 * 128;
            double dMTX4 = E22 * 128;
            double dMTX5 = F22 * 128;
            double dMTX6 = G22 * 128;

            richTextBox1.Text += "dMTX1 = " + dMTX1.ToString() + "\n";
            richTextBox1.Text += "dMTX2 = " + dMTX2.ToString() + "\n";
            richTextBox1.Text += "dMTX3 = " + dMTX3.ToString() + "\n";
            richTextBox1.Text += "dMTX4 = " + dMTX4.ToString() + "\n";
            richTextBox1.Text += "dMTX5 = " + dMTX5.ToString() + "\n";
            richTextBox1.Text += "dMTX6 = " + dMTX6.ToString() + "\n";

            int MTX1 = (int)Math.Round(dMTX1);
            int MTX2 = (int)Math.Round(dMTX2);
            int MTX3 = (int)Math.Round(dMTX3);
            int MTX4 = (int)Math.Round(dMTX4);
            int MTX5 = (int)Math.Round(dMTX5);
            int MTX6 = (int)Math.Round(dMTX6);

            if (MTX1 >= 0)
                richTextBox1.Text += "MTX1 = 0x" + MTX1.ToString("X2") + " = " + MTX1.ToString() + "\n";
            else
                richTextBox1.Text += "MTX1 = -0x" + (-MTX1).ToString("X2") + " = " + MTX1.ToString() + "\n";
            if (MTX2 >= 0)
                richTextBox1.Text += "MTX2 = 0x" + MTX2.ToString("X2") + " = " + MTX2.ToString() + "\n";
            else
                richTextBox1.Text += "MTX2 = -0x" + (-MTX2).ToString("X2") + " = " + MTX2.ToString() + "\n";
            if (MTX3 >= 0)
                richTextBox1.Text += "MTX3 = 0x" + MTX3.ToString("X2") + " = " + MTX3.ToString() + "\n";
            else
                richTextBox1.Text += "MTX3 = -0x" + (-MTX3).ToString("X2") + " = " + MTX3.ToString() + "\n";
            if (MTX4 >= 0)
                richTextBox1.Text += "MTX4 = 0x" + MTX4.ToString("X2") + " = " + MTX4.ToString() + "\n";
            else
                richTextBox1.Text += "MTX4 = -0x" + (-MTX4).ToString("X2") + " = " + MTX4.ToString() + "\n";
            if (MTX5 >= 0)
                richTextBox1.Text += "MTX5 = 0x" + MTX5.ToString("X2") + " = " + MTX5.ToString() + "\n";
            else
                richTextBox1.Text += "MTX5 = -0x" + (-MTX5).ToString("X2") + " = " + MTX5.ToString() + "\n";
            if (MTX6 >= 0)
                richTextBox1.Text += "MTX6 = 0x" + MTX6.ToString("X2") + " = " + MTX6.ToString() + "\n";
            else
                richTextBox1.Text += "MTX6 = -0x" + (-MTX6).ToString("X2") + " = " + MTX6.ToString() + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Color Matrix的使用 2\n";

            int MTX1 = 0;
            int MTX2 = 83;
            int MTX3 = -84;
            int MTX4 = 0;
            int MTX5 = -29;
            int MTX6 = 28;

            richTextBox1.Text += "MTX1 = 0x" + MTX1.ToString("X2") + " = " + MTX1.ToString() + "\n";
            richTextBox1.Text += "MTX2 = 0x" + MTX2.ToString("X2") + " = " + MTX2.ToString() + "\n";
            richTextBox1.Text += "MTX3 = 0x" + MTX3.ToString("X2") + " = " + MTX3.ToString() + "\n";
            richTextBox1.Text += "MTX4 = 0x" + MTX4.ToString("X2") + " = " + MTX4.ToString() + "\n";
            richTextBox1.Text += "MTX5 = 0x" + MTX5.ToString("X2") + " = " + MTX5.ToString() + "\n";
            richTextBox1.Text += "MTX6 = 0x" + MTX6.ToString("X2") + " = " + MTX6.ToString() + "\n";

            int CMXSIGN = 0;
            int CMX16 = 0;
            int CMX15 = 0;
            int CMX14 = 0;
            int CMX13 = 0;
            int CMX12 = 0;
            int CMX11 = 0;

            if (MTX1 >= 0)
            {
                CMX11 = MTX1;
            }
            else
            {
                CMX11 = -MTX1;
                CMXSIGN += 1;
            }
            if (MTX2 >= 0)
            {
                CMX12 = MTX2;
            }
            else
            {
                CMX12 = -MTX2;
                CMXSIGN += 2;
            }
            if (MTX3 >= 0)
            {
                CMX13 = MTX3;
            }
            else
            {
                CMX13 = -MTX3;
                CMXSIGN += 4;
            }
            if (MTX4 >= 0)
            {
                CMX14 = MTX4;
            }
            else
            {
                CMX14 = -MTX4;
                CMXSIGN += 8;
            }
            if (MTX5 >= 0)
            {
                CMX15 = MTX5;
            }
            else
            {
                CMX15 = -MTX5;
                CMXSIGN += 16;
            }
            if (MTX6 >= 0)
            {
                CMX16 = MTX6;
            }
            else
            {
                CMX16 = -MTX6;
                CMXSIGN += 32;
            }

            richTextBox1.Text += "CMXSIGN = 0x" + CMXSIGN.ToString("X2") + " = " + CMXSIGN.ToString() + "\n";
            richTextBox1.Text += "CMX11 = 0x" + CMX11.ToString("X2") + " = " + CMX11.ToString() + "\n";
            richTextBox1.Text += "CMX12 = 0x" + CMX12.ToString("X2") + " = " + CMX12.ToString() + "\n";
            richTextBox1.Text += "CMX13 = 0x" + CMX13.ToString("X2") + " = " + CMX13.ToString() + "\n";
            richTextBox1.Text += "CMX14 = 0x" + CMX14.ToString("X2") + " = " + CMX14.ToString() + "\n";
            richTextBox1.Text += "CMX15 = 0x" + CMX15.ToString("X2") + " = " + CMX15.ToString() + "\n";
            richTextBox1.Text += "CMX16 = 0x" + CMX16.ToString("X2") + " = " + CMX16.ToString() + "\n";
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
