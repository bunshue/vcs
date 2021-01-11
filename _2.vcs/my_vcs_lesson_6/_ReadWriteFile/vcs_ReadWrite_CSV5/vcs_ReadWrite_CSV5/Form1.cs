using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;

namespace vcs_ReadWrite_CSV5
{
    public partial class Form1 : Form
    {
        // Structure to hold price data.
        private struct PriceData
        {
            public DateTime Date;
            public float Price;
            public PriceData(DateTime new_Date, float new_Price)
            {
                Date = new_Date;
                Price = new_Price;
            }
        };

        public Form1()
        {
            InitializeComponent();
        }

        // The historical prices.
        private List<PriceData> Prices;

        // Investment information.
        private List<PointF[]> Investments;
        private List<string> InvestmentNames;
        private List<Color> InvestmentColors;
        private const float InitialInvestment = 4000;   // The money we start with.
        private const float BaseInterestRate = 0.01f;   // Interest rate for uninvested money.

        // Draw the graph.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Load the data.
            Prices = GetDjiPrices();

            // Make investments.
            MakeInvestments();

            DrawGraph();
        }

        // Draw the graph.
        private void picRefresh_Click(object sender, EventArgs e)
        {
            DrawGraph();
        }

        // Draw the graph.
        private void DrawGraph()
        {
            this.Cursor = Cursors.WaitCursor;

            // Graph it.
            DrawGraph(Prices);

            this.Cursor = Cursors.Default;
        }

        // Get the historical prices.
        private List<PriceData> GetDjiPrices()
        {
            // Get the data by lines.
            string[] lines = File.ReadAllLines("DjiPrices.csv");

            // See which header fields contains Date and Adj Close.
            string[] fields = lines[0].Split(',');
            int date_field = -1, close_field = -1;
            for (int i = 0; i < fields.Length; i++)
            {
                if (fields[i].ToLower() == "adj close")
                    close_field = i;
                else if (fields[i].ToLower() == "date")
                    date_field = i;
            }

            // Process the lines, skipping the header.
            List<PriceData> price_data = new List<PriceData>();
            for (int i = 1; i < lines.Length; i++)
            {
                fields = lines[i].Split(',');
                price_data.Add(new PriceData(
                    DateTime.Parse(fields[date_field]),
                    float.Parse(fields[close_field])));
            }

            // Reverse so the data is in historical order.
            price_data.Reverse();
            return price_data;
        }

        // Draw the graph.
        private void DrawGraph(List<PriceData> price_data)
        {
            // Make the bitmap.
            Bitmap bm = new Bitmap(
                picGraph.ClientSize.Width,
                picGraph.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Get the largest price.
                var max_query = from PriceData data in price_data select data.Price;
                float max_price = max_query.Max() + 500;
                for (int i = 0; i < Investments.Count; i++)
                {
                    var test_query = from PointF pt in Investments[i] select pt.Y;
                    float test_max = test_query.Max() + 500;
                    if (max_price < test_max) max_price = test_max;
                }


                // Scale and translate the graph.
                float scale_x = picGraph.ClientSize.Width / (float)price_data.Count;
                float scale_y = -picGraph.ClientSize.Height / max_price;
                gr.ScaleTransform(scale_x, scale_y);
                gr.TranslateTransform(
                    0,
                    picGraph.ClientSize.Height,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                using (Pen thin_pen = new Pen(Color.Gray, 0))
                {
                    // Draw the horizontal grid lines.
                    for (int y = 0; y <= max_price; y += 1000)
                    {
                        // Draw the line.
                        gr.DrawLine(thin_pen, 0, y, price_data.Count, y);

                        // Draw the value.
                        if (y > 0)
                            DrawTextAt(gr, y.ToString("C"), 10, y, Color.Blue,
                                StringAlignment.Near, StringAlignment.Far);
                    }

                    // Draw the vertical grid lines.
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        int last_year = 0;
                        for (int i = 0; i < price_data.Count; i++)
                        {
                            // See if this is the start of a new year.
                            if (price_data[i].Date.Year > last_year)
                            {
                                last_year = price_data[i].Date.Year;

                                // Draw a line for the year.
                                gr.DrawLine(thin_pen, i, 0, i, 750);

                                // Draw the year number.
                                DrawTextAt(gr, last_year.ToString(), i, 0, Color.Blue,
                                    StringAlignment.Center, StringAlignment.Far);
                            }
                        }
                    }
                }

                //// Draw the prices. Make the data points.
                //PointF[] points = new PointF[price_data.Count];
                //for (int i = 0; i < price_data.Count; i++)
                //{
                //    points[i] = new PointF(i, price_data[i].Price);
                //}

                //// Draw the points.
                //using (Pen thin_pen = new Pen(Color.Black, 0))
                //{
                //    gr.DrawLines(thin_pen, points);
                //}

                // Draw investments.
                float label_y = (int)(max_price / 1000 - 1) * 1000;
                using (Pen thin_pen = new Pen(Color.Red, 0))
                {
                    int num_periods = Investments[0].Length;
                    for (int i = 0; i < Investments.Count; i++)
                    {
                        // Draw the graph for this investment.
                        thin_pen.Color = InvestmentColors[i];
                        gr.DrawLines(thin_pen, Investments[i]);

                        // Draw the investment's name and return.
                        DrawTextAt(gr, InvestmentNames[i], 500,
                            label_y, InvestmentColors[i],
                            StringAlignment.Near, StringAlignment.Far);
                        float end_balance = Investments[i][num_periods - 1].Y;
                        float pct = 100 * (end_balance - InitialInvestment) / InitialInvestment;
                        DrawTextAt(gr, pct.ToString("0.00") + "%", 1700,
                            label_y, InvestmentColors[i],
                            StringAlignment.Near, StringAlignment.Far);
                        label_y -= 1000;
                    }
                }
            }

            // Display the result.
            picGraph.Image = bm;
        }

        // Draw the text at the specified location.
        private void DrawTextAt(Graphics gr, string txt, float x, float y, Color clr, StringAlignment alignment, StringAlignment line_alignment)
        {
            // See where the point is in PictureBox coordinates.
            Matrix old_transformation = gr.Transform;
            PointF[] pt = { new PointF(x, y) };
            gr.Transform.TransformPoints(pt);

            // Reset the transformation.
            gr.ResetTransform();

            // Draw the text.
            using (Font small_font = new Font("Arial", 8))
            {
                using (SolidBrush br = new SolidBrush(clr))
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = alignment;
                        string_format.LineAlignment = line_alignment;
                        gr.DrawString(txt, small_font, br, pt[0].X, pt[0].Y, string_format);
                    }
                }
            }

            // Restore the original transformation.
            gr.Transform = old_transformation;
        }

        // Make investments using different strategies.
        private void MakeInvestments()
        {
            // Make room for the results.
            int num_points = Prices.Count;
            Investments = new List<PointF[]>();
            InvestmentNames = new List<string>();
            InvestmentColors = new List<Color>();

            // Strategy: All in at the start.
            StrategyAllIn();

            // Strategy: Fixed interest.
            StrategyInterest(0.05f);

            // Strategy: Fixed amount per period.
            StrategyFixedPerPeriod(100);

            //// Strategy: $100 every time there is a streak of down periods in a row.
            //StrategyDownStreak(2, Color.Orange);

            // Strategy: $100 every time there is a streak of down periods in a row.
            StrategyDownStreak(3, Color.Blue);

            //// Strategy: $100 when down by a given percent.
            //StrategyDownPercent(0.002f, Color.Plum);

            // Strategy: $100 when down by a given percent.
            StrategyDownPercent(0.001f, Color.Purple);

            // Strategy: $100 when down by $10.
            StrategyDownAmount(10, 100, Color.Brown);

            //// Strategy: $100 every time there is a streak of up periods in a row.
            //StrategyUpStreak(2, Color.Orange);

            // Strategy: $100 every time there is a streak of up periods in a row.
            StrategyUpStreak(3, Color.Orange);

            // Make perfect guesses.
            StrategyPerfectGuess(100, Color.Black);
        }

        // Strategy: 5% interest.
        private void StrategyInterest(float interest_rate)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;

            InvestmentNames.Add(interest_rate * 100 + "% interest");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(Color.Gray);

            for (int i = 0; i < num_points; i++)
            {
                // If this is a new year, add interest.
                if (i > 0)
                {
                    if (Prices[i].Date.Year > Prices[i - 1].Date.Year)
                    {
                        money_left += money_left * interest_rate;
                    }
                }
                Investments[investment_num][i] = new PointF(i, money_left);
            }
        }

        // Strategy: All in at the start.
        private void StrategyAllIn()
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;

            InvestmentNames.Add("All In");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(Color.Red);
            investment_num = Investments.Count - 1;
            float shares = InitialInvestment / Prices[0].Price;
            for (int i = 0; i < num_points; i++)
            {
                Investments[investment_num][i] = new PointF(i, shares * Prices[i].Price);
            }
        }

        // Strategy: $10 per period.
        private void StrategyFixedPerPeriod(float amount)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + amount + " per period");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(Color.Green);
            investment_num = Investments.Count - 1;
            for (int i = 0; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);
                BuyShares(ref money_left, ref shares, amount, Prices[i].Price);
                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 every time there is a streak of down periods in a row.
        // The best number depends on the data. For this data, 3 periods works.
        // For data that doesn't include the big drops at the end, 2 works better.
        private void StrategyDownStreak(int num_down, Color clr)
        {
            const float investment_per_period = 100;
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + investment_per_period + " per " + num_down + " down periods");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            shares = 0;
            money_left = InitialInvestment;
            for (int i = 0; i < num_down; i++)
            {
                AddBaseInterest(i, ref money_left);
                Investments[investment_num][i] = new PointF(i, money_left);
            }
            for (int i = num_down; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                // See if the last num_down periods were declines.
                bool all_down = true;
                for (int look_back = 0; look_back < num_down; look_back++)
                {
                    // See if this period was not a decline.
                    if (Prices[i - look_back].Price >= Prices[i - look_back - 1].Price)
                    {
                        all_down = false;
                    }
                }

                // If all periods were declines, invest.
                if (all_down)
                {
                    BuyShares(ref money_left, ref shares, investment_per_period, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 when down by a given percent.
        private void StrategyDownPercent(float target_down_percent, Color clr)
        {
            const float investment_per_period = 10;
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + investment_per_period + " when down by " + target_down_percent * 100 + "%");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            Investments[investment_num][0] = new PointF(0, money_left);
            for (int i = 1; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                float percent_down = (Prices[i - 1].Price - Prices[i].Price) / Prices[i - 1].Price;
                if (percent_down > target_down_percent)
                {
                    BuyShares(ref money_left, ref shares, investment_per_period, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 when down by a given amount.
        private void StrategyDownAmount(float down_amount, float amount, Color clr)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + amount + " when down by $" + down_amount);
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            Investments[investment_num][0] = new PointF(0, money_left);
            for (int i = 1; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                float amount_down = Prices[i - 1].Price - Prices[i].Price;
                if (amount_down > down_amount)
                {
                    BuyShares(ref money_left, ref shares, amount, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 every time there is a streak of up periods in a row.
        private void StrategyUpStreak(int num_up, Color clr)
        {
            const float investment_per_period = 100;
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + investment_per_period + " per " + num_up + " up periods");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            shares = 0;
            money_left = InitialInvestment;
            for (int i = 0; i < num_up; i++)
            {
                AddBaseInterest(i, ref money_left);
                Investments[investment_num][i] = new PointF(i, money_left);
            }
            for (int i = num_up; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                // See if the last num_up periods were increases.
                bool all_up = true;
                for (int look_back = 0; look_back < num_up; look_back++)
                {
                    // See if this period was not an increase.
                    if (Prices[i - look_back].Price <= Prices[i - look_back - 1].Price)
                    {
                        all_up = false;
                    }
                }
                // If all periods were increases, invest.
                if (all_up)
                {
                    BuyShares(ref money_left, ref shares, investment_per_period, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: Invest whenever the price is about to go up by more than the base interest rate.
        private void StrategyPerfectGuess(float amount, Color clr)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + amount + " if increase > " + BaseInterestRate * 100 + "%");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            shares = 0;
            money_left = InitialInvestment;
            for (int i = 0; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                // See what the increase will be in the next period.
                if (i < num_points - 1)
                {
                    float increase_percent = (Prices[i + 1].Price - Prices[i].Price) / Prices[i].Price;
                    if (increase_percent > BaseInterestRate)
                    {
                        BuyShares(ref money_left, ref shares, amount, Prices[i].Price);
                    }
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // If it's a new year, add base interest.
        private void AddBaseInterest(int period_number, ref float money_left)
        {
            if (period_number > 0)
            {
                if (Prices[period_number].Date.Year > Prices[period_number - 1].Date.Year)
                {
                    money_left += money_left * BaseInterestRate;
                }
            }
        }

        // Buy shares.
        private void BuyShares(ref float money_left, ref float shares, float investment_per_period, float price)
        {
            if (money_left < investment_per_period)
            {
                shares += money_left / price;
                money_left = 0;
            }
            else
            {
                shares += investment_per_period / price;
                money_left -= investment_per_period;
            }
        }
    }
}
