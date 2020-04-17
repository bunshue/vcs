namespace WindowsFormsApplication1
{
    partial class ch2ex
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
            this.btnYellowBackColor = new System.Windows.Forms.Button();
            this.lblOutput = new System.Windows.Forms.Label();
            this.txtInput = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnRedForeColor = new System.Windows.Forms.Button();
            this.btnDisplay = new System.Windows.Forms.Button();
            this.btnRestore = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnYellowBackColor
            // 
            this.btnYellowBackColor.Location = new System.Drawing.Point(74, 112);
            this.btnYellowBackColor.Margin = new System.Windows.Forms.Padding(4);
            this.btnYellowBackColor.Name = "btnYellowBackColor";
            this.btnYellowBackColor.Size = new System.Drawing.Size(50, 37);
            this.btnYellowBackColor.TabIndex = 12;
            this.btnYellowBackColor.Text = "黃底";
            this.btnYellowBackColor.UseVisualStyleBackColor = true;
            this.btnYellowBackColor.Click += new System.EventHandler(this.btnYellowBackColor_Click);
            // 
            // lblOutput
            // 
            this.lblOutput.BackColor = System.Drawing.Color.Pink;
            this.lblOutput.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblOutput.ForeColor = System.Drawing.Color.Blue;
            this.lblOutput.Location = new System.Drawing.Point(16, 61);
            this.lblOutput.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblOutput.Name = "lblOutput";
            this.lblOutput.Size = new System.Drawing.Size(224, 36);
            this.lblOutput.TabIndex = 11;
            this.lblOutput.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // txtInput
            // 
            this.txtInput.Location = new System.Drawing.Point(92, 15);
            this.txtInput.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.txtInput.Name = "txtInput";
            this.txtInput.Size = new System.Drawing.Size(148, 27);
            this.txtInput.TabIndex = 8;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 26);
            this.label1.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(72, 16);
            this.label1.TabIndex = 7;
            this.label1.Text = "輸入文字";
            // 
            // btnRedForeColor
            // 
            this.btnRedForeColor.Location = new System.Drawing.Point(132, 112);
            this.btnRedForeColor.Margin = new System.Windows.Forms.Padding(4);
            this.btnRedForeColor.Name = "btnRedForeColor";
            this.btnRedForeColor.Size = new System.Drawing.Size(50, 37);
            this.btnRedForeColor.TabIndex = 13;
            this.btnRedForeColor.Text = "紅字";
            this.btnRedForeColor.UseVisualStyleBackColor = true;
            this.btnRedForeColor.Click += new System.EventHandler(this.btnRedForeColor_Click);
            // 
            // btnDisplay
            // 
            this.btnDisplay.Location = new System.Drawing.Point(16, 112);
            this.btnDisplay.Margin = new System.Windows.Forms.Padding(4);
            this.btnDisplay.Name = "btnDisplay";
            this.btnDisplay.Size = new System.Drawing.Size(50, 37);
            this.btnDisplay.TabIndex = 14;
            this.btnDisplay.Text = "顯示";
            this.btnDisplay.UseVisualStyleBackColor = true;
            this.btnDisplay.Click += new System.EventHandler(this.btnDisplay_Click);
            // 
            // btnRestore
            // 
            this.btnRestore.Location = new System.Drawing.Point(190, 112);
            this.btnRestore.Margin = new System.Windows.Forms.Padding(4);
            this.btnRestore.Name = "btnRestore";
            this.btnRestore.Size = new System.Drawing.Size(50, 37);
            this.btnRestore.TabIndex = 15;
            this.btnRestore.Text = "還原";
            this.btnRestore.UseVisualStyleBackColor = true;
            this.btnRestore.Click += new System.EventHandler(this.btnRestore_Click);
            // 
            // ch2ex
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(260, 166);
            this.Controls.Add(this.btnRestore);
            this.Controls.Add(this.btnDisplay);
            this.Controls.Add(this.btnRedForeColor);
            this.Controls.Add(this.btnYellowBackColor);
            this.Controls.Add(this.lblOutput);
            this.Controls.Add(this.txtInput);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "ch2ex";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "表單範例";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnYellowBackColor;
        private System.Windows.Forms.Label lblOutput;
        private System.Windows.Forms.TextBox txtInput;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnRedForeColor;
        private System.Windows.Forms.Button btnDisplay;
        private System.Windows.Forms.Button btnRestore;
    }
}