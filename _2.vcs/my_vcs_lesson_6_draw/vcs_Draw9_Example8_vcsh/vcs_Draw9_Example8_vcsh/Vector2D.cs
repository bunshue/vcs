using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_Draw9_Example8_vcsh
{
    public class Vector2D
    {
        public float X, Y;

        public Vector2D(float x, float y)
        {
            X = x;
            Y = y;
        }
        public Vector2D(PointF from_point, PointF to_point)
        {
            X = to_point.X - from_point.X;
            Y = to_point.Y - from_point.Y;
        }

        public static Vector2D operator +(Vector2D v1, Vector2D v2)
        {
            return new Vector2D(v1.X + v2.X, v1.Y + v2.Y);
        }

        public static Vector2D operator -(Vector2D v1)
        {
            return new Vector2D(-v1.X, -v1.Y);
        }

        public static PointF operator *(Vector2D vector, float scale)
        {
            return new PointF(vector.X * scale, vector.Y * scale);
        }

        public static PointF operator /(Vector2D vector, float scale)
        {
            return new PointF(vector.X / scale, vector.Y / scale);
        }

        public static PointF operator +(Vector2D vector, PointF point)
        {
            return new PointF(point.X + vector.X, point.Y + vector.Y);
        }
        public static PointF operator +(PointF point, Vector2D vector)
        {
            return new PointF(point.X + vector.X, point.Y + vector.Y);
        }
    }
}
