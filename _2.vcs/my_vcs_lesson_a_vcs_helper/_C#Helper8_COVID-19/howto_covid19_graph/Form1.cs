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

namespace howto_covid19_graph
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
        private CountryDataComparer Comparer = new CountryDataComparer(CountryDataComparer.CompareTypes.ByMaxCases);

        // Used to prevent redraws while checking or unchecking all countries.
        private bool IgnoreItemCheck = false;

        float[] data_in = new float[252];
        float[] data_out = new float[252];
        PointF[] curvePoints = new PointF[252];    //一維陣列內有 N 個Point

        int selectedIndex = 0;

        bool flag_use_test_data = true;   //使用測試資料 TBD
        string csv_filename = "covid19_data2021_06_27.part.csv";

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
            checkedListBox1.DataSource = CountryList;
            checkedListBox1.CheckOnClick = true;

            richTextBox1.Size = new Size(400, 900);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox2.Image = null;

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Load and prepare the data.
        private void LoadData()
        {
            // Compose the local data file name.
            string filename;

            if (flag_use_test_data == true)
            {
                filename = csv_filename;
            }
            else
            {
                filename = "data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";
                richTextBox1.Text += "下載檔案: " + filename + "\n";
                // Download today's data.
                DownloadFile(filename);
            }

            richTextBox1.Text += "讀取檔案: " + filename + "\t從csv => fields\n";
            // Read the file.
            object[,] fields = LoadCsv(filename);

            richTextBox1.Text += "CreateCountryData: " + filename + "\t從fields => 各欄位\n";
            // Create the country data.
            CreateCountryData(fields);
        }

        // Create the country data.
        private void CreateCountryData(object[,] fields)
        {
            // Load the dates.
            Dictionary<string, CountryData> country_dict = new Dictionary<string, CountryData>();
            const int first_date_col = 5;       //CSV檔的第一筆日期資料，從1起數
            int max_row = fields.GetUpperBound(0);
            int max_col = fields.GetUpperBound(1);
            int num_dates = max_col - first_date_col + 1;   //此CSV檔的所有日期資料 行數(Column)

            richTextBox1.Text += "CreateCountryData fields資料大小\n";
            richTextBox1.Text += "共有 " + max_row.ToString() + " 列(Row)\n";  //每列代表一個國家的資料
            richTextBox1.Text += "共有 " + max_col.ToString() + " 欄(Column)\n";   //每欄代表一天的資料
            richTextBox1.Text += "此 fields 的資料欄數 " + num_dates.ToString() + " 欄(Column)\n"; //扣掉檔頭 真實的資料天數

            CountryData.Dates = new DateTime[num_dates];
            for (int col = 1; col <= num_dates; col++)  //每天的資料
            {
                // Convert the date into a double and then into a date.
                double double_value = (double)fields[1, col + first_date_col - 1];  //從1900/1/1至今的天數
                CountryData.Dates[col - 1] = DateTime.FromOADate(double_value);

                if (col <= 10)
                {
                    richTextBox1.Text += "col = " + col.ToString() + "\tdouble_value = " + double_value.ToString() + "\n";
                    richTextBox1.Text += "num = " + (col + first_date_col - 1).ToString() + "\n";
                    richTextBox1.Text += "data = " + CountryData.Dates[col - 1].ToString() + "\n";
                }
            }

            // Load the country data.
            const int country_col = 2;
            for (int country_num = 2; country_num <= max_row; country_num++)
            {
                // Get the country's name.
                string country_name = fields[country_num, country_col].ToString();

                //debug
                if (country_name == "Taiwan*")
                {
                    richTextBox1.Text += "get country name : " + country_name + "\tcountry_num = " + country_num.ToString() + "\n";
                }

                //debug
                if (country_num == 246)
                {
                    for (int j = 2; j < 10; j++)
                    {
                        richTextBox1.Text += "j = " + j.ToString() + "\t" + fields[country_num, j].ToString() + "\n";
                    }
                }

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

                if (country_name == "Taiwan*")
                {
                    richTextBox1.Text += "從 fields 取得案例數\n";
                }

                // Add to the country's data.
                for (int col = 1; col <= num_dates; col++)
                {
                    // Add the value to the country's total.
                    country_data.Cases[col - 1] += (int)(double)fields[country_num, col + first_date_col - 1];
                    if (country_name == "Taiwan*")
                    {
                        //debug
                        richTextBox1.Text += country_data.Cases[col - 1].ToString() + "\t";
                    }
                }
                if (country_name == "Taiwan*")
                    richTextBox1.Text += "\n";
            }

            // Convert CountryDict into CountryList.
            CountryList = country_dict.Values.ToList();

            // Set MaxCases values.
            foreach (CountryData country in CountryList)
            {
                //設定每個國家的總數
                country.SetMax();
                richTextBox1.Text += "國家:" + country.Name + " 確診數:" + country.MaxCases.ToString() + ", ";
            }

            // Sort.
            richTextBox1.Text += "\n依 預設(總數) 排序\n\n";
            CountryList.Sort(Comparer);

            // Set MaxCases values.
            foreach (CountryData country in CountryList)
            {
                //richTextBox1.Text += country.Name + " " + country.MaxCases.ToString() + "  ";
            }

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
            if (!File.Exists(filename))
            {
                // Download the file.
                this.Cursor = Cursors.WaitCursor;
                Application.DoEvents();

                try
                {
                    // Make a WebClient.
                    WebClient web_client = new WebClient();

                    // Download the file.
                    const string url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
                    web_client.DownloadFile(url, filename);

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
        private void checkedListBox1_ItemCheck(object sender, ItemCheckEventArgs e)
        {
            richTextBox1.Text += "點選\t" + checkedListBox1.Items[e.Index] + "\t" + checkedListBox1.SelectedIndex.ToString() + "\n";
            // Do nothing if the user clicked All or None.
            if (IgnoreItemCheck)
            {
                return;
            }

            // Get the current list of checked items.
            CountryData checked_country = checkedListBox1.Items[e.Index] as CountryData;
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
            if (checkedListBox1.CheckedItems.Count == 0)
            {
                // Create a new list.
                country_list = new List<CountryData>();
            }
            else
            {
                // Convert the selected objects into CountryData objects.
                country_list =
                    checkedListBox1.CheckedItems.Cast<CountryData>().ToList();
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
            richTextBox1.Text += "重畫資料 cnt = " + SelectedCountries.Count.ToString() + "\t";
            ClosePoint = new PointF(-1, -1);
            if (SelectedCountries.Count == 0)
            {
                pictureBox1.Image = null;
                richTextBox1.Text += "\t未選取國家\n";
                return;
            }
            else
            {
                richTextBox1.Text += "\n";
            }

            // Get the maximum value.
            float y_max = SelectedCountries.Max(country => country.Cases.Max());
            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            if (y_max < 10)
                y_max = 10;
            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";

            // Create a transformation to make the data fit the PictureBox.
            DefineTransform(SelectedCountries, y_max);

            // Create a bitmap.
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.TextRenderingHint = TextRenderingHint.AntiAlias;
                g.Transform = Transform;

                // Draw the axes.
                DrawAxes(g);

                // Draw the curves. //預設的曲線顏色 輪流顯示
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
                        richTextBox1.Text += "國家 : " + country.Name + "\t顏色 : " + pen.Color + "\n";
                        country.Draw(g, pen, Transform);
                    }
                }
            }

            // Display the result.
            pictureBox1.Image = bm;
        }

        private void DefineTransform(List<CountryData> country_list, float y_max)
        {
            int num_cases = country_list[0].Cases.Length;
            WorldBounds = new RectangleF(0, 0, num_cases, y_max);
            int wid = pictureBox1.ClientSize.Width;
            int hgt = pictureBox1.ClientSize.Height - 1;
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
                    richTextBox1.Text += "draw y = " + y.ToString() + "\n";
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
                        richTextBox1.Text += "draw string = " + y.ToString("n0") + "\n";
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
            richTextBox1.Text += "按了 全選\n";
            IgnoreItemCheck = true;
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked(i, true);
            }
            IgnoreItemCheck = false;
            RedrawGraph();
        }

        private void btnNone_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "按了 全不選\n";
            IgnoreItemCheck = true;
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked(i, false);
            }
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

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = e.Location.ToString();
            SetTooltip(e.Location);
        }

        private void SetTooltip(PointF point)
        {
            if (pictureBox1.Image == null)
            {
                return;
            }
            if (SelectedCountries == null)
            {
                return;
            }

            string mesg = "";
            int day_num;
            int num_cases;
            foreach (CountryData country in SelectedCountries)
            {
                if (country.PointIsAt(point, out day_num, out num_cases, out ClosePoint))
                {
                    //由 point 找到第幾天 再對應到日期 找到當時的總數
                    //richTextBox1.Text += point.ToString() + " " + day_num.ToString() + " " + CountryData.Dates[day_num].ToShortDateString() + " " + num_cases.ToString() + " ";

                    mesg = country.Name + "\n" +
                        CountryData.Dates[day_num].ToShortDateString() + "\n" +
                        num_cases.ToString("n0") + " 例";

                    richTextBox1.Text += country.Name + "\t" + CountryData.Dates[day_num].ToShortDateString() + "\t總數: " + num_cases.ToString("n0") + "\n";
                    break;
                }
            }

            if (toolTip1.GetToolTip(pictureBox1) != mesg)
            {
                toolTip1.SetToolTip(pictureBox1, mesg);
            }
            pictureBox1.Refresh();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            //richTextBox1.Text += "pictureBox1_Paint\n";
            if (ClosePoint.X < 0)
            {
                return;
            }

            const int radius = 3;
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            float x = ClosePoint.X - radius;
            float y = ClosePoint.Y - radius;
            e.Graphics.FillEllipse(Brushes.White, x, y, 2 * radius, 2 * radius);
            e.Graphics.DrawEllipse(Pens.Red, x, y, 2 * radius, 2 * radius);
            //richTextBox1.Text += "(" + ClosePoint.X.ToString() + ", " + ClosePoint.Y.ToString() + ") ";
        }

        private void radSortByName_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "按了 依 國名 排序\n";

            if (CountryList == null)
            {
                return;
            }
            Comparer = new CountryDataComparer(CountryDataComparer.CompareTypes.ByName);
            checkedListBox1.DataSource = null;
            CountryList.Sort(Comparer);
            checkedListBox1.DataSource = CountryList;
            RedrawGraph();
        }

        private void radSortByMaxCases_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "按了 依 總數 排序\n";

            if (CountryList == null)
            {
                return;
            }
            Comparer = new CountryDataComparer(CountryDataComparer.CompareTypes.ByMaxCases);
            checkedListBox1.DataSource = null;
            CountryList.Sort(Comparer);
            checkedListBox1.DataSource = CountryList;
            RedrawGraph();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int len;
            int len2;

            if (CountryList != null)
            {
                len = CountryList.Count;
                richTextBox1.Text += "CountryList len = " + len.ToString() + "\n";
                for (i = 0; i < len; i++)
                {
                    //richTextBox1.Text += "i = " + i.ToString() + "\t" + CountryList[i].Name + "\n";
                    if (CountryList[i].Name == "Taiwan*")
                    {
                        richTextBox1.Text += "台灣的位置在 " + i.ToString() + "\t設定讀取此筆資料\n";
                        checkedListBox1.SetItemChecked(i, true);  //直接選取台灣
                    }
                }
            }

            len = checkedListBox1.Items.Count;

            richTextBox1.Text += "分析資料\n";
            richTextBox1.Text += "checkedListBox1 len = " + len.ToString() + "\n";
            len = 5;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + checkedListBox1.Items[i] + "\n";
            }

            if (CountryList != null)
            {
                len = CountryList.Count;
                richTextBox1.Text += "CountryList len = " + len.ToString() + "\n";
                len = 5;
                for (i = 0; i < len; i++)
                {
                    richTextBox1.Text += "i = " + i.ToString() + "\t" + CountryList[i].Name + "\n";
                }
            }

            int day_num;
            for (day_num = 0; day_num < 5; day_num++)
            {
                richTextBox1.Text += "第　" + day_num.ToString() + " 天, 日期: " + CountryData.Dates[day_num].ToShortDateString() + "\n";
            }

            if (SelectedCountries != null)
            {
                len = SelectedCountries.Count;
                richTextBox1.Text += "Selected countries len = " + len.ToString() + "\n";
                for (i = 0; i < len; i++)
                {
                    richTextBox1.Text += "i = " + i.ToString() + "\tNumber: " + SelectedCountries[i].CountryNumber.ToString() + "\t";
                    richTextBox1.Text += "Name: " + SelectedCountries[i].Name + "\t";

                    richTextBox1.Text += "MaxCases:\t" + SelectedCountries[i].MaxCases.ToString() + "\n";

                    len2 = SelectedCountries[i].Cases.Length;
                    len2 = 10;
                    richTextBox1.Text += "case len:\t" + len2.ToString() + "\n";
                    for (j = 0; j < len2; j++)
                    {
                        richTextBox1.Text += SelectedCountries[i].Cases[j].ToString() + "\t";
                    }
                    richTextBox1.Text += "\n";

                    len2 = SelectedCountries[i].DeviceCoords.Length;
                    //len2 = 10;
                    richTextBox1.Text += "DeviceCoords len:\t" + len2.ToString() + "\n";
                    for (j = 0; j < len2; j++)
                    {
                        //richTextBox1.Text += SelectedCountries[i].DeviceCoords[j].ToString() + "\t";
                    }
                    richTextBox1.Text += "\n";

                    // Create a bitmap.
                    Bitmap bm = new Bitmap(pictureBox2.ClientSize.Width, pictureBox2.ClientSize.Height);
                    using (Graphics g = Graphics.FromImage(bm))
                    {
                        Pen p = new Pen(Color.Red, 1);

                        g.SmoothingMode = SmoothingMode.AntiAlias;
                        if (len2 > 1)
                        {
                            g.DrawLines(p, SelectedCountries[i].DeviceCoords.ToArray());
                        }

                    }
                    // Display the result.
                    pictureBox2.Image = bm;

                    //copy data
                    for (j = 0; j < 252; j++)
                    {
                        data_in[j] = SelectedCountries[i].DeviceCoords[j].X;
                        data_out[j] = SelectedCountries[i].DeviceCoords[j].Y;
                    }
                }
                float y_max = SelectedCountries.Max(country => country.Cases.Max());
                richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";

                float y_min = SelectedCountries.Min(country => country.Cases.Min());
                richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            //int j;

            pictureBox2.Image = null;
            richTextBox1.Clear();
            //richTextBox1.Text += "pictureBox2, W = " + pictureBox2.Width.ToString() + ", H = " + pictureBox2.Height.ToString() + "\n";
            for (i = 0; i < 252; i++)
            {
                //curvePoints[i].X = data_in[i] * 3;
                //curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;

                curvePoints[i].X = data_in[i];
                if (i < 252 / 2)
                    curvePoints[i].Y = data_out[i];
                else
                    curvePoints[i].Y = data_out[252 / 2];
            }

            // Create a bitmap.
            Bitmap bm = new Bitmap(pictureBox2.ClientSize.Width, pictureBox2.ClientSize.Height);
            using (Graphics g = Graphics.FromImage(bm))
            {
                Pen p = new Pen(Color.Green, 2);

                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.DrawLines(p, curvePoints.ToArray());
                //g.DrawLines(p, curvePoints);
            }
            // Display the result.
            pictureBox2.Image = bm;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //解讀CSV資料

            richTextBox1.Text += "CountryList 長度 : " + CountryList.Count.ToString() + "\n";
            int i;
            for (i = 0; i < CountryList.Count; i++)
            {
                richTextBox1.Text += CountryList[i].Name + "\t" + CountryList[i].CountryNumber.ToString() + "\t" + CountryList[i].MaxCases.ToString() + "\n";
            }

            richTextBox1.Text += "改變排序, 依名排序\n";

            Comparer = new CountryDataComparer(CountryDataComparer.CompareTypes.ByName);
            CountryList.Sort(Comparer);

            for (i = 0; i < CountryList.Count; i++)
            {
                richTextBox1.Text += CountryList[i].Name + "\t" + CountryList[i].CountryNumber.ToString() + "\t" + CountryList[i].MaxCases.ToString() + "\n";
            }

            richTextBox1.Text += "改變排序, 依名確診數排序\n";

            Comparer = new CountryDataComparer(CountryDataComparer.CompareTypes.ByMaxCases);
            CountryList.Sort(Comparer);

            for (i = 0; i < CountryList.Count; i++)
            {
                richTextBox1.Text += CountryList[i].Name + "\t" + CountryList[i].CountryNumber.ToString() + "\t" + CountryList[i].MaxCases.ToString() + "\n";
            }





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

