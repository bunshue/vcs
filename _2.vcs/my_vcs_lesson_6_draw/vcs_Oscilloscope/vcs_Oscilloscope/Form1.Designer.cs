namespace vcs_Oscilloscope
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
            this.btnLoad = new System.Windows.Forms.Button();
            this.UCOscilloscope1 = new vcs_Oscilloscope.UCOscilloscope();
            this.SuspendLayout();
            // 
            // btnLoad
            // 
            this.btnLoad.Location = new System.Drawing.Point(12, 12);
            this.btnLoad.Name = "btnLoad";
            this.btnLoad.Size = new System.Drawing.Size(75, 23);
            this.btnLoad.TabIndex = 0;
            this.btnLoad.Text = "Load";
            this.btnLoad.UseVisualStyleBackColor = true;
            this.btnLoad.Click += new System.EventHandler(this.btnLoad_Click);
            // 
            // UCOscilloscope1
            // 
            this.UCOscilloscope1.LineColor = System.Drawing.Color.BlueViolet;
            this.UCOscilloscope1.LineWidth = 2;
            this.UCOscilloscope1.Location = new System.Drawing.Point(7, 34);
            this.UCOscilloscope1.MappingDatas = null;
            this.UCOscilloscope1.MaxValue = 0;
            this.UCOscilloscope1.Name = "UCOscilloscope1";
            this.UCOscilloscope1.Ratio = 50;
            this.UCOscilloscope1.Size = new System.Drawing.Size(650, 200);
            this.UCOscilloscope1.TabIndex = 2;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(665, 268);
            this.Controls.Add(this.UCOscilloscope1);
            this.Controls.Add(this.btnLoad);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Mapping Oscilloscope";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnLoad;
        private UCOscilloscope UCOscilloscope1;
    }
}

