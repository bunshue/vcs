using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace ImageCopy
{
    public partial class Form1 : Form
    {
        string str;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.ShowDialog();
            str = openFileDialog1.FileName;
            Image myImage = System.Drawing.Image.FromFile(str);
            pictureBox1.Image = myImage;
            button2.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == string.Empty || textBox2.Text == string.Empty || textBox3.Text == string.Empty || textBox4.Text == string.Empty)
            {
                MessageBox.Show("請將要拷貝區域的資料填寫完整！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                textBox1.Focus();
            }
            else
            {
                Graphics graphics = this.CreateGraphics();
                Bitmap bitmap = new Bitmap(str);
                Rectangle rectangle = new Rectangle(Convert.ToInt32(textBox1.Text.Trim()), Convert.ToInt32(textBox2.Text.Trim()),
                    Convert.ToInt32(textBox3.Text.Trim()), Convert.ToInt32(textBox4.Text.Trim()));
                Bitmap cloneBitmap = bitmap.Clone(rectangle, PixelFormat.DontCare);
                pictureBox2.Image = cloneBitmap;
            }
        }
    }
}