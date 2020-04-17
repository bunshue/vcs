using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class SimpleEditor : Form
    {
        public SimpleEditor()
        {
            InitializeComponent();
        }

        private void mExit_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void SimpleEditor_Load(object sender, EventArgs e)
        {
            int y = menuStrip1.Size.Height;
            richTextBox1.Location = new Point(0, y);

            int width = this.ClientSize.Width;
            int height = this.ClientSize.Height - y;
            richTextBox1.Size = new Size(width, height);

        }

        private void SimpleEditor_Resize(object sender, EventArgs e)
        {
            int y = menuStrip1.Size.Height;
            richTextBox1.Location = new Point(0, y);

            int width = this.ClientSize.Width;
            int height = this.ClientSize.Height - y;
            richTextBox1.Size = new Size(width, height);
        }

        private void mSetting_Click(object sender, EventArgs e)
        {

        }

        private void mCopy_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionLength != 0)
                richTextBox1.Copy();
        }

        private void mPaste_Click(object sender, EventArgs e)
        {
            richTextBox1.Paste();
        }

        private void mCut_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionLength != 0)
                richTextBox1.Cut();
        }

        private void mUndo_Click(object sender, EventArgs e)
        {
            richTextBox1.Undo();
        }

        private void mSelectAll_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectAll();
        }

        private void mOpen_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if(openFileDialog1.FilterIndex == 1)
                    richTextBox1.LoadFile(openFileDialog1.FileName,
                        RichTextBoxStreamType.PlainText);
                else
                    richTextBox1.LoadFile(openFileDialog1.FileName,
                        RichTextBoxStreamType.RichText);
            }
        }

        private void mSave_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if(saveFileDialog1.FilterIndex == 1)
                    richTextBox1.SaveFile(saveFileDialog1.FileName,
                        RichTextBoxStreamType.PlainText);
                else
                    richTextBox1.SaveFile(saveFileDialog1.FileName,
                        RichTextBoxStreamType.RichText);
            }
        }

        private void mFont_Click(object sender, EventArgs e)
        {
            fontDialog1.Color = richTextBox1.ForeColor;
            fontDialog1.Font = richTextBox1.Font;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.SelectionColor = fontDialog1.Color;
            }
        }

        private void mColor_Click(object sender, EventArgs e)
        {
            colorDialog1.Color = richTextBox1.ForeColor;
            colorDialog1.AllowFullOpen = true;
            colorDialog1.FullOpen = true;            
            if (colorDialog1.ShowDialog() == DialogResult.OK)
                richTextBox1.SelectionColor = colorDialog1.Color;
        }
    }
}
