using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// For System.Collections.IEnumerable.
using System.Collections;

namespace vcs_ComboBox2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Initialize the ComboBox and ListBox.
        private void Form1_Load(object sender, EventArgs e)
        {
            foreach (TimeZoneInfo info in
                TimeZoneInfo.GetSystemTimeZones())
            {
                cboTimeZones.Items.Add(info);
                lstTimeZones.Items.Add(info);
            }

            // Select some defaults.
            cboTimeZones.SelectedItem =
                FindItemContaining(cboTimeZones.Items, "Mountain Time");
            lstTimeZones.SelectedItem =
                FindItemContaining(lstTimeZones.Items, "Mountain Time");
        }

        // Select an item containing the target string.
        private object FindItemContaining(IEnumerable items, string target)
        {
            foreach (object item in items)
                if (item.ToString().Contains(target))
                    return item;

            // Return null;
            return null;
        }
    }
}
