namespace howto_pickover_popcorn_color
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
            this.btnClear = new System.Windows.Forms.Button();
            this.txtDx = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.txtIterationsPerPixel = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btnPlotAll = new System.Windows.Forms.Button();
            this.txtH = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // btnClear
            // 
            this.btnClear.Location = new System.Drawing.Point(349, 9);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(60, 21);
            this.btnClear.TabIndex = 25;
            this.btnClear.Text = "Clear";
            this.btnClear.UseVisualStyleBackColor = true;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // txtDx
            // 
            this.txtDx.Location = new System.Drawing.Point(217, 11);
            this.txtDx.Name = "txtDx";
            this.txtDx.Size = new System.Drawing.Size(34, 22);
            this.txtDx.TabIndex = 21;
            this.txtDx.Text = "10";
            this.txtDx.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(190, 14);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(20, 12);
            this.label3.TabIndex = 24;
            this.label3.Text = "dx:";
            // 
            // txtIterationsPerPixel
            // 
            this.txtIterationsPerPixel.Location = new System.Drawing.Point(141, 11);
            this.txtIterationsPerPixel.Name = "txtIterationsPerPixel";
            this.txtIterationsPerPixel.Size = new System.Drawing.Size(34, 22);
            this.txtIterationsPerPixel.TabIndex = 19;
            this.txtIterationsPerPixel.Text = "50";
            this.txtIterationsPerPixel.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(82, 14);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(51, 12);
            this.label2.TabIndex = 23;
            this.label2.Text = "Iterations:";
            // 
            // btnPlotAll
            // 
            this.btnPlotAll.Location = new System.Drawing.Point(283, 9);
            this.btnPlotAll.Name = "btnPlotAll";
            this.btnPlotAll.Size = new System.Drawing.Size(60, 21);
            this.btnPlotAll.TabIndex = 22;
            this.btnPlotAll.Text = "Plot All";
            this.btnPlotAll.UseVisualStyleBackColor = true;
            this.btnPlotAll.Click += new System.EventHandler(this.btnPlotAll_Click);
            // 
            // txtH
            // 
            this.txtH.Location = new System.Drawing.Point(33, 11);
            this.txtH.Name = "txtH";
            this.txtH.Size = new System.Drawing.Size(34, 22);
            this.txtH.TabIndex = 17;
            this.txtH.Text = "0.05";
            this.txtH.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(11, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(14, 12);
            this.label1.TabIndex = 20;
            this.label1.Text = "h:";
            // 
            // picCanvas
            // 
            this.picCanvas.BackColor = System.Drawing.Color.Black;
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Cursor = System.Windows.Forms.Cursors.Default;
            this.picCanvas.Location = new System.Drawing.Point(11, 36);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(400, 277);
            this.picCanvas.TabIndex = 18;
            this.picCanvas.TabStop = false;
            this.picCanvas.MouseClick += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseClick);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnPlotAll;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(684, 562);
            this.Controls.Add(this.btnClear);
            this.Controls.Add(this.txtDx);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtIterationsPerPixel);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnPlotAll);
            this.Controls.Add(this.txtH);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picCanvas);
            this.Name = "Form1";
            this.Text = "howto_pickover_popcorn_color";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.TextBox txtDx;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtIterationsPerPixel;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnPlotAll;
        private System.Windows.Forms.TextBox txtH;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox picCanvas;
    }
}

