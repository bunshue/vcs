using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace PrintFormData
{
    public partial class PrintFormData : Form
    {
        public PrintFormData()
        {
            InitializeComponent();
        }

        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            e.Graphics.DrawString(label1.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 260, 400);
            e.Graphics.DrawString(textBox1.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 330, 400);
            e.Graphics.DrawString(label2.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 270,420);
            e.Graphics.DrawString(textBox2.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 330, 420);
            e.Graphics.DrawString(label3.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 270, 440);
            e.Graphics.DrawString(textBox3.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 330, 440);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            printDialog1.ShowDialog();
            printPreviewDialog1.Document = this.printDocument1;
            printPreviewDialog1.ShowDialog();
        }
    }
}