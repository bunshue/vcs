namespace vcs_AForgeTest1
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
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button0 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.chart1 = new AForge.Controls.Chart();
            this.listView1 = new System.Windows.Forms.ListView();
            this.chart2 = new AForge.Controls.Chart();
            this.chart3 = new AForge.Controls.Chart();
            this.cellWorld1 = new vcs_AForgeTest1.CellWorld();
            this.chart4 = new AForge.Controls.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(366, 155);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(66, 40);
            this.bt_clear.TabIndex = 133;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(346, 117);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 132;
            this.richTextBox1.Text = "";
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(12, 12);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(200, 60);
            this.button0.TabIndex = 137;
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(12, 74);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(200, 60);
            this.button1.TabIndex = 136;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(12, 198);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(200, 60);
            this.button3.TabIndex = 135;
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(12, 137);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(200, 60);
            this.button2.TabIndex = 134;
            this.button2.Text = "map";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(228, 117);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 138;
            this.pictureBox1.TabStop = false;
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(12, 261);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(200, 60);
            this.button4.TabIndex = 140;
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(12, 324);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(200, 60);
            this.button5.TabIndex = 141;
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(12, 387);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(200, 60);
            this.button6.TabIndex = 142;
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button7.Location = new System.Drawing.Point(12, 450);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(200, 60);
            this.button7.TabIndex = 143;
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button8.Location = new System.Drawing.Point(12, 513);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(200, 60);
            this.button8.TabIndex = 144;
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.Location = new System.Drawing.Point(12, 575);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(200, 60);
            this.button9.TabIndex = 145;
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // chart1
            // 
            this.chart1.Location = new System.Drawing.Point(346, 11);
            this.chart1.Name = "chart1";
            this.chart1.RangeX = ((AForge.Range)(resources.GetObject("chart1.RangeX")));
            this.chart1.RangeY = ((AForge.Range)(resources.GetObject("chart1.RangeY")));
            this.chart1.Size = new System.Drawing.Size(100, 100);
            this.chart1.TabIndex = 146;
            this.chart1.Text = "chart1";
            // 
            // listView1
            // 
            this.listView1.Location = new System.Drawing.Point(228, 11);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(100, 100);
            this.listView1.TabIndex = 147;
            this.listView1.UseCompatibleStateImageBehavior = false;
            // 
            // chart2
            // 
            this.chart2.Location = new System.Drawing.Point(463, 11);
            this.chart2.Name = "chart2";
            this.chart2.RangeX = ((AForge.Range)(resources.GetObject("chart2.RangeX")));
            this.chart2.RangeY = ((AForge.Range)(resources.GetObject("chart2.RangeY")));
            this.chart2.Size = new System.Drawing.Size(100, 100);
            this.chart2.TabIndex = 148;
            this.chart2.Text = "chart2";
            // 
            // chart3
            // 
            this.chart3.Location = new System.Drawing.Point(346, 223);
            this.chart3.Name = "chart3";
            this.chart3.RangeX = ((AForge.Range)(resources.GetObject("chart3.RangeX")));
            this.chart3.RangeY = ((AForge.Range)(resources.GetObject("chart3.RangeY")));
            this.chart3.Size = new System.Drawing.Size(100, 100);
            this.chart3.TabIndex = 150;
            this.chart3.Text = "chart3";
            // 
            // cellWorld1
            // 
            this.cellWorld1.Coloring = null;
            this.cellWorld1.Location = new System.Drawing.Point(228, 223);
            this.cellWorld1.Map = null;
            this.cellWorld1.Name = "cellWorld1";
            this.cellWorld1.Size = new System.Drawing.Size(100, 100);
            this.cellWorld1.TabIndex = 149;
            this.cellWorld1.Text = "cellWorld1";
            // 
            // chart4
            // 
            this.chart4.Location = new System.Drawing.Point(228, 347);
            this.chart4.Name = "chart4";
            this.chart4.RangeX = ((AForge.Range)(resources.GetObject("chart4.RangeX")));
            this.chart4.RangeY = ((AForge.Range)(resources.GetObject("chart4.RangeY")));
            this.chart4.Size = new System.Drawing.Size(100, 100);
            this.chart4.TabIndex = 151;
            this.chart4.Text = "chart4";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(711, 643);
            this.Controls.Add(this.chart4);
            this.Controls.Add(this.chart3);
            this.Controls.Add(this.cellWorld1);
            this.Controls.Add(this.chart2);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private AForge.Controls.Chart chart1;
        private System.Windows.Forms.ListView listView1;
        private AForge.Controls.Chart chart2;
        private CellWorld cellWorld1;
        private AForge.Controls.Chart chart3;
        private AForge.Controls.Chart chart4;
    }
}

