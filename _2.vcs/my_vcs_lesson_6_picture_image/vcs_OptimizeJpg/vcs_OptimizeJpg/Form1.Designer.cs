namespace vcs_OptimizeJpg
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
            this.lblFileSize = new System.Windows.Forms.Label();
            this.lblCI = new System.Windows.Forms.Label();
            this.lbl100 = new System.Windows.Forms.Label();
            this.Label3 = new System.Windows.Forms.Label();
            this.Label2 = new System.Windows.Forms.Label();
            this.cboCI = new System.Windows.Forms.ComboBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button2 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // lblFileSize
            // 
            this.lblFileSize.AutoSize = true;
            this.lblFileSize.Location = new System.Drawing.Point(139, 84);
            this.lblFileSize.Name = "lblFileSize";
            this.lblFileSize.Size = new System.Drawing.Size(0, 12);
            this.lblFileSize.TabIndex = 17;
            // 
            // lblCI
            // 
            this.lblCI.AutoSize = true;
            this.lblCI.Location = new System.Drawing.Point(91, 84);
            this.lblCI.Name = "lblCI";
            this.lblCI.Size = new System.Drawing.Size(29, 12);
            this.lblCI.TabIndex = 16;
            this.lblCI.Text = "lblCI";
            // 
            // lbl100
            // 
            this.lbl100.AutoSize = true;
            this.lbl100.Location = new System.Drawing.Point(139, 62);
            this.lbl100.Name = "lbl100";
            this.lbl100.Size = new System.Drawing.Size(0, 12);
            this.lbl100.TabIndex = 15;
            // 
            // Label3
            // 
            this.Label3.AutoSize = true;
            this.Label3.Location = new System.Drawing.Point(12, 84);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(79, 12);
            this.Label3.TabIndex = 14;
            this.Label3.Text = "File Size at CI =";
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Location = new System.Drawing.Point(12, 62);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(100, 12);
            this.Label2.TabIndex = 13;
            this.Label2.Text = "File Size at CI = 100";
            // 
            // cboCI
            // 
            this.cboCI.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboCI.Items.AddRange(new object[] {
            "100",
            "95",
            "90",
            "85",
            "80",
            "75",
            "70",
            "65",
            "60",
            "55",
            "50",
            "45",
            "40",
            "35",
            "30",
            "25",
            "20",
            "15",
            "10",
            "5"});
            this.cboCI.Location = new System.Drawing.Point(185, 28);
            this.cboCI.Name = "cboCI";
            this.cboCI.Size = new System.Drawing.Size(48, 20);
            this.cboCI.TabIndex = 9;
            this.cboCI.SelectedIndexChanged += new System.EventHandler(this.cboCI_SelectedIndexChanged);
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(12, 30);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(140, 12);
            this.Label1.TabIndex = 12;
            this.Label1.Text = "JPG Compression Index (CI)";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 167);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(62, 54);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 19;
            this.pictureBox1.TabStop = false;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(466, 30);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(90, 44);
            this.button2.TabIndex = 22;
            this.button2.Text = "SAVE";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Right;
            this.richTextBox1.Location = new System.Drawing.Point(878, 0);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(250, 749);
            this.richTextBox1.TabIndex = 23;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1128, 749);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.lblFileSize);
            this.Controls.Add(this.lblCI);
            this.Controls.Add(this.lbl100);
            this.Controls.Add(this.Label3);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.cboCI);
            this.Controls.Add(this.Label1);
            this.Name = "Form1";
            this.Text = "vcs_OptimizeJpg";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label lblFileSize;
        internal System.Windows.Forms.Label lblCI;
        internal System.Windows.Forms.Label lbl100;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.ComboBox cboCI;
        internal System.Windows.Forms.Label Label1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

