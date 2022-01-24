namespace vcs_MyPlayer3
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
            this.lb_title = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.lb_main_mesg2 = new System.Windows.Forms.Label();
            this.lb_main_mesg3 = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // lb_title
            // 
            this.lb_title.AutoSize = true;
            this.lb_title.Location = new System.Drawing.Point(28, 21);
            this.lb_title.Name = "lb_title";
            this.lb_title.Size = new System.Drawing.Size(33, 12);
            this.lb_title.TabIndex = 0;
            this.lb_title.Text = "label1";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 208);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(764, 195);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "";
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // lb_main_mesg1
            // 
            this.lb_main_mesg1.AutoSize = true;
            this.lb_main_mesg1.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg1.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1.Location = new System.Drawing.Point(26, 58);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg1.TabIndex = 134;
            this.lb_main_mesg1.Text = "mesg1";
            // 
            // lb_main_mesg2
            // 
            this.lb_main_mesg2.AutoSize = true;
            this.lb_main_mesg2.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg2.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2.Location = new System.Drawing.Point(26, 94);
            this.lb_main_mesg2.Name = "lb_main_mesg2";
            this.lb_main_mesg2.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg2.TabIndex = 135;
            this.lb_main_mesg2.Text = "mesg2";
            // 
            // lb_main_mesg3
            // 
            this.lb_main_mesg3.AutoSize = true;
            this.lb_main_mesg3.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg3.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg3.Location = new System.Drawing.Point(26, 132);
            this.lb_main_mesg3.Name = "lb_main_mesg3";
            this.lb_main_mesg3.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg3.TabIndex = 136;
            this.lb_main_mesg3.Text = "mesg3";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(788, 415);
            this.Controls.Add(this.lb_main_mesg3);
            this.Controls.Add(this.lb_main_mesg2);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.lb_title);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_title;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Label lb_main_mesg2;
        private System.Windows.Forms.Label lb_main_mesg3;
        private System.Windows.Forms.Timer timer_display;
    }
}

