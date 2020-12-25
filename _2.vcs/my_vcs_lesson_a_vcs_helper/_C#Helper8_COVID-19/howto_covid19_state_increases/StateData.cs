using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace howto_covid19_state_increases
{
    public class StateData
    {
        static public DateTime[] Dates = null;
        public string Name = null;

        public float[] Positive = null;
        public float[] Negative = null;
        public float[] Pending = null;
        public float[] HospitalizedNow = null;
        public float[] HospitalizedTotal = null;
        public float[] IcuNow = null;
        public float[] IcuTotal = null;
        public float[] VentNow = null;
        public float[] VentTotal = null;
        public float[] Recovered = null;
        public float[] Deaths = null;
        public float[] DeathsPerResolution = null;
        public float[] PositiveIncrease = null;
        public float[] HospitalizedIncrease = null;
        public float[] DeathsIncrease = null;

        public float MaxPositive = 0;
        public float MaxNegative = 0;
        public float MaxPending = 0;
        public float MaxHospitalizedNow = 0;
        public float MaxHospitalizedTotal = 0;
        public float MaxIcuNow = 0;
        public float MaxIcuTotal = 0;
        public float MaxVentNow = 0;
        public float MaxVentTotal = 0;
        public float MaxRecovered = 0;
        public float MaxDeaths = 0;
        public float MaxDeathsPerResolution = 0;
        public float MaxPositiveIncrease= 0;
        public float MaxHospitalizedIncrease = 0;
        public float MaxDeathsIncrease = 0;

        public float MaxDataValue = 0;

        public int StateNumber = -1;
        public int FirstDrawnDate = -1;
        public long Population = -1;

        public List<PointF[]> DataCurves = new List<PointF[]>();
        public List<PointF[]> DeviceCurves = new List<PointF[]>();
        public List<string> DatasetNames = new List<string>();

        public override string ToString()
        {
            //return Name + " (" + Population.ToString("n0") + ")";
            return Name;
        }

        // Draw this state's data.
        public void Draw(int align_cases, Graphics gr, Pen pen,
            Matrix transform, string state_name)
        {
            DataCurves = new List<PointF[]>();
            DeviceCurves = new List<PointF[]>();
            DatasetNames = new List<string>();

            // Find the first date with align_cases cases.
            FirstDrawnDate = -1;
            int num_dates = Positive.Length;
            for (int i = 0; i < num_dates; i++)
                if (Positive[i] >= align_cases)
                {
                    FirstDrawnDate = i;
                    break;
                }

            // Don't draw unless we have at least one day of data left.
            if ((FirstDrawnDate < 0) || (FirstDrawnDate >= num_dates - 1)) return;

            // Draw the selected data.
            if (SelectedDataSets.Positive)
                DrawData(gr, Positive, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Positive", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.Negative)
                DrawData(gr, Negative, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Negative", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.Pending)
                DrawData(gr, Pending, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Pending", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.HospitalizedNow)
                DrawData(gr, HospitalizedNow, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Hospitalized Now", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.HospitalizedTotal)
                DrawData(gr, HospitalizedTotal, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Hospitalized Total", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.IcuNow)
                DrawData(gr, IcuNow, FirstDrawnDate,
                    num_dates, pen, transform,
                    " ICU Now", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.IcuTotal)
                DrawData(gr, IcuTotal, FirstDrawnDate,
                    num_dates, pen, transform,
                    " ICU Total", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.VentNow)
                DrawData(gr, VentNow, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Ventillator Now", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.VentTotal)
                DrawData(gr, VentTotal, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Ventillator Now", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.Recovered)
                DrawData(gr, Recovered, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Recovered", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.Deaths)
                DrawData(gr, Deaths, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Deaths", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.DeathsPerResolution)
                DrawData(gr, DeathsPerResolution, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Deaths Per Resolution", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.PositiveIncrease)
                DrawData(gr, PositiveIncrease, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Positive Per Day", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.HospitalizedIncrease)
                DrawData(gr, HospitalizedIncrease, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Hospitalized Per Day", DataCurves, DeviceCurves, DatasetNames);
            if (SelectedDataSets.DeathsIncrease)
                DrawData(gr, DeathsIncrease, FirstDrawnDate,
                    num_dates, pen, transform,
                    " Deaths Per Day", DataCurves, DeviceCurves, DatasetNames);
        }

        public void DrawData(Graphics gr,
            float[] data, int first_drawn_date, int num_dates, Pen pen,
            Matrix transform, string dataset_name,
            List<PointF[]> data_curves, List<PointF[]> device_curves,
            List<string> dataset_names)
        {
            // Make the points.
            List<PointF> point_list = new List<PointF>();
            for (int i = FirstDrawnDate; i < num_dates; i++)
                point_list.Add(new PointF(i - FirstDrawnDate, data[i]));
            PointF[] points = point_list.ToArray();

            // Divide by per million if desired.
            if (SelectedDataSets.PerMillion)
            {
                float millions = Population / 1000000f;
                for (int i = 0; i < points.Length; i++)
                {
                    points[i].Y /= millions;
                }
            }

            // Draw the curve.
            gr.DrawLines(pen, points);
            data_curves.Add(points);

            // Find device coordinates for tooltips.
            PointF[] device_points = new PointF[points.Length];
            Array.Copy(points, device_points, points.Length);
            transform.TransformPoints(device_points);
            device_curves.Add(device_points);
            dataset_names.Add(dataset_name);
        }

        public bool PointIsAt(PointF device_point, out int day_num,
            out string descr, out PointF close_point)
        {
            for (int curve_num = 0; curve_num < DeviceCurves.Count; curve_num++)
            {
                PointF[] curve = DeviceCurves[curve_num];
                const double close_dist = 4;
                PointF closest;
                for (int pt_num = 1; pt_num < curve.Length; pt_num++)
                {
                    double dist = FindDistanceToSegment(device_point,
                        curve[pt_num - 1], curve[pt_num], out closest);

                    if (dist <= close_dist)
                    {
                        // See whether it is closer to this this
                        // segment's left or right point.
                        if (DistanceBetweenPoints(curve[pt_num - 1], closest) <
                            DistanceBetweenPoints(curve[pt_num], closest))
                            pt_num--;
                        day_num = pt_num;

                        float data_value = DataCurves[curve_num][day_num].Y;

                        // Make the descriptive part as in "100 Deaths."
                        if (data_value < 1)
                            descr = data_value.ToString("n2") + DatasetNames[curve_num];
                        else
                            descr = data_value.ToString("n0") + DatasetNames[curve_num];
                        
                        // Use the closer segment end point.
                        close_point = curve[day_num];
                        return true;
                    }
                }
            }

            day_num = -1;
            descr = "";
            close_point = new PointF(-1, -1);
            return false;
        }

        public void SetMaxDataValues()
        {
            MaxPositive = Positive.Max();
            MaxNegative = Negative.Max();
            MaxPending = Pending.Max();
            MaxHospitalizedNow = HospitalizedNow.Max();
            MaxHospitalizedTotal = HospitalizedTotal.Max();
            MaxIcuNow = IcuNow.Max();
            MaxIcuTotal = IcuTotal.Max();
            MaxVentNow = VentNow.Max();
            MaxVentTotal = VentTotal.Max();
            MaxRecovered = Recovered.Max();
            MaxDeaths = Deaths.Max();
            MaxDeathsPerResolution = DeathsPerResolution.Max();
            MaxPositiveIncrease = PositiveIncrease.Max();
            MaxHospitalizedIncrease = HospitalizedIncrease.Max();
            MaxDeathsIncrease = DeathsIncrease.Max();
        }

        public void SetMaxDataValue()
        {
            float max = 0;

            if (SelectedDataSets.Positive)
                max = Math.Max(max, MaxPositive);
            if (SelectedDataSets.Negative)
                max = Math.Max(max, MaxNegative);
            if (SelectedDataSets.Pending)
                max = Math.Max(max, MaxPending);
            if (SelectedDataSets.HospitalizedNow)
                max = Math.Max(max, MaxHospitalizedNow);
            if (SelectedDataSets.HospitalizedTotal)
                max = Math.Max(max, MaxHospitalizedTotal);
            if (SelectedDataSets.IcuNow)
                max = Math.Max(max, MaxIcuNow);
            if (SelectedDataSets.IcuTotal)
                max = Math.Max(max, MaxIcuTotal);
            if (SelectedDataSets.VentNow)
                max = Math.Max(max, MaxVentNow);
            if (SelectedDataSets.VentTotal)
                max = Math.Max(max, MaxVentTotal);
            if (SelectedDataSets.Recovered)
                max = Math.Max(max, MaxRecovered);
            if (SelectedDataSets.Deaths)
                max = Math.Max(max, MaxDeaths);

            if (SelectedDataSets.PerMillion) max = max / (Population / 1000000f);

            if (SelectedDataSets.DeathsPerResolution)
            {
                for (int i = 0; i < this.Deaths.Length; i++)
                {
                    float deaths_per_resolution;
                    if ((Deaths[i] == 0) || (Recovered[i] == 0))
                    {
                        deaths_per_resolution = 0;
                    }
                    else
                    {
                        deaths_per_resolution =
                            Deaths[i] / (Deaths[i] + Recovered[i]);
                    }
                    max = Math.Max(max, deaths_per_resolution);
                }
            }

            if (SelectedDataSets.PositiveIncrease)
                max = Math.Max(max, MaxPositiveIncrease);
            if (SelectedDataSets.HospitalizedIncrease)
                max = Math.Max(max, MaxHospitalizedIncrease);
            if (SelectedDataSets.DeathsIncrease)
                max = Math.Max(max, MaxDeathsIncrease);

            MaxDataValue = max;
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
    }
}
