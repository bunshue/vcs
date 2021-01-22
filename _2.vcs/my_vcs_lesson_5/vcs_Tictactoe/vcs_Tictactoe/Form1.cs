using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Tictactoe
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Make an array to hold the Labels.
        private const int NumRows = 3;
        private const int NumCols = 3;
        private Label[,] Squares = new Label[NumRows, NumCols];

        // Build the Label controls.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Make a TableLayoutPanel.
            TableLayoutPanel tlpBoard =
                new TableLayoutPanel();
            tlpBoard.Anchor =
                AnchorStyles.Top |
                AnchorStyles.Bottom |
                AnchorStyles.Left |
                AnchorStyles.Right;
            tlpBoard.Location = new Point(10, 10);
            tlpBoard.Size = new Size(
                ClientSize.Width - 20,
                ClientSize.Height - 20);
            Controls.Add(tlpBoard);

            // Make the TableLayoutPanel rows and columns.
            tlpBoard.RowCount = NumRows + 1;
            tlpBoard.ColumnCount = NumCols;

            // Give the first row a fixed height.
            tlpBoard.RowStyles.Clear();
            tlpBoard.RowStyles.Add(new RowStyle(SizeType.Absolute, 30));

            // Give the other rows and columns the same percent size.
            for (int row = 0; row < NumRows; row++)
                tlpBoard.RowStyles.Add(
                    new RowStyle(SizeType.Percent, 1));

            tlpBoard.ColumnStyles.Clear();
            for (int col = 0; col < NumCols; col++)
                tlpBoard.ColumnStyles.Add(
                    new ColumnStyle(SizeType.Percent, 1));

            // Make a Clear button.
            Button btn = new Button();
            btn.Text = "Clear";
            btn.Click += btnClear_Click;
            btn.Dock = DockStyle.Fill;
            tlpBoard.SetRow(btn, 0);
            tlpBoard.SetColumn(btn, NumCols / 2);
            tlpBoard.Controls.Add(btn);

            // Make a big font.
            Font square_font = new Font("Times New Roman", 40);

            // Add Labels.
            for (int row = 0; row < NumCols; row++)
                for (int col = 0; col < NumCols; col++)
                {
                    // Create the Label.
                    Label lbl = new Label();
                    lbl.Margin = new Padding(0);
                    lbl.Dock = DockStyle.Fill;
                    lbl.TextAlign = ContentAlignment.MiddleCenter;
                    lbl.Font = square_font;
                    lbl.BorderStyle = BorderStyle.FixedSingle;
                    Squares[row, col] = lbl;
                    tlpBoard.Controls.Add(lbl);

                    // Set its row and column.
                    tlpBoard.SetRow(lbl, row + 1);
                    tlpBoard.SetColumn(lbl, col);

                    // Hook up a Click event handler.
                    lbl.Click += square_Click;
                }
        }

        // The user clicked a square.
        private void square_Click(object sender, EventArgs e)
        {
            Label lbl = sender as Label;
            if (lbl.Text == "X") lbl.Text = "O";
            else lbl.Text = "X";
        }

        // Clear the labels.
        private void btnClear_Click(object sender, EventArgs e)
        {
            foreach (Label lbl in Squares) lbl.Text = "";
            //for (int row = 0; row < NumRows; row++)
            //    for (int col = 0; col < NumCols; col++)
            //        Squares[row, col].Text = "";
        }
    }
}