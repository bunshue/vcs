namespace vcs_PictureMagnify1
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rb_magnifying_type2 = new System.Windows.Forms.RadioButton();
            this.rb_magnifying_type1 = new System.Windows.Forms.RadioButton();
            this.rb_magnifying_type0 = new System.Windows.Forms.RadioButton();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rb_magnifying_type2);
            this.groupBox1.Controls.Add(this.rb_magnifying_type1);
            this.groupBox1.Controls.Add(this.rb_magnifying_type0);
            this.groupBox1.Location = new System.Drawing.Point(696, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(133, 168);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "放大鏡形式";
            // 
            // rb_magnifying_type2
            // 
            this.rb_magnifying_type2.AutoSize = true;
            this.rb_magnifying_type2.Location = new System.Drawing.Point(25, 103);
            this.rb_magnifying_type2.Name = "rb_magnifying_type2";
            this.rb_magnifying_type2.Size = new System.Drawing.Size(47, 16);
            this.rb_magnifying_type2.TabIndex = 2;
            this.rb_magnifying_type2.TabStop = true;
            this.rb_magnifying_type2.Text = "心形";
            this.rb_magnifying_type2.UseVisualStyleBackColor = true;
            this.rb_magnifying_type2.CheckedChanged += new System.EventHandler(this.rb_magnifying_type_CheckedChanged);
            // 
            // rb_magnifying_type1
            // 
            this.rb_magnifying_type1.AutoSize = true;
            this.rb_magnifying_type1.Location = new System.Drawing.Point(25, 63);
            this.rb_magnifying_type1.Name = "rb_magnifying_type1";
            this.rb_magnifying_type1.Size = new System.Drawing.Size(47, 16);
            this.rb_magnifying_type1.TabIndex = 1;
            this.rb_magnifying_type1.TabStop = true;
            this.rb_magnifying_type1.Text = "圓形";
            this.rb_magnifying_type1.UseVisualStyleBackColor = true;
            this.rb_magnifying_type1.CheckedChanged += new System.EventHandler(this.rb_magnifying_type_CheckedChanged);
            // 
            // rb_magnifying_type0
            // 
            this.rb_magnifying_type0.AutoSize = true;
            this.rb_magnifying_type0.Location = new System.Drawing.Point(25, 31);
            this.rb_magnifying_type0.Name = "rb_magnifying_type0";
            this.rb_magnifying_type0.Size = new System.Drawing.Size(47, 16);
            this.rb_magnifying_type0.TabIndex = 0;
            this.rb_magnifying_type0.TabStop = true;
            this.rb_magnifying_type0.Text = "矩形";
            this.rb_magnifying_type0.UseVisualStyleBackColor = true;
            this.rb_magnifying_type0.CheckedChanged += new System.EventHandler(this.rb_magnifying_type_CheckedChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(841, 509);
            this.Controls.Add(this.groupBox1);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "呈現部分影像";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseMove);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb_magnifying_type0;
        private System.Windows.Forms.RadioButton rb_magnifying_type2;
        private System.Windows.Forms.RadioButton rb_magnifying_type1;
    }
}

