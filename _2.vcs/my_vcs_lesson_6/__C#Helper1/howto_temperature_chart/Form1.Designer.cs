namespace howto_temperature_chart
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.btnCreateChart = new System.Windows.Forms.Button();
            this.pdocChart = new System.Drawing.Printing.PrintDocument();
            this.ppdChart = new System.Windows.Forms.PrintPreviewDialog();
            this.SuspendLayout();
            // 
            // btnCreateChart
            // 
            this.btnCreateChart.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.btnCreateChart.Location = new System.Drawing.Point(120, 34);
            this.btnCreateChart.Name = "btnCreateChart";
            this.btnCreateChart.Size = new System.Drawing.Size(75, 23);
            this.btnCreateChart.TabIndex = 0;
            this.btnCreateChart.Text = "Create Chart";
            this.btnCreateChart.UseVisualStyleBackColor = true;
            this.btnCreateChart.Click += new System.EventHandler(this.btnCreateChart_Click);
            // 
            // pdocChart
            // 
            this.pdocChart.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.pdocChart_PrintPage);
            // 
            // ppdChart
            // 
            this.ppdChart.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.ppdChart.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.ppdChart.ClientSize = new System.Drawing.Size(400, 300);
            this.ppdChart.Document = this.pdocChart;
            this.ppdChart.Enabled = true;
            this.ppdChart.Icon = ((System.Drawing.Icon)(resources.GetObject("ppdChart.Icon")));
            this.ppdChart.Name = "ppdChart";
            this.ppdChart.Visible = false;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnCreateChart;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(314, 91);
            this.Controls.Add(this.btnCreateChart);
            this.Name = "Form1";
            this.Text = "howto_temperature_chart";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCreateChart;
        private System.Drawing.Printing.PrintDocument pdocChart;
        private System.Windows.Forms.PrintPreviewDialog ppdChart;
    }
}

