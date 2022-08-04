using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

// Add a reference to Microsoft Word 14.0 Object Library.
using Word = Microsoft.Office.Interop.Word;

namespace vcs_ReadWrite_WORD1
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

        // Remove the document's hyperlinks
        private void btnRemoveHyperlinks_Click(object sender, EventArgs e)
        {
            string doc_filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\vcs_ReadWrite_WORD1.docx";

            richTextBox1.Text += "開啟檔案 : " + doc_filename + "\n";

            Refresh();

            // Get the Word application object.
            Word._Application word_app = new Word.Application();

            // Make Word visible (optional).
            word_app.Visible = true;

            // Open the Word document.
            object missing = Type.Missing;
            object filename = doc_filename;
            object confirm_conversions = false;
            object read_only = false;
            object add_to_recent_files = false;
            object format = 0;
            Word._Document word_doc =
                word_app.Documents.Open(ref filename, ref confirm_conversions,
                    ref read_only, ref add_to_recent_files,
                    ref missing, ref missing, ref missing, ref missing,
                    ref missing, ref format, ref missing, ref missing,
                    ref missing, ref missing, ref missing, ref missing);

            // Remove the hyperlinks.
            object index = 1;
            while (word_doc.Hyperlinks.Count > 0)
            {
                word_doc.Hyperlinks.get_Item(ref index).Delete();
            }

            // Save and close the document without prompting.
            object save_changes = true;
            word_doc.Close(ref save_changes, ref missing, ref missing);

            // Close the word application.
            word_app.Quit(ref save_changes, ref missing, ref missing);

            richTextBox1.Text += "完成\n";
        }

        private void btnGo_Click(object sender, EventArgs e)
        {

        }
    }
}


