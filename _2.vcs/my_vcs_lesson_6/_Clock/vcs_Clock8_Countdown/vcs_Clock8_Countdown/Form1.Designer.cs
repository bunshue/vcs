namespace vcs_Clock8_Countdown
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
            this.components = new System.ComponentModel.Container();
            this.Label1 = new System.Windows.Forms.Label();
            this.lblEvent = new System.Windows.Forms.Label();
            this.tmrCheckTime = new System.Windows.Forms.Timer(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.lb_time = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.ForeColor = System.Drawing.Color.Red;
            this.Label1.Location = new System.Drawing.Point(21, 225);
            this.Label1.Margin = new System.Windows.Forms.Padding(12, 0, 12, 0);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(107, 46);
            this.Label1.TabIndex = 11;
            this.Label1.Text = "Until";
            // 
            // lblEvent
            // 
            this.lblEvent.AutoSize = true;
            this.lblEvent.ForeColor = System.Drawing.Color.Red;
            this.lblEvent.Location = new System.Drawing.Point(137, 261);
            this.lblEvent.Margin = new System.Windows.Forms.Padding(12, 0, 12, 0);
            this.lblEvent.Name = "lblEvent";
            this.lblEvent.Size = new System.Drawing.Size(167, 46);
            this.lblEvent.TabIndex = 10;
            this.lblEvent.Text = "<event>";
            // 
            // tmrCheckTime
            // 
            this.tmrCheckTime.Interval = 500;
            this.tmrCheckTime.Tick += new System.EventHandler(this.tmrCheckTime_Tick);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 341);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(509, 169);
            this.richTextBox1.TabIndex = 12;
            this.richTextBox1.Text = "";
            // 
            // lb_time
            // 
            this.lb_time.AutoSize = true;
            this.lb_time.ForeColor = System.Drawing.Color.Blue;
            this.lb_time.Location = new System.Drawing.Point(21, 18);
            this.lb_time.Margin = new System.Windows.Forms.Padding(12, 0, 12, 0);
            this.lb_time.Name = "lb_time";
            this.lb_time.Size = new System.Drawing.Size(165, 46);
            this.lb_time.TabIndex = 13;
            this.lb_time.Text = "10 days";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(24F, 46F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(868, 522);
            this.Controls.Add(this.lb_time);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.lblEvent);
            this.Font = new System.Drawing.Font("Arial", 30F, System.Drawing.FontStyle.Bold);
            this.Margin = new System.Windows.Forms.Padding(12, 11, 12, 11);
            this.Name = "Form1";
            this.Text = "vcs_Clock8_Countdown";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.Label lblEvent;
        internal System.Windows.Forms.Timer tmrCheckTime;
        private System.Windows.Forms.RichTextBox richTextBox1;
        internal System.Windows.Forms.Label lb_time;
    }
}

