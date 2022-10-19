namespace Test
{
    partial class FrmMain2
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
            this.components = new System.ComponentModel.Container();
            this.ucledDataTime1 = new HZH_Controls.Controls.UCLEDDataTime();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // ucledDataTime1
            // 
            this.ucledDataTime1.LineWidth = 8;
            this.ucledDataTime1.Location = new System.Drawing.Point(54, 81);
            this.ucledDataTime1.Name = "ucledDataTime1";
            this.ucledDataTime1.Size = new System.Drawing.Size(650, 58);
            this.ucledDataTime1.TabIndex = 0;
            this.ucledDataTime1.Value = new System.DateTime(2022, 10, 19, 11, 3, 53, 163);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // FrmMain2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.ucledDataTime1);
            this.Name = "FrmMain2";
            this.Text = "FrmMain2";
            this.Load += new System.EventHandler(this.FrmMain2_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private HZH_Controls.Controls.UCLEDDataTime ucledDataTime1;
        private System.Windows.Forms.Timer timer1;
    }
}