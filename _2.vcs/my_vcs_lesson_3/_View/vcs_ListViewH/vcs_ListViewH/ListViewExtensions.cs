using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;

namespace vcs_ListViewH
{
    public static class ListViewExtensions
    {
        // Make a ListView row.
        public static void AddRow(this ListView lvw, params string[] values)
        {
            // Make the item.
            ListViewItem new_item = lvw.Items.Add(values[0]);

            // Make the sub-items.
            for (int i = 1; i < values.Length; i++)
            {
                new_item.SubItems.Add(values[i]);
            }
        }

        // Make the ListView's column headers.
        // The params entries should alternate between
        // strings and HorizontalAlignment values.
        public static void SetColumnHeaders(this ListView lvw, params object[] header_info)
        {
            // Remove any existing headers.
            lvw.Columns.Clear();

            // Make the column headers.
            for (int i = header_info.GetLowerBound(0); i <= header_info.GetUpperBound(0); i += 2)
            {
                lvw.Columns.Add(
                    (string)header_info[i],
                    -1,
                    (HorizontalAlignment)header_info[i + 1]);
            }
        }

        // Set the ListView's column sizes to the same value.
        public static void SetColumnSizes(this ListView lvw, int width)
        {
            foreach (ColumnHeader col in lvw.Columns)
            {
                col.Width = width;
            }
        }

        // Size the columns to fit their data.
        public static void SizeColumnsToFitData(this ListView lvw)
        {
            SetColumnSizes(lvw, -1);
        }

        // Size the columns to fit their data and headers.
        public static void SizeColumnsToFitDataAndHeaders(this ListView lvw)
        {
            SetColumnSizes(lvw, -2);
        }

        // Prepare the ListView for column sorting.
        public enum SortMode
        {
            SortNone,
            SortOnClickedColumn,
            SortOnAllColumns
        }
        public static void SetSortMode(this ListView lvw, SortMode sort_mode)
        {
            // Get the current sort mode.
            SortMode old_sort_mode =
                (SortMode)lvw.GetValue("ListViewSortMode", SortMode.SortNone);

            // If the sort mode isn't changing, do nothing.
            if (sort_mode == old_sort_mode) return;

            // See what the current sorting mode is.
            if (old_sort_mode == SortMode.SortOnClickedColumn)
            {
                // Stop sorting on clicked columns.
                ListViewSortManager SortManager =
                    (ListViewSortManager)lvw.GetValue("ListViewSortManager", null);
                SortManager.Disable();
                lvw.RemoveValue("ListViewSortManager");
                lvw.ListViewItemSorter = null;
            }
            else if (old_sort_mode == SortMode.SortOnAllColumns)
            {
                // Stop sorting on all columns.
                lvw.ListViewItemSorter = null;
            }

            // Start the new sort mode.
            if (sort_mode == SortMode.SortNone)
            {
                lvw.RemoveValue("ListViewSortMode");
                return;
            }

            if (sort_mode == SortMode.SortOnClickedColumn)
            {
                // Sort on clicked columns.
                lvw.SetValue("ListViewSortManager", new ListViewSortManager(lvw));
            }
            else if (sort_mode == SortMode.SortOnAllColumns)
            {
                // Sort on all columns.
                lvw.ListViewItemSorter = new ListViewAllColumnComparer(SortOrder.Ascending);
                lvw.Sort();
            }

            // Save the new sort mode.
            lvw.SetValue("ListViewSortMode", sort_mode);
        }

        // A class to manage sorting for a ListView.
        private class ListViewSortManager
        {
            // The ListView we are sorting.
            private ListView MyListView;

            // The column we are currently using for sorting.
            private ColumnHeader SortingColumn;

            // Constructor.
            public ListViewSortManager(ListView lvw)
            {
                // Save the control.
                MyListView = lvw;

                // Initially no column is selected for sorting.
                SortingColumn = null;

                // Install the column click event handler.
                MyListView.ColumnClick += MyListView_ColumnClick;
            }

            // No longer sort on columns clicked.
            // Note that this ListViewSortManager can no longer be used
            // after this because it no longer has a reference to a ListView.
            public void Disable()
            {
                // Remove the old sort indicator, if there is one.
                if (SortingColumn != null)
                    SortingColumn.Text = SortingColumn.Text.Substring(2);

                MyListView.ColumnClick -= MyListView_ColumnClick;
                MyListView = null;
            }

            // Sort on the clicked column.
            private void MyListView_ColumnClick(object sender, ColumnClickEventArgs e)
            {
                // Get the new sorting column.
                ColumnHeader new_sorting_column = MyListView.Columns[e.Column];

                // Figure out the new sorting order.
                System.Windows.Forms.SortOrder sort_order;
                if (SortingColumn == null)
                {
                    // New column. Sort ascending.
                    sort_order = SortOrder.Ascending;
                }
                else
                {
                    // See if this is the same column.
                    if (new_sorting_column == SortingColumn)
                    {
                        // Same column. Switch the sort order.
                        if (SortingColumn.Text.StartsWith("> "))
                        {
                            sort_order = SortOrder.Descending;
                        }
                        else
                        {
                            sort_order = SortOrder.Ascending;
                        }
                    }
                    else
                    {
                        // New column. Sort ascending.
                        sort_order = SortOrder.Ascending;
                    }

                    // Remove the old sort indicator.
                    SortingColumn.Text = SortingColumn.Text.Substring(2);
                }

                // Display the new sort order.
                SortingColumn = new_sorting_column;
                if (sort_order == SortOrder.Ascending)
                {
                    SortingColumn.Text = "> " + SortingColumn.Text;
                }
                else
                {
                    SortingColumn.Text = "< " + SortingColumn.Text;
                }

                // Create a comparer.
                MyListView.ListViewItemSorter = new ListViewComparer(e.Column, sort_order);

                // Sort.
                MyListView.Sort();
            }
        }

        // Compares two ListView items based on a selected column.
        private class ListViewComparer : System.Collections.IComparer
        {
            private int ColumnNumber;
            private SortOrder SortOrder;

            public ListViewComparer(int column_number, SortOrder sort_order)
            {
                ColumnNumber = column_number;
                SortOrder = sort_order;
            }

            // Compare two ListViewItems.
            public int Compare(object object_x, object object_y)
            {
                // Get the objects as ListViewItems.
                ListViewItem item_x = object_x as ListViewItem;
                ListViewItem item_y = object_y as ListViewItem;

                // Get the corresponding sub-item values.
                string string_x;
                if (item_x.SubItems.Count <= ColumnNumber)
                {
                    string_x = "";
                }
                else
                {
                    string_x = item_x.SubItems[ColumnNumber].Text;
                }

                string string_y;
                if (item_y.SubItems.Count <= ColumnNumber)
                {
                    string_y = "";
                }
                else
                {
                    string_y = item_y.SubItems[ColumnNumber].Text;
                }

                // Compare them.
                int result;
                double double_x, double_y;
                DateTime date_x, date_y;
                if (double.TryParse(string_x, out double_x) &&
                    double.TryParse(string_y, out double_y))
                {
                    // Treat as a number.
                    result = double_x.CompareTo(double_y);
                }
                else if (DateTime.TryParse(string_x, out date_x) &&
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

        // Compares two ListView items using all of their columns.
        private class ListViewAllColumnComparer : System.Collections.IComparer
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
}
