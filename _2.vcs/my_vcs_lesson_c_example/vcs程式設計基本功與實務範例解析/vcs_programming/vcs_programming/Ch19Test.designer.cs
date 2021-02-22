namespace vcs_programming
{
    partial class Ch19Test
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
            this.btnCircle = new System.Windows.Forms.Button();
            this.btnCylinder = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnCircle
            // 
            this.btnCircle.Location = new System.Drawing.Point(13, 13);
            this.btnCircle.Margin = new System.Windows.Forms.Padding(4);
            this.btnCircle.Name = "btnCircle";
            this.btnCircle.Size = new System.Drawing.Size(133, 31);
            this.btnCircle.TabIndex = 1;
            this.btnCircle.Text = "Circle物件";
            this.btnCircle.UseVisualStyleBackColor = true;
            this.btnCircle.Click += new System.EventHandler(this.btnCircle_Click);
            // 
            // btnCylinder
            // 
            this.btnCylinder.Location = new System.Drawing.Point(175, 13);
            this.btnCylinder.Margin = new System.Windows.Forms.Padding(4);
            this.btnCylinder.Name = "btnCylinder";
            this.btnCylinder.Size = new System.Drawing.Size(133, 31);
            this.btnCylinder.TabIndex = 2;
            this.btnCylinder.Text = "Cylinder物件";
            this.btnCylinder.UseVisualStyleBackColor = true;
            this.btnCylinder.Click += new System.EventHandler(this.btnCylinder_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(175, 63);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(133, 31);
            this.button4.TabIndex = 3;
            this.button4.Text = "new改寫一";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(13, 115);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(133, 31);
            this.button5.TabIndex = 4;
            this.button5.Text = "new改寫二";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(175, 115);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(133, 31);
            this.button6.TabIndex = 5;
            this.button6.Text = "virtual與override";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(13, 63);
            this.button1.Margin = new System.Windows.Forms.Padding(4);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(133, 31);
            this.button1.TabIndex = 6;
            this.button1.Text = "型態轉換";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Ch19Test
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(323, 161);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.btnCylinder);
            this.Controls.Add(this.btnCircle);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "Ch19Test";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "繼承與多型";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCircle;
        private System.Windows.Forms.Button btnCylinder;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button1;
    }
}