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

namespace vcs_AnalysisArticle2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files1\__RW\_txt\article.txt";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        // List the words in the file.
        private void button1_Click(object sender, EventArgs e)
        {
            // Get the file's text.
            FileInfo file_info = new FileInfo(filename);
            string extension = file_info.Extension.ToLower();
            string txt;
            richTextBox1.Text += "plain text files\n";
            txt = File.ReadAllText(filename);

            richTextBox1.Text += "原資料\n" + txt + "\n";

            // Use regular expressions to replace characters
            // that are not letters or numbers with spaces.
            Regex reg_exp = new Regex("[^a-zA-Z0-9]");
            txt = reg_exp.Replace(txt, " ");

            richTextBox1.Text += "去標點符號後的資料\n" + txt + "\n";

            // Split the text into words.
            string[] words = txt.Split(
                new char[] { ' ' },
                StringSplitOptions.RemoveEmptyEntries);

            // Use LINQ to get the unique words.
            var word_query =
                (from string word in words
                 orderby word
                 select word).Distinct();

            // Display the result.
            string[] result = word_query.ToArray();

            richTextBox1.Text += "\n\n\n" + result.Length.ToString() + "\n";
            int len = result.Length;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + result[i] + "\n";


            }
            listBox1.DataSource = result;

            richTextBox1.Text += "\n共 " + result.Length.ToString() + " 字\n";
        }

    }
}
