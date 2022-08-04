namespace vcs_ReadWrite_EXCEL6
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
            this.btnRead = new System.Windows.Forms.Button();
            this.lblTitle1 = new System.Windows.Forms.Label();
            this.lstItems1 = new System.Windows.Forms.ListBox();
            this.lstItems2 = new System.Windows.Forms.ListBox();
            this.lblTitle2 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnRead
            // 
            this.btnRead.Location = new System.Drawing.Point(12, 12);
            this.btnRead.Name = "btnRead";
            this.btnRead.Size = new System.Drawing.Size(92, 38);
            this.btnRead.TabIndex = 3;
            this.btnRead.Text = "Read";
            this.btnRead.UseVisualStyleBackColor = true;
            this.btnRead.Click += new System.EventHandler(this.btnRead_Click);
            // 
            // lblTitle1
            // 
            this.lblTitle1.Location = new System.Drawing.Point(10, 67);
            this.lblTitle1.Name = "lblTitle1";
            this.lblTitle1.Size = new System.Drawing.Size(120, 17);
            this.lblTitle1.TabIndex = 5;
            this.lblTitle1.Text = "label2";
            this.lblTitle1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lstItems1
            // 
            this.lstItems1.FormattingEnabled = true;
            this.lstItems1.ItemHeight = 12;
            this.lstItems1.Location = new System.Drawing.Point(10, 86);
            this.lstItems1.Name = "lstItems1";
            this.lstItems1.Size = new System.Drawing.Size(120, 448);
            this.lstItems1.TabIndex = 6;
            // 
            // lstItems2
            // 
            this.lstItems2.FormattingEnabled = true;
            this.lstItems2.ItemHeight = 12;
            this.lstItems2.Location = new System.Drawing.Point(153, 86);
            this.lstItems2.Name = "lstItems2";
            this.lstItems2.Size = new System.Drawing.Size(120, 448);
            this.lstItems2.TabIndex = 8;
            // 
            // lblTitle2
            // 
            this.lblTitle2.Location = new System.Drawing.Point(153, 67);
            this.lblTitle2.Name = "lblTitle2";
            this.lblTitle2.Size = new System.Drawing.Size(120, 17);
            this.lblTitle2.TabIndex = 7;
            this.lblTitle2.Text = "label2";
            this.lblTitle2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(312, 86);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(463, 448);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(312, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(92, 38);
            this.button1.TabIndex = 10;
            this.button1.Text = "開啟Excel檔並新增工作表";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnRead;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(788, 547);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.lstItems2);
            this.Controls.Add(this.lblTitle2);
            this.Controls.Add(this.lstItems1);
            this.Controls.Add(this.lblTitle1);
            this.Controls.Add(this.btnRead);
            this.Name = "Form1";
            this.Text = "vcs_ReadWrite_EXCEL6";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnRead;
        private System.Windows.Forms.Label lblTitle1;
        private System.Windows.Forms.ListBox lstItems1;
        private System.Windows.Forms.ListBox lstItems2;
        private System.Windows.Forms.Label lblTitle2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
    }
}

