using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

namespace vcs_ReadWrite_BMP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int ww = 256;
            int hh = 300;
            int size = ww * hh * 4 + 0x36;
            int h_res = 0x0EC4;
            int v_res = 0x0EC4;

            byte[] data = new byte[size];

            for (i = 0; i < size; i++)
            {
                data[i] = 0;
            }
            data[0] = (byte)'B';
            data[1] = (byte)'M';
            data[2] = (byte)(size % 256);
            data[3] = (byte)((size / 256) % 256);
            data[4] = (byte)((size / 256 / 256) % 256);
            data[5] = (byte)((size / 256 / 256) % 256);
            data[10] = 0x36;
            data[14] = 0x28;

            data[18] = (byte)(ww % 256);
            data[19] = (byte)((ww / 256) % 256);
            data[20] = (byte)((ww / 256 / 256) % 256);
            data[21] = (byte)((ww / 256 / 256) % 256);

            data[22] = (byte)(hh % 256);
            data[23] = (byte)((hh / 256) % 256);
            data[24] = (byte)((hh / 256 / 256) % 256);
            data[25] = (byte)((hh / 256 / 256) % 256);

            data[26] = 0x01;
            data[28] = 0x20;

            data[38] = (byte)(h_res % 256);
            data[39] = (byte)((h_res / 256) % 256);
            data[40] = (byte)((h_res / 256 / 256) % 256);
            data[41] = (byte)((h_res / 256 / 256) % 256);

            data[42] = (byte)(v_res % 256);
            data[43] = (byte)((v_res / 256) % 256);
            data[44] = (byte)((v_res / 256 / 256) % 256);
            data[45] = (byte)((v_res / 256 / 256) % 256);

            for (j = 0; j < hh; j++)
            {
                for (i = 0; i < ww; i++)
                {
                    if (j < hh / 20)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0xCC;    //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0xBB;    //G
                        data[54 + ww * 4 * j + i * 4 + 2] = 0xAA;    //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;       //A
                    }
                    else if (j < hh / 10)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = (byte)i;    //B
                        data[54 + ww * 4 * j + i * 4 + 1] = (byte)i;    //G
                        data[54 + ww * 4 * j + i * 4 + 2] = (byte)i;    //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;       //A
                    }
                    else if (j < hh / 3)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;   //B
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;   //G
                        data[54 + ww * 4 * j + i * 4 + 2] = (byte)i;   //R
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;   //A
                    }
                    else if (j < hh / 3 * 2)
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = 0;
                        data[54 + ww * 4 * j + i * 4 + 1] = (byte)i;
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;
                    }
                    else
                    {
                        data[54 + ww * 4 * j + i * 4 + 0] = (byte)i;
                        data[54 + ww * 4 * j + i * 4 + 1] = 0;
                        data[54 + ww * 4 * j + i * 4 + 2] = 0;
                        data[54 + ww * 4 * j + i * 4 + 3] = 0xFF;
                    }
                }
            }

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "寫成檔案" + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__RW\\_bmp\\ims_image.bmp";

            //讀取資料
            byte[] data = File.ReadAllBytes(filename);
            richTextBox1.Text += "讀取檔案" + filename + "\t";
            richTextBox1.Text += "len = " + data.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */
            int i;
            for (i = 0; i < 0x36; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if ((i % 32) == 31)
                {
                    richTextBox1.Text += "\n";
                }
                else if ((i % 4) == 3)
                {
                    richTextBox1.Text += "  ";
                }
            }
            richTextBox1.Text += "\n";

            int ww;
            int hh;
            int size;// = ww * hh * 4 + 0x36;
            int h_res;  // = 0x0EC4;
            int v_res;  // = 0x0EC4;

            if ((data[0] != 'B')||(data[1] != 'M'))
            {
                richTextBox1.Text += "非BMP檔";
                    return;
            }

            size = data[2] + data[3] * 256 + data[4] * 256 * 256 + data[5] * 256 * 256 * 256;

            //data[10] = 0x36;
            //data[14] = 0x28;

            ww = data[18] + data[19] * 256 + data[20] * 256 * 256 + data[21] * 256 * 256 * 256;
            hh = data[22] + data[23] * 256 + data[24] * 256 * 256 + data[25] * 256 * 256 * 256;

            //data[26] = 0x01;
            //data[28] = 0x20;

            h_res = data[38] + data[39] * 256 + data[40] * 256 * 256 + data[41] * 256 * 256 * 256;
            v_res = data[42] + data[43] * 256 + data[44] * 256 * 256 + data[45] * 256 * 256 * 256;

            richTextBox1.Text += "ww = " + ww.ToString() + " hh = " + hh.ToString() + "\n";

            Image img = Image.FromFile(filename);

            richTextBox1.Text += "W : " + img.Width.ToString() + "\n";
            richTextBox1.Text += "H : " + img.Height.ToString() + "\n";
            richTextBox1.Text += "size : " + img.Size.Width.ToString() + " X " + img.Size.Height.ToString() + "\n";
            richTextBox1.Text += "P W : " + img.PhysicalDimension.Width.ToString() + "\n";
            richTextBox1.Text += "P H : " + img.PhysicalDimension.Height.ToString() + "\n";
            pictureBox1.Image = img;
        }
    }
}
