namespace vcs_AMCap1
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.checkBox2 = new System.Windows.Forms.CheckBox();
            this.timer_focus = new System.Windows.Forms.Timer(this.components);
            this.rb_3X3 = new System.Windows.Forms.RadioButton();
            this.rb_4X4 = new System.Windows.Forms.RadioButton();
            this.rb_5X5 = new System.Windows.Forms.RadioButton();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(135, 27);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDoubleClick);
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(22, 19);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(82, 24);
            this.lb_main_mesg.TabIndex = 2;
            this.lb_main_mesg.Text = "label1";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // checkBox2
            // 
            this.checkBox2.AutoSize = true;
            this.checkBox2.Font = new System.Drawing.Font("標楷體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox2.Location = new System.Drawing.Point(12, 102);
            this.checkBox2.Name = "checkBox2";
            this.checkBox2.Size = new System.Drawing.Size(117, 25);
            this.checkBox2.TabIndex = 4;
            this.checkBox2.Text = "顯示格線";
            this.checkBox2.UseVisualStyleBackColor = true;
            this.checkBox2.CheckedChanged += new System.EventHandler(this.checkBox2_CheckedChanged);
            // 
            // timer_focus
            // 
            this.timer_focus.Enabled = true;
            this.timer_focus.Interval = 3000;
            this.timer_focus.Tick += new System.EventHandler(this.timer_focus_Tick);
            // 
            // rb_3X3
            // 
            this.rb_3X3.AutoSize = true;
            this.rb_3X3.Location = new System.Drawing.Point(44, 134);
            this.rb_3X3.Name = "rb_3X3";
            this.rb_3X3.Size = new System.Drawing.Size(43, 16);
            this.rb_3X3.TabIndex = 13;
            this.rb_3X3.Text = "3X3";
            this.rb_3X3.UseVisualStyleBackColor = true;
            // 
            // rb_4X4
            // 
            this.rb_4X4.AutoSize = true;
            this.rb_4X4.Checked = true;
            this.rb_4X4.Location = new System.Drawing.Point(44, 156);
            this.rb_4X4.Name = "rb_4X4";
            this.rb_4X4.Size = new System.Drawing.Size(43, 16);
            this.rb_4X4.TabIndex = 14;
            this.rb_4X4.TabStop = true;
            this.rb_4X4.Text = "4X4";
            this.rb_4X4.UseVisualStyleBackColor = true;
            // 
            // rb_5X5
            // 
            this.rb_5X5.AutoSize = true;
            this.rb_5X5.Location = new System.Drawing.Point(44, 178);
            this.rb_5X5.Name = "rb_5X5";
            this.rb_5X5.Size = new System.Drawing.Size(43, 16);
            this.rb_5X5.TabIndex = 15;
            this.rb_5X5.Text = "5X5";
            this.rb_5X5.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(959, 706);
            this.Controls.Add(this.rb_5X5);
            this.Controls.Add(this.rb_4X4);
            this.Controls.Add(this.rb_3X3);
            this.Controls.Add(this.checkBox2);
            this.Controls.Add(this.lb_main_mesg);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Capture";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Form1_FormClosed);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label lb_main_mesg;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.CheckBox checkBox2;
        private System.Windows.Forms.Timer timer_focus;
        private System.Windows.Forms.RadioButton rb_3X3;
        private System.Windows.Forms.RadioButton rb_4X4;
        private System.Windows.Forms.RadioButton rb_5X5;
    }
}

