namespace howto_double_buffer
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
            this.chkDoubleBuffer = new System.Windows.Forms.CheckBox();
            this.btnRedraw = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // chkDoubleBuffer
            // 
            this.chkDoubleBuffer.AutoSize = true;
            this.chkDoubleBuffer.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.chkDoubleBuffer.ForeColor = System.Drawing.Color.White;
            this.chkDoubleBuffer.Location = new System.Drawing.Point(12, 11);
            this.chkDoubleBuffer.Name = "chkDoubleBuffer";
            this.chkDoubleBuffer.Size = new System.Drawing.Size(176, 23);
            this.chkDoubleBuffer.TabIndex = 0;
            this.chkDoubleBuffer.Text = "使用 Double Buffer";
            this.chkDoubleBuffer.UseVisualStyleBackColor = true;
            this.chkDoubleBuffer.CheckedChanged += new System.EventHandler(this.chkDoubleBuffer_CheckedChanged);
            // 
            // btnRedraw
            // 
            this.btnRedraw.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnRedraw.Location = new System.Drawing.Point(717, 11);
            this.btnRedraw.Name = "btnRedraw";
            this.btnRedraw.Size = new System.Drawing.Size(75, 32);
            this.btnRedraw.TabIndex = 1;
            this.btnRedraw.Text = "重畫";
            this.btnRedraw.UseVisualStyleBackColor = true;
            this.btnRedraw.Click += new System.EventHandler(this.btnRedraw_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("標楷體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.ForeColor = System.Drawing.Color.Red;
            this.label1.Location = new System.Drawing.Point(236, 11);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(175, 32);
            this.label1.TabIndex = 2;
            this.label1.Text = "按重畫按鈕";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnRedraw;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.ClientSize = new System.Drawing.Size(804, 611);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnRedraw);
            this.Controls.Add(this.chkDoubleBuffer);
            this.Name = "Form1";
            this.Text = "howto_double_buffer";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox chkDoubleBuffer;
        private System.Windows.Forms.Button btnRedraw;
        private System.Windows.Forms.Label label1;

    }
}

