using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.ComponentModel;

namespace vcs_PropertyGrid3
{
    [TypeConverter(typeof(StreetAddressConverter))]
    class StreetAddress
    {
        private string _Street;
        [Description("The street number, name, apartment number, etc. as in '123 N. Elm Ave Suite 21'")]
        public string Street
        {
            get
            {
                return _Street;
            }
            set
            {
                _Street = value;
            }
        }

        private string _City;
        [Description("The mailing address city")]
        public string City
        {
            get
            {
                return _City;
            }
            set
            {
                _City = value;
            }
        }

        private string _State;
        [Description("The two-letter state abbreviation")]
        public string State
        {
            get
            {
                return _State;
            }
            set
            {
                _State = value;
            }
        }

        private string _Zip;
        [Description("The postal ZIP or ZIP+4 code")]
        public string Zip
        {
            get
            {
                return _Zip;
            }
            set
            {
                _Zip = value;
            }
        }

        // Return as a comma-delimited string.
        public override string ToString()
        {
            return Street + "," + City + "," + State + "," + Zip;
        }
    }
}
