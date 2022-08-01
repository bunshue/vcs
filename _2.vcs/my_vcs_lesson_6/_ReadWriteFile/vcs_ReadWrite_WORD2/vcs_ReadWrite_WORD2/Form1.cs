using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

// Open the Add References dialog. On the COM tab, select
// "Microsoft Word 12.0 Object Library" (or whatever version you
// have installed on your system). 

using Word = Microsoft.Office.Interop.Word;
using Core = Microsoft.Office.Core;

namespace vcs_ReadWrite_WORD2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Initialize the paths.
        private void Form1_Load(object sender, EventArgs e)
        {
            txtPicture.Text = Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..")) +"\\test.png";
        }

        // Add the text and picture to the Word document.
        private void btnGo_Click(object sender, EventArgs e)
        {
            // Get the Word application object.
            Word._Application word_app = new Word.ApplicationClass();

            // Make Word visible (optional).
            word_app.Visible = true;

            // Create the Word document.
            object missing = Type.Missing;
            Word._Document word_doc = word_app.Documents.Add(ref missing, ref missing,
                ref missing, ref missing);

            // Create a header paragraph.
            Word.Paragraph para = word_doc.Paragraphs.Add(ref missing);
            para.Range.Text = "Lorem Ipsum";
            object style_name = "Heading 1";
            //para.Range.set_Style(ref style_name);
            para.Range.InsertParagraphAfter();

            // Add some paragraphs.
            string[] paragraphs =
            {
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tristique id ex ac mollis. Maecenas vestibulum porta arcu ac dictum. Praesent placerat hendrerit dui eu porttitor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Phasellus vitae dui sit amet ligula feugiat accumsan in sit amet tellus. Duis lobortis justo nec lobortis tempor. Nunc sagittis egestas dolor, sit amet iaculis massa sagittis eu. Quisque et turpis a massa tincidunt pharetra non pretium felis. Morbi fringilla sapien eu ex interdum hendrerit non facilisis lacus. Donec fermentum eros ut lectus consectetur, at accumsan nunc dignissim. Etiam varius iaculis vestibulum. Sed id condimentum neque, quis efficitur elit.",
                "Nam lacinia, risus ac ullamcorper commodo, ex diam mollis augue, ac dictum lacus est quis enim. Praesent vestibulum lorem id sem aliquet finibus. Etiam elementum tempor hendrerit. Mauris id interdum sapien. Vestibulum id viverra velit, ut mollis libero. Pellentesque orci lacus, facilisis vitae laoreet nec, molestie non urna. Fusce interdum dolor in varius luctus. Praesent sit amet malesuada libero. Ut rutrum diam eget erat iaculis vulputate.",
                "Nunc nec leo congue, facilisis tellus et, dignissim arcu. Vivamus vehicula congue consequat. Aliquam erat volutpat. In at porta lectus, nec feugiat tortor. Suspendisse vitae pellentesque magna. Phasellus fermentum est ut mauris tincidunt, ac luctus nisi fermentum. Sed gravida blandit est. Phasellus egestas lorem at lacus dapibus semper. Vestibulum sodales rhoncus diam, vel semper nisl ultrices malesuada. Suspendisse mattis arcu nunc, quis ullamcorper turpis facilisis ut.",
                "Vivamus interdum diam id dictum consectetur. Ut nisi nisl, tincidunt in massa sit amet, sollicitudin accumsan ipsum. Sed leo eros, aliquet a augue non, placerat hendrerit tellus. Fusce sodales est vel libero efficitur, id ultricies nisl pharetra. Suspendisse orci dui, placerat nec sapien ut, aliquet venenatis diam. Cras at leo ante. Fusce ut orci nisl. Nulla vehicula eget tortor sit amet interdum. Ut sagittis tellus risus, et convallis est gravida vitae. Donec fringilla lorem et arcu feugiat mattis.",
                "Vestibulum euismod mauris eget velit iaculis, vel aliquam ex accumsan. Donec ante urna, bibendum mollis ipsum vitae, luctus pulvinar neque. In ullamcorper leo id volutpat suscipit. Morbi ex mauris, commodo at leo quis, ultricies fermentum magna. Sed odio justo, pharetra a malesuada eget, ullamcorper eu lorem. Suspendisse lacinia augue neque, at fringilla ipsum imperdiet nec. Nulla sapien orci, faucibus non iaculis vel, porta vitae dui. Aenean at imperdiet mauris.",
            };

            // Add more text.
            foreach (string paragraph in paragraphs)
            {
                para.Range.Text = paragraph;
                para.Range.InsertParagraphAfter();
            }

            // Find the beginning of the document.
            // For other pre-defined bookmarks, see:
            //      http://support.microsoft.com/kb/212555
            object start_of_doc = "\\startofdoc";

            // Get a Range at the start of the document.
            Word.Range start_range = word_doc.Bookmarks.get_Item(ref start_of_doc).Range;

            // Add the picture to the Range's InlineShapes.
            string picture_file = txtPicture.Text;
            Word.InlineShape inline_shape = start_range.InlineShapes.AddPicture(
                picture_file, ref missing, ref missing, ref missing);

            // Format the picture.
            Word.Shape shape = inline_shape.ConvertToShape();

            // Scale uniformly by 50%.
            shape.LockAspectRatio = Core.MsoTriState.msoTrue;
            shape.ScaleHeight(0.5f, Core.MsoTriState.msoTrue,
                Core.MsoScaleFrom.msoScaleFromTopLeft);

            // Wrap text around the picture's square.
            shape.WrapFormat.Type = Word.WdWrapType.wdWrapSquare;

            // Align the picture on the upper right.
            shape.Left = (float)Word.WdShapePosition.wdShapeRight;
            shape.Top = (float)Word.WdShapePosition.wdShapeTop;

            // Save the document.
            object filename = Application.StartupPath + "\\word_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".doc";

            word_doc.SaveAs(ref filename, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing);

            // Close.
            object save_changes = false;
            word_doc.Close(ref save_changes, ref missing, ref missing);
            word_app.Quit(ref save_changes, ref missing, ref missing);

            richTextBox1.Text += "建立Word檔案完成\t檔名 : " + filename + "\n";
        }
    }
}
