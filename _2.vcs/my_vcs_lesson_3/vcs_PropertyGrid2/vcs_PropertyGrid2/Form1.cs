using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_use_property_grid_descriptions
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make some people.
            Person[] people =
            {
                new Person() {FirstName="Ann", LastName="Archer", Street="101 Ash Ave", City="Ann Arbor", State="MI", Zip="12345", Email="Ann@anywhere.com", Phone="703-287-3798"}, 
                new Person() {FirstName="Ben", LastName="Best", Street="231 Beach Blvd", City="Boulder", State="CO", Zip="24361", Email="Ben@bestplace.com", Phone="209-783-2918"}, 
                new Person() {FirstName="Cindy", LastName="Carter", Street="3783 Cherry Ct", City="Cedar Rapids", State="IA", Zip="36268", Email="CindyCarter@TheCarters.com", Phone="404-329-0182"}, 
            };

            // Display them in a ListBox.
            lstPeople.DataSource = people;
        }

        // Display this person's properties in the PropertyGrid.
        private void lstPeople_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Reset the DisplayMember to make
            // the ListBox refresh its list.
            lstPeople.DisplayMember = "FirstName";
            lstPeople.DisplayMember = null;

            // Display the selected Person in the PropertyGrid.
            propertyGrid1.SelectedObject = lstPeople.SelectedItem;
        }
    }
}
