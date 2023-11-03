using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1108
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] choice = {
            "國文", "英文", "數學", "理化", "地理",
            "歷史", "自然科學", "生物" };
            lstChoice.Items.AddRange(choice);
        }

        private void lstChoice_SelectedIndexChanged(
              object sender, EventArgs e)
        {
            //將第一個清單方塊選取的科目加到第二個清單方塊
            lstSubject.Items.Add(
               lstChoice.SelectedItems[0].ToString());
        }
    }
}
