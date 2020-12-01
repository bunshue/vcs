using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//listBox 的屬性 SelectionMode 改成 MultiExtended   可多選

namespace my_vcs_21_ListBox2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetButtonsEditable();
        }

        // Move selected items to listBox2.
        private void button1_Click(object sender, EventArgs e)
        {
            MoveSelectedItems(listBox1, listBox2);
        }

        // Move all items to listBox2.
        private void button2_Click(object sender, EventArgs e)
        {
            MoveAllItems(listBox1, listBox2);
        }

        // Move all items to listBox1.
        private void button3_Click(object sender, EventArgs e)
        {
            MoveAllItems(listBox2, listBox1);
        }

        // Move selected items to listBox1.
        private void button4_Click(object sender, EventArgs e)
        {
            MoveSelectedItems(listBox2, listBox1);
        }

        // Move selected items from one ListBox to another.
        private void MoveSelectedItems(ListBox lstFrom, ListBox lstTo)
        {
            while (lstFrom.SelectedItems.Count > 0)
            {
                string item = (string)lstFrom.SelectedItems[0];
                lstTo.Items.Add(item);
                lstFrom.Items.Remove(item);
            }
            SetButtonsEditable();
        }

        // Move all items from one ListBox to another.
        private void MoveAllItems(ListBox lstFrom, ListBox lstTo)
        {
            lstTo.Items.AddRange(lstFrom.Items);
            lstFrom.Items.Clear();
            SetButtonsEditable();
        }

        // Enable and disable buttons.
        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            SetButtonsEditable();
        }

        // Enable and disable buttons.
        private void SetButtonsEditable()
        {
            button1.Enabled = (listBox1.SelectedItems.Count > 0);
            button2.Enabled = (listBox1.Items.Count > 0);
            button4.Enabled = (listBox2.SelectedItems.Count > 0);
            button3.Enabled = (listBox2.Items.Count > 0);
        }



    }
}
