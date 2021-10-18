using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;

//C#實現wav波形圖

namespace draw_wave
{
    public partial class Form1 : Form
    {
        const int byteSample = 2;
        const int dataPosition = 40;
        //0x16 2byte 0002  雙聲道
        //0x22 2byte 0010  16位
        //0x18 4byte 0000AC44   44100采樣率

        const bool leftStatus = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取wav，保存音頻數據到txt
            string filename1 = @"C:\______test_files\_wav\start.wav";
            string filename2 = @"start.txt";

            byte[] length = new byte[4];
            FileStream fs = new FileStream(filename1, FileMode.Open, FileAccess.Read);
            fs.Position = dataPosition;
            fs.Read(length, 0, 4);
            byte[] content = new byte[getHexToInt(length)];
            string[] sample = new string[content.Length / byteSample];
            fs.Read(content, 0, content.Length);
            getHex(content);
            sample = getSample(content);
            StreamWriter sw = new StreamWriter(filename2, true, Encoding.Default);
            foreach (string i in sample)
            {
                sw.Flush();
                sw.WriteLine(i);
            }
            sw.Close();
        }

        static int getHexToInt(byte[] x)
        {
            string retValue = "";
            for (int i = x.Length - 1; i >= 0; i--)
            {
                retValue += x[i].ToString("X");
            }
            return Convert.ToInt32(retValue, 16);
        }

        static void getHex(byte[] x)
        {
            byte tmp;
            for (int i = 0; i < x.Length; i++)
            {
                tmp = Convert.ToByte(x[i].ToString("X"), 16);
                x[i] = tmp;
            }
        }

        static string[] getSample(byte[] x)
        {
            string[] retValue = new string[x.Length / byteSample];

            for (int i = 0; i < retValue.Length; i++)
            {
                for (int j = (i + 1) * byteSample - 1; j >= i * byteSample; j--)
                {
                    retValue[i] += x[j].ToString("X");
                }
                retValue[i] = ((double)Convert.ToInt16(retValue[i], 16) / 32768).ToString("F4");
            }
            return retValue;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename2 = @"start.txt";

            this.Width = 1650;
            this.Height = 600;

            new Thread(new ThreadStart(() =>
            {
                this.Invoke(new MethodInvoker(() => { label1.Text = leftStatus ? "左聲道" : "右聲道"; }));
                List<double> list = new List<double>();
                StreamReader sr = new StreamReader(filename2, Encoding.Default);
                int m = 0;
                while (!sr.EndOfStream)
                {
                    if (leftStatus)
                    {
                        if (m % 2 == 0)
                            list.Add(double.Parse(sr.ReadLine()));
                    }
                    else
                    {
                        if (m % 2 != 0)
                            list.Add(double.Parse(sr.ReadLine()));
                    }
                    m++;
                }
                sr.Close();
                Bitmap bitmap = new Bitmap(pictureBox1.Width, pictureBox1.Height);
                Graphics g = Graphics.FromImage(bitmap);
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                g.DrawLine(new Pen(Color.Black, 5), new Point(20, 20), new Point(20, 540));
                g.DrawLine(new Pen(Color.Black, 5), new Point(20, 290), new Point(1600, 290));

                int k = list.Count / 1550;

                for (int i = 0; i < list.Count; i++)
                {
                    g.DrawLine(new Pen(Color.Green, 1), new Point(20 + i / k, 290), new Point(20 + i / k, 290 + (int)(list[i] * 250 * 2)));
                }
                this.pictureBox1.Image = bitmap;
            })).Start();
        }
    }
}

