using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1fffff
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap image1;
            // Retrieve the image.
            image1 = new Bitmap("picture.bmp", true);

            int x, y;

            // Loop through the images pixels to reset color.
            for (x = 0; x < image1.Width; x++)
            {
                for (y = 0; y < image1.Height; y++)
                {
                    Color pixelColor = image1.GetPixel(x, y);
                    //Color newColor = Color.FromArgb(pixelColor.R, 0, 0);
                    //Color newColor = Color.FromArgb(0, pixelColor.G, 0);
                    Color newColor = Color.FromArgb(0, 0, pixelColor.B);
                    image1.SetPixel(x, y, newColor);
                }
            }

            // Set the PictureBox to display the image.
            pictureBox1.Image = image1;

            // Display the pixel format in Label1.
            richTextBox1.Text += "Pixel format: "+image1.PixelFormat.ToString() + "\n";
        


        }

        private void button2_Click(object sender, EventArgs e)
        {
            string str1 = "群曜醫電股份有限公司 Insight Medical Solutions Inc.";
            string str2 = string.Empty;
            str2 = str1.Substring(0, 4);    //從0取4
            richTextBox1.Text += "str2 = " + str2 + "\n";
            str2 = str1.Substring(4, 6);    //從4取6
            richTextBox1.Text += "str2 = " + str2 + "\n";
            str2 = str1.Substring(8, 10);   //從8取10
            richTextBox1.Text += "str2 = " + str2 + "\n";

            //char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };
            str1 = "中間路線";
            byte[] byteData = Encoding.Default.GetBytes(str1);
            foreach (byte b in byteData)
            {
                richTextBox1.Text += b.ToString("X2") + " ";


            }
            richTextBox1.Text += "\n";

            string nn = string.Empty;
            nn = Encoding.Default.GetString(byteData);
            richTextBox1.Text += "new string : " + nn + "\n";


            byteData[1] = (byte)(byteData[1] + 2);
            nn = Encoding.Default.GetString(byteData);
            richTextBox1.Text += "new string : " + nn + "\n";

            str1 = "专业知识中";
            byte[] byteData2 = Encoding.Default.GetBytes(str1);
            foreach (byte b in byteData2)
            {
                richTextBox1.Text += b.ToString("X2") + " ";


            }
            richTextBox1.Text += "\n";

        }
    }
}
