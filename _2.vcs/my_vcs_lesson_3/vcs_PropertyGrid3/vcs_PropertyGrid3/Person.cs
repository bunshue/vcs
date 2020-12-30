using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.ComponentModel;

namespace vcs_PropertyGrid3
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

        private StreetAddress _Address;
        [Description("The person's street address")]
        [Category("Contact Info")]
        public StreetAddress Address
        {
            get
            {
                return _Address;
            }
            set
            {
                _Address = value;
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
