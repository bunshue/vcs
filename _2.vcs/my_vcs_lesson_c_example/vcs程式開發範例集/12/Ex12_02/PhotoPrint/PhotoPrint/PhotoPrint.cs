using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace PhotoPrint
{
    public partial class PhotoPrint : Form
    {
        public PhotoPrint()
        {
            InitializeComponent();
        }

        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            try
            {
                Bitmap bitmap = new Bitmap( "image.jpg");
                e.Graphics.DrawImage(bitmap, 150, 240, 350, 300);
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            printPreviewDialog1.Document = this.printDocument1;
            printPreviewDialog1.ShowDialog();
            printDocument1.Print();
        }

        private void printPreviewControl1_Click(object sender, EventArgs e)
        {

        }
    }
}