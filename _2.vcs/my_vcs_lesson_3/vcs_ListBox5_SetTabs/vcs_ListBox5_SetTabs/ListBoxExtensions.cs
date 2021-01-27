using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;

namespace vcs_ListBox5_SetTabs
{
    public static class ListBoxExtensions
    {
        // Set tab stops inside a ListBox.
        public static void SetTabs(this ListBox lst, IList<int> tabs)
        {
            // Make sure the control will use them.
            lst.UseTabStops = true;
            lst.UseCustomTabOffsets = true;

            // Get the control's tab offset collection.
            ListBox.IntegerCollection offsets = lst.CustomTabOffsets;

            // Define the tabs.
            foreach (int tab in tabs)
            {
                offsets.Add(tab);
            }
        }
    }
}
