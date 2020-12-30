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

        private void button2_Click(object sender, EventArgs e)
        {
            // Save the culture (to make the following code shorter).
            CultureInfo info = CultureInfo.InstalledUICulture;

            // Day/Month values.
            AddHeader("Day/Month:");
            AddArrayItems("Day", info.DateTimeFormat.DayNames);
            AddArrayItems("Abbrev Day", info.DateTimeFormat.AbbreviatedDayNames);
            AddArrayItems("Short Days", info.DateTimeFormat.ShortestDayNames);
            AddArrayItems("Month", info.DateTimeFormat.MonthNames);
            AddArrayItems("Abbrev Month", info.DateTimeFormat.AbbreviatedMonthNames);

            // Date/Time values.
            AddHeader("Date/Time Format:");
            AddItem("AMDesignator", info.DateTimeFormat.AMDesignator);
            AddItem("DateSeparator", info.DateTimeFormat.DateSeparator);
            AddItem("FirstDayOfWeek", info.DateTimeFormat.FirstDayOfWeek.ToString());
            AddItem("FullDateTimePattern", info.DateTimeFormat.FullDateTimePattern);
            AddItem("LongDatePattern", info.DateTimeFormat.LongDatePattern);
            AddItem("LongTimePattern", info.DateTimeFormat.LongTimePattern);
            AddItem("MonthDayPattern", info.DateTimeFormat.MonthDayPattern);
            AddItem("NativeCalendarName", info.DateTimeFormat.NativeCalendarName);
            AddItem("PMDesignator", info.DateTimeFormat.PMDesignator);
            AddItem("RFC1123Pattern", info.DateTimeFormat.RFC1123Pattern);
            AddItem("ShortDatePattern", info.DateTimeFormat.ShortDatePattern);
            AddItem("ShortTimePattern", info.DateTimeFormat.ShortTimePattern);
            AddItem("SortableDateTimePattern", info.DateTimeFormat.SortableDateTimePattern);
            AddItem("TimeSeparator", info.DateTimeFormat.TimeSeparator);

            // Culture values.
            AddHeader("Culture:");
            AddItem("Culture Name", info.Name);
            AddItem("Culture Native Name", info.NativeName);
            AddItem("Culture Display Name", info.DisplayName);
            AddItem("Culture English Name", info.EnglishName);
            AddItem("IetfLanguageTag", info.IetfLanguageTag);
            AddItem("IsNeutralCulture", info.IsNeutralCulture.ToString());

            // Currency values.
            AddHeader("Currency Format:");
            AddItem("Decimal Digits", info.NumberFormat.CurrencyDecimalDigits.ToString());
            AddItem("Decimal Separator", info.NumberFormat.CurrencyDecimalSeparator);
            AddItem("Group Separator", info.NumberFormat.CurrencyGroupSeparator);
            AddIntegerArrayItems("Group Size", info.NumberFormat.CurrencyGroupSizes);
            AddItem("Negative Pattern", info.NumberFormat.CurrencyNegativePattern.ToString());
            AddItem("Positive Pattern", info.NumberFormat.CurrencyPositivePattern.ToString());
            AddItem("Currency Symbol", info.NumberFormat.CurrencySymbol);

            // Number values.
            AddHeader("Number Format:");
            AddItem("NaN", info.NumberFormat.NaNSymbol);
            AddArrayItems("Native Digits", info.NumberFormat.NativeDigits);
            AddItem("Infinity Symbol", info.NumberFormat.NegativeInfinitySymbol);
            AddItem("Negative Sign", info.NumberFormat.NegativeSign);
            AddItem("Decimal Separator", info.NumberFormat.NumberDecimalSeparator);
            AddItem("Group Separator", info.NumberFormat.NumberGroupSeparator);
            AddIntegerArrayItems("Group Size", info.NumberFormat.PercentGroupSizes);
            AddItem("Negative Pattern", info.NumberFormat.NumberNegativePattern.ToString());
            AddItem("Positive Infinity Symbol", info.NumberFormat.PositiveInfinitySymbol);
            AddItem("Positive Sign", info.NumberFormat.PositiveSign);

            // Percent values.
            AddHeader("Percent Format:");
            AddItem("Decimal Digits", info.NumberFormat.PercentDecimalDigits.ToString());
            AddItem("Decimal Separator", info.NumberFormat.PercentDecimalSeparator);
            AddItem("Group Separator", info.NumberFormat.PercentGroupSeparator);
            AddIntegerArrayItems("Group Size", info.NumberFormat.PercentGroupSizes);
            AddItem("Negative Pattern", info.NumberFormat.PercentNegativePattern.ToString());
            AddItem("Positive Pattern", info.NumberFormat.PercentPositivePattern.ToString());
            AddItem("Percent Symbol", info.NumberFormat.PercentSymbol);
            AddItem("PerMilleSymbol", info.NumberFormat.PerMilleSymbol);
        }

        // Add a header row.
        private void AddHeader(string name)
        {
            richTextBox1.Text += "\n--------------------\t" + name + "\t--------------------\n";
        }

        // Add a value to the result.
        private void AddItem(string name, string value)
        {
            richTextBox1.Text += name + "\t" + value + "\n";
        }

        // Add all values in an array.
        private void AddArrayItems(string name, string[] values)
        {
            for (int i = 0; i < values.Length; i++)
            {
                AddItem(name + "[" + i + "]", values[i]);
                //richTextBox1.Text += name + "[" + i + "]" + "\t" + values[i] + "\n";
            }
        }

        // Add all values in an integer array.
        private void AddIntegerArrayItems(string name, int[] values)
        {
            for (int i = 0; i < values.Length; i++)
            {
                AddItem(name + "[" + i + "]", values[i].ToString());
                //richTextBox1.Text += name + "[" + i + "]" + "\t" + values[i].ToString() + "\n";
            }
        }



    }
}
