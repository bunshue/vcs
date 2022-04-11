using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;
using System.Drawing.Drawing2D;
using System.Drawing.Text;
using Excel = Microsoft.Office.Interop.Excel;

// Data from https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases

namespace howto_covid19_align_starts
{
    public partial class Form1 : Form
    {
        // The data.
        private List<CountryData> CountryList = null;
        private List<CountryData> SelectedCountries = null;

        private Matrix Transform = null;
        private Matrix InverseTransform = null;
        private RectangleF WorldBounds;
        private PointF ClosePoint = new PointF(-1, -1);
        private CountryDataComparer Comparer =
            new CountryDataComparer(CountryDataComparer.CompareTypes.ByMaxCases);

        // Used to prevent redraws while checking or unchecking all countries.
        private bool IgnoreItemCheck = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //網頁protocol	解決  要求已經中止: 無法建立 SSL/TLS 的安全通道。
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            // Load the data.
            LoadData();

            // Display the countries in the checked list box.
            clbCountries.DataSource = CountryList;
            clbCountries.CheckOnClick = true;
        }

        // Load and prepare the data.
        private void LoadData()
        {
            // Compose the local data file name.
            string filename = "data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            DownloadFile(filename);

            richTextBox1.Text += "filename : " + filename + "\n";

            // Read the file.
            object[,] fields = LoadCsv(filename);

            // Create the country data.
            CreateCountryData(fields);
        }

        // Create the country data.
        private void CreateCountryData(object[,] fields)
        {
            // Load the dates.
            Dictionary<string, CountryData> country_dict =
                new Dictionary<string, CountryData>();
            const int first_date_col = 5;
            int max_row = fields.GetUpperBound(0);
            int max_col = fields.GetUpperBound(1);
            int num_dates = max_col - first_date_col + 1;
            CountryData.Dates = new DateTime[num_dates];
            for (int col = 1; col <= num_dates; col++)
            {
                // Convert the date into a double and then into a date.
                double double_value = (double)fields[1, col + first_date_col - 1];
                CountryData.Dates[col - 1] =
                    DateTime.FromOADate(double_value);
            }

            // Load the country data.
            const int country_col = 2;
            for (int country_num = 2; country_num <= max_row; country_num++)
            {
                // Get the country's name.
                string country_name = fields[country_num, country_col].ToString();

                // Get or create the country's CountryData object.
                CountryData country_data;
                if (country_dict.ContainsKey(country_name))
                {
                    country_data = country_dict[country_name];
                }
                else
                {
                    country_data = new CountryData();
                    country_data.Name = country_name;
                    country_data.Cases = new int[num_dates];
                    country_dict.Add(country_name, country_data);
                }

                // Add to the country's data.
                for (int col = 1; col <= num_dates; col++)
                {
                    // Add the value to the country's total.
                    country_data.Cases[col - 1] +=
                        (int)(double)fields[country_num, col + first_date_col - 1];
                }
            }

            // Convert CountryDict into CountryList.
            CountryList = country_dict.Values.ToList();

            // Set MaxCases values.
            foreach (CountryData country in CountryList)
            {
                country.SetMax();
            }

            // Sort.
            CountryList.Sort(Comparer);

            // Number the countries and set MaxCases values.
            for (int i = 0; i < CountryList.Count; i++)
            {
                CountryList[i].CountryNumber = i;
            }
        }

