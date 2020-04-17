using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class FiveNumbers : Form
    {
        public FiveNumbers()
        {
            InitializeComponent();
        }

        private void btnCompute_Click(object sender, EventArgs e)
        {
            /*----------------------------*
             *     第六章練習:選擇結構    *
             *----------------------------*/

            int pass = 0;
            int A = 0, B = 0, C = 0, D = 0, E = 0;
            int sum = 0;
            int s;
            
            // Score 1
            s = Convert.ToInt32(txtNum1.Text);

            if (s >= 60) pass++;

            if (s >= 90) A++;
            else if (s >= 80) B++;
            else if (s >= 70) C++;
            else if (s >= 60) D++;
            else E++;

            sum += s;

            // Score 2
            s = Convert.ToInt32(txtNum2.Text);

            if (s >= 60) pass++;

            if (s >= 90) A++;
            else if (s >= 80) B++;
            else if (s >= 70) C++;
            else if (s >= 60) D++;
            else E++;

            sum += s;

            // Score 3
            s = Convert.ToInt32(txtNum3.Text);

            if (s >= 60) pass++;

            if (s >= 90) A++;
            else if (s >= 80) B++;
            else if (s >= 70) C++;
            else if (s >= 60) D++;
            else E++;

            sum += s;

            // Score 4
            s = Convert.ToInt32(txtNum4.Text);

            if (s >= 60) pass++;

            if (s >= 90) A++;
            else if (s >= 80) B++;
            else if (s >= 70) C++;
            else if (s >= 60) D++;
            else E++;

            sum += s;

            // Score 5
            s = Convert.ToInt32(txtNum5.Text);

            if (s >= 60) pass++;

            if (s >= 90) A++;
            else if (s >= 80) B++;
            else if (s >= 70) C++;
            else if (s >= 60) D++;
            else E++;

            sum += s;

            string res = "及格: " + pass + "人\r\n";
            res += "等級A: " + A + "人\r\n";
            res += "等級B: " + B + "人\r\n";
            res += "等級C: " + C + "人\r\n";
            res += "等級D: " + D + "人\r\n";
            res += "等級E: " + E + "人\r\n";
            res += "平均 = " + (sum / 5.0);

            txtOutput.Text = res;            

        }

        private void FiveNumbers_Load(object sender, EventArgs e)
        {

        }
    }
}
