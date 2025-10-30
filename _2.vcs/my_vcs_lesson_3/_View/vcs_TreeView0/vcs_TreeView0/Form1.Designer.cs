namespace vcs_TreeView0
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            System.Windows.Forms.TreeNode treeNode1 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode2 = new System.Windows.Forms.TreeNode("Documents");
            System.Windows.Forms.TreeNode treeNode3 = new System.Windows.Forms.TreeNode("Environment", new System.Windows.Forms.TreeNode[] {
            treeNode1,
            treeNode2});
            System.Windows.Forms.TreeNode treeNode4 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode5 = new System.Windows.Forms.TreeNode("Defaults");
            System.Windows.Forms.TreeNode treeNode6 = new System.Windows.Forms.TreeNode("Projects", new System.Windows.Forms.TreeNode[] {
            treeNode4,
            treeNode5});
            System.Windows.Forms.TreeNode treeNode7 = new System.Windows.Forms.TreeNode("All Languages");
            System.Windows.Forms.TreeNode treeNode8 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode9 = new System.Windows.Forms.TreeNode("Tabs");
            System.Windows.Forms.TreeNode treeNode10 = new System.Windows.Forms.TreeNode("Advanced");
            System.Windows.Forms.TreeNode treeNode11 = new System.Windows.Forms.TreeNode("C#", new System.Windows.Forms.TreeNode[] {
            treeNode8,
            treeNode9,
            treeNode10});
            System.Windows.Forms.TreeNode treeNode12 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode13 = new System.Windows.Forms.TreeNode("Tabs");
            System.Windows.Forms.TreeNode treeNode14 = new System.Windows.Forms.TreeNode("Advanced");
            System.Windows.Forms.TreeNode treeNode15 = new System.Windows.Forms.TreeNode("Visual Basic", new System.Windows.Forms.TreeNode[] {
            treeNode12,
            treeNode13,
            treeNode14});
            System.Windows.Forms.TreeNode treeNode16 = new System.Windows.Forms.TreeNode("Text Editor", new System.Windows.Forms.TreeNode[] {
            treeNode7,
            treeNode11,
            treeNode15});
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button9 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.treeView3 = new System.Windows.Forms.TreeView();
            this.treeView4 = new System.Windows.Forms.TreeView();
            this.treeView5 = new System.Windows.Forms.TreeView();
            this.treeView0 = new System.Windows.Forms.TreeView();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.treeView2 = new System.Windows.Forms.TreeView();
            this.label0 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(803, 124);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(66, 40);
            this.bt_clear.TabIndex = 140;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(729, 27);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(150, 150);
            this.richTextBox1.TabIndex = 141;
            this.richTextBox1.Text = "";
            // 
            // button9
            // 
            this.button9.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.Location = new System.Drawing.Point(573, 566);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(140, 60);
            this.button9.TabIndex = 151;
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button8
            // 
            this.button8.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button8.Location = new System.Drawing.Point(573, 501);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(140, 60);
            this.button8.TabIndex = 150;
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(573, 4);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(140, 60);
            this.button0.TabIndex = 149;
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(573, 372);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(140, 60);
            this.button6.TabIndex = 148;
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(573, 66);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(140, 60);
            this.button1.TabIndex = 147;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(573, 311);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(140, 60);
            this.button5.TabIndex = 146;
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button7
            // 
            this.button7.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button7.Location = new System.Drawing.Point(573, 436);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(140, 60);
            this.button7.TabIndex = 145;
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(573, 250);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(140, 60);
            this.button4.TabIndex = 144;
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(573, 189);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(140, 60);
            this.button3.TabIndex = 143;
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(573, 127);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(140, 60);
            this.button2.TabIndex = 142;
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // treeView1
            // 
            this.treeView1.Location = new System.Drawing.Point(12, 107);
            this.treeView1.Name = "treeView1";
            this.treeView1.Size = new System.Drawing.Size(121, 97);
            this.treeView1.TabIndex = 152;
            // 
            // treeView3
            // 
            this.treeView3.Location = new System.Drawing.Point(148, 4);
            this.treeView3.Name = "treeView3";
            this.treeView3.Size = new System.Drawing.Size(121, 97);
            this.treeView3.TabIndex = 154;
            // 
            // treeView4
            // 
            this.treeView4.Location = new System.Drawing.Point(148, 107);
            this.treeView4.Name = "treeView4";
            this.treeView4.Size = new System.Drawing.Size(121, 97);
            this.treeView4.TabIndex = 155;
            // 
            // treeView5
            // 
            this.treeView5.Location = new System.Drawing.Point(148, 213);
            this.treeView5.Name = "treeView5";
            this.treeView5.Size = new System.Drawing.Size(121, 97);
            this.treeView5.TabIndex = 156;
            // 
            // treeView0
            // 
            this.treeView0.Location = new System.Drawing.Point(12, 4);
            this.treeView0.Name = "treeView0";
            this.treeView0.Size = new System.Drawing.Size(121, 97);
            this.treeView0.TabIndex = 157;
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "open.png");
            this.imageList1.Images.SetKeyName(1, "text.png");
            // 
            // treeView2
            // 
            this.treeView2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.treeView2.Location = new System.Drawing.Point(12, 316);
            this.treeView2.Name = "treeView2";
            treeNode1.Name = "Node1";
            treeNode1.Tag = "0";
            treeNode1.Text = "General";
            treeNode2.Name = "Node2";
            treeNode2.Tag = "1";
            treeNode2.Text = "Documents";
            treeNode3.Name = "Node0";
            treeNode3.Tag = "0";
            treeNode3.Text = "Environment";
            treeNode4.Name = "Node5";
            treeNode4.Tag = "2";
            treeNode4.Text = "General";
            treeNode5.Name = "Node6";
            treeNode5.Tag = "3";
            treeNode5.Text = "Defaults";
            treeNode6.Name = "Node4";
            treeNode6.Tag = "2";
            treeNode6.Text = "Projects";
            treeNode7.Name = "Node8";
            treeNode7.Tag = "4";
            treeNode7.Text = "All Languages";
            treeNode8.Name = "Node12";
            treeNode8.Tag = "5";
            treeNode8.Text = "General";
            treeNode9.Name = "Node13";
            treeNode9.Tag = "6";
            treeNode9.Text = "Tabs";
            treeNode10.Name = "Node14";
            treeNode10.Tag = "7";
            treeNode10.Text = "Advanced";
            treeNode11.Name = "Node9";
            treeNode11.Tag = "5";
            treeNode11.Text = "C#";
            treeNode12.Name = "Node15";
            treeNode12.Tag = "8";
            treeNode12.Text = "General";
            treeNode13.Name = "Node16";
            treeNode13.Tag = "9";
            treeNode13.Text = "Tabs";
            treeNode14.Name = "Node17";
            treeNode14.Tag = "10";
            treeNode14.Text = "Advanced";
            treeNode15.Name = "Node11";
            treeNode15.Tag = "8";
            treeNode15.Text = "Visual Basic";
            treeNode16.Name = "Node7";
            treeNode16.Tag = "4";
            treeNode16.Text = "Text Editor";
            this.treeView2.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode3,
            treeNode6,
            treeNode16});
            this.treeView2.Size = new System.Drawing.Size(156, 170);
            this.treeView2.TabIndex = 158;
            // 
            // label0
            // 
            this.label0.AutoSize = true;
            this.label0.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label0.Location = new System.Drawing.Point(275, 9);
            this.label0.Name = "label0";
            this.label0.Size = new System.Drawing.Size(64, 24);
            this.label0.TabIndex = 159;
            this.label0.Text = "label0";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(275, 40);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(64, 24);
            this.label1.TabIndex = 160;
            this.label1.Text = "label1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(275, 66);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(64, 24);
            this.label2.TabIndex = 161;
            this.label2.Text = "label2";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(345, 9);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(64, 24);
            this.label3.TabIndex = 162;
            this.label3.Text = "label3";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(345, 40);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(64, 24);
            this.label4.TabIndex = 163;
            this.label4.Text = "label4";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(345, 66);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(64, 24);
            this.label5.TabIndex = 164;
            this.label5.Text = "label5";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(972, 628);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label0);
            this.Controls.Add(this.treeView2);
            this.Controls.Add(this.treeView0);
            this.Controls.Add(this.treeView5);
            this.Controls.Add(this.treeView4);
            this.Controls.Add(this.treeView3);
            this.Controls.Add(this.treeView1);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.TreeView treeView3;
        private System.Windows.Forms.TreeView treeView4;
        private System.Windows.Forms.TreeView treeView5;
        private System.Windows.Forms.TreeView treeView0;
        private System.Windows.Forms.ImageList imageList1;
        private System.Windows.Forms.TreeView treeView2;
        private System.Windows.Forms.Label label0;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
    }
}

