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

using Spire.Pdf;
using Spire.Pdf.Graphics;
using Spire.Pdf.Annotations;

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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";

            Form f2 = new Form2(filename);
            f2.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //1. 新建一個PDF文檔對象，再添加一個新頁面。
            PdfDocument doc = new PdfDocument();

            PdfPageBase page = doc.Pages.Add();

            //2. 文檔中添加文本，並設置文本的位置、字體大小、顏色。
            PdfFont font = new PdfFont(PdfFontFamily.Helvetica, 13);

            string text = "HelloWorld";

            PointF point = new PointF(200, 100);

            page.Canvas.DrawString(text, font, PdfBrushes.Red, point);

            //3. 給文本添加注釋，並設置注釋的邊框、顏色及位置。

            PdfTextMarkupAnnotation annotation1 = new PdfTextMarkupAnnotation("管理員", "一般來說，這是每一種計算機編程語言中最基本、最簡單的程序", text, new PointF(0, 0), font);

            annotation1.Border = new PdfAnnotationBorder(0.75f);

            annotation1.TextMarkupColor = Color.Green;

            annotation1.Location = new PointF(point.X + doc.PageSettings.Margins.Left, point.Y + doc.PageSettings.Margins.Left);

            //4. 將注釋添加到頁面，最後保存文檔。

            (page as PdfNewPage).Annotations.Add(annotation1);

            doc.SaveToFile("result.pdf");

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //給pdf檔添加自由文本注釋

            //1. 新建一個PDF文檔對象，並添加一個新頁面。

            PdfDocument doc = new PdfDocument();

            PdfPageBase page = doc.Pages.Add();

            //2. 初始化一個PdfFreeTextAnnotation，然後自定義注釋的文本。

            RectangleF rect = new RectangleF(0, 40, 150, 50);

            PdfFreeTextAnnotation textAnnotation = new PdfFreeTextAnnotation(rect);

            textAnnotation.Text = "Free text annotation ";

            //3. 設置注釋的屬性，包括字體、填充顏色、邊框顏色和透明度。

            PdfFont font = new PdfFont(PdfFontFamily.TimesRoman, 10);

            PdfAnnotationBorder border = new PdfAnnotationBorder(1f);

            textAnnotation.Font = font;

            textAnnotation.Border = border;

            textAnnotation.BorderColor = Color.Purple;

            textAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle;

            textAnnotation.Color = Color.Pink;

            textAnnotation.Opacity = 0.8f;

            //4. 添加注釋到頁面。

            page.AnnotationsWidget.Add(textAnnotation);

            //5. 保存

            doc.SaveToFile("FreeTextAnnotation.pdf", FileFormat.PDF);

            //System.Diagnostics.Process.Start("FreeTextAnnotation.pdf");
        }
    }
}

