using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.CodeDom.Compiler;
using System.Reflection;

namespace vcs_Draw_ToolTip1
{
    public partial class Form1 : Form
    {
        // The transformation and inverse.
        private Matrix Transform = null, Inverse = null;

        // The compiled function.
        private MethodInfo Function = null;

        public Form1()
        {
            InitializeComponent();
        }

        // Draw the graph.
        private void Form1_Load(object sender, EventArgs e)
        {
            MakeGraph();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            MakeGraph();
        }

        private void btnGraph_Click(object sender, EventArgs e)
        {
            MakeGraph();
        }

        // Make the graph.
        private void MakeGraph()
        {
            // Get the bounds.
            float xmin = float.Parse(txtXmin.Text);
            float xmax = float.Parse(txtXmax.Text);
            float ymin = float.Parse(txtYmin.Text);
            float ymax = float.Parse(txtYmax.Text);

            // Make the Bitmap.
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Transform to map the graph bounds to the Bitmap.
                RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);
                PointF[] pts = 
                {
                    new PointF(0, H),
                    new PointF(W, H),
                    new PointF(0, 0),
                };
                g.Transform = new Matrix(rect, pts);

                // Draw the graph.
                using (Pen p = new Pen(Color.Blue, 0))
                {
                    // Draw the axes.
                    g.DrawLine(p, xmin, 0, xmax, 0);
                    g.DrawLine(p, 0, ymin, 0, ymax);
                    p.Color = Color.Red;

                    // See how big 1 pixel is horizontally.
                    Transform = g.Transform;
                    Inverse = g.Transform;
                    Inverse.Invert();
                    PointF[] pixel_pts =
                    {
                        new PointF(0, 0),
                        new PointF(1, 0)
                    };
                    Inverse.TransformPoints(pixel_pts);
                    float dx = pixel_pts[1].X - pixel_pts[0].X;
                    dx /= 2;

                    // Compile the function.
                    Function = null;
                    try
                    {
                        Function = CompileFunction(txtEquation.Text);
                    }
                    catch (Exception ex)
                    {
                        // If we couldn't compile the code, give up.
                        Function = null;
                        MessageBox.Show(ex.Message, "Expression Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        return;
                    }

                    // Loop over x values to generate points.
                    List<PointF> points = new List<PointF>();
                    for (float x = xmin; x <= xmax; x += dx)
                    {
                        bool valid_point = false;
                        try
                        {
                            // Get the next point.
                            float y = F(Function, x);

                            // If the slope is reasonable, this is a valid point.
                            if (points.Count == 0)
                            {
                                valid_point = true;
                            }
                            else
                            {
                                float dy = y - points[points.Count - 1].Y;
                                if (Math.Abs(dy / dx) < 1000)
                                {
                                    valid_point = true;
                                }
                            }
                            if (valid_point)
                            {
                                points.Add(new PointF(x, y));
                            }
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show("Error evaluating function.\n" + ex.Message, "Error Evaluating Function", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                        // If the new point is invalid, draw
                        // the points in the latest batch.
                        if (!valid_point)
                        {
                            if (points.Count > 1)
                            {
                                g.DrawLines(p, points.ToArray());
                            }
                            points.Clear();
                        }
                    }

                    // Draw the last batch of points.
                    if (points.Count > 1)
                    {
                        g.DrawLines(p, points.ToArray());
                    }
                }
            }
            // Display the result.
            pictureBox1.Image = bitmap1;
        }

        // The function to graph.
        private float F(MethodInfo function, float x)
        {
            double result = (double)function.Invoke(null, new object[] { x });
            return (float)result;
        }

        // Compile the function and return a MethodInfo to execute it.
        private MethodInfo CompileFunction(string equation_text)
        {
            // Turn the equation into a function.
            string function_text =
                "using System;" +
                "public static class Evaluator" +
                "{" +
                "    public static double Evaluate(double x)" +
                "    {" +
                "        return " + equation_text + ";" +
                "    }" +
                "}";

            // Compile the function.
            CodeDomProvider code_provider = CodeDomProvider.CreateProvider("C#");

            // Generate a non-executable assembly in memory.
            CompilerParameters parameters = new CompilerParameters();
            parameters.GenerateInMemory = true;
            parameters.GenerateExecutable = false;

            // Compile the code.
            CompilerResults results = code_provider.CompileAssemblyFromSource(parameters, function_text);

            // If there are errors, display them.
            if (results.Errors.Count > 0)
            {
                string msg = "Error compiling the expression.";
                foreach (CompilerError compiler_error in results.Errors)
                {
                    msg += "\n" + compiler_error.ErrorText;
                }
                throw new InvalidProgramException(msg);
            }
            else
            {
                // Get the Evaluator class type.
                Type evaluator_type = results.CompiledAssembly.GetType("Evaluator");

                // Get a MethodInfo object describing the Evaluate method.
                return evaluator_type.GetMethod("Evaluate");
            }
        }

        // If the mouse is over the curve,
        // display a tooltip showing the curve's value.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Get the tooltip that we should display.
            string tooltip = GetGraphToolTip(e.Location);

            // See if the tooltip has changed.
            string old_tooltip = toolTip1.GetToolTip(pictureBox1);
            if (old_tooltip == tooltip)
            {
                return;
            }

            // Display the new tooltip.
            toolTip1.SetToolTip(pictureBox1, tooltip);
        }

        // Get the tooltip for the point in device coordinates.
        // Return null if the point isn't on the curve.
        private string GetGraphToolTip(Point point)
        {
            if (Function == null)
            {
                return null;
            }

            // Convert the mouse's location into world coordinates.
            PointF[] world_points = { point };
            Inverse.TransformPoints(world_points);

            // Find the Y coordinate in device coordinates.
            float x = world_points[0].X;
            float y = F(Function, x);
            PointF[] device_points = { new PointF(x, y) };
            Transform.TransformPoints(device_points);

            // See if the mouse's position is within
            // five pixels of this point's location.
            if (Math.Abs(point.Y - device_points[0].Y) > 10)
            {
                return null;
            }

            // Compose the tooltip.
            return "(" + x.ToString("0.00") + ", " + y.ToString("0.00") + ")";
        }
    }
}

