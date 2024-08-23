namespace vcs_Thread_Example1
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
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.button02 = new System.Windows.Forms.Button();
            this.button01 = new System.Windows.Forms.Button();
            this.button00 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.button12 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button22 = new System.Windows.Forms.Button();
            this.button21 = new System.Windows.Forms.Button();
            this.button20 = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.button32 = new System.Windows.Forms.Button();
            this.button31 = new System.Windows.Forms.Button();
            this.button30 = new System.Windows.Forms.Button();
            this.groupBox7 = new System.Windows.Forms.GroupBox();
            this.button72 = new System.Windows.Forms.Button();
            this.button71 = new System.Windows.Forms.Button();
            this.button70 = new System.Windows.Forms.Button();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.button62 = new System.Windows.Forms.Button();
            this.button61 = new System.Windows.Forms.Button();
            this.button60 = new System.Windows.Forms.Button();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.button52 = new System.Windows.Forms.Button();
            this.button51 = new System.Windows.Forms.Button();
            this.button50 = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.button42 = new System.Windows.Forms.Button();
            this.button41 = new System.Windows.Forms.Button();
            this.button40 = new System.Windows.Forms.Button();
            this.groupBox0.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox7.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(665, 83);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(71, 30);
            this.bt_clear.TabIndex = 27;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(636, 13);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 26;
            this.richTextBox1.Text = "";
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.button02);
            this.groupBox0.Controls.Add(this.button01);
            this.groupBox0.Controls.Add(this.button00);
            this.groupBox0.Location = new System.Drawing.Point(12, 13);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(150, 150);
            this.groupBox0.TabIndex = 28;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "Thread使用範例0";
            // 
            // button02
            // 
            this.button02.Location = new System.Drawing.Point(23, 104);
            this.button02.Name = "button02";
            this.button02.Size = new System.Drawing.Size(90, 30);
            this.button02.TabIndex = 2;
            this.button02.Text = "狀態";
            this.button02.UseVisualStyleBackColor = true;
            this.button02.Click += new System.EventHandler(this.button02_Click);
            // 
            // button01
            // 
            this.button01.Location = new System.Drawing.Point(23, 59);
            this.button01.Name = "button01";
            this.button01.Size = new System.Drawing.Size(90, 30);
            this.button01.TabIndex = 1;
            this.button01.Text = "停止";
            this.button01.UseVisualStyleBackColor = true;
            this.button01.Click += new System.EventHandler(this.button01_Click);
            // 
            // button00
            // 
            this.button00.Location = new System.Drawing.Point(23, 21);
            this.button00.Name = "button00";
            this.button00.Size = new System.Drawing.Size(90, 30);
            this.button00.TabIndex = 0;
            this.button00.Text = "啟動";
            this.button00.UseVisualStyleBackColor = true;
            this.button00.Click += new System.EventHandler(this.button00_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button12);
            this.groupBox1.Controls.Add(this.button11);
            this.groupBox1.Controls.Add(this.button10);
            this.groupBox1.Location = new System.Drawing.Point(168, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(150, 150);
            this.groupBox1.TabIndex = 29;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Thread使用範例1";
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(23, 104);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(90, 30);
            this.button12.TabIndex = 2;
            this.button12.Text = "狀態";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(23, 59);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(90, 30);
            this.button11.TabIndex = 1;
            this.button11.Text = "停止";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(23, 21);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(90, 30);
            this.button10.TabIndex = 0;
            this.button10.Text = "啟動";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button22);
            this.groupBox2.Controls.Add(this.button21);
            this.groupBox2.Controls.Add(this.button20);
            this.groupBox2.Location = new System.Drawing.Point(324, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(150, 150);
            this.groupBox2.TabIndex = 30;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Thread使用範例2";
            // 
            // button22
            // 
            this.button22.Location = new System.Drawing.Point(23, 104);
            this.button22.Name = "button22";
            this.button22.Size = new System.Drawing.Size(90, 30);
            this.button22.TabIndex = 2;
            this.button22.Text = "狀態";
            this.button22.UseVisualStyleBackColor = true;
            this.button22.Click += new System.EventHandler(this.button22_Click);
            // 
            // button21
            // 
            this.button21.Location = new System.Drawing.Point(23, 59);
            this.button21.Name = "button21";
            this.button21.Size = new System.Drawing.Size(90, 30);
            this.button21.TabIndex = 1;
            this.button21.Text = "停止";
            this.button21.UseVisualStyleBackColor = true;
            this.button21.Click += new System.EventHandler(this.button21_Click);
            // 
            // button20
            // 
            this.button20.Location = new System.Drawing.Point(23, 21);
            this.button20.Name = "button20";
            this.button20.Size = new System.Drawing.Size(90, 30);
            this.button20.TabIndex = 0;
            this.button20.Text = "啟動";
            this.button20.UseVisualStyleBackColor = true;
            this.button20.Click += new System.EventHandler(this.button20_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.button32);
            this.groupBox3.Controls.Add(this.button31);
            this.groupBox3.Controls.Add(this.button30);
            this.groupBox3.Location = new System.Drawing.Point(480, 13);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(150, 150);
            this.groupBox3.TabIndex = 30;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Thread使用範例3";
            // 
            // button32
            // 
            this.button32.Location = new System.Drawing.Point(23, 104);
            this.button32.Name = "button32";
            this.button32.Size = new System.Drawing.Size(90, 30);
            this.button32.TabIndex = 2;
            this.button32.Text = "狀態";
            this.button32.UseVisualStyleBackColor = true;
            this.button32.Click += new System.EventHandler(this.button32_Click);
            // 
            // button31
            // 
            this.button31.Location = new System.Drawing.Point(23, 59);
            this.button31.Name = "button31";
            this.button31.Size = new System.Drawing.Size(90, 30);
            this.button31.TabIndex = 1;
            this.button31.Text = "停止";
            this.button31.UseVisualStyleBackColor = true;
            this.button31.Click += new System.EventHandler(this.button31_Click);
            // 
            // button30
            // 
            this.button30.Location = new System.Drawing.Point(23, 21);
            this.button30.Name = "button30";
            this.button30.Size = new System.Drawing.Size(90, 30);
            this.button30.TabIndex = 0;
            this.button30.Text = "啟動";
            this.button30.UseVisualStyleBackColor = true;
            this.button30.Click += new System.EventHandler(this.button30_Click);
            // 
            // groupBox7
            // 
            this.groupBox7.Controls.Add(this.button72);
            this.groupBox7.Controls.Add(this.button71);
            this.groupBox7.Controls.Add(this.button70);
            this.groupBox7.Location = new System.Drawing.Point(480, 169);
            this.groupBox7.Name = "groupBox7";
            this.groupBox7.Size = new System.Drawing.Size(150, 150);
            this.groupBox7.TabIndex = 33;
            this.groupBox7.TabStop = false;
            this.groupBox7.Text = "Thread使用範例7";
            // 
            // button72
            // 
            this.button72.Location = new System.Drawing.Point(23, 104);
            this.button72.Name = "button72";
            this.button72.Size = new System.Drawing.Size(90, 30);
            this.button72.TabIndex = 2;
            this.button72.Text = "狀態";
            this.button72.UseVisualStyleBackColor = true;
            this.button72.Click += new System.EventHandler(this.button72_Click);
            // 
            // button71
            // 
            this.button71.Location = new System.Drawing.Point(23, 59);
            this.button71.Name = "button71";
            this.button71.Size = new System.Drawing.Size(90, 30);
            this.button71.TabIndex = 1;
            this.button71.Text = "停止";
            this.button71.UseVisualStyleBackColor = true;
            this.button71.Click += new System.EventHandler(this.button71_Click);
            // 
            // button70
            // 
            this.button70.Location = new System.Drawing.Point(23, 21);
            this.button70.Name = "button70";
            this.button70.Size = new System.Drawing.Size(90, 30);
            this.button70.TabIndex = 0;
            this.button70.Text = "啟動";
            this.button70.UseVisualStyleBackColor = true;
            this.button70.Click += new System.EventHandler(this.button70_Click);
            // 
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.button62);
            this.groupBox6.Controls.Add(this.button61);
            this.groupBox6.Controls.Add(this.button60);
            this.groupBox6.Location = new System.Drawing.Point(324, 168);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(150, 150);
            this.groupBox6.TabIndex = 34;
            this.groupBox6.TabStop = false;
            this.groupBox6.Text = "Thread使用範例6";
            // 
            // button62
            // 
            this.button62.Location = new System.Drawing.Point(23, 104);
            this.button62.Name = "button62";
            this.button62.Size = new System.Drawing.Size(90, 30);
            this.button62.TabIndex = 2;
            this.button62.Text = "狀態";
            this.button62.UseVisualStyleBackColor = true;
            this.button62.Click += new System.EventHandler(this.button62_Click);
            // 
            // button61
            // 
            this.button61.Location = new System.Drawing.Point(23, 59);
            this.button61.Name = "button61";
            this.button61.Size = new System.Drawing.Size(90, 30);
            this.button61.TabIndex = 1;
            this.button61.Text = "停止";
            this.button61.UseVisualStyleBackColor = true;
            this.button61.Click += new System.EventHandler(this.button61_Click);
            // 
            // button60
            // 
            this.button60.Location = new System.Drawing.Point(23, 21);
            this.button60.Name = "button60";
            this.button60.Size = new System.Drawing.Size(90, 30);
            this.button60.TabIndex = 0;
            this.button60.Text = "啟動";
            this.button60.UseVisualStyleBackColor = true;
            this.button60.Click += new System.EventHandler(this.button60_Click);
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.button52);
            this.groupBox5.Controls.Add(this.button51);
            this.groupBox5.Controls.Add(this.button50);
            this.groupBox5.Location = new System.Drawing.Point(168, 168);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(150, 150);
            this.groupBox5.TabIndex = 32;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Thread使用範例5";
            // 
            // button52
            // 
            this.button52.Location = new System.Drawing.Point(23, 104);
            this.button52.Name = "button52";
            this.button52.Size = new System.Drawing.Size(90, 30);
            this.button52.TabIndex = 2;
            this.button52.Text = "狀態";
            this.button52.UseVisualStyleBackColor = true;
            this.button52.Click += new System.EventHandler(this.button52_Click);
            // 
            // button51
            // 
            this.button51.Location = new System.Drawing.Point(23, 59);
            this.button51.Name = "button51";
            this.button51.Size = new System.Drawing.Size(90, 30);
            this.button51.TabIndex = 1;
            this.button51.Text = "停止";
            this.button51.UseVisualStyleBackColor = true;
            this.button51.Click += new System.EventHandler(this.button51_Click);
            // 
            // button50
            // 
            this.button50.Location = new System.Drawing.Point(23, 21);
            this.button50.Name = "button50";
            this.button50.Size = new System.Drawing.Size(90, 30);
            this.button50.TabIndex = 0;
            this.button50.Text = "啟動";
            this.button50.UseVisualStyleBackColor = true;
            this.button50.Click += new System.EventHandler(this.button50_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.button42);
            this.groupBox4.Controls.Add(this.button41);
            this.groupBox4.Controls.Add(this.button40);
            this.groupBox4.Location = new System.Drawing.Point(12, 169);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(150, 150);
            this.groupBox4.TabIndex = 31;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Thread使用範例4";
            // 
            // button42
            // 
            this.button42.Location = new System.Drawing.Point(23, 104);
            this.button42.Name = "button42";
            this.button42.Size = new System.Drawing.Size(90, 30);
            this.button42.TabIndex = 2;
            this.button42.Text = "狀態";
            this.button42.UseVisualStyleBackColor = true;
            this.button42.Click += new System.EventHandler(this.button42_Click);
            // 
            // button41
            // 
            this.button41.Location = new System.Drawing.Point(23, 59);
            this.button41.Name = "button41";
            this.button41.Size = new System.Drawing.Size(90, 30);
            this.button41.TabIndex = 1;
            this.button41.Text = "停止";
            this.button41.UseVisualStyleBackColor = true;
            this.button41.Click += new System.EventHandler(this.button41_Click);
            // 
            // button40
            // 
            this.button40.Location = new System.Drawing.Point(23, 21);
            this.button40.Name = "button40";
            this.button40.Size = new System.Drawing.Size(90, 30);
            this.button40.TabIndex = 0;
            this.button40.Text = "啟動";
            this.button40.UseVisualStyleBackColor = true;
            this.button40.Click += new System.EventHandler(this.button40_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(752, 334);
            this.Controls.Add(this.groupBox7);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox6);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Thread使用範例";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox0.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox7.ResumeLayout(false);
            this.groupBox6.ResumeLayout(false);
            this.groupBox5.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.Button button02;
        private System.Windows.Forms.Button button01;
        private System.Windows.Forms.Button button00;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button22;
        private System.Windows.Forms.Button button21;
        private System.Windows.Forms.Button button20;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Button button32;
        private System.Windows.Forms.Button button31;
        private System.Windows.Forms.Button button30;
        private System.Windows.Forms.GroupBox groupBox7;
        private System.Windows.Forms.Button button72;
        private System.Windows.Forms.Button button71;
        private System.Windows.Forms.Button button70;
        private System.Windows.Forms.GroupBox groupBox6;
        private System.Windows.Forms.Button button62;
        private System.Windows.Forms.Button button61;
        private System.Windows.Forms.Button button60;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.Button button52;
        private System.Windows.Forms.Button button51;
        private System.Windows.Forms.Button button50;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button button42;
        private System.Windows.Forms.Button button41;
        private System.Windows.Forms.Button button40;
    }
}

