using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

using delRendererFunction = Plot3D.Graph3D.delRendererFunction;
using cPoint3D            = Plot3D.Graph3D.cPoint3D;
using eRaster             = Plot3D.Graph3D.eRaster;
using eNormalize          = Plot3D.Graph3D.eNormalize;
using eSchema             = Plot3D.ColorSchema.eSchema;

namespace Plot3D
{
    public partial class Graph3DMainForm : Form
    {
        public Graph3DMainForm()
        {
            InitializeComponent();
        }

        protected override void OnLoad(EventArgs e)
        {
            base.OnLoad(e);

            // This is optional. If you don't want to use Trackbars leave this away.
            graph3D.AssignTrackBars(trackRho, trackTheta, trackPhi);

            // This is option. If you don't want a legend leave this away.
            graph3D.EnableLegend(Color.FromArgb(255, 200, 200, 150));

            comboRaster.Sorted = false;
            foreach (eRaster e_Raster in Enum.GetValues(typeof(eRaster)))
            {
                comboRaster.Items.Add(e_Raster);
            }
            comboRaster.SelectedIndex = (int)eRaster.Off;

            comboColors.Sorted = false;
            foreach (eSchema e_Schema in Enum.GetValues(typeof(eSchema)))
            {
                comboColors.Items.Add(e_Schema);
            }
            comboColors.SelectedIndex = (int)eSchema.Rainbow1;

            comboDataSrc.SelectedIndex = 0; // set "Callback"
        }

