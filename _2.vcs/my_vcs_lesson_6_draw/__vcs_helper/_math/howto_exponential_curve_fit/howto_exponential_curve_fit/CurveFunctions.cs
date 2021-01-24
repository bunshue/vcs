using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace howto_exponential_curve_fit
{
    class CurveFunctions
    {
        private const double TINY = 0.0000001;
        private const double G_A_MIN = -100;
        private const double G_A_MAX = 100;
        private const double G_B_MIN = -10;
        private const double G_B_MAX = 10;
        private const double G_C_MIN = -10;
        private const double G_C_MAX = 10;

        // Return the function for x, a, b, and c.
        public static double F(double x, double a, double b, double c)
        {
            return a + b * Math.Exp(c * x);
        }

        // dF/da
        private static double dFda(double x, double a, double b, double c)
        {
            return 1;
        }

        // dF/db
        private static double dFdb(double x, double a, double b, double c)
        {
            return Math.Exp(c * x);
        }

        // dF/dc
        private static double dFdc(double x, double a, double b, double c)
        {
            return b * Math.Exp(c * x) * x;
        }

        // Return the sum of errors squared for the given points and parameters.
        public static double ErrorSquared(List<PointF> pts, double a, double b, double c)
        {
            double total_error = 0;
            for (int i = 0; i < pts.Count; i++)
            {
                double new_error = pts[i].Y - F(pts[i].X, a, b, c);
                if (total_error > 1E+15) break;
                total_error += new_error * new_error;
            }

            return total_error;
        }

        // dE/da
        private static double dEda(List<PointF> pts, double a, double b, double c)
        {
            double total = 0;
            for (int i = 0; i < pts.Count; i++)
            {
                total += 2 * (pts[i].Y - F(pts[i].X, a, b, c)) *
                    -dFda(pts[i].X, a, b, c);
            }
            return total;
        }

        // dE/db
        private static double dEdb(List<PointF> pts, double a, double b, double c)
        {
            double total = 0;
            for (int i = 0; i < pts.Count; i++)
            {
                total += 2 * (pts[i].Y - F(pts[i].X, a, b, c)) *
                    -dFdb(pts[i].X, a, b, c);
            }
            return total;
        }

        // dE/dc
        private static double dEdc(List<PointF> pts, double a, double b, double c)
        {
            double total = 0;
            for (int i = 0; i < pts.Count; i++)
            {
                total += 2 * (pts[i].Y - F(pts[i].X, a, b, c)) *
                    -dFdc(pts[i].X, a, b, c);
            }
            return total;
        }

        // Find a good curve fit.
        public static double FindGoodFit(List<PointF> pts,
            out double best_a, out double best_b, out double best_c,
            int num_steps, int max_iterations)
        {
            best_a = 0;
            best_b = 0;
            best_c = 0;
            double test_a = 0, test_b = 0, test_c = 0;
            double g_a_step = (G_A_MAX - G_A_MIN) / (num_steps - 1);
            double g_b_step = (G_B_MAX - G_B_MIN) / (num_steps - 1);
            double g_c_step = (G_C_MAX - G_C_MIN) / (num_steps - 1);

            double best_error2 = double.MaxValue;
            for (double a = G_A_MIN; a <= G_A_MAX; a += g_a_step)
            {
                for (double b = G_B_MIN; b <= G_B_MAX; b += g_b_step)
                {
                    for (double c = G_C_MIN; c <= G_C_MAX; c += g_c_step)
                    {
                        double test_error2 = FollowGradient(pts, a, b, c,
                            out test_a, out test_b, out test_c, max_iterations);
                        if (test_error2 < best_error2)
                        {
                            best_a = test_a;
                            best_b = test_b;
                            best_c = test_c;
                            best_error2 = test_error2;
                        }
                    }
                }
            }

            return Math.Sqrt(best_error2);
        }

        // Starting at (X, Y), follow the error
        // function's gradient to try to improve it.
        private static double FollowGradient(List<PointF> pts,
            double a, double b, double c,
            out double best_a, out double best_b, out double best_c,
            int max_iterations)
        {
            const double CUTOFF_ERROR = 1.0;

            // Set the initial distance to move.
            double dist = 0.25;

            // Start with the initial point.
            best_a = a;
            best_b = b;
            best_c = c;
            double best_error2 = ErrorSquared(pts, a, b, c);

            for (int iteration = 0; iteration < max_iterations; iteration++)
            {
                // Get the gradient at this point.
                double na = dEda(pts, a, b, c);
                double nb = dEdb(pts, a, b, c);
                double nc = dEdc(pts, a, b, c);

                // Normalize it.
                double length = na * na + nb * nb + nc * nc;
                length = Math.Sqrt(length);
                // If the length is too small, return the result so far.
                if (length < TINY) return best_error2;
                na = -na / length;
                nb = -nb / length;
                nc = -nc / length;

                // Try moving along the gradient.
                double va = na * dist;
                double vb = nb * dist;
                double vc = nc * dist;
                double test_error2 = ErrorSquared(pts, a + va, b + vb, c + vc);

                // Try increasingly smaller vectors
                // until we find an improvement.
                while (test_error2 > best_error2)
                {
                    dist /= 2;
                    if (dist < TINY)
                    {
                        // We're not moving far enough. Stop.
                        // Return the result so far.
                        return best_error2;
                    }
                    va = na * dist;
                    vb = nb * dist;
                    vc = nc * dist;
                    test_error2 = ErrorSquared(pts, a + va, b + vb, c + vc);
                }

                // Hopefully at this point we have found an improvement.
                a += va;
                b += vb;
                c += vc;
                best_a = a;
                best_b = b;
                best_c = c;
                best_error2 = test_error2;

                // If the error is small enough, return.
                if (best_error2 < CUTOFF_ERROR) return best_error2;
            } // Next iteration.

            // Return the error.
            return best_error2;
        }
    }
}
