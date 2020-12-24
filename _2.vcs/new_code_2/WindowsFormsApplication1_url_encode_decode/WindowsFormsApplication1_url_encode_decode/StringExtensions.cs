using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

// Add a reference to System.Web.
using System.Web;

namespace WindowsFormsApplication1_url_encode_decode
{
    static class StringExtensions
    {
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
