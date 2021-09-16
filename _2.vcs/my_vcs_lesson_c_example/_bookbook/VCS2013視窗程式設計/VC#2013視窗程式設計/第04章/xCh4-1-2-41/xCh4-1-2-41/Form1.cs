using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_2_41
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var source = new AutoCompleteStringCollection();
            source.AddRange(new string[]
                    {
                        "行政院衛生署",
                        "行政院教育部",
                        "行政院法務部",
                        "行政院經濟部",
                        "行政院農委會"
                    });
            textBox1.AutoCompleteCustomSource = source;
            textBox1.AutoCompleteSource = AutoCompleteSource.CustomSource;
            textBox1.AutoCompleteMode = AutoCompleteMode.Suggest;
        }
    }
}
