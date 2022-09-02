namespace howto_compare_directories_timed
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
            this.Label2 = new System.Windows.Forms.Label();
            this.Label1 = new System.Windows.Forms.Label();
            this.btnCompare = new System.Windows.Forms.Button();
            this.txtDir2 = new System.Windows.Forms.TextBox();
            this.txtDir1 = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.txtGetFilesTime = new System.Windows.Forms.TextBox();
            this.txtLinqTwiceTime = new System.Windows.Forms.TextBox();
            this.txtLinqJoinsTime = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Location = new System.Drawing.Point(10, 39);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(61, 13);
            this.Label2.TabIndex = 18;
            this.Label2.Text = "Directory 2:";
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(10, 15);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(61, 13);
            this.Label1.TabIndex = 17;
            this.Label1.Text = "Directory 1:";
            // 
            // btnCompare
            // 
            this.btnCompare.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnCompare.Location = new System.Drawing.Point(152, 62);
            this.btnCompare.Name = "btnCompare";
            this.btnCompare.Size = new System.Drawing.Size(64, 40);
            this.btnCompare.TabIndex = 16;
            this.btnCompare.Text = "Compare";
            this.btnCompare.UseVisualStyleBackColor = true;
            this.btnCompare.Click += new System.EventHandler(this.btnCompare_Click);
            // 
            // txtDir2
            // 
            this.txtDir2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtDir2.Location = new System.Drawing.Point(77, 12);
            this.txtDir2.Name = "txtDir2";
            this.txtDir2.Size = new System.Drawing.Size(279, 20);
            this.txtDir2.TabIndex = 14;
            this.txtDir2.Text = "C:\\Windows\\System32";
            // 
            // txtDir1
            // 
            this.txtDir1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtDir1.Location = new System.Drawing.Point(77, 36);
            this.txtDir1.Name = "txtDir1";
            this.txtDir1.Size = new System.Drawing.Size(279, 20);
            this.txtDir1.TabIndex = 15;
            this.txtDir1.Text = "C:\\Windows\\System32";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 124);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(93, 13);
            this.label3.TabIndex = 19;
            this.label3.Text = "Directory.GetFiles:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 150);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(67, 13);
            this.label4.TabIndex = 20;
            this.label4.Text = "LINQ Twice:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 176);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(62, 13);
            this.label5.TabIndex = 21;
            this.label5.Text = "LINQ Joins:";
            // 
            // txtGetFilesTime
            // 
            this.txtGetFilesTime.Location = new System.Drawing.Point(111, 121);
            this.txtGetFilesTime.Name = "txtGetFilesTime";
            this.txtGetFilesTime.Size = new System.Drawing.Size(100, 20);
            this.txtGetFilesTime.TabIndex = 22;
            // 
            // txtLinqTwiceTime
            // 
            this.txtLinqTwiceTime.Location = new System.Drawing.Point(111, 147);
            this.txtLinqTwiceTime.Name = "txtLinqTwiceTime";
            this.txtLinqTwiceTime.Size = new System.Drawing.Size(100, 20);
            this.txtLinqTwiceTime.TabIndex = 23;
            // 
            // txtLinqJoinsTime
            // 
            this.txtLinqJoinsTime.Location = new System.Drawing.Point(111, 173);
            this.txtLinqJoinsTime.Name = "txtLinqJoinsTime";
            this.txtLinqJoinsTime.Size = new System.Drawing.Size(100, 20);
            this.txtLinqJoinsTime.TabIndex = 24;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnCompare;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(368, 205);
            this.Controls.Add(this.txtLinqJoinsTime);
            this.Controls.Add(this.txtLinqTwiceTime);
            this.Controls.Add(this.txtGetFilesTime);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.btnCompare);
            this.Controls.Add(this.txtDir2);
            this.Controls.Add(this.txtDir1);
            this.Name = "Form1";
            this.Text = "howto_compare_directories_timed";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.Button btnCompare;
        internal System.Windows.Forms.TextBox txtDir2;
        internal System.Windows.Forms.TextBox txtDir1;
        internal System.Windows.Forms.Label label3;
        internal System.Windows.Forms.Label label4;
        internal System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox txtGetFilesTime;
        private System.Windows.Forms.TextBox txtLinqTwiceTime;
        private System.Windows.Forms.TextBox txtLinqJoinsTime;
    }
}

