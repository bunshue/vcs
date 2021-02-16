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

namespace vcs_ReadWrite_WORD5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Make a Word document.
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
            para.Range.Text = "Chrysanthemum Curve";
            object style_name = "Heading 1";
            //para.Range.set_Style(ref style_name);
            para.Range.InsertParagraphAfter();

            // Add more text.
            para.Range.Text = "To make a chrysanthemum curve, use the following " +
                "parametric equations as t goes from 0 to 21 * π to generate " +
                "points and then connect them.";
            para.Range.InsertParagraphAfter();

            // Save the current font and start using Courier New.
            string old_font = para.Range.Font.Name;
            para.Range.Font.Name = "Courier New";

            // Add the equations.
            para.Range.Text =
                "  r = 5 * (1 + Sin(11 * t / 5)) -\n" +
                "      4 * Sin(17 * t / 3) ^ 4 *\n" +
                "      Sin(2 * Cos(3 * t) - 28 * t) ^ 8\n" +
                "  x = r * Cos(t)\n" +
                "  y = r * Sin(t)";

            // Start a new paragraph and then switch back to the original font.
            para.Range.InsertParagraphAfter();
            para.Range.Font.Name = old_font;

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
