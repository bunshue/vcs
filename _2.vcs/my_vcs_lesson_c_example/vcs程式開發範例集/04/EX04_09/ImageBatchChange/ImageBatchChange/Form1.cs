using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;
using System.IO;

namespace ImageBatchChange
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.Title = "打開圖片文件";
            openFileDialog1.Multiselect = false;
            openFileDialog1.ShowDialog();
            listBox1.Items.Add(openFileDialog1.FileName);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (comboBox1.SelectedItem == null)
            {
                return;
            }
            else
            {
                for (int i = 0; i < listBox1.Items.Count; i++)
                {
                    Bitmap bitmap = new Bitmap(listBox1.Items[i].ToString());
                    string fileName = listBox1.Items[i].ToString().Substring(0, listBox1.Items[i].ToString().LastIndexOf("\\") + 1) 
                        + listBox1.Items[i].ToString().Substring(listBox1.Items[i].ToString().LastIndexOf("\\") + 1, 
                        listBox1.Items[i].ToString().LastIndexOf(".") - listBox1.Items[i].ToString().LastIndexOf("\\") - 1);
                    switch (comboBox1.Text)
                    {
                        case "*.bmp":
                            bitmap.Save(fileName + ".bmp", ImageFormat.Bmp);
                            break;
                        case "*.jpg":
                            bitmap.Save(fileName + ".jpg", ImageFormat.Jpeg);
                            break;
                        case "*.gif":
                            bitmap.Save(fileName + ".gif", ImageFormat.Gif);
                            break;
                        case "*.tif":
                            bitmap.Save(fileName + ".tif", ImageFormat.Tiff);
                            break;
                        case "*.png":
                            bitmap.Save(fileName + ".png", ImageFormat.Png);
                            break;
                        case "*.wmf":
                            bitmap.Save(fileName + ".wmf", ImageFormat.Wmf);
                            break;
                    }
                }
                MessageBox.Show("轉換完成", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }
}