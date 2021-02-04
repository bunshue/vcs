using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization;
using System.Drawing.Drawing2D;

namespace howto_401k_graph
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Compare plans.
        private void btnGo_Click(object sender, EventArgs e)
        {
            decimal annual_contribution = decimal.Parse(
                txtAnnualContribution.Text, NumberStyles.Any);

            richTextBox1.Text += "annual_contribution = " + annual_contribution.ToString() + "\n";

            decimal tax_rate =
                decimal.Parse(txtTaxRate.Text.Replace("%", ""),
                    NumberStyles.Any) / 100;

            richTextBox1.Text += "tax_rate = " + tax_rate.ToString() + "\n";

            if (tax_rate >= 1)
                tax_rate /= 100;

            richTextBox1.Text += "tax_rate = " + tax_rate.ToString() + "\n";

            decimal interest_rate =
                decimal.Parse(txtInterestRate.Text.Replace("%", ""),
                    NumberStyles.Any) / 100;

            richTextBox1.Text += "interest_rate = " + interest_rate.ToString() + "\n";

            if (interest_rate >= 1) interest_rate /= 100;

            richTextBox1.Text += "interest_rate = " + interest_rate.ToString() + "\n";

            int num_years = (int)nudYears.Value;

            richTextBox1.Text += "num_years = " + num_years.ToString() + "\n";

            decimal balance_bank = 0;
            decimal balance_401k = 0;
            decimal balance_roth = 0;

            // Generate the data points.
            PointF[] pt_bank = new PointF[num_years * 2];
            PointF[] pt_401k = new PointF[num_years + 1];
            PointF[] pt_roth = new PointF[num_years + 1];
            for (int year = 0; year < num_years; year++)
            {
                // Bank balance += interest + contribution, ...
                decimal interest = balance_bank * interest_rate;
                balance_bank += interest + annual_contribution;
                pt_bank[2 * year] = new PointF(year, (float)balance_bank);

                // ... minus taxes on the interest and contribution.
                balance_bank -= tax_rate * (interest + annual_contribution);
                pt_bank[2 * year + 1] = new PointF(year, (float)balance_bank);

                // 401(k) balance += interest + contribution.
                balance_401k += (balance_401k * interest_rate + annual_contribution);
                pt_401k[year] = new PointF(year, (float)balance_401k);

                // Roth balance += interest + contribution - taxes on contribution.
                balance_roth += balance_roth * interest_rate +
                    annual_contribution * (1 - tax_rate);
                pt_roth[year] = new PointF(year, (float)balance_roth);
            }

            // Display the final results.
            txtFinalSavings.Text = balance_bank.ToString("c");
            richTextBox1.Text += "(1) balance_bank = " + balance_bank.ToString() + "\n";
            txtFinal401k.Text = balance_401k.ToString("c");
            richTextBox1.Text += "(2) balance_401k = " + balance_401k.ToString() + "\n";
            txtFinalRoth.Text = balance_roth.ToString("c");
            richTextBox1.Text += "(4) balance_roth = " + balance_roth.ToString() + "\n";

            // Add the final point after removing taxes from the 401(k).
            decimal penalty =
                decimal.Parse(txtPenalty.Text.Replace("%", ""),
                    NumberStyles.Any) / 100;

            richTextBox1.Text += "penalty = " + penalty.ToString() + "\n";
            if (penalty >= 1) penalty /= 100;
            richTextBox1.Text += "penalty = " + penalty.ToString() + "\n";

            decimal tax_at_end =
                decimal.Parse(txtTaxAtEnd.Text.Replace("%", ""),
                    NumberStyles.Any) / 100;

            richTextBox1.Text += "tax_at_end = " + tax_at_end.ToString() + "\n";
            if (tax_at_end >= 1) tax_at_end /= 100;
            richTextBox1.Text += "tax_at_end = " + tax_at_end.ToString() + "\n\n";


            balance_401k *= 1 - (penalty + tax_at_end);
            pt_401k[num_years] = new PointF(num_years - 1, (float)balance_401k);

            balance_roth *= 1 - penalty;
            pt_roth[num_years] = new PointF(num_years - 1, (float)balance_roth);

            // Display the final surrender values.
            txt401kSurrendered.Text = balance_401k.ToString("c");
            richTextBox1.Text += "(3)balance_401k = " + balance_401k.ToString() + "\n";
            txtRothSurrendered.Text = balance_roth.ToString("c");
            richTextBox1.Text += "(5)balance_roth = " + balance_roth.ToString() + "\n";

            // Plot the results.
            // Find a reasonable scale.
            float scale_x = picGraph.ClientSize.Width / num_years;
            float scale_y = picGraph.ClientSize.Height / pt_401k[num_years - 1].Y;
            scale_y *= 0.95f;

            Bitmap bm = new Bitmap(picGraph.ClientSize.Width, picGraph.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Scale the image.
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.ScaleTransform(scale_x, -scale_y);

                // Translate the image so it shows.
                //gr.TranslateTransform(0, pt_401k[2 * num_years - 1].Y,
                //    MatrixOrder.Append);
                gr.TranslateTransform(0,
                    picGraph.ClientSize.Height - 3,
                    MatrixOrder.Append);

                // Draw the curves.
                gr.DrawLines(Pens.Red, pt_bank);
                gr.DrawLines(Pens.Blue, pt_401k);
                gr.DrawLines(Pens.Green, pt_roth);

                // Transform the final points.
                PointF[] transformed_points = new PointF[3];
                transformed_points[0] = pt_bank[2 * num_years - 1];
                transformed_points[1] = pt_401k[num_years];
                transformed_points[2] = pt_roth[num_years];
                gr.Transform.TransformPoints(transformed_points);

                // Draw the final values.
                gr.ResetTransform();
                gr.FillEllipse(Brushes.Red,
                    transformed_points[0].X - 2,
                    transformed_points[0].Y - 2,
                    5, 5);
                gr.FillEllipse(Brushes.Blue,
                    transformed_points[1].X - 2,
                    transformed_points[1].Y - 2,
                    5, 5);
                gr.FillEllipse(Brushes.Green,
                    transformed_points[2].X - 2,
                    transformed_points[2].Y - 2,
                    5, 5);
            }

            // Display the result.
            picGraph.Image = bm;
        }
    }
}
