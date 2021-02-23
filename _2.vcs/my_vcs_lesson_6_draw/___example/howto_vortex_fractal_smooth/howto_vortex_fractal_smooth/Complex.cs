using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace howto_vortex_fractal
{
    public class Complex
    {
        public double Re = 0, Im = 0;

        // Constructors.
        public Complex(double real, double imaginary)
        {
            Re = real;
            Im = imaginary;
        }
        public Complex(double real)
        {
            Re = real;
            Im = 0;
        }

        // Parse a String of the form R + Ii.
        public static Complex Parse(string string_value)
        {
            // Remove spaces and the "i".
            string_value = string_value.Replace(" ", "");
            string_value = string_value.ToLower().Replace("i", "");

            // Find the + or - between the parts.
            char[] plus_or_minus = { '+', '-' };
            int pos = string_value.IndexOfAny(plus_or_minus);
            if (pos == 0)
            {
                // Skip the leading +/-.
                pos = string_value.IndexOfAny(plus_or_minus, 1);
            }

            // Get the real and imaginary parts.
            double re = double.Parse(string_value.Substring(0, pos));
            double im = double.Parse(string_value.Substring(pos));

            return new Complex(re, im);
        }

        // Operators.
        // Unary -.
        public static Complex operator -(Complex c1)
        {
            return new Complex(-c1.Re, -c1.Im);
        }

        // Binary +.
        public static Complex operator +(Complex c1, Complex c2)
        {
            return new Complex(c1.Re + c2.Re, c1.Im + c2.Im);
        }

        // Binary *.
        public static Complex operator *(Complex c1, Complex c2)
        {
            return new Complex(
                c1.Re * c2.Re - c1.Im * c2.Im,
                c1.Re * c2.Im + c1.Im * c2.Re);
        }

        // Binary -.
        public static Complex operator -(Complex c1, Complex c2)
        {
            return new Complex(c1.Re - c2.Re, c1.Im - c2.Im);
        }

        // Binary /.
        public static Complex operator /(Complex c1, Complex c2)
        {
            double denominator = c2.Re * c2.Re + c2.Im * c2.Im;
            double re =
                (c1.Re * c2.Re + c1.Im * c2.Im) /
                denominator;
            double im =
                (c1.Im * c2.Re - c1.Re * c2.Im) /
                denominator;
            return new Complex(re, im);
        }

        // Convert between double and Complex.
        public static implicit operator Complex(double re)
        {
            return new Complex(re, 0);
        }
        public static explicit operator double(Complex c1)
        {
            return c1.Magnitude;
        }

        // Return the number's magnitude.
        public double Magnitude
        {
            get
            {
                return (Math.Sqrt(Re * Re + Im * Im));
            }
        }

        // Return the number's magnitude squared.
        public double MagnitudeSquared
        {
            get
            {
                return (Re * Re + Im * Im);
            }
        }

        // Unary +.
        public static Complex operator +(Complex c1)
        {
            return new Complex(c1.Re, c1.Im);
        }

        // < and >.
        public static bool operator <(Complex c1, Complex c2)
        {
            return (c1.Magnitude < c2.Magnitude);
        }
        public static bool operator >(Complex c1, Complex c2)
        {
            return (c1.Magnitude > c2.Magnitude);
        }

        // <= and >=.
        public static bool operator <=(Complex c1, Complex c2)
        {
            return (c1.Magnitude <= c2.Magnitude);
        }
        public static bool operator >=(Complex c1, Complex c2)
        {
            return (c1.Magnitude >= c2.Magnitude);
        }

        // == and !=.
        public static bool operator ==(Complex c1, Complex c2)
        {
            return (c1.Re == c2.Re && c1.Im == c2.Im);
        }
        public static bool operator !=(Complex c1, Complex c2)
        {
            return !(c1 == c2);
        }
        public override bool Equals(object obj)
        {
            Complex c1 = obj as Complex;
            return this == c1;
        }
        public override int GetHashCode()
        {
            return Re.GetHashCode() | Im.GetHashCode();
        }

        // Return the number formatted as a string.
        public override string ToString()
        {
            if (Im == 0) return String.Format("{0}", Re);
            if (Re == 0) return String.Format("{0}i", Im);
            if (Im < 0) return String.Format("{0} - {1}i", Re, Math.Abs(Im));
            return String.Format("{0} + {1}i", Re, Im);
        }
        public string ToString(string format)
        {
            if (Im == 0) return String.Format("{0:" + format + "}", Re);
            if (Re == 0) return String.Format("{0:" + format + "}i", Im);
            if (Im < 0) return String.Format("{0:" + format + "} - {1:" + format + "}i", Re, Math.Abs(Im));
            return String.Format("{0:" + format + "} + {1:" + format + "}i", Re, Im);
        }
    }
}
