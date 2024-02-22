using System;

using System.Windows.Forms;
using System.Collections;

namespace vcs_ListView1
{
    // Compares two ListView items using all of their columns.
    public class ListViewAllColumnComparer : IComparer
    {
        private SortOrder SortOrder;

        public ListViewAllColumnComparer(SortOrder sort_order)
        {
            SortOrder = sort_order;
        }

        // Compare two ListViewItems.
        public int Compare(object object_x, object object_y)
        {
            // Get the objects as ListViewItems.
            ListViewItem item_x = object_x as ListViewItem;
            ListViewItem item_y = object_y as ListViewItem;

            // Loop through the sub-items.
            for (int i = 0; i < item_x.SubItems.Count; i++)
            {
                // If item_y is out of sub-items,
                // then it comes first.
                if (item_y.SubItems.Count <= i) return 1;

                // Get the sub-items.
                string string_x = item_x.SubItems[i].Text;
                string string_y = item_y.SubItems[i].Text;

                // Compare them.
                int result = CompareValues(string_x, string_y);

                if (result != 0) return result;
            }

            // If we get here, we have an exact match.
            return 0;
        }

        // Compare two items. If they look like
        // numbers or dates, compare them as such.
        private int CompareValues(string string_x, string string_y)
        {
            // Compare them.
            int result;
            double double_x, double_y;
            if (double.TryParse(string_x, out double_x) &&
                double.TryParse(string_y, out double_y))
            {
                // Treat as a number.
                result = double_x.CompareTo(double_y);
            }
            else
            {
                DateTime date_x, date_y;
                if (DateTime.TryParse(string_x, out date_x) &&
                    DateTime.TryParse(string_y, out date_y))
                {
                    // Treat as a date.
                    result = date_x.CompareTo(date_y);
                }
                else
                {
                    // Treat as a string.
                    result = string_x.CompareTo(string_y);
                }
            }

            // Return the correct result depending on whether
            // we're sorting ascending or descending.
            if (SortOrder == SortOrder.Ascending)
            {
                return result;
            }
            else
            {
                return -result;
            }
        }
    }
}
