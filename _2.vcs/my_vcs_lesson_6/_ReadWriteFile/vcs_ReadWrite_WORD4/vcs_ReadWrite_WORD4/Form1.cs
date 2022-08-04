using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Text.RegularExpressions;
using Word = Microsoft.Office.Interop.Word;

namespace vcs_ReadWrite_WORD4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\Step.doc";
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\bmp_format.docx";

            richTextBox1.Text += "讀取檔案 : " + filename + " ...\n";
            string txt = GrabWordFileWords(filename);
            richTextBox1.Text += txt + "\n";
            richTextBox1.Text += "完成\n";
        }

        // Read the text contents of a Word file.
        private string GrabWordFileWords(string file_name)
        {
            // Get the Word application object.
            Word._Application word_app = new Word.ApplicationClass();

            // Make Word visible (optional).
            word_app.Visible = false;

            // Open the file.
            object filename = file_name;
            object confirm_conversions = false;
            object read_only = true;
            object add_to_recent_files = false;
            object format = 0;
            object missing = System.Reflection.Missing.Value;

            Word._Document word_doc =
                word_app.Documents.Open(ref filename, ref confirm_conversions,
                    ref read_only, ref add_to_recent_files,
                    ref missing, ref missing, ref missing, ref missing,
                    ref missing, ref format, ref missing, ref missing,
                    ref missing, ref missing, ref missing, ref missing);

            // Return the document's text.
            string result = word_doc.Content.Text;

            //richTextBox1.Text += result + "\n";

            // Close the document without prompting.
            object save_changes = false;
            word_doc.Close(ref save_changes, ref missing, ref missing);
            word_app.Quit(ref save_changes, ref missing, ref missing);

            // Return the result.
            return result;
        }


    }
}
