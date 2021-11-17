using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;

namespace vcs_ListViewB
{
    public static class ListViewExtensions
    {
        // Add the items as a new row in the ListView control.
        public static void AddRow(this ListView lvw, params string[] items)
        {
            // Make the main item.
            ListViewItem new_item = lvw.Items.Add(items[0]);

            // Make the sub-items.
            for (int i = 1; i < items.Length; i++)
                new_item.SubItems.Add(items[i]);
        }

        // Make the ListView's column headers.
        // The ParamArray entries should alternate between
        // strings and HorizontalAlignment values.
        public static void MakeColumnHeaders(this ListView lvw,
            params object[] header_info)
        {
            if (header_info.Length % 2 != 0)
                throw new ArgumentException(
                    "The method must have an even number " +
                    "of header_info parameters");

            // Remove any existing headers.
            lvw.Columns.Clear();

            // Make the column headers.
            for (int i = 0; i < header_info.Length; i += 2)
            {
                lvw.Columns.Add(
                    (string)header_info[i],
                    -1,
                    (HorizontalAlignment)header_info[i + 1]);
            }
        }

        // Set all columns' sizes.
        public static void SizeColumns(this ListView lvw, int size)
        {
            for (int i = 0; i < lvw.Columns.Count; i++)
                lvw.Columns[i].Width = -2;
        }
    }
}
