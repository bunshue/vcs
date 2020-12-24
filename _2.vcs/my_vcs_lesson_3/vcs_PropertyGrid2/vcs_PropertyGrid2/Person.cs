using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.ComponentModel;

namespace howto_use_property_grid_descriptions
{
    class Person
    {
        private string _FirstName;
        [Description("The person's first or given name")]
        [Category("Name")]
        public string FirstName
        {
            get
            {
                return _FirstName;
            }
            set
            {
                _FirstName = value;
            }
        }

        private string _LastName;
        [Description("The person's last or family name")]
        [Category("Name")]
        public string LastName
        {
            get
            {
                return _LastName;
            }
            set
            {
                _LastName = value;
            }
        }

        private string _Street;
        [Description("The street number, name, apartment number, etc. as in '123 N. Elm Ave Suite 21'")]
        [Category("Address")]
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
        [Category("Address")]
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
        [Category("Address")]
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
        [Category("Address")]
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

        private string _Email;
        [Description("The person's primary email address")]
        [Category("Contact Info")]
        public string Email
        {
            get
            {
                return _Email;
            }
            set
            {
                _Email = value;
            }
        }

        private string _Phone;
        [Description("The person's business phone number")]
        [Category("Contact Info")]
        public string Phone
        {
            get
            {
                return _Phone;
            }
            set
            {
                _Phone = value;
            }
        }

        // Return the Person as a string for display purposes.
        public override string ToString()
        {
            return FirstName + " " + LastName;
        }
    }
}
