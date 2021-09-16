using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_4_41
{
    public partial class Form1 : Form
    {
        ToolStripComboBox toolStripComboBox1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolStripComboBox1 = new ToolStripComboBox();

            toolStripComboBox1.AutoCompleteCustomSource.AddRange(new string[] {
            "http://tw.yahoo.com",
            "http://msdn.microsoft.com.tw",
            "http://www.google.com.tw",
            "http://www.kingsinfo.com.tw"});
            toolStripComboBox1.AutoCompleteMode =AutoCompleteMode.SuggestAppend;
            toolStripComboBox1.AutoCompleteSource = AutoCompleteSource.CustomSource;

            toolStripComboBox1.DropDownHeight = 40;
            toolStripComboBox1.DropDownWidth = 160;
            toolStripComboBox1.FlatStyle = FlatStyle.Standard;
            toolStripComboBox1.IntegralHeight = false;

            toolStripComboBox1.Items.AddRange(new object[] {
            "http://tw.yahoo.com",
            "http://msdn.microsoft.com.tw",
            "http://www.google.com.tw",
            "http://www.kingsinfo.com.tw"});

            toolStripComboBox1.MaxDropDownItems = 3;
            toolStripComboBox1.MergeAction = MergeAction.Insert;
            toolStripComboBox1.Size = new Size(200, 25);
            toolStripComboBox1.Sorted = true;
            toolStripComboBox1.ToolTipText = "請選擇所需的網址";
            toolStripComboBox1.SelectedIndexChanged += 
                new EventHandler(toolStripComboBox1_SelectedIndexChanged);

            toolStrip1.Items.Add(toolStripComboBox1);
        }

        private void toolStripComboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            ToolStripComboBox x = (ToolStripComboBox)sender;
            string URL = x.Items[x.SelectedIndex].ToString();
            System.Diagnostics.Process.Start("IEXPLORE.EXE", URL);
        }
    }
}
