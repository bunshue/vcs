namespace vcs_Remove_Bin_Obj
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.checkBox2 = new System.Windows.Forms.CheckBox();
            this.checkBox3 = new System.Windows.Forms.CheckBox();
            this.checkBox4 = new System.Windows.Forms.CheckBox();
            this.button3 = new System.Windows.Forms.Button();
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
            this.checkBox7 = new System.Windows.Forms.CheckBox();
            this.checkBox8 = new System.Windows.Forms.CheckBox();
            this.checkBox9 = new System.Windows.Forms.CheckBox();
            this.checkBox10 = new System.Windows.Forms.CheckBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.groupBox_remove = new System.Windows.Forms.GroupBox();
            this.rb_remove_opengl = new System.Windows.Forms.RadioButton();
            this.rb_remove_cuda = new System.Windows.Forms.RadioButton();
            this.rb_remove_vcs = new System.Windows.Forms.RadioButton();
            this.groupBox_replace = new System.Windows.Forms.GroupBox();
            this.lb_path = new System.Windows.Forms.Label();
            this.bt_open_dir = new System.Windows.Forms.Button();
            this.rb_file_type3 = new System.Windows.Forms.RadioButton();
            this.lb_string_new = new System.Windows.Forms.Label();
            this.bt_replace = new System.Windows.Forms.Button();
            this.lb_string_old = new System.Windows.Forms.Label();
            this.tb_string_new = new System.Windows.Forms.TextBox();
            this.cb_confirm = new System.Windows.Forms.CheckBox();
            this.tb_string_old = new System.Windows.Forms.TextBox();
            this.rb_file_type2 = new System.Windows.Forms.RadioButton();
            this.rb_file_type1 = new System.Windows.Forms.RadioButton();
            this.rb_file_type0 = new System.Windows.Forms.RadioButton();
            this.listView1 = new System.Windows.Forms.ListView();
            this.bt_open_dir2 = new System.Windows.Forms.Button();
            this.groupBox_remove.SuspendLayout();
            this.groupBox_replace.SuspendLayout();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(12, 335);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(104, 39);
            this.button1.TabIndex = 0;
            this.button1.Text = "刪除";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(258, 51);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(285, 267);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Checked = true;
            this.checkBox1.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox1.Location = new System.Drawing.Point(15, 64);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(145, 28);
            this.checkBox1.TabIndex = 2;
            this.checkBox1.Text = "刪除 bin obj";
            this.checkBox1.UseVisualStyleBackColor = true;
            // 
            // checkBox2
            // 
            this.checkBox2.AutoSize = true;
            this.checkBox2.Checked = true;
            this.checkBox2.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox2.Location = new System.Drawing.Point(15, 144);
            this.checkBox2.Name = "checkBox2";
            this.checkBox2.Size = new System.Drawing.Size(170, 28);
            this.checkBox2.TabIndex = 3;
            this.checkBox2.Text = "刪除 .suo .user";
            this.checkBox2.UseVisualStyleBackColor = true;
            // 
            // checkBox3
            // 
            this.checkBox3.AutoSize = true;
            this.checkBox3.Checked = true;
            this.checkBox3.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox3.Location = new System.Drawing.Point(15, 24);
            this.checkBox3.Name = "checkBox3";
            this.checkBox3.Size = new System.Drawing.Size(145, 28);
            this.checkBox3.TabIndex = 5;
            this.checkBox3.Text = "顯示 bin obj";
            this.checkBox3.UseVisualStyleBackColor = true;
            // 
            // checkBox4
            // 
            this.checkBox4.AutoSize = true;
            this.checkBox4.Checked = true;
            this.checkBox4.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox4.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox4.Location = new System.Drawing.Point(15, 104);
            this.checkBox4.Name = "checkBox4";
            this.checkBox4.Size = new System.Drawing.Size(170, 28);
            this.checkBox4.TabIndex = 6;
            this.checkBox4.Text = "顯示 .suo .user";
            this.checkBox4.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(12, 613);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(104, 52);
            this.button3.TabIndex = 8;
            this.button3.Text = "檔名簡中轉正中";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(254, 24);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(66, 24);
            this.lb_main_mesg.TabIndex = 134;
            this.lb_main_mesg.Text = "mesg";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(363, 163);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(85, 35);
            this.bt_clear.TabIndex = 135;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // checkBox7
            // 
            this.checkBox7.AutoSize = true;
            this.checkBox7.Checked = true;
            this.checkBox7.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox7.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox7.Location = new System.Drawing.Point(15, 184);
            this.checkBox7.Name = "checkBox7";
            this.checkBox7.Size = new System.Drawing.Size(126, 28);
            this.checkBox7.TabIndex = 136;
            this.checkBox7.Text = "顯示 misc";
            this.checkBox7.UseVisualStyleBackColor = true;
            // 
            // checkBox8
            // 
            this.checkBox8.AutoSize = true;
            this.checkBox8.Checked = true;
            this.checkBox8.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox8.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox8.Location = new System.Drawing.Point(15, 224);
            this.checkBox8.Name = "checkBox8";
            this.checkBox8.Size = new System.Drawing.Size(126, 28);
            this.checkBox8.TabIndex = 137;
            this.checkBox8.Text = "刪除 misc";
            this.checkBox8.UseVisualStyleBackColor = true;
            // 
            // checkBox9
            // 
            this.checkBox9.AutoSize = true;
            this.checkBox9.Checked = true;
            this.checkBox9.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox9.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox9.Location = new System.Drawing.Point(15, 264);
            this.checkBox9.Name = "checkBox9";
            this.checkBox9.Size = new System.Drawing.Size(173, 28);
            this.checkBox9.TabIndex = 138;
            this.checkBox9.Text = "顯示空資料夾";
            this.checkBox9.UseVisualStyleBackColor = true;
            // 
            // checkBox10
            // 
            this.checkBox10.AutoSize = true;
            this.checkBox10.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox10.Location = new System.Drawing.Point(15, 301);
            this.checkBox10.Name = "checkBox10";
            this.checkBox10.Size = new System.Drawing.Size(173, 28);
            this.checkBox10.TabIndex = 139;
            this.checkBox10.Text = "刪除空資料夾";
            this.checkBox10.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(12, 538);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(104, 52);
            this.button2.TabIndex = 140;
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(132, 538);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(104, 52);
            this.button4.TabIndex = 141;
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // groupBox_remove
            // 
            this.groupBox_remove.Controls.Add(this.rb_remove_opengl);
            this.groupBox_remove.Controls.Add(this.rb_remove_cuda);
            this.groupBox_remove.Controls.Add(this.rb_remove_vcs);
            this.groupBox_remove.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox_remove.Location = new System.Drawing.Point(132, 335);
            this.groupBox_remove.Name = "groupBox_remove";
            this.groupBox_remove.Size = new System.Drawing.Size(104, 97);
            this.groupBox_remove.TabIndex = 144;
            this.groupBox_remove.TabStop = false;
            this.groupBox_remove.Text = "清理範圍";
            // 
            // rb_remove_opengl
            // 
            this.rb_remove_opengl.AutoSize = true;
            this.rb_remove_opengl.Location = new System.Drawing.Point(20, 70);
            this.rb_remove_opengl.Name = "rb_remove_opengl";
            this.rb_remove_opengl.Size = new System.Drawing.Size(76, 23);
            this.rb_remove_opengl.TabIndex = 2;
            this.rb_remove_opengl.Text = "opengl";
            this.rb_remove_opengl.UseVisualStyleBackColor = true;
            // 
            // rb_remove_cuda
            // 
            this.rb_remove_cuda.AutoSize = true;
            this.rb_remove_cuda.Location = new System.Drawing.Point(20, 45);
            this.rb_remove_cuda.Name = "rb_remove_cuda";
            this.rb_remove_cuda.Size = new System.Drawing.Size(61, 23);
            this.rb_remove_cuda.TabIndex = 1;
            this.rb_remove_cuda.Text = "cuda";
            this.rb_remove_cuda.UseVisualStyleBackColor = true;
            // 
            // rb_remove_vcs
            // 
            this.rb_remove_vcs.AutoSize = true;
            this.rb_remove_vcs.Checked = true;
            this.rb_remove_vcs.Location = new System.Drawing.Point(20, 20);
            this.rb_remove_vcs.Name = "rb_remove_vcs";
            this.rb_remove_vcs.Size = new System.Drawing.Size(51, 23);
            this.rb_remove_vcs.TabIndex = 0;
            this.rb_remove_vcs.TabStop = true;
            this.rb_remove_vcs.Text = "vcs";
            this.rb_remove_vcs.UseVisualStyleBackColor = true;
            // 
            // groupBox_replace
            // 
            this.groupBox_replace.Controls.Add(this.lb_path);
            this.groupBox_replace.Controls.Add(this.bt_open_dir);
            this.groupBox_replace.Controls.Add(this.rb_file_type3);
            this.groupBox_replace.Controls.Add(this.lb_string_new);
            this.groupBox_replace.Controls.Add(this.bt_replace);
            this.groupBox_replace.Controls.Add(this.lb_string_old);
            this.groupBox_replace.Controls.Add(this.tb_string_new);
            this.groupBox_replace.Controls.Add(this.cb_confirm);
            this.groupBox_replace.Controls.Add(this.tb_string_old);
            this.groupBox_replace.Controls.Add(this.rb_file_type2);
            this.groupBox_replace.Controls.Add(this.rb_file_type1);
            this.groupBox_replace.Controls.Add(this.rb_file_type0);
            this.groupBox_replace.Location = new System.Drawing.Point(258, 335);
            this.groupBox_replace.Name = "groupBox_replace";
            this.groupBox_replace.Size = new System.Drawing.Size(320, 150);
            this.groupBox_replace.TabIndex = 145;
            this.groupBox_replace.TabStop = false;
            this.groupBox_replace.Text = "置換檔案內的文字";
            // 
            // lb_path
            // 
            this.lb_path.AutoSize = true;
            this.lb_path.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_path.Location = new System.Drawing.Point(12, 130);
            this.lb_path.Name = "lb_path";
            this.lb_path.Size = new System.Drawing.Size(33, 13);
            this.lb_path.TabIndex = 151;
            this.lb_path.Text = "路徑";
            // 
            // bt_open_dir
            // 
            this.bt_open_dir.BackgroundImage = global::vcs_Remove_Bin_Obj.Properties.Resources.open_folder;
            this.bt_open_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_open_dir.Location = new System.Drawing.Point(116, 110);
            this.bt_open_dir.Name = "bt_open_dir";
            this.bt_open_dir.Size = new System.Drawing.Size(40, 40);
            this.bt_open_dir.TabIndex = 146;
            this.bt_open_dir.UseVisualStyleBackColor = true;
            this.bt_open_dir.Click += new System.EventHandler(this.bt_open_dir_Click);
            // 
            // rb_file_type3
            // 
            this.rb_file_type3.AutoSize = true;
            this.rb_file_type3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type3.Location = new System.Drawing.Point(228, 96);
            this.rb_file_type3.Name = "rb_file_type3";
            this.rb_file_type3.Size = new System.Drawing.Size(49, 23);
            this.rb_file_type3.TabIndex = 150;
            this.rb_file_type3.Text = "*.*";
            this.rb_file_type3.UseVisualStyleBackColor = true;
            // 
            // lb_string_new
            // 
            this.lb_string_new.AutoSize = true;
            this.lb_string_new.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_string_new.Location = new System.Drawing.Point(4, 58);
            this.lb_string_new.Name = "lb_string_new";
            this.lb_string_new.Size = new System.Drawing.Size(66, 19);
            this.lb_string_new.TabIndex = 149;
            this.lb_string_new.Text = "新字串";
            // 
            // bt_replace
            // 
            this.bt_replace.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_replace.Location = new System.Drawing.Point(10, 87);
            this.bt_replace.Name = "bt_replace";
            this.bt_replace.Size = new System.Drawing.Size(100, 40);
            this.bt_replace.TabIndex = 146;
            this.bt_replace.Text = "置換";
            this.bt_replace.UseVisualStyleBackColor = true;
            this.bt_replace.Click += new System.EventHandler(this.bt_replace_Click);
            // 
            // lb_string_old
            // 
            this.lb_string_old.AutoSize = true;
            this.lb_string_old.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_string_old.Location = new System.Drawing.Point(6, 27);
            this.lb_string_old.Name = "lb_string_old";
            this.lb_string_old.Size = new System.Drawing.Size(66, 19);
            this.lb_string_old.TabIndex = 148;
            this.lb_string_old.Text = "原字串";
            // 
            // tb_string_new
            // 
            this.tb_string_new.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_string_new.Location = new System.Drawing.Point(73, 55);
            this.tb_string_new.Name = "tb_string_new";
            this.tb_string_new.Size = new System.Drawing.Size(150, 30);
            this.tb_string_new.TabIndex = 147;
            // 
            // cb_confirm
            // 
            this.cb_confirm.AutoSize = true;
            this.cb_confirm.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_confirm.Location = new System.Drawing.Point(116, 91);
            this.cb_confirm.Name = "cb_confirm";
            this.cb_confirm.Size = new System.Drawing.Size(104, 23);
            this.cb_confirm.TabIndex = 146;
            this.cb_confirm.Text = "確認置換";
            this.cb_confirm.UseVisualStyleBackColor = true;
            // 
            // tb_string_old
            // 
            this.tb_string_old.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_string_old.Location = new System.Drawing.Point(73, 27);
            this.tb_string_old.Name = "tb_string_old";
            this.tb_string_old.Size = new System.Drawing.Size(150, 30);
            this.tb_string_old.TabIndex = 146;
            // 
            // rb_file_type2
            // 
            this.rb_file_type2.AutoSize = true;
            this.rb_file_type2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type2.Location = new System.Drawing.Point(228, 70);
            this.rb_file_type2.Name = "rb_file_type2";
            this.rb_file_type2.Size = new System.Drawing.Size(58, 23);
            this.rb_file_type2.TabIndex = 2;
            this.rb_file_type2.Text = "*.py";
            this.rb_file_type2.UseVisualStyleBackColor = true;
            // 
            // rb_file_type1
            // 
            this.rb_file_type1.AutoSize = true;
            this.rb_file_type1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type1.Location = new System.Drawing.Point(228, 45);
            this.rb_file_type1.Name = "rb_file_type1";
            this.rb_file_type1.Size = new System.Drawing.Size(92, 23);
            this.rb_file_type1.TabIndex = 1;
            this.rb_file_type1.Text = "*.c *.cpp";
            this.rb_file_type1.UseVisualStyleBackColor = true;
            // 
            // rb_file_type0
            // 
            this.rb_file_type0.AutoSize = true;
            this.rb_file_type0.Checked = true;
            this.rb_file_type0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type0.Location = new System.Drawing.Point(228, 20);
            this.rb_file_type0.Name = "rb_file_type0";
            this.rb_file_type0.Size = new System.Drawing.Size(55, 23);
            this.rb_file_type0.TabIndex = 0;
            this.rb_file_type0.TabStop = true;
            this.rb_file_type0.Text = "*.cs";
            this.rb_file_type0.UseVisualStyleBackColor = true;
            // 
            // listView1
            // 
            this.listView1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.listView1.Location = new System.Drawing.Point(581, 51);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(221, 217);
            this.listView1.TabIndex = 146;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            // 
            // bt_open_dir2
            // 
            this.bt_open_dir2.BackgroundImage = global::vcs_Remove_Bin_Obj.Properties.Resources.open_folder;
            this.bt_open_dir2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_dir2.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_open_dir2.Location = new System.Drawing.Point(179, 472);
            this.bt_open_dir2.Name = "bt_open_dir2";
            this.bt_open_dir2.Size = new System.Drawing.Size(50, 50);
            this.bt_open_dir2.TabIndex = 147;
            this.bt_open_dir2.UseVisualStyleBackColor = true;
            this.bt_open_dir2.Click += new System.EventHandler(this.bt_open_dir2_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(955, 678);
            this.Controls.Add(this.bt_open_dir2);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.groupBox_replace);
            this.Controls.Add(this.groupBox_remove);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.checkBox10);
            this.Controls.Add(this.checkBox9);
            this.Controls.Add(this.checkBox8);
            this.Controls.Add(this.checkBox7);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.lb_main_mesg);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.checkBox4);
            this.Controls.Add(this.checkBox3);
            this.Controls.Add(this.checkBox2);
            this.Controls.Add(this.checkBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "刪除檔案";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_remove.ResumeLayout(false);
            this.groupBox_remove.PerformLayout();
            this.groupBox_replace.ResumeLayout(false);
            this.groupBox_replace.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.CheckBox checkBox2;
        private System.Windows.Forms.CheckBox checkBox3;
        private System.Windows.Forms.CheckBox checkBox4;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label lb_main_mesg;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.CheckBox checkBox7;
        private System.Windows.Forms.CheckBox checkBox8;
        private System.Windows.Forms.CheckBox checkBox9;
        private System.Windows.Forms.CheckBox checkBox10;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.GroupBox groupBox_remove;
        private System.Windows.Forms.RadioButton rb_remove_opengl;
        private System.Windows.Forms.RadioButton rb_remove_cuda;
        private System.Windows.Forms.RadioButton rb_remove_vcs;
        private System.Windows.Forms.GroupBox groupBox_replace;
        private System.Windows.Forms.RadioButton rb_file_type2;
        private System.Windows.Forms.RadioButton rb_file_type1;
        private System.Windows.Forms.RadioButton rb_file_type0;
        private System.Windows.Forms.Button bt_replace;
        private System.Windows.Forms.CheckBox cb_confirm;
        private System.Windows.Forms.Label lb_string_new;
        private System.Windows.Forms.Label lb_string_old;
        private System.Windows.Forms.TextBox tb_string_new;
        private System.Windows.Forms.TextBox tb_string_old;
        private System.Windows.Forms.RadioButton rb_file_type3;
        private System.Windows.Forms.Button bt_open_dir;
        private System.Windows.Forms.Label lb_path;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.Button bt_open_dir2;
    }
}

