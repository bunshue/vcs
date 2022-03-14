#region Using directives

using System;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

#endregion

namespace AviDemo {
    public class CopyForm : Form {
		/// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.NumericUpDown numStart;
        private System.Windows.Forms.NumericUpDown numStop;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.Button btnCancel;
 
        private int start=0, stop=0;

        public int Start {
            get { return start; }
        }

        public int Stop {
            get { return stop; }
        }

		/// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.numStart = new System.Windows.Forms.NumericUpDown();
            this.numStop = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.btnOK = new System.Windows.Forms.Button();
            this.btnCancel = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.numStart)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numStop)).BeginInit();
            this.SuspendLayout();
// 
// numStart
// 
            this.numStart.Location = new System.Drawing.Point(118, 13);
            this.numStart.Name = "numStart";
            this.numStart.Size = new System.Drawing.Size(50, 20);
            this.numStart.TabIndex = 0;
// 
// numStop
// 
            this.numStop.Location = new System.Drawing.Point(229, 13);
            this.numStop.Name = "numStop";
            this.numStop.Size = new System.Drawing.Size(50, 20);
            this.numStop.TabIndex = 1;
// 
// label1
// 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(98, 14);
            this.label1.TabIndex = 2;
            this.label1.Text = "Copy from Second";
// 
// label2
// 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(170, 13);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(55, 14);
            this.label2.TabIndex = 3;
            this.label2.Text = "to Second";
// 
// btnOK
// 
            this.btnOK.Location = new System.Drawing.Point(113, 53);
            this.btnOK.Name = "btnOK";
            this.btnOK.TabIndex = 4;
            this.btnOK.Text = "OK";
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
// 
// btnCancel
// 
            this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnCancel.Location = new System.Drawing.Point(204, 53);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.TabIndex = 5;
            this.btnCancel.Text = "Cancel";
            this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
// 
// CopyForm
// 
            this.AcceptButton = this.btnOK;
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
            this.CancelButton = this.btnCancel;
            this.ClientSize = new System.Drawing.Size(294, 94);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.numStop);
            this.Controls.Add(this.numStart);
            this.Name = "CopyForm";
            this.Text = "Copy Video and Sound";
            ((System.ComponentModel.ISupportInitialize)(this.numStart)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numStop)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        public CopyForm(int min, int max) {
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
