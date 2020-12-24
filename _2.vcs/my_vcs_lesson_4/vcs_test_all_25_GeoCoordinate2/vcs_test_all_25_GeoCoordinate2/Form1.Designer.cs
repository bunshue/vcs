namespace vcs_test_all_25_GeoCoordinate2
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
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.txtLat1 = new System.Windows.Forms.TextBox();
            this.txtLon1 = new System.Windows.Forms.TextBox();
            this.txtLon2 = new System.Windows.Forms.TextBox();
            this.txtLat2 = new System.Windows.Forms.TextBox();
            this.cboCity1 = new System.Windows.Forms.ComboBox();
            this.cboCity2 = new System.Windows.Forms.ComboBox();
            this.btnCalculate = new System.Windows.Forms.Button();
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.label3 = new System.Windows.Forms.Label();
            this.lblDistance = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.tableLayoutPanel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(3, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(46, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "Latitude:";
            // 
            // label2
            // 
            this.label2.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(3, 51);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(56, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "Longitude:";
            // 
            // txtLat1
            // 
            this.txtLat1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtLat1.Location = new System.Drawing.Point(73, 26);
            this.txtLat1.Name = "txtLat1";
            this.txtLat1.Size = new System.Drawing.Size(181, 22);
            this.txtLat1.TabIndex = 2;
            this.txtLat1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtLon1
            // 
            this.txtLon1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtLon1.Location = new System.Drawing.Point(73, 49);
            this.txtLon1.Name = "txtLon1";
            this.txtLon1.Size = new System.Drawing.Size(181, 22);
            this.txtLon1.TabIndex = 4;
            this.txtLon1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtLon2
            // 
            this.txtLon2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtLon2.Location = new System.Drawing.Point(260, 49);
            this.txtLon2.Name = "txtLon2";
            this.txtLon2.Size = new System.Drawing.Size(181, 22);
            this.txtLon2.TabIndex = 5;
            this.txtLon2.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtLat2
            // 
            this.txtLat2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtLat2.Location = new System.Drawing.Point(260, 26);
            this.txtLat2.Name = "txtLat2";
            this.txtLat2.Size = new System.Drawing.Size(181, 22);
            this.txtLat2.TabIndex = 3;
            this.txtLat2.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // cboCity1
            // 
            this.cboCity1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.cboCity1.FormattingEnabled = true;
            this.cboCity1.Location = new System.Drawing.Point(73, 3);
            this.cboCity1.Name = "cboCity1";
            this.cboCity1.Size = new System.Drawing.Size(181, 20);
            this.cboCity1.TabIndex = 0;
            this.cboCity1.SelectedIndexChanged += new System.EventHandler(this.cboCity1_SelectedIndexChanged);
            // 
            // cboCity2
            // 
            this.cboCity2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.cboCity2.FormattingEnabled = true;
            this.cboCity2.Location = new System.Drawing.Point(260, 3);
            this.cboCity2.Name = "cboCity2";
            this.cboCity2.Size = new System.Drawing.Size(181, 20);
            this.cboCity2.TabIndex = 1;
            this.cboCity2.SelectedIndexChanged += new System.EventHandler(this.cboCity2_SelectedIndexChanged);
            // 
            // btnCalculate
            // 
            this.btnCalculate.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.tableLayoutPanel1.SetColumnSpan(this.btnCalculate, 3);
            this.btnCalculate.Location = new System.Drawing.Point(184, 459);
            this.btnCalculate.Name = "btnCalculate";
            this.btnCalculate.Size = new System.Drawing.Size(75, 17);
            this.btnCalculate.TabIndex = 6;
            this.btnCalculate.Text = "Calculate";
            this.btnCalculate.UseVisualStyleBackColor = true;
            this.btnCalculate.Click += new System.EventHandler(this.btnCalculate_Click);
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.tableLayoutPanel1.ColumnCount = 3;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 70F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel1.Controls.Add(this.cboCity2, 2, 0);
            this.tableLayoutPanel1.Controls.Add(this.cboCity1, 1, 0);
            this.tableLayoutPanel1.Controls.Add(this.label1, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.label2, 0, 2);
            this.tableLayoutPanel1.Controls.Add(this.txtLon2, 2, 2);
            this.tableLayoutPanel1.Controls.Add(this.txtLat1, 1, 1);
            this.tableLayoutPanel1.Controls.Add(this.txtLon1, 1, 2);
            this.tableLayoutPanel1.Controls.Add(this.txtLat2, 2, 1);
            this.tableLayoutPanel1.Controls.Add(this.label3, 0, 4);
            this.tableLayoutPanel1.Controls.Add(this.lblDistance, 1, 4);
            this.tableLayoutPanel1.Controls.Add(this.btnCalculate, 1, 3);
            this.tableLayoutPanel1.Location = new System.Drawing.Point(12, 11);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 5;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 23F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 23F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 23F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 23F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(444, 499);
            this.tableLayoutPanel1.TabIndex = 9;
            // 
            // label3
            // 
            this.label3.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(3, 483);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(47, 12);
            this.label3.TabIndex = 9;
            this.label3.Text = "Distance:";
            // 
            // lblDistance
            // 
            this.lblDistance.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.lblDistance.AutoSize = true;
            this.tableLayoutPanel1.SetColumnSpan(this.lblDistance, 2);
            this.lblDistance.Location = new System.Drawing.Point(73, 483);
            this.lblDistance.Name = "lblDistance";
            this.lblDistance.Size = new System.Drawing.Size(0, 12);
            this.lblDistance.TabIndex = 10;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(462, 14);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(245, 492);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnCalculate;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(719, 522);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.tableLayoutPanel1);
            this.Name = "Form1";
            this.Text = "vcs_test_all_25_GeoCoordinate2";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtLat1;
        private System.Windows.Forms.TextBox txtLon1;
        private System.Windows.Forms.TextBox txtLon2;
        private System.Windows.Forms.TextBox txtLat2;
        private System.Windows.Forms.ComboBox cboCity1;
        private System.Windows.Forms.ComboBox cboCity2;
        private System.Windows.Forms.Button btnCalculate;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label lblDistance;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

