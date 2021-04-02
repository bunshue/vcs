using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace SnatchControlNameAndContent
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            foreach (Control cont in this.Controls)
            {
                switch (cont.GetType().ToString())
                {
                    case "System.Windows.Forms.TextBox":
                        listView1.Items.Add(cont.Name.ToString()+" "+cont.Text);
                        break;
                    case "System.Windows.Forms.Label":
                        listView1.Items.Add(cont.Name.ToString() + " " + cont.Text);
                        break;
                    case "System.Windows.Forms.ComboBox":
                        listView1.Items.Add(cont.Name.ToString() + " " + cont.Text);
                        break;
                    case "System.Windows.Forms.Button":
                        listView1.Items.Add(cont.Name.ToString() + " " + cont.Text);
                        break;
                }
           
                
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}