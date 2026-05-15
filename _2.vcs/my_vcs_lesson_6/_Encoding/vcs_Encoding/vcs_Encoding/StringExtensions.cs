using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web

namespace vcs_Encoding
{
    public static class StringExtensions
    {
        // Return a string that represents the byte array
        // as a series of hexadecimal values separated
        // by a separator character.
        public static string ToHex(this byte[] the_bytes, char separator)
        {
            return BitConverter.ToString(the_bytes, 0).Replace('-', separator);
        }

        // Convert a string containing 2-digit hexadecimal
        // values into a byte array.
        public static byte[] ToBytes(this string the_string)
        {
            // Get the separator character.
            char separator = the_string[2];

            // Split at the separators.
            string[] pairs = the_string.Split(separator);
            byte[] bytes = new byte[pairs.Length];
            for (int i = 0; i < pairs.Length; i++)
                bytes[i] = Convert.ToByte(pairs[i], 16);
            return bytes;
        }

        // Extension to replace spaces with &nbsp;
        public static string SpaceToNbsp(this string s)
        {
            return s.Replace(" ", "&nbsp;");
        }

        // Url encode an ASCII string.
        public static string UrlEncode(this string s)
        {
            return HttpUtility.UrlEncode(s);
        }

        // Url decode an ASCII string.
        public static string UrlDecode(this string s)
        {
            return HttpUtility.UrlDecode(s);
        }

    }
}