        private void comboDataSrc_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboDataSrc.SelectedIndex)
            {
                case 0: 
                    comboRaster.SelectedIndex = (int)eRaster.Off; // FIRST
                    comboRaster.Enabled = false; // Coord System does not work with negative values
                    SetCallback(); // AFTER
                    break;
                case 1: 
                    comboRaster.SelectedIndex = (int)eRaster.Off; // FIRST
                    comboRaster.Enabled = false; // Coord System does not work with negative values
                    SetFormula(); // AFTER 
                    break;
                case 2: 
                    comboRaster.SelectedIndex = (int)eRaster.Labels; // FIRST
                    comboRaster.Enabled = true;
                    SetFixValues(); // AFTER
                    break;
            }
        }

        private void comboColors_SelectedIndexChanged(object sender, EventArgs e)
        {
            graph3D.ColorSchema = ColorSchema.GetSchema((eSchema)comboColors.SelectedIndex);
        }

        private void comboRaster_SelectedIndexChanged(object sender, EventArgs e)
        {
            graph3D.Raster = (eRaster)comboRaster.SelectedIndex;
        }

        private void checkFitScreen_CheckedChanged(object sender, EventArgs e)
        {
            graph3D.AutoFitScreen = checkAutoFitScreen.Checked;
        }

        // ================================================================================================

        /// <summary>
        /// This demonstrates how to use a callback function which calculates Z values from X and Y
        /// </summary>
        private void SetCallback()
        {
            delRendererFunction f_Callback = delegate(double X, double Y)
            {
                double r = 0.15 * Math.Sqrt(X * X + Y * Y);
                if (r < 1e-10) return 120;
                else           return 120 * Math.Sin(r) / r;
            };

            // IMPORTANT: Do not set AdaptZ otherwise Z values from the function will be distorted
            graph3D.SetFunction(f_Callback, new PointF(-120, -80), new PointF(120, 80), 5, eNormalize.Center);

            lblPolygons.Text = "Polygons: " + graph3D.PolygonCount;
        }

        /// <summary>
        /// This demonstrates how to use a string formula which calculates Z values from X and Y
        /// </summary>
        private void SetFormula()
        {
            String s_Formula = "12 * sin(x) * cos(y) / (sqrt(sqrt(x * x + y * y)) + 0.2)";
            CompiledFunction f_Compiled = FunctionCompiler.Compile(s_Formula);
            
            delRendererFunction f_Function = delegate(double X, double Y)
            {
                return f_Compiled(X, Y);
            };

            // IMPORTANT: Do not set AdaptZ otherwise Z values from the formula will be distorted
            graph3D.SetFunction(f_Function, new PointF(-10, -10), new PointF(10, 10), 0.5, eNormalize.Center);

            lblPolygons.Text = "Polygons: " + graph3D.PolygonCount;
        }

        /// <summary>
        /// This demonstrates how to set X, Y, Z values directly (without function)
        /// </summary>
        private void SetFixValues()
        {
            int[,] s32_Values = new int[,]
            {
                { 9059,   9634, 10617, 11141, 11838, 12681, 13411, 13861, 14121, 14624, 14868, 15172, 15368, 15368, 15368, 15368, 15368 },
                { 9684,  10387, 11141, 11796, 12546, 13337, 14029, 14320, 14549, 14811, 14939, 15434, 15794, 15794, 15794, 15794, 15794 },
                { 10486, 11370, 12255, 13009, 13861, 14746, 15172, 15368, 15434, 15630, 15794, 15991, 16351, 16351, 16351, 16351, 16351 },
                { 11469, 12354, 13533, 14287, 15008, 15925, 16187, 16482, 16690, 16976, 17105, 17302, 17531, 17531, 17531, 17531, 17531 },
                { 12452, 13435, 14615, 15499, 16253, 17105, 17596, 17924, 18153, 18285, 18428, 18776, 19104, 19104, 19104, 19104, 19104 },
                { 13337, 14516, 15729, 16679, 17564, 18514, 18907, 19169, 19399, 19661, 19792, 19594, 20152, 20152, 20152, 20152, 20152 },
                { 14746, 15860, 17039, 17990, 18842, 19595, 20050, 20349, 20546, 20840, 20972, 20972, 21332, 21332, 21332, 21332, 21332 },
                { 16155, 17236, 18350, 19399, 20251, 20677, 21016, 21332, 21660, 21791, 21889, 21955, 22217, 22217, 22217, 22217, 22217 },
                { 17334, 18579, 19497, 20775, 21463, 21848, 22288, 22446, 22643, 22446, 22643, 22708, 23069, 23069, 23069, 23069, 23069 },
                { 18743, 19792, 20808, 22086, 22805, 23167, 23486, 23366, 23757, 23411, 23691, 23822, 23822, 23822, 23822, 23822, 23822 },
                { 20677, 21445, 22544, 23593, 24441, 24785, 24538, 24644, 24773, 24299, 24062, 24576, 24510, 24510, 24510, 24510, 24510 },
                { 23475, 23888, 24478, 25330, 26212, 26199, 25701, 25664, 25740, 25013, 24904, 25068, 25374, 25374, 25374, 25374, 25374 },
                { 27525, 27518, 26701, 27334, 27682, 27402, 26903, 26707, 26444, 25887, 25719, 25690, 26122, 26122, 26122, 26122, 26122 },
                { 30769, 30423, 29917, 29231, 29392, 28705, 28075, 27726, 27263, 26691, 26417, 26182, 26575, 26575, 25246, 25246, 25246 },
                { 32672, 32178, 31916, 31469, 31246, 30540, 29852, 29065, 28377, 27623, 27263, 26706, 26935, 26367, 25049, 25049, 25049 },
                { 33522, 33227, 32702, 32615, 32452, 31851, 30933, 30179, 29295, 28358, 27984, 27132, 27301, 26367, 25049, 25049, 25049 },
                { 33980, 33587, 33161, 32935, 32588, 32342, 31621, 30802, 29852, 29000, 28377, 27689, 27421, 26367, 25049, 25049, 25049 },
                { 34210, 33784, 33423, 33161, 32801, 32408, 31785, 31097, 30474, 29622, 29000, 28115, 27623, 26367, 25049, 25049, 25049 },
                { 34472, 34079, 33653, 33161, 32768, 32408, 31785, 31162, 30802, 30048, 29360, 28312, 27755, 26367, 25049, 25049, 25049 },
                { 34603, 34144, 33718, 33227, 32768, 32342, 31719, 30999, 31228, 30333, 29622, 28606, 27886, 26492, 25167, 25167, 25167 },
                { 34669, 34210, 33653, 33096, 32539, 32047, 31490, 30933, 31293, 30671, 29983, 28803, 27886, 26492, 25167, 25167, 25167 },
                { 34767, 34210, 33718, 33096, 32342, 31851, 31228, 30867, 31457, 30867, 30266, 28934, 27984, 26492, 25167, 25167, 25167 }
            };

            cPoint3D[,] i_Points3D = new cPoint3D[s32_Values.GetLength(0), s32_Values.GetLength(1)];
            for (int X=0; X<s32_Values.GetLength(0); X++)
            {
                for (int Y=0; Y<s32_Values.GetLength(1); Y++)
                {
                    i_Points3D[X,Y] = new cPoint3D(X * 100, Y * 100, s32_Values[X,Y]);
                }
            }

            // IMPORTANT: set AdaptZ because there is an extreme mismatch between X,Y values (< 30) and Z values (> 30000)
            graph3D.SetValues(i_Points3D, eNormalize.CenterAdaptZ);

            lblPolygons.Text = "Polygons: " + graph3D.PolygonCount;
        }
    }
}
