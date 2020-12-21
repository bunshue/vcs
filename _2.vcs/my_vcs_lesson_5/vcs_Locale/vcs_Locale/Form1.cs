using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization; //for CultureInfo CultureTypes

namespace vcs_Locale
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            float float_value = 1234.56f;
            decimal dec_value = 1234.56m;
            DateTime now = DateTime.Now;

            // Loop through the locales.
            foreach (CultureInfo info in
                CultureInfo.GetCultures(CultureTypes.AllCultures))
            {
                ListViewItem item = listView1.Items.Add(
                    info.EnglishName);
                item.SubItems.Add(info.NativeName);
                item.SubItems.Add(info.Name);

                // You can't use a neutral culture as a format
                // provider, so if the CultureInfo is neutral,
                // look for a non-neutral ancestor.
                CultureInfo culture = info;
                while ((culture != null) && (culture.IsNeutralCulture))
                    culture = culture.Parent;
                if (culture != null)
                {
                    item.SubItems.Add(float_value.ToString("N", culture));
                    item.SubItems.Add(dec_value.ToString("C", culture));
                    item.SubItems.Add(now.ToString("d", culture));
                    item.SubItems.Add(now.ToString("t", culture));
                }
            }


        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "共有 " + CultureInfo.GetCultures(CultureTypes.AllCultures).Length.ToString() + " 筆Locale\n";

            // Add the locale information.
            foreach (CultureInfo info in CultureInfo.GetCultures(CultureTypes.AllCultures))
            {
                richTextBox1.Text += info.EnglishName + '\t' + info.NativeName + "\n";
            }

        }
    }
}
