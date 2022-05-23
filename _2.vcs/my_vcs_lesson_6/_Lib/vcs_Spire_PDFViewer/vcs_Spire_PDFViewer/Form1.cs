using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

using Spire.PdfViewer.Forms;

namespace vcs_Spire_PDFViewer
{
    public partial class Form1 : Form
    {

        private static PdfDocumentViewer viewer = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_pdf\note_Linux_workstation.pdf";

            Form f2 = new Form2(filename);
            f2.Show();
        }
    }
}
