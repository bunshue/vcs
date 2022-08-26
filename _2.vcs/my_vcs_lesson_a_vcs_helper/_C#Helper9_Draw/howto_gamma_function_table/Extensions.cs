using System.Windows.Forms;

namespace howto_gamma_function_table
{
    public static class Extensions
    {
        // Add an item and subitems to a ListView.
        public static void AddRow(this ListView lvw,
            string item, params string[] subitems)
        {
            ListViewItem list_view_item = lvw.Items.Add(item);
            foreach (string subitem in subitems)
                list_view_item.SubItems.Add(subitem);
        }

        // Autosize all columns.
        public static void AutoSizeColumns(this ListView lvw,
            params string[] values)
        {
            foreach (ColumnHeader column in lvw.Columns)
                column.Width = -2;
        }
    }
}
