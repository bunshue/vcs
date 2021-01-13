using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace howto_covid19_all_rev1
{
    public class CountryData
    {
        static public DateTime[] Dates = null;
        public string Name = null;
        public float[] SelectedData = null;
        public float[] Cases = null;
        public float[] CasesPerMillion = null;
        public float[] Deaths = null;
        public float[] DeathsPerMillion = null;
        public float[] Recoveries = null;
        public float[] RecoveriesPerMillion = null;
        public float[] DeathsPerResolution = null;
        public float MaxDataValue = 0;
        public int CountryNumber = -1;
        public int FirstDrawnDate = -1;
        public long Population = -1;

        public PointF[] DeviceCoords = null;

        // The kinds of data we can select.
        public enum DataSets
        {
            Cases,
            CasesPerMillion,
            Deaths,
            DeathsPerMillion,
            Recoveries,
            RecoveriesPerMillion,
            DeathsPerResolution,
        }

        public override string ToString()
        {
            //return Name + " (" + Population.ToString("n0") + ")";
            return Name;
        }

        public void SetMax()
        {
            if (SelectedData == null)
                MaxDataValue = 0;
            else
                MaxDataValue = SelectedData.Max();
        }

        // Draw this country's data.
        public void Draw(int align_cases, Graphics gr, Pen pen, Matrix transform)
        {
            // Find the first date with align_cases cases.
            FirstDrawnDate = -1;
            int num_cases = Cases.Length;
            for (int i = 0; i < num_cases; i++)
                if (Cases[i] >= align_cases)
                {
                    FirstDrawnDate = i;
                    break;
                }

            // Don't draw unless we have at least one day of data left.
            if ((FirstDrawnDate < 0) || (FirstDrawnDate >= num_cases - 1)) return;

            // Make the points.
            List<PointF> point_list = new List<PointF>();
            for (int i = FirstDrawnDate; i < num_cases; i++)
                point_list.Add(new PointF(i - FirstDrawnDate, SelectedData[i]));
            PointF[] points = point_list.ToArray();

            // Draw the curve.
            gr.DrawLines(pen, points);

            // Find device coordinates for tooltips.
            transform.TransformPoints(points);
            DeviceCoords = points;
        }

        public bool PointIsAt(PointF device_point, out int day_num,
            out float data_value, out PointF close_point)
        {
            if (FirstDrawnDate >= 0)
            {
                const double close_dist = 4;
                PointF closest;
                for (int i = FirstDrawnDate + 1; i < SelectedData.Length; i++)
                {
                    int coord_num = i - FirstDrawnDate;
                    double dist = FindDistanceToSegment(device_point,
                        DeviceCoords[coord_num - 1], DeviceCoords[coord_num], out closest);
                    if (dist <= close_dist)
                    {
                        // See whether it is closer to this this
                        // segment's left or right point.
                        if (DistanceBetweenPoints(DeviceCoords[coord_num - 1], closest) <
                            DistanceBetweenPoints(DeviceCoords[coord_num], closest))
                            coord_num--;
                        day_num = coord_num + FirstDrawnDate;
                        data_value = SelectedData[day_num];

                        // Use the point on the segment.
                        //close_point = closest;

                        // Use the closer segment end point.
                        close_point = DeviceCoords[coord_num];
                        return true;
                    }
                }
            }

            day_num = -1;
            data_value = -1;
            close_point = new PointF(-1, -1);
            return false;
        }

        // http://csharphelper.com/blog/2016/09/find-the-shortest-distance-between-a-point-and-a-line-segment-in-c/
        // Calculate the distance between
        // point pt and the segment p1 --> p2.
        private double FindDistanceToSegment(
            PointF pt, PointF p1, PointF p2, out PointF closest)
        {
            float dx = p2.X - p1.X;
            float dy = p2.Y - p1.Y;
            if ((dx == 0) && (dy == 0))
            {
                // It's a point not a line segment.
                closest = p1;
                dx = pt.X - p1.X;
                dy = pt.Y - p1.Y;
                return Math.Sqrt(dx * dx + dy * dy);
            }

            // Calculate the t that minimizes the distance.
            float t = ((pt.X - p1.X) * dx + (pt.Y - p1.Y) * dy) /
                (dx * dx + dy * dy);

            // See if this represents one of the segment's
            // end points or a point in the middle.
            if (t < 0)
            {
                closest = new PointF(p1.X, p1.Y);
                dx = pt.X - p1.X;
                dy = pt.Y - p1.Y;
            }
            else if (t > 1)
            {
                closest = new PointF(p2.X, p2.Y);
                dx = pt.X - p2.X;
                dy = pt.Y - p2.Y;
            }
            else
            {
                closest = new PointF(p1.X + t * dx, p1.Y + t * dy);
                dx = pt.X - closest.X;
                dy = pt.Y - closest.Y;
            }

            return Math.Sqrt(dx * dx + dy * dy);
        }

        private double DistanceBetweenPoints(PointF p1, PointF p2)
        {
            float dx = p2.X - p1.X;
            float dy = p2.Y - p1.Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }

        // Copy the selected data into SelectedData.
        public void SelectData(DataSets data_set)
        {
            switch (data_set)
            {
                case DataSets.Cases:
                    SelectedData = Cases;
                    break;
                case DataSets.CasesPerMillion:
                    SelectedData = CasesPerMillion;
                    break;
                case DataSets.Deaths:
                    SelectedData = Deaths;
                    break;
                case DataSets.DeathsPerMillion:
                    SelectedData = DeathsPerMillion;
                    break;
                case DataSets.Recoveries:
                    SelectedData = Recoveries;
                    break;
                case DataSets.RecoveriesPerMillion:
                    SelectedData = RecoveriesPerMillion;
                    break;
                case DataSets.DeathsPerResolution:
                    SelectedData = DeathsPerResolution;
                    break;
            }
        }

        // Calculate cases per million.
        public void CalculateCasesPerMillion()
        {
            // Create the CasesPerMillion array. (Initially all zeros.)
            CasesPerMillion = new float[Cases.Length];
            if (Population > 0)
            {
                Array.Copy(Cases, CasesPerMillion, Cases.Length);
                for (int i = 0; i < Cases.Length; i++)
                {
                    CasesPerMillion[i] = CasesPerMillion[i] / Population * 1000000;
                }
            }
        }

        // Calculate deaths per million.
        public void CalculateDeathsPerMillion()
        {
            // Create the DeathsPerMillion array. (Initially all zeros.)
            DeathsPerMillion = new float[Deaths.Length];
            if (Population > 0)
            {
                Array.Copy(Deaths, DeathsPerMillion, Deaths.Length);
                for (int i = 0; i < Deaths.Length; i++)
                {
                    DeathsPerMillion[i] = DeathsPerMillion[i] / Population * 1000000;
                }
            }
        }

        // Calculate recoveries per million.
        public void CalculateRecoveriesPerMillion()
        {
            // Create the RecoveriesPerMillion array. (Initially all zeros.)
            RecoveriesPerMillion = new float[Recoveries.Length];
            if (Population > 0)
            {
                Array.Copy(Recoveries, RecoveriesPerMillion, Recoveries.Length);
                for (int i = 0; i < Recoveries.Length; i++)
                {
                    RecoveriesPerMillion[i] = RecoveriesPerMillion[i] / Population * 1000000;
                }
            }
        }

        // Calculate deaths per resolved case.
        public void CalculateDeathsPerResolution()
        {
            // Create the DeathsPerRecovery array.
            DeathsPerResolution = new float[Deaths.Length];

            Array.Copy(Deaths, DeathsPerResolution, Deaths.Length);
            for (int i = 0; i < Deaths.Length; i++)
            {
                float resolutions = Recoveries[i] + Deaths[i];
                if (resolutions == 0)
                    DeathsPerResolution[i] = 0;
                else
                    DeathsPerResolution[i] /= resolutions;
            }
        }
    }
}
