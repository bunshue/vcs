namespace vcs_programming
{
    partial class ShapeManagerForm
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
            this.lblCounter = new System.Windows.Forms.Label();
            this.txtOutput = new System.Windows.Forms.TextBox();
            this.btnTriangle = new System.Windows.Forms.Button();
            this.btnRectangle = new System.Windows.Forms.Button();
            this.btnListing = new System.Windows.Forms.Button();
            this.btnCompare = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblCounter
            // 
            this.lblCounter.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblCounter.Location = new System.Drawing.Point(12, 16);
            this.lblCounter.Name = "lblCounter";
            this.lblCounter.Size = new System.Drawing.Size(638, 29);
            this.lblCounter.TabIndex = 13;
            this.lblCounter.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(12, 48);
            this.txtOutput.Multiline = true;
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ReadOnly = true;
            this.txtOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtOutput.Size = new System.Drawing.Size(638, 176);
            this.txtOutput.TabIndex = 10;
            this.txtOutput.WordWrap = false;
            // 
            // btnTriangle
            // 
            this.btnTriangle.Location = new System.Drawing.Point(656, 16);
            this.btnTriangle.Name = "btnTriangle";
            this.btnTriangle.Size = new System.Drawing.Size(162, 31);
            this.btnTriangle.TabIndex = 14;
            this.btnTriangle.Text = "新增三角形";
            this.btnTriangle.UseVisualStyleBackColor = true;
            this.btnTriangle.Click += new System.EventHandler(this.btnTriangle_Click);
            // 
            // btnRectangle
            // 
            this.btnRectangle.Location = new System.Drawing.Point(656, 53);
            this.btnRectangle.Name = "btnRectangle";
            this.btnRectangle.Size = new System.Drawing.Size(162, 31);
            this.btnRectangle.TabIndex = 15;
            this.btnRectangle.Text = "新增矩形";
            this.btnRectangle.UseVisualStyleBackColor = true;
            this.btnRectangle.Click += new System.EventHandler(this.btnRectangle_Click);
            // 
            // btnListing
            // 
            this.btnListing.Location = new System.Drawing.Point(656, 90);
            this.btnListing.Name = "btnListing";
            this.btnListing.Size = new System.Drawing.Size(162, 31);
            this.btnListing.TabIndex = 16;
            this.btnListing.Text = "列出所有圖形";
            this.btnListing.UseVisualStyleBackColor = true;
            this.btnListing.Click += new System.EventHandler(this.btnListing_Click);
            // 
            // btnCompare
            // 
            this.btnCompare.Location = new System.Drawing.Point(656, 131);
            this.btnCompare.Name = "btnCompare";
            this.btnCompare.Size = new System.Drawing.Size(162, 31);
            this.btnCompare.TabIndex = 17;
            this.btnCompare.Text = "圖形比較";
            this.btnCompare.UseVisualStyleBackColor = true;
            this.btnCompare.Click += new System.EventHandler(this.btnCompare_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 230);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(806, 385);
            this.richTextBox1.TabIndex = 18;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(749, 572);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(58, 31);
            this.bt_clear.TabIndex = 19;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // ShapeManagerForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(830, 627);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btnCompare);
            this.Controls.Add(this.btnListing);
            this.Controls.Add(this.btnRectangle);
            this.Controls.Add(this.btnTriangle);
            this.Controls.Add(this.lblCounter);
            this.Controls.Add(this.txtOutput);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "ShapeManagerForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "圖形管理";
            this.Load += new System.EventHandler(this.ShapeManagerForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblCounter;
        private System.Windows.Forms.TextBox txtOutput;
        private System.Windows.Forms.Button btnTriangle;
        private System.Windows.Forms.Button btnRectangle;
        private System.Windows.Forms.Button btnListing;
        private System.Windows.Forms.Button btnCompare;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
    }
}