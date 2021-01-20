namespace vcs_PID
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.button1 = new System.Windows.Forms.Button();
            this.tb_kp = new System.Windows.Forms.TextBox();
            this.tb_ki = new System.Windows.Forms.TextBox();
            this.tb_kd = new System.Windows.Forms.TextBox();
            this.tb_target = new System.Windows.Forms.TextBox();
            this.tb_max_speed = new System.Windows.Forms.TextBox();
            this.tb_max_duty = new System.Windows.Forms.TextBox();
            this.tb_min_speed = new System.Windows.Forms.TextBox();
            this.tb_min_duty = new System.Windows.Forms.TextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.tb_tolerance = new System.Windows.Forms.TextBox();
            this.cb_steps = new System.Windows.Forms.ComboBox();
            this.label_max_speed = new System.Windows.Forms.Label();
            this.label_STEP = new System.Windows.Forms.Label();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.label_pid_max = new System.Windows.Forms.Label();
            this.label_pid_min = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.ForeColor = System.Drawing.Color.Red;
            this.button1.Location = new System.Drawing.Point(330, 28);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(135, 32);
            this.button1.TabIndex = 0;
            this.button1.Text = "PID 1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // tb_kp
            // 
            this.tb_kp.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_kp.Location = new System.Drawing.Point(12, 29);
            this.tb_kp.Name = "tb_kp";
            this.tb_kp.Size = new System.Drawing.Size(100, 32);
            this.tb_kp.TabIndex = 1;
            this.tb_kp.Text = "0.4";
            this.tb_kp.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_ki
            // 
            this.tb_ki.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_ki.Location = new System.Drawing.Point(118, 29);
            this.tb_ki.Name = "tb_ki";
            this.tb_ki.Size = new System.Drawing.Size(100, 32);
            this.tb_ki.TabIndex = 2;
            this.tb_ki.Text = "0.4";
            this.tb_ki.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_kd
            // 
            this.tb_kd.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_kd.Location = new System.Drawing.Point(224, 29);
            this.tb_kd.Name = "tb_kd";
            this.tb_kd.Size = new System.Drawing.Size(100, 32);
            this.tb_kd.TabIndex = 3;
            this.tb_kd.Text = "0";
            this.tb_kd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_target
            // 
            this.tb_target.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_target.Location = new System.Drawing.Point(12, 91);
            this.tb_target.Name = "tb_target";
            this.tb_target.Size = new System.Drawing.Size(100, 32);
            this.tb_target.TabIndex = 4;
            this.tb_target.Text = "1000";
            this.tb_target.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_max_speed
            // 
            this.tb_max_speed.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_max_speed.Location = new System.Drawing.Point(118, 91);
            this.tb_max_speed.Name = "tb_max_speed";
            this.tb_max_speed.Size = new System.Drawing.Size(100, 32);
            this.tb_max_speed.TabIndex = 6;
            this.tb_max_speed.Text = "30000";
            this.tb_max_speed.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_max_duty
            // 
            this.tb_max_duty.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_max_duty.Location = new System.Drawing.Point(118, 150);
            this.tb_max_duty.Name = "tb_max_duty";
            this.tb_max_duty.Size = new System.Drawing.Size(100, 32);
            this.tb_max_duty.TabIndex = 7;
            this.tb_max_duty.Text = "100";
            this.tb_max_duty.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_min_speed
            // 
            this.tb_min_speed.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_min_speed.Location = new System.Drawing.Point(224, 91);
            this.tb_min_speed.Name = "tb_min_speed";
            this.tb_min_speed.Size = new System.Drawing.Size(100, 32);
            this.tb_min_speed.TabIndex = 8;
            this.tb_min_speed.Text = "0";
            this.tb_min_speed.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_min_duty
            // 
            this.tb_min_duty.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_min_duty.Location = new System.Drawing.Point(224, 150);
            this.tb_min_duty.Name = "tb_min_duty";
            this.tb_min_duty.Size = new System.Drawing.Size(100, 32);
            this.tb_min_duty.TabIndex = 9;
            this.tb_min_duty.Text = "0";
            this.tb_min_duty.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("Consolas", 12.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.Location = new System.Drawing.Point(224, 250);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(100, 32);
            this.button2.TabIndex = 10;
            this.button2.Text = "Reset";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox1.Location = new System.Drawing.Point(12, 294);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(453, 299);
            this.richTextBox1.TabIndex = 11;
            this.richTextBox1.Text = "";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(44, 5);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(250, 24);
            this.label1.TabIndex = 12;
            this.label1.Text = "KP       KI       KD";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(25, 67);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(298, 24);
            this.label2.TabIndex = 13;
            this.label2.Text = "Target  max_rpm  min_rpm";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(30, 126);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(298, 24);
            this.label3.TabIndex = 14;
            this.label3.Text = "steps  max_duty min_duty";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(471, 33);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(720, 560);
            this.panel1.TabIndex = 15;
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button3.ForeColor = System.Drawing.Color.Yellow;
            this.button3.Location = new System.Drawing.Point(330, 202);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(135, 32);
            this.button3.TabIndex = 17;
            this.button3.Text = "Linear";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("Consolas", 12.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button4.Location = new System.Drawing.Point(330, 250);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(135, 32);
            this.button4.TabIndex = 18;
            this.button4.Text = "Clear";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(7, 185);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(118, 24);
            this.label4.TabIndex = 20;
            this.label4.Text = "tolerance";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // tb_tolerance
            // 
            this.tb_tolerance.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_tolerance.Location = new System.Drawing.Point(12, 212);
            this.tb_tolerance.Name = "tb_tolerance";
            this.tb_tolerance.Size = new System.Drawing.Size(100, 32);
            this.tb_tolerance.TabIndex = 19;
            this.tb_tolerance.Text = "80";
            this.tb_tolerance.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // cb_steps
            // 
            this.cb_steps.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.cb_steps.FormattingEnabled = true;
            this.cb_steps.Items.AddRange(new object[] {
            "50",
            "100",
            "200"});
            this.cb_steps.Location = new System.Drawing.Point(12, 150);
            this.cb_steps.Name = "cb_steps";
            this.cb_steps.Size = new System.Drawing.Size(100, 32);
            this.cb_steps.TabIndex = 21;
            this.cb_steps.Text = "50";
            // 
            // label_max_speed
            // 
            this.label_max_speed.AutoSize = true;
            this.label_max_speed.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label_max_speed.ForeColor = System.Drawing.Color.Red;
            this.label_max_speed.Location = new System.Drawing.Point(131, 193);
            this.label_max_speed.Name = "label_max_speed";
            this.label_max_speed.Size = new System.Drawing.Size(58, 24);
            this.label_max_speed.TabIndex = 22;
            this.label_max_speed.Text = "Max:";
            // 
            // label_STEP
            // 
            this.label_STEP.AutoSize = true;
            this.label_STEP.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label_STEP.ForeColor = System.Drawing.Color.Black;
            this.label_STEP.Location = new System.Drawing.Point(119, 221);
            this.label_STEP.Name = "label_STEP";
            this.label_STEP.Size = new System.Drawing.Size(70, 24);
            this.label_STEP.TabIndex = 23;
            this.label_STEP.Text = "STEP:";
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button5.ForeColor = System.Drawing.Color.Green;
            this.button5.Location = new System.Drawing.Point(330, 91);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(135, 32);
            this.button5.TabIndex = 24;
            this.button5.Text = "PID 2";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button6.ForeColor = System.Drawing.Color.Blue;
            this.button6.Location = new System.Drawing.Point(330, 149);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(135, 32);
            this.button6.TabIndex = 25;
            this.button6.Text = "PID 3";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // label_pid_max
            // 
            this.label_pid_max.AutoSize = true;
            this.label_pid_max.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label_pid_max.ForeColor = System.Drawing.Color.Black;
            this.label_pid_max.Location = new System.Drawing.Point(12, 246);
            this.label_pid_max.Name = "label_pid_max";
            this.label_pid_max.Size = new System.Drawing.Size(90, 22);
            this.label_pid_max.TabIndex = 26;
            this.label_pid_max.Text = "pid_max:";
            // 
            // label_pid_min
            // 
            this.label_pid_min.AutoSize = true;
            this.label_pid_min.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label_pid_min.ForeColor = System.Drawing.Color.Black;
            this.label_pid_min.Location = new System.Drawing.Point(12, 269);
            this.label_pid_min.Name = "label_pid_min";
            this.label_pid_min.Size = new System.Drawing.Size(90, 22);
            this.label_pid_min.TabIndex = 27;
            this.label_pid_min.Text = "pid_min:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1200, 601);
            this.Controls.Add(this.label_pid_min);
            this.Controls.Add(this.label_pid_max);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.label_STEP);
            this.Controls.Add(this.label_max_speed);
            this.Controls.Add(this.cb_steps);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.tb_tolerance);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.tb_min_duty);
            this.Controls.Add(this.tb_min_speed);
            this.Controls.Add(this.tb_max_duty);
            this.Controls.Add(this.tb_max_speed);
            this.Controls.Add(this.tb_target);
            this.Controls.Add(this.tb_kd);
            this.Controls.Add(this.tb_ki);
            this.Controls.Add(this.tb_kp);
            this.Controls.Add(this.button1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "PID Test";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox tb_kp;
        private System.Windows.Forms.TextBox tb_ki;
        private System.Windows.Forms.TextBox tb_kd;
        private System.Windows.Forms.TextBox tb_target;
        private System.Windows.Forms.TextBox tb_max_speed;
        private System.Windows.Forms.TextBox tb_max_duty;
        private System.Windows.Forms.TextBox tb_min_speed;
        private System.Windows.Forms.TextBox tb_min_duty;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox tb_tolerance;
        private System.Windows.Forms.ComboBox cb_steps;
        private System.Windows.Forms.Label label_max_speed;
        private System.Windows.Forms.Label label_STEP;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Label label_pid_max;
        private System.Windows.Forms.Label label_pid_min;
    }
}

