using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;

namespace vcs_test_all_04_Font2
{
    public partial class Form1 : Form
    {
        string sample_string = "流水落花春去也，天上人間。ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()";
        public Form1()
        {
            InitializeComponent();
        }

        // List the installed fonts.
        private void Form1_Load(object sender, EventArgs e)
        {
            // List the font families.
            InstalledFontCollection fonts = new InstalledFontCollection();
            foreach (FontFamily font_family in fonts.Families)
            {
                lstFonts.Items.Add(font_family.Name);
            }

            // Select the first font.
            lstFonts.SelectedIndex = 0;
        }

        // Display a sample of the selected font.
        private void ShowSample()
        {
            // Compose the font style.
            FontStyle font_style = FontStyle.Regular;
            if (chkBold.Checked) font_style |= FontStyle.Bold;
            if (chkItalic.Checked) font_style |= FontStyle.Italic;
            if (chkUnderline.Checked) font_style |= FontStyle.Underline;
            if (chkStrikeout.Checked) font_style |= FontStyle.Strikeout;

            // Get the font size.
            float font_size = 8;
            try
            {
                font_size = float.Parse(txtSize.Text);
            }
            catch
            {
            }

            // Get the font family name.
            string family_name = "Times New Roman";
            if (!(lstFonts.SelectedItem == null))
            {
                family_name = lstFonts.SelectedItem.ToString();
            }

            // Set the sample's font.
            richTextBox1.Font = new Font(family_name, font_size, font_style);
            richTextBox1.Text = "字型: " + family_name + Environment.NewLine + sample_string;
        }

        // If something changes, display a new sample of the selected font.
        // This event handler catches all of the events for controls
        // that influence the font's properties.
        private void SomethingChanged(object sender, EventArgs e)
        {
            ShowSample();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //指明使用特定字型檔
            //路徑             
            string path = @"../../font/金梅重黑浮體白字.ttf";
            //讀取字體文件             
            PrivateFontCollection pfc = new PrivateFontCollection();
            pfc.AddFontFile(path);
            //實例化字體             
            Font f = new Font(pfc.Families[0], 40);
            //設置字體            
            richTextBox1.Font = f;
        }
    }
}
