using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_10_Math_Random
{
    class Fraction
    {
        public long Numerator, Denominator;

        // Initialize the fraction from a string A/B.
        public Fraction(string txt)
        {
            string[] pieces = txt.Split('/');
            Numerator = long.Parse(pieces[0]);
            Denominator = long.Parse(pieces[1]);
            Simplify();
        }

        // Initialize the fraction from numerator and denominator.
        public Fraction(long numer, long denom)
        {
            Numerator = numer;
            Denominator = denom;
            Simplify();
        }

        // Return a * b.
        public static Fraction operator *(Fraction a, Fraction b)
        {
            // Swap numerators and denominators to simplify.
            Fraction result1 = new Fraction(a.Numerator, b.Denominator);
            Fraction result2 = new Fraction(b.Numerator, a.Denominator);

            return new Fraction(
                result1.Numerator * result2.Numerator,
                result1.Denominator * result2.Denominator);
        }

        // Return -a.
        public static Fraction operator -(Fraction a)
        {
            return new Fraction(-a.Numerator, a.Denominator);
        }

        // Return a + b.
        public static Fraction operator +(Fraction a, Fraction b)
        {
            // Get the denominators' greatest common divisor.
            long gcd_ab = MathStuff.GCD(a.Denominator, b.Denominator);

            long numer =
                a.Numerator * (b.Denominator / gcd_ab) +
                b.Numerator * (a.Denominator / gcd_ab);
            long denom =
                a.Denominator * (b.Denominator / gcd_ab);
            return new Fraction(numer, denom);
        }

        // Return a - b.
        public static Fraction operator -(Fraction a, Fraction b)
        {
            return a + -b;
        }

        // Return a / b.
        public static Fraction operator /(Fraction a, Fraction b)
        {
            return a * new Fraction(b.Denominator, b.Numerator);
        }

        // Return a < b.
        public static bool operator <(Fraction a, Fraction b)
        {
            return (double)a < (double)b;
        }

        // Return a > b.
        public static bool operator >(Fraction a, Fraction b)
        {
            return (double)a > (double)b;
        }

        // Return a == b.
        public static bool operator ==(Fraction a, Fraction b)
        {
            return ((a.Numerator == b.Numerator) &&
                    (a.Denominator == b.Denominator));
        }

        // Return a != b.
        public static bool operator !=(Fraction a, Fraction b)
        {
            return (!(a == b));
        }

        // Return true if the objects are equal.
        public override bool Equals(object obj)
        {
            if (!(obj is Fraction)) return false;
            Fraction b = obj as Fraction;
            return (this == b);
        }

        // Return true if the objects are equal.
        public override int GetHashCode()
        {
            return Numerator.GetHashCode() ^ Denominator.GetHashCode();
        }

        // Simplify the fraction.
        private void Simplify()
        {
            // Simplify the sign.
            if (Denominator < 0)
            {
                Numerator = -Numerator;
                Denominator = -Denominator;
            }

            // Factor out the greatest common divisor of the
            // numerator and the denominator.
            if (Numerator == 0) return;

            long gcd_ab = MathStuff.GCD(Numerator, Denominator);
            Numerator = Numerator / gcd_ab;
            Denominator = Denominator / gcd_ab;
        }

        // Convert a to a double.
        public static implicit operator double(Fraction a)
        {
            return (double)a.Numerator / a.Denominator;
        }

        // Convert a long into a Fraction.
        public static implicit operator Fraction(long numer)
        {
            return new Fraction(numer, 1);
        }

        // Return the fraction's value as a string.
        public override string ToString()
        {
            if (Denominator == 1) return Numerator.ToString();
            return Numerator.ToString() + "/" + Denominator.ToString();
        }
    }
}
