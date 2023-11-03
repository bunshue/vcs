using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH0202
{
   public partial class Form1 : Form
   {
      public Form1()
      {
         InitializeComponent();
      }

      private void BtnShow_Click(object sender, 
         EventArgs e)
      {
         //取得系統目前的日期
         DateTime today = DateTime.Today;

         //變數name取得輸入的名稱
         string name = txtName.Text;

         //顯示今天的日期
         lblData.Text = $"Hi, {name}\n 今天是{today:D}";
      }
   }
}