        // Download today's data.
        private void DownloadFile(string filename)
        {
            // See if we have today's file.
            if (File.Exists(filename) == false)
            {
                // Download the file.
                this.Cursor = Cursors.WaitCursor;
                Application.DoEvents();

                try
                {
                    // Make a WebClient.
                    WebClient wc = new WebClient();

                    // Download the file.
                    const string url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
                    wc.DownloadFile(url, filename);

                    richTextBox1.Text += "url : " + url + "\n";
                    richTextBox1.Text += "filename : " + filename + "\n";
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "Download Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                }
                finally
                {
                    this.Cursor = Cursors.Default;
                }
            }
        }

        // Load a CSV file into a 1-based array.
        private object[,] LoadCsv(string filename)
        {
            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            //excel_app.Visible = true;

            // Open the workbook read-only.
            filename = Application.StartupPath + "\\" + filename;
            Excel.Workbook workbook = excel_app.Workbooks.Open(
                filename,
                Type.Missing, true, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing);

            // Get the first worksheet.
            Excel.Worksheet sheet = (Excel.Worksheet)workbook.Sheets[1];

            // Get the used range.
            Excel.Range used_range = sheet.UsedRange;

            // Get the sheet's values.
            object[,] values = (object[,])used_range.Value2;

            // Close the workbook without saving changes.
            workbook.Close(false, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();

            return values;
        }

        // An item has been checked or unchecked.
        private void clbCountries_ItemCheck(object sender, ItemCheckEventArgs e)
        {
            // Do nothing if the user clicked All or None.
            if (IgnoreItemCheck) return;

            // Get the current list of checked items.
            CountryData checked_country =
                clbCountries.Items[e.Index] as CountryData;
            SelectedCountries = GetCountryList(checked_country, e.NewValue);

            // Graph the results.
            GraphCountries();

            // Redisplay the tooltip if appropriate.
            SetTooltip(ClosePoint);
        }

        // Get the list of checked items,
        // adding or removing a checked item.
        private List<CountryData> GetCountryList(
            CountryData checked_country, CheckState checked_state)
        {
            // Get the current list of checked items.
            List<CountryData> country_list;
            if (clbCountries.CheckedItems.Count == 0)
            {
                // Create a new list.
                country_list = new List<CountryData>();
            }
            else
            {
                // Convert the selected objects into CountryData objects.
                country_list =
                    clbCountries.CheckedItems.Cast<CountryData>().ToList();
            }

            if (checked_country != null)
            {
                // See if the clicked country is being checked or unchecked.
                if (checked_state == CheckState.Checked)
                {
                    // Add the item to the list.
                    country_list.Add(checked_country);
                }
                else
                {
                    // Remove the item from the list.
                    country_list.Remove(checked_country);
                }
            }

            return country_list;
        }

        // Draw the graph.
        private void GraphCountries()
        {
            ClosePoint = new PointF(-1, -1);
            if (SelectedCountries.Count == 0)
            {
                picGraph.Image = null;
                return;
            }

            // Get the maximum value.
            float y_max = SelectedCountries.Max(country => country.Cases.Max());
            if (y_max < 10) y_max = 10;

            // Create a transformation to make the data fit the PictureBox.
            DefineTransform(SelectedCountries, y_max);

            // Get the number of cases where we should align countries.
            int align_cases = 0;
            int.TryParse(txtAlignCases.Text, out align_cases);

            // Create a bitmap.
            Bitmap bm = new Bitmap(
                picGraph.ClientSize.Width,
                picGraph.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.TextRenderingHint = TextRenderingHint.AntiAlias;
                gr.Transform = Transform;

                // Draw the axes.
                DrawAxes(gr);

                // Draw the curves.
                Color[] colors =
                {
                    Color.Red, Color.Green, Color.Blue, Color.Black,
                    Color.Cyan, Color.Orange,
                };
                int num_colors = colors.Length;
                using (Pen pen = new Pen(Color.Black, 0))
                {
                    foreach (CountryData country in SelectedCountries)
                    {
                        pen.Color = colors[country.CountryNumber % num_colors];
                        country.Draw(align_cases, gr, pen, Transform);
                    }
                }
            }

            // Display the result.
            picGraph.Image = bm;
        }

        private void DefineTransform(List<CountryData> country_list, float y_max)
        {
            int num_cases = country_list[0].Cases.Length;
            WorldBounds = new RectangleF(0, 0, num_cases, y_max);
            int wid = picGraph.ClientSize.Width;
            int hgt = picGraph.ClientSize.Height - 1;
            const int margin = 4;
            PointF[] dest_points =
            {
                new PointF(margin, hgt - margin),
                new PointF(wid - margin, hgt - margin),
                new PointF(margin, margin),
            };
            Transform = new Matrix(WorldBounds, dest_points);
            InverseTransform = Transform.Clone();
            InverseTransform.Invert();
        }

        private void DrawAxes(Graphics gr)
        {
            using (Pen pen = new Pen(Color.Red, 0))
            {
                // Calculate the Y step value.
                // Find the largest power of 10 less than y_max.
                float y_max = WorldBounds.Bottom;
                int power = (int)Math.Log10(y_max);
                // If this is more than 1/2 of y_max, use the next smaller power.
                if (Math.Pow(10, power) > y_max / 2) power--;
                int y_step = (int)Math.Pow(10, power);
                if (y_step < 1) y_step = 1;

                // Draw the Y axis.
                gr.DrawLine(pen, 0, 0, 0, y_max);

                pen.Color = Color.Silver;
                float num_cases = WorldBounds.Right;
                for (int y = y_step; y < y_max; y += y_step)
                {
                    gr.DrawLine(pen, 0, y, num_cases, y);
                }

                GraphicsState state = gr.Save();
                gr.ResetTransform();
                using (Font font = new Font("Arial", 12, FontStyle.Regular))
                {
                    for (int y = y_step; y < y_max; y += y_step)
                    {
                        Point[] p = { new Point(0, y) };
                        Transform.TransformPoints(p);

                        gr.DrawString(y.ToString("n0"), font, Brushes.Black, p[0]);
                    }
                }
                gr.Restore(state);

                // Draw the X axis.
                pen.Color = Color.Red;
                gr.DrawLine(pen, 0, 0, num_cases, 0);

                // Calculate the tick mark size.
                const int tick_y_pixels = 5;
                PointF[] tick_points = { new PointF(0, tick_y_pixels) };
                InverseTransform.TransformVectors(tick_points);
                float tick_y = -tick_points[0].Y;

                // Draw tick marks.
                for (int i = 0; i < num_cases; i++)
                {
                    gr.DrawLine(pen, i, -tick_y, i, tick_y);
                }
            }
        }

        private void btnAll_Click(object sender, EventArgs e)
        {
            IgnoreItemCheck = true;
            for (int i = 0; i < clbCountries.Items.Count; i++)
                clbCountries.SetItemChecked(i, true);
            IgnoreItemCheck = false;
            RedrawGraph();
        }

        private void btnNone_Click(object sender, EventArgs e)
        {
            IgnoreItemCheck = true;
            for (int i = 0; i < clbCountries.Items.Count; i++)
                clbCountries.SetItemChecked(i, false);
            IgnoreItemCheck = false;
            RedrawGraph();
        }

        private void RedrawGraph()
        {
            // Get the current list of checked items.
            SelectedCountries = GetCountryList(null, CheckState.Indeterminate);

            // Graph the results.
            GraphCountries();

            // Redisplay the tooltip if appropriate.
            SetTooltip(ClosePoint);
        }

        private void picGraph_MouseMove(object sender, MouseEventArgs e)
        {
            SetTooltip(e.Location);
        }

        private void SetTooltip(PointF point)
        {
            if (picGraph.Image == null)
                return;
            if (SelectedCountries == null)
                return;

            string mesg = "";
            int day_num;
            int num_cases;
            foreach (CountryData country in SelectedCountries)
            {
                if (country.PointIsAt(point, out day_num, out num_cases, out ClosePoint))
                {
                    mesg = country.Name + "\n" +
                        CountryData.Dates[day_num].ToShortDateString() + "\n" +
                        num_cases.ToString("n0") + " cases";
                    break;
                }
            }

            if (toolTip1.GetToolTip(picGraph) != mesg)
                toolTip1.SetToolTip(picGraph, mesg);
            picGraph.Refresh();
        }

        private void picGraph_Paint(object sender, PaintEventArgs e)
        {
            if (ClosePoint.X < 0) return;

            const int radius = 3;
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            float x = ClosePoint.X - radius;
            float y = ClosePoint.Y - radius;
            e.Graphics.FillEllipse(Brushes.White, x, y, 2 * radius, 2 * radius);
            e.Graphics.DrawEllipse(Pens.Red, x, y, 2 * radius, 2 * radius);
        }

        private void radSortByName_Click(object sender, EventArgs e)
        {
            if (CountryList == null) return;
            Comparer = new CountryDataComparer(CountryDataComparer.CompareTypes.ByName);
            clbCountries.DataSource = null;
            CountryList.Sort(Comparer);
            clbCountries.DataSource = CountryList;
            RedrawGraph();
        }

        private void radSortByMaxCases_Click(object sender, EventArgs e)
        {
            if (CountryList == null) return;
            Comparer = new CountryDataComparer(CountryDataComparer.CompareTypes.ByMaxCases);
            clbCountries.DataSource = null;
            CountryList.Sort(Comparer);
            clbCountries.DataSource = CountryList;
            RedrawGraph();
        }

        private void txtAlignCases_TextChanged(object sender, EventArgs e)
        {
            GraphCountries();
        }
    }

    //3Form1之外
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }
}
