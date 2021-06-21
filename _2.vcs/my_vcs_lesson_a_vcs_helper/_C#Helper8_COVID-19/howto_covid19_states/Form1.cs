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

// Data from https://covidtracking.com/api

namespace howto_covid19_states
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The data.
        private int NumDates = 0;
        private List<StateData> StateList = null;
        private List<StateData> SelectedStates =
            new List<StateData>();

        private Dictionary<string, StateData> StateDict =
            new Dictionary<string, StateData>();

        private Matrix Transform = null;
        private Matrix InverseTransform = null;
        private RectangleF WorldBounds;
        private PointF ClosePoint = new PointF(-1, -1);
        private StateDataComparer Comparer =
            new StateDataComparer(StateDataComparer.CompareTypes.ByMaxCases);

        // Used to prevent redraws while checking or unchecking all countries.
        private bool IgnoreItemCheck = false;

        // Make an array of CheckBoxes for the All and None buttons.
        private CheckBox[] CheckBoxes;

        // Used to prevent redraws while checking or unchecking all data sets.
        private bool IgnoreCheckedChanged = false;

        private void Form1_Load(object sender, EventArgs e)
        {
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            ServicePointManager.SecurityProtocol =
                Protocols.protocol_Tls11 | Protocols.protocol_Tls12;

            // Initialize the CheckBoxes array.
            CheckBoxes = new CheckBox[]
            {
                chkTotalPositive,
                chkTotalNegative,
                chkPending,
                chkHospitalizedNow,
                chkHospitalizedTotal,
                chkIcuNow,
                chkIcuTotal,
                chkVentNow,
                chkVentTotal,
                chkRecovered,
                chkDeaths,
            };

            Show();

            // Load the data.
            lblLoading.Text = "Loading data...";
            lblLoading.Refresh();
            LoadData();

            // Make StateList.
            StateList = StateDict.Values.ToList();

            // Number the states.
            for (int i = 0; i < StateList.Count; i++)
            {
                StateList[i].StateNumber = i;
            }

            // Load the population data.
            LoadPopulationData();

            // Display the states in sorted order.
            SortStates();

            lblLoading.Text = "";
            lblLoading.Refresh();
        }

        // Load and prepare the data.
        private void LoadData()
        {
            // Compose the local data file name.
            string filename = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            const string url = "https://covidtracking.com/api/v1/states/daily.csv";
            DownloadFile(url, filename);

            richTextBox1.Text += "url : " + url + "\n";
            richTextBox1.Text += "filename : " + filename + "\n";

            // Read the file.
            object[,] fields = LoadCsv(filename);

            // Create the state data.
            CreateStateData(fields);
        }

        // Get or create a StateData object.
        private StateData GetOrCreateStateData(string state_name)
        {
            if (StateDict.ContainsKey(state_name))
                return StateDict[state_name];

            StateData state_data = new StateData();
            state_data.Name = state_name;
            state_data.Positive = new float[NumDates];
            state_data.Negative = new float[NumDates];
            state_data.Pending = new float[NumDates];
            state_data.HospitalizedNow = new float[NumDates];
            state_data.HospitalizedTotal = new float[NumDates];
            state_data.IcuNow = new float[NumDates];
            state_data.IcuTotal = new float[NumDates];
            state_data.VentNow = new float[NumDates];
            state_data.VentTotal = new float[NumDates];
            state_data.Recovered = new float[NumDates];
            state_data.Deaths = new float[NumDates];
            state_data.DeathsPerResolution = new float[NumDates];

            StateDict.Add(state_name, state_data);
            return state_data;
        }

        // Create the state data.
        private void CreateStateData(object[,] fields)
        {
            const int colDate = 1;
            const int colState = 2;
            const int colPositive = 3;
            const int colNegative = 4;
            const int colPending = 5;
            const int colHospitalizedNow = 6;
            const int colHospitalizedTotal = 7;
            const int colIcuNow = 8;
            const int colIcuTotal = 9;
            const int colVentNow = 10;
            const int colVentTotal = 11;
            const int colRecovered = 12;
            const int colDeaths = 17;

            // Get the first and last dates.
            int max_row = fields.GetUpperBound(0);
            DateTime last_date = ParseDate(fields[2, colDate].ToString());
            DateTime first_date = ParseDate(fields[max_row, colDate].ToString());
            TimeSpan time_span = last_date - first_date;
            NumDates = (int)time_span.TotalDays + 1;

            StateData.Dates = new DateTime[NumDates + 1];
            for (int day_num = 0; day_num <= NumDates; day_num++)
            {
                StateData.Dates[day_num] = first_date.AddDays(day_num);
            }

            // Create the state's StateData object.
            StateData all_data =
                GetOrCreateStateData("ALL STATES");

            // Load the state data.
            for (int row = 2; row < max_row; row++)
            {
                // Get the state's name.
                string state_name = fields[row, colState].ToString();

                // Get or create the state's StateData object.
                StateData state_data =
                    GetOrCreateStateData(state_name);

                // Find the date number.
                DateTime cur_date = ParseDate(fields[row, colDate].ToString());
                int date_num = (int)(cur_date - first_date).TotalDays;

                state_data.Positive[date_num] = ParseValue(fields[row, colPositive]);
                state_data.Negative[date_num] = ParseValue(fields[row, colNegative]);
                state_data.Pending[date_num] = ParseValue(fields[row, colPending]);
                state_data.HospitalizedNow[date_num] = ParseValue(fields[row, colHospitalizedNow]);
                state_data.HospitalizedTotal[date_num] = ParseValue(fields[row, colHospitalizedTotal]);
                state_data.IcuNow[date_num] = ParseValue(fields[row, colIcuNow]);
                state_data.IcuTotal[date_num] = ParseValue(fields[row, colIcuTotal]);
                state_data.VentNow[date_num] = ParseValue(fields[row, colVentNow]);
                state_data.VentTotal[date_num] = ParseValue(fields[row, colVentTotal]);
                state_data.Recovered[date_num] = ParseValue(fields[row, colRecovered]);
                state_data.Deaths[date_num] = ParseValue(fields[row, colDeaths]);

                if ((state_data.Deaths[date_num] == 0) ||
                    (state_data.Recovered[date_num] == 0))
                {
                    state_data.DeathsPerResolution[date_num] = 0;
                }
                else
                {
                    state_data.DeathsPerResolution[date_num] =
                        state_data.Deaths[date_num] / (
                            state_data.Deaths[date_num] + state_data.Recovered[date_num]);
                }

                // Add to the national totals.
                all_data.Positive[date_num] += state_data.Positive[date_num];
                all_data.Positive[date_num] += state_data.Positive[date_num];
                all_data.Negative[date_num] += state_data.Negative[date_num];
                all_data.Pending[date_num] += state_data.Pending[date_num];
                all_data.HospitalizedNow[date_num] += state_data.HospitalizedNow[date_num];
                all_data.HospitalizedTotal[date_num] += state_data.HospitalizedTotal[date_num];
                all_data.IcuNow[date_num] += state_data.IcuNow[date_num];
                all_data.IcuTotal[date_num] += state_data.IcuTotal[date_num];
                all_data.VentNow[date_num] += state_data.VentNow[date_num];
                all_data.VentTotal[date_num] += state_data.VentTotal[date_num];
                all_data.Recovered[date_num] += state_data.Recovered[date_num];
                all_data.Deaths[date_num] += state_data.Deaths[date_num];
            }

            for (int date_num = 0;
                date_num < all_data.DeathsPerResolution.Length;
                date_num++)
            {
                if ((all_data.Deaths[date_num] == 0) ||
                    (all_data.Recovered[date_num] == 0))
                {
                    all_data.DeathsPerResolution[date_num] = 0;
                }
                else
                {
                    all_data.DeathsPerResolution[date_num] =
                        all_data.Deaths[date_num] / (
                            all_data.Deaths[date_num] + all_data.Recovered[date_num]);
                }
            }

            // Set maximum values.
            foreach (StateData state_data in StateDict.Values)
                state_data.SetMaxDataValues();
        }

        // Parse a dater with format 20200517.
        private DateTime ParseDate(string date_text)
        {
            int year = int.Parse(date_text.Substring(0, 4));
            int month = int.Parse(date_text.Substring(4, 2));
            int day = int.Parse(date_text.Substring(6));
            return new DateTime(year, month, day);
        }

        // Return a value from the CSV file.
        private int ParseValue(object value)
        {
            if (value == null) return 0;
 
            int result;
            if (int.TryParse(value.ToString(), out result)) return result;
            return 0;
        }

        // Download today's data.
        private void DownloadFile(string url, string filename)
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
                    web_client.DownloadFile(url, filename);
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
            StateData checked_state =
                clbStates.Items[e.Index] as StateData;
            SelectedStates = GetStateList(checked_state, e.NewValue);

            // Graph the results.
            GraphStates();

            // Redisplay the tooltip if appropriate.
            SetTooltip(ClosePoint);
        }

        // Get the list of checked items,
        // adding or removing a checked item.
        private List<StateData> GetStateList(
            StateData checked_state, CheckState checked_status)
        {
            // Get the current list of checked items.
            List<StateData> state_list;
            if (clbStates.CheckedItems.Count == 0)
            {
                // Create a new list.
                state_list = new List<StateData>();
            }
            else
            {
                // Convert the selected objects into StateData objects.
                state_list =
                    clbStates.CheckedItems.Cast<StateData>().ToList();
            }

            if (checked_state != null)
            {
                // See if the clicked state is being checked or unchecked.
                if (checked_status == CheckState.Checked)
                {
                    // Add the item to the list.
                    state_list.Add(checked_state);
                }
                else
                {
                    // Remove the item from the list.
                    state_list.Remove(checked_state);
                }
            }

            return state_list;
        }

        // Draw the graph.
        private void GraphStates()
        {
            ClosePoint = new PointF(-1, -1);

            // Do nothing if no states are selected or
            // if no datasets are selected.
            if ((SelectedStates.Count == 0) ||
                (!SelectedDataSets.DataSetsAreSelected))
            {
                picGraph.Image = null;
                return;
            }

            // Get the maximum value.
            foreach (StateData state in SelectedStates)
                state.SetMaxDataValue();
            float y_max = SelectedStates.Max(state => state.MaxDataValue);
            if (y_max < 1) y_max = 1;

            // Create a transformation to make the data fit the PictureBox.
            DefineTransform(SelectedStates, y_max);

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
                    Color.Orange,
                };
                int num_colors = colors.Length;
                using (Pen pen = new Pen(Color.Black, 0))
                {
                    foreach (StateData state in SelectedStates)
                    {
                        pen.Color = colors[state.StateNumber % num_colors];
                        state.Draw(align_cases, gr, pen, Transform, state.Name);
                    }
                }
            }

            // Display the result.
            picGraph.Image = bm;
        }

        private void DefineTransform(List<StateData> state_list, float y_max)
        {
            WorldBounds = new RectangleF(0, 0, NumDates, y_max);
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
                float y_step = (float)Math.Pow(10, power);
                //if (y_step < 1) y_step = 1;

                // Draw the Y axis.
                gr.DrawLine(pen, 0, 0, 0, y_max);

                pen.Color = Color.Silver;
                float num_cases = WorldBounds.Right;
                for (float y = y_step; y < y_max; y += y_step)
                {
                    gr.DrawLine(pen, 0, y, num_cases, y);
                }

                GraphicsState state = gr.Save();
                gr.ResetTransform();
                using (Font font = new Font("Arial", 12, FontStyle.Regular))
                {
                    for (float y = y_step; y < y_max; y += y_step)
                    {
                        PointF[] p = { new PointF(0, y) };
                        Transform.TransformPoints(p);

                        if (y < 1)
                            gr.DrawString(y.ToString("n"), font, Brushes.Black, p[0]);
                        else
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
            for (int i = 0; i < clbStates.Items.Count; i++)
                clbStates.SetItemChecked(i, true);
            IgnoreItemCheck = false;
            RedrawGraph();
        }

        private void btnNone_Click(object sender, EventArgs e)
        {
            IgnoreItemCheck = true;
            for (int i = 0; i < clbStates.Items.Count; i++)
                clbStates.SetItemChecked(i, false);
            IgnoreItemCheck = false;
            RedrawGraph();
        }

        private void RedrawGraph()
        {
            if (IgnoreCheckedChanged) return;

            // Get the current list of checked items.
            SelectedStates = GetStateList(null, CheckState.Indeterminate);

            // Get the checked data items.
            SelectedDataSets.SetSelectedDataSets(this);

            // Graph the results.
            GraphStates();

            // Redisplay the tooltip if appropriate.
            SetTooltip(ClosePoint);
        }

        private void picGraph_MouseMove(object sender, MouseEventArgs e)
        {
            SetTooltip(e.Location);
        }

        private void SetTooltip(PointF point)
        {
            if (picGraph.Image == null) return;
            if (SelectedStates == null) return;

            string new_tip = "";
            int day_num;
            string descr;

            foreach (StateData state in SelectedStates)
            {
                if (state.PointIsAt(point, out day_num,
                    out descr, out ClosePoint))
                {
                    new_tip = state.Name + "\n" +
                        StateData.Dates[day_num].ToShortDateString() + "\n" +
                        descr;
                    if (chkPerMillion.Checked)
                        new_tip += " per million";
                    break;
                }
            }

            if (tipGraph.GetToolTip(picGraph) != new_tip)
                tipGraph.SetToolTip(picGraph, new_tip);
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

        // Redraw the graph aligned on the left.
        private void txtAlignCases_TextChanged(object sender, EventArgs e)
        {
            GraphStates();
        }

        // A sorting radio button has been clicked. Update the display.
        private void radSort_Click(object sender, EventArgs e)
        {
            SortStates();
        }

        // Sort the countries by the selected data.
        private void SortStates()
        {
            if (StateList == null) return;

            // Make the appropriate comparer.
            if (radSortByName.Checked)
                Comparer = new StateDataComparer(StateDataComparer.CompareTypes.ByName);
            else if (radSortByMaxCases.Checked)
                Comparer = new StateDataComparer(StateDataComparer.CompareTypes.ByMaxCases);

            // Redisplay the state list in the new order.
            clbStates.DataSource = null;
            StateList.Sort(Comparer);
            clbStates.DataSource = StateList;

            // Check the currently selected countries.
            foreach (StateData state in SelectedStates)
            {
                int index = clbStates.Items.IndexOf(state);
                if (index >= 0) clbStates.SetItemChecked(index, true);
            }
        }

        private void chkDataSet_CheckedChanged(object sender, EventArgs e)
        {
            RedrawGraph();
        }

        private void btnAllDataSets_Click(object sender, EventArgs e)
        {
            IgnoreCheckedChanged = true;
            foreach (CheckBox chk in CheckBoxes)
                chk.Checked = true;
            IgnoreCheckedChanged = false;
            RedrawGraph();
        }

        private void btnNoDataSets_Click(object sender, EventArgs e)
        {
            IgnoreCheckedChanged = true;
            foreach (CheckBox chk in CheckBoxes)
                chk.Checked = false;
            IgnoreCheckedChanged = false;
            RedrawGraph();
        }
    }
}
