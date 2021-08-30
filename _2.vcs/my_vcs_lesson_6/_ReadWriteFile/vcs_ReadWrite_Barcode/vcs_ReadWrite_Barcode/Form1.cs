using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using NBarCodes;

namespace vcs_ReadWrite_Barcode
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //產生Code128
            NBarCodes.BarCodeSettings bs = new BarCodeSettings();
            bs.Type = BarCodeType.Code128;
            bs.Data = "4710085221226";

            BarCodeGenerator generator = new BarCodeGenerator(bs);
            Image image = generator.GenerateImage();
            pictureBox1.Image = image;
       }
    }
}
