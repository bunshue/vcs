namespace vcs_FunctionGenerator
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
            this.label1 = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.numericUpDown_dc = new System.Windows.Forms.NumericUpDown();
            this.rb_4 = new System.Windows.Forms.RadioButton();
            this.rb_3 = new System.Windows.Forms.RadioButton();
            this.rb_2 = new System.Windows.Forms.RadioButton();
            this.rb_1 = new System.Windows.Forms.RadioButton();
            this.panel1 = new System.Windows.Forms.Panel();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_dc)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(12, 284);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 21);
            this.label1.TabIndex = 1;
            this.label1.Text = "label1";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(16, 369);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(451, 204);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(12, 334);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(58, 21);
            this.label2.TabIndex = 3;
            this.label2.Text = "label2";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.numericUpDown_dc);
            this.groupBox1.Controls.Add(this.rb_4);
            this.groupBox1.Controls.Add(this.rb_3);
            this.groupBox1.Controls.Add(this.rb_2);
            this.groupBox1.Controls.Add(this.rb_1);
            this.groupBox1.Location = new System.Drawing.Point(16, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(197, 201);
            this.groupBox1.TabIndex = 4;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "信號種類";
            // 
            // numericUpDown_dc
            // 
            this.numericUpDown_dc.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown_dc.Location = new System.Drawing.Point(99, 160);
            this.numericUpDown_dc.Maximum = new decimal(new int[] {
            10,
            0,
            0,
            0});
            this.numericUpDown_dc.Minimum = new decimal(new int[] {
            10,
            0,
            0,
            -2147483648});
            this.numericUpDown_dc.Name = "numericUpDown_dc";
            this.numericUpDown_dc.Size = new System.Drawing.Size(80, 33);
            this.numericUpDown_dc.TabIndex = 4;
            this.numericUpDown_dc.ValueChanged += new System.EventHandler(this.numericUpDown_dc_ValueChanged);
            // 
            // rb_4
            // 
            this.rb_4.AutoSize = true;
            this.rb_4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_4.Location = new System.Drawing.Point(17, 162);
            this.rb_4.Name = "rb_4";
            this.rb_4.Size = new System.Drawing.Size(52, 23);
            this.rb_4.TabIndex = 3;
            this.rb_4.Text = "DC";
            this.rb_4.UseVisualStyleBackColor = true;
            this.rb_4.CheckedChanged += new System.EventHandler(this.rb_4_CheckedChanged);
            // 
            // rb_3
            // 
            this.rb_3.AutoSize = true;
            this.rb_3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_3.Location = new System.Drawing.Point(17, 117);
            this.rb_3.Name = "rb_3";
            this.rb_3.Size = new System.Drawing.Size(65, 23);
            this.rb_3.TabIndex = 2;
            this.rb_3.Text = "隨機";
            this.rb_3.UseVisualStyleBackColor = true;
            this.rb_3.CheckedChanged += new System.EventHandler(this.rb_3_CheckedChanged);
            // 
            // rb_2
            // 
            this.rb_2.AutoSize = true;
            this.rb_2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_2.Location = new System.Drawing.Point(17, 71);
            this.rb_2.Name = "rb_2";
            this.rb_2.Size = new System.Drawing.Size(65, 23);
            this.rb_2.TabIndex = 1;
            this.rb_2.Text = "正弦";
            this.rb_2.UseVisualStyleBackColor = true;
            this.rb_2.CheckedChanged += new System.EventHandler(this.rb_2_CheckedChanged);
            // 
            // rb_1
            // 
            this.rb_1.AutoSize = true;
            this.rb_1.Checked = true;
            this.rb_1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_1.Location = new System.Drawing.Point(17, 31);
            this.rb_1.Name = "rb_1";
            this.rb_1.Size = new System.Drawing.Size(65, 23);
            this.rb_1.TabIndex = 0;
            this.rb_1.TabStop = true;
            this.rb_1.Text = "線性";
            this.rb_1.UseVisualStyleBackColor = true;
            this.rb_1.CheckedChanged += new System.EventHandler(this.rb_1_CheckedChanged);
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(239, 16);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(503, 320);
            this.panel1.TabIndex = 5;
            this.panel1.Paint += new System.Windows.Forms.PaintEventHandler(this.panel1_Paint);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(965, 585);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label1);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_dc)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb_3;
        private System.Windows.Forms.RadioButton rb_2;
        private System.Windows.Forms.RadioButton rb_1;
        private System.Windows.Forms.NumericUpDown numericUpDown_dc;
        private System.Windows.Forms.RadioButton rb_4;
        private System.Windows.Forms.Panel panel1;
    }
}

