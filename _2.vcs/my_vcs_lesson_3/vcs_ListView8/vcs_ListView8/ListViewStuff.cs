using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace vcs_ListView8
{
    public static class ListViewStuff
    {
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int GetScrollPos(IntPtr hWnd, int nBar);
        public const int SB_HORZ = 0;

        // Find and column at this position.
        // Return true if we are successful.
        // Return false if the mouse is not under a ListView cell.
        static public bool FindListViewRowColumn(this ListView lvw, int x, int y, out int row, out int column)
        {
            // Find the row under the mouse.
            for (int i = 0; i < lvw.Items.Count; i++)
            {
                if (lvw.Items[i].Bounds.Contains(x, y))
                {
                    row = i;

                    // See which column is under the mouse.
                    column = GetListViewColumn(lvw, x);
                    return true;
                }
            }

            row = column = -1;
            return false;
        }

        // Return the column under this X position.
        static public int GetListViewColumn(this ListView lvw, int x)
        {
            // Get the horizontal scroll bar's position.
            x += GetScrollPos(lvw.Handle, SB_HORZ);

            // Get the column headers in their current display order.
            List<ColumnHeader> headers = GetListViewColumnsInDisplayOrder(lvw);

            // Find the column that includes this X position.
            for (int i = 0; i < headers.Count; i++)
            {
                x -= headers[i].Width;
                if (x <= 0) return headers[i].Index;
            }

            return -1;
        }

        // Return the ListView's columns in their display order.
        static public List<ColumnHeader> GetListViewColumnsInDisplayOrder(this ListView lvw)
        {
            List<ColumnHeader> headers = new List<ColumnHeader>();

            // Find each of the headers in their display order.
            for (int i = 0; i < lvw.Columns.Count; i++)
            {
                // Find the column with display index i.
                for (int j = 0; j < lvw.Columns.Count; j++)
                {
                    if (lvw.Columns[j].DisplayIndex == i)
                    {
                        // This is the one. Add it to the list.
                        headers.Add(lvw.Columns[j]);
                        break;
                    }
                }
            }
            return headers;
        }

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
