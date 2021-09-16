using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;

namespace xCh8_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ArrayList TaiwanProvinces = new ArrayList();
            TaiwanProvinces.Add(new TaiwanProvince("台中", "中"));
            TaiwanProvinces.Add(new TaiwanProvince("彰化", "彰"));
            TaiwanProvinces.Add(new TaiwanProvince("南投", "投"));
            TaiwanProvinces.Add(new TaiwanProvince("雲林", "雲"));
            TaiwanProvinces.Add(new TaiwanProvince("嘉義", "嘉"));
            TaiwanProvinces.Add(new TaiwanProvince("台南", "南"));

            listBox1.DataSource = TaiwanProvinces;
            listBox1.DisplayMember = "LongName";
            listBox1.ValueMember = "ShortName";
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex != -1)
                textBox1.Text = listBox1.SelectedValue.ToString();
        }
    }
    public class TaiwanProvince
    {
        private string myShortName; // 縣市名的簡稱
        private string myLongName;  // 縣市名的全名

        public TaiwanProvince(string strLongName, string strShortName)
        {
            this.myShortName = strShortName;
            this.myLongName = strLongName;
        }

        public string ShortName
        {
            get
            {
                return myShortName;
            }
        }

        public string LongName
        {
            get
            {
                return myLongName;
            }
        }

        public override string ToString()
        {
            return LongName + "的簡稱是「" + ShortName + "」 ";
        }
    }
}
