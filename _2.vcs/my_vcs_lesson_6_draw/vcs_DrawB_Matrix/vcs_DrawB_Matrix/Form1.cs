using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;

namespace vcs_DrawB_Matrix
{
    public partial class Form1 : Form
    {
        // Some random values.
        private int[,] Values =
        {
            {1, 2, 3, 4, 5},
            {6, 7, 8, 9, 10},
            {11, 12, 13, 14, 15},
            {16, 17, 18, 19, 20},
        };

        public Form1()
        {
            InitializeComponent();
        }

        // Randomize.
        private void button1_Click(object sender, EventArgs e)
        {
            Values.Randomize();
            Refresh();
        }

        // Draw the values.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int num_rows = Values.GetUpperBound(0) + 1;
            int num_cols = Values.GetUpperBound(1) + 1;
            int col_wid = this.ClientSize.Width / num_cols;
            int row_hgt =
                (this.ClientSize.Height - button1.Bottom) / num_rows;

            e.Graphics.TextRenderingHint =
                TextRenderingHint.AntiAliasGridFit;
            using (Font the_font = new Font("Times New Roman", 20))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    int y = button1.Bottom;
                    for (int row = 0; row < num_rows; row++)
                    {
                        int x = 0;
                        for (int col = 0; col < num_cols; col++)
                        {
                            Rectangle rect = new Rectangle(
                                x, y, col_wid, row_hgt);
                            e.Graphics.DrawString(Values[row, col].ToString(),
                                the_font, Brushes.Blue, rect, string_format);
                            x += col_wid;
                        }
                        y += row_hgt;
                    }
                }
            }
        }
    }
}
