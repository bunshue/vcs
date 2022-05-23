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
    public partial class Form2 : Form
    {
        string filename = string.Empty;
        private static PdfDocumentViewer viewer = null;

        public Form2(string pdf_filename)
        {
            InitializeComponent();

            filename = pdf_filename;
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            viewer = new PdfDocumentViewer();
            viewer.LoadFromFile(filename);

            this.Text = filename;
            this.Size = new System.Drawing.Size(1000, 800);
            this.StartPosition = FormStartPosition.CenterScreen;

            TableLayoutPanel table = new TableLayoutPanel();
            table.ColumnCount = 3;
            table.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));
            table.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 20));
            table.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));
            table.RowCount = 2;
            table.RowStyles.Add(new RowStyle(SizeType.Percent, 100));
            table.RowStyles.Add(new RowStyle(SizeType.Absolute, 30));

            table.Controls.Add(viewer, 0, 0);
            table.SetColumnSpan(viewer, 3);
            viewer.Dock = DockStyle.Fill;

            //Export current page to one image
            Button button = new Button();
            button.Text = "Export to one image";
            button.Size = new Size(180, 24);
            button.TextAlign = ContentAlignment.MiddleCenter;
            table.Controls.Add(button, 0, 1);
            button.Dock = DockStyle.Right;
            button.Click += ExportToOneImage;

            //Export current pdf document to multiple images
            button = new Button();
            button.Text = "Export to multiple images";
            button.Size = new Size(180, 24);
            button.TextAlign = ContentAlignment.MiddleCenter;
            table.Controls.Add(button, 2, 1);
            button.Dock = DockStyle.Left;
            button.Click += ExportToMultipleImages;

            this.Controls.Add(table);
            table.Dock = DockStyle.Fill;

            //f2.Show();
        }

        private static void ExportToOneImage(object sender, EventArgs e)
        {
            if (viewer.PageCount > 0)
            {
                SaveFileDialog dialog = new SaveFileDialog();
                dialog.Filter = "PNG Format(*.png)|*.png";
                if (dialog.ShowDialog() == DialogResult.OK)
                {
                    int currentPage = viewer.CurrentPageNumber;
                    Bitmap image = (Bitmap)viewer.SaveAsImage(currentPage - 1);
                    image.Save(dialog.FileName);
                }
            }
        }

        private static void ExportToMultipleImages(object sender, EventArgs e)
        {
            if (viewer.PageCount > 0)
            {
                FolderBrowserDialog dialog = new FolderBrowserDialog();
                if (dialog.ShowDialog() == DialogResult.OK)
                {
                    int currentPage = viewer.CurrentPageNumber;
                    Bitmap[] images = (Bitmap[])viewer.SaveAsImage(0, currentPage - 1);
                    for (int i = 0; i < images.Length; i++)
                    {
                        String fileName = Path.Combine(dialog.SelectedPath, String.Format("PDFViewer-{0}.png", i));
                        images[i].Save(fileName);
                    }
                }
            }
        }
    }
}

