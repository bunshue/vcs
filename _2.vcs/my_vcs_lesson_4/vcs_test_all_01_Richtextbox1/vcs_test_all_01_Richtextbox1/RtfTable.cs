using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_01_Richtextbox1
{
    public class RtfTable
    {
        public int InternalMargin = 180;
        public int NumRows, NumCols;
        public int[] ColumnWidths = null;
        public string[,] Contents = null;

        public RtfTable(int num_rows, int num_cols, int internal_margin)
        {
            NumRows = num_rows;
            NumCols = num_cols;
            InternalMargin = internal_margin;
            ColumnWidths = Enumerable.Repeat(1440, NumCols).ToArray();

            Contents = new string[NumRows, NumCols];
            for (int r = 0; r < NumRows; r++)
                for (int c = 0; c < NumCols; c++)
                    Contents[r, c] = "";
        }

        public void SetColumnWidths(params int[] widths)
        {
            for (int c = 0; c < NumCols; c++)
                ColumnWidths[c] = widths[c];
        }

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            string column_widths_string = ColumnWidthsString();

            for (int r = 0; r < NumRows; r++)
            {
                // Start the row.
                sb.Append(@"\trowd");
                sb.Append(@"\trgaph" + InternalMargin.ToString());

                // Column widths.
                sb.Append(column_widths_string);

                // Column contents.
                for (int c = 0; c < NumCols; c++)
                {
                    sb.Append(@"\pard\intbl{" +
                        Contents[r, c].Replace(@"\", @"\\") +
                        @"}\cell");
                }

                // End the row.
                sb.Append(@"\row");
            }
            return sb.ToString();
        }

        private string ColumnWidthsString()
        {
            StringBuilder sb = new StringBuilder();
            int total = 0;
            for (int c = 0; c < NumCols; c++)
            {
                total += ColumnWidths[c];
                sb.Append(@"\cellx" + total.ToString());
            }
            return sb.ToString();
        }
    }
}
