using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_PNG
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            FileStream fs = File.OpenRead("ims-small-logo.png"); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            richTextBox1.Text += "len = 0x" + filelength.ToString("X6") + " = " + filelength.ToString() + "\n";

            filelength = 8;
            Byte[] w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取

            int i;

            for (i = 0; i < filelength; i++)
            {
                richTextBox1.Text += w[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";

            for (i = 1; i < 4; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];

            }
            richTextBox1.Text += "\n";

            filelength = 24;
            w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取
            fs.Close();

            for (i = 0; i < filelength; i++)
            {
                richTextBox1.Text += w[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }

            richTextBox1.Text += "\n";

            for (i = 4; i < 8; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];
            }
            richTextBox1.Text += "\n";

            int datasize;
            int width;
            int height;
            int bit_depth;
            int color_type;
            int compression_method;
            int filter_method;
            int interlace_method;

            for (i = 1; i < 4; i++)
            {
                //richTextBox1.Text += image[i].ToString("C");
                richTextBox1.Text += (char)w[i];
            }

            /*
            datasize = w[8] << 24 | w[9] << 16 | w[10] << 8 | w[11];
            width = w[16] << 24 | w[17] << 16 | w[18] << 8 | w[19];
            height = w[20] << 24 | w[21] << 16 | w[22] << 8 | w[23];
            bit_depth = w[24];
            color_type = w[25];
            compression_method = w[26];
            filter_method = w[27];
            interlace_method = w[28];
            */
            datasize = w[0] << 24 | w[1] << 16 | w[2] << 8 | w[3];
            width = w[8] << 24 | w[9] << 16 | w[10] << 8 | w[11];
            height = w[12] << 24 | w[13] << 16 | w[14] << 8 | w[15];
            bit_depth = w[16];
            color_type = w[17];
            compression_method = w[18];
            filter_method = w[19];
            interlace_method = w[20];

            richTextBox1.Text += "datasize : " + datasize.ToString() + "\n";
            richTextBox1.Text += "W : " + width.ToString() + "\n";
            richTextBox1.Text += "H : " + height.ToString() + "\n";
            richTextBox1.Text += "bit_depth : " + bit_depth.ToString() + "\n";
            richTextBox1.Text += "color_type : " + color_type.ToString() + "\n";
            richTextBox1.Text += "compression_method : " + compression_method.ToString() + "\n";
            richTextBox1.Text += "filter_method : " + filter_method.ToString() + "\n";
            richTextBox1.Text += "interlace_method : " + interlace_method.ToString() + "\n";


            //顯示圖片
            fs = File.OpenRead(@"C:\______test_vcs\ims-small-logo.png"); //OpenRead[二進位讀檔]
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = result;


            //讀前面256拜
            fs = File.OpenRead(@"C:\______test_vcs\ims-small-logo.png"); //OpenRead[二進位讀檔]

            filelength = 256;
            w = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(w, 0, filelength); //按位元組流讀取
            fs.Close();

            for (i = 0; i < filelength; i++)
            {
                //richTextBox1.Text += w[i].ToString("X2");

                if (((w[i] >= '0') && (w[i] <= '9')) || ((w[i] >= 'A') && (w[i] <= 'Z')) || ((w[i] >= 'a') && (w[i] <= 'z')))
                {
                    richTextBox1.Text += (char)w[i];
                }
                else
                    richTextBox1.Text += ".";

                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";
            }

            fs.Close();

        }
    }
}
