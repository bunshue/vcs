#region Using directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

#endregion

namespace AviDemo {
    partial class CopyForm : Form {

        private int start=0, stop=0;

        public int Start {
            get { return start; }
        }

        public int Stop {
            get { return stop; }
        }

		public CopyForm(int min, int max)
		{
            InitializeComponent();

			numStart.Minimum = min;
            numStop.Minimum = min;

			numStart.Maximum = max;
            numStop.Maximum = max;

			numStart.Value = min;
            numStop.Value = max;
        }

        private void btnOK_Click(object sender, EventArgs e) {
            start = (int)numStart.Value;
            stop = (int)numStop.Value;
            this.DialogResult = DialogResult.OK;
            this.Close();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
            this.Close();
        }
    }
}