namespace WindowsFormsApplication2
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.p2 = new System.Windows.Forms.Panel();
            this.p3 = new System.Windows.Forms.Panel();
            this.p1 = new System.Windows.Forms.Panel();
            this.p0 = new System.Windows.Forms.Panel();
            this.button3 = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 74);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(340, 508);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.p2);
            this.panel1.Controls.Add(this.p3);
            this.panel1.Controls.Add(this.p1);
            this.panel1.Controls.Add(this.p0);
            this.panel1.Location = new System.Drawing.Point(380, 74);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(500, 500);
            this.panel1.TabIndex = 3;
            // 
            // p2
            // 
            this.p2.Location = new System.Drawing.Point(184, 188);
            this.p2.Name = "p2";
            this.p2.Size = new System.Drawing.Size(80, 59);
            this.p2.TabIndex = 1;
            // 
            // p3
            // 
            this.p3.Location = new System.Drawing.Point(87, 188);
            this.p3.Name = "p3";
            this.p3.Size = new System.Drawing.Size(80, 59);
            this.p3.TabIndex = 1;
            // 
            // p1
            // 
            this.p1.Location = new System.Drawing.Point(184, 112);
            this.p1.Name = "p1";
            this.p1.Size = new System.Drawing.Size(80, 59);
            this.p1.TabIndex = 1;
            // 
            // p0
            // 
            this.p0.Location = new System.Drawing.Point(87, 112);
            this.p0.Name = "p0";
            this.p0.Size = new System.Drawing.Size(80, 59);
            this.p0.TabIndex = 0;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(277, 30);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 4;
            this.button3.Text = "clear";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 200;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1099, 645);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.richTextBox1);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Panel p2;
        private System.Windows.Forms.Panel p3;
        private System.Windows.Forms.Panel p1;
        private System.Windows.Forms.Panel p0;
    }
}

