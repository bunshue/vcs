using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace IMSCap2
{
    public partial class Form1 : Form
    {
        Color background_color = Color.White;
        Color key_press_color = Color.Green;

        //第一群Label, 指示用Label
        Label lb_1_id = new Label();
        Label lb_1_name = new Label();
        Label lb_1_sex = new Label();
        Label lb_1_birthday = new Label();
        Label lb_1_age = new Label();

        //第二群Label, 顯示結果用Label
        Label lb_2_id = new Label();
        Label lb_2_name = new Label();
        Label lb_2_sex = new Label();
        Label lb_2_birthday = new Label();
        Label lb_2_age = new Label();

        TextBox tb_id = new TextBox();
        TextBox tb_name = new TextBox();
        TextBox tb_sex = new TextBox();
        TextBox tb_birthday = new TextBox();
        TextBox tb_age = new TextBox();

        Button bt_id = new Button();
        Button bt_name = new Button();
        Button bt_sex = new Button();
        Button bt_birthday = new Button();
        Button bt_age = new Button();

        Label lb_1_date = new Label();
        Label lb_1_time = new Label();
        Label lb_serial = new Label();
        Label lb_version = new Label();


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackColor = Color.Black;
            int w = 160;
            int h = 40;
            int x_st = 20;
            int y_st = 20;
            int dx = w + 5;
            int dy = h + 5;

            lb_1_id.Name = "lb_1_id";
            lb_1_name.Name = "lb_1_name";
            lb_1_sex.Name = "lb_1_sex";
            lb_1_birthday.Name = "lb_1_birthday";
            lb_1_age.Name = "lb_1_age";
            lb_1_date.Name = "lb_1_date";
            lb_1_time.Name = "lb_1_time";

            lb_1_id.Text = "ID NO:";
            lb_1_name.Text = "NAME:";
            lb_1_sex.Text = "SEX:";
            lb_1_birthday.Text = "Birthday:";
            lb_1_age.Text = "Age:";
            lb_1_date.Text = "12/05/2022 Mon";
            lb_1_time.Text = "13:53:55";

            x_st = 20;
            y_st = 20;
            dx = w + 5;
            dy = h + 5;
            lb_1_id.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_1_name.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_1_sex.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_1_birthday.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_1_age.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_1_date.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            lb_1_time.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            this.Controls.Add(lb_1_id);
            this.Controls.Add(lb_1_name);
            this.Controls.Add(lb_1_sex);
            this.Controls.Add(lb_1_birthday);
            this.Controls.Add(lb_1_age);
            this.Controls.Add(lb_1_date);
            this.Controls.Add(lb_1_time);

            lb_2_id.Name = "lb_2_id";
            lb_2_name.Name = "lb_2_name";
            lb_2_sex.Name = "lb_2_sex";
            lb_2_birthday.Name = "lb_2_birthday";
            lb_2_age.Name = "lb_2_age";

            lb_2_id.Text = "ID NO:";
            lb_2_name.Text = "NAME:";
            lb_2_sex.Text = "SEX:";
            lb_2_birthday.Text = "Birthday:";
            lb_2_age.Text = "Age:";

            x_st = 220;
            y_st = 20;
            dx = w + 5;
            dy = h + 5;
            lb_2_id.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_2_name.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_2_sex.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_2_birthday.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_2_age.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            this.Controls.Add(lb_2_id);
            this.Controls.Add(lb_2_name);
            this.Controls.Add(lb_2_sex);
            this.Controls.Add(lb_2_birthday);
            this.Controls.Add(lb_2_age);

            tb_id.Name = "tb_id";
            tb_name.Name = "tb_name";
            tb_sex.Name = "tb_sex";
            tb_birthday.Name = "tb_birthday";
            tb_age.Name = "tb_age";

            tb_id.Text = "ID NO:";
            tb_name.Text = "NAME:";
            tb_sex.Text = "SEX:";
            tb_birthday.Text = "Birthday:";
            tb_age.Text = "Age:";

            x_st = 420;
            y_st = 20;
            dx = w + 5;
            dy = h + 5;
            tb_id.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            tb_name.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            tb_sex.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            tb_birthday.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            tb_age.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            this.Controls.Add(tb_id);
            this.Controls.Add(tb_name);
            this.Controls.Add(tb_sex);
            this.Controls.Add(tb_birthday);
            this.Controls.Add(tb_age);

            bt_id.Name = "bt_id";
            bt_name.Name = "bt_name";
            bt_sex.Name = "bt_sex";
            bt_birthday.Name = "bt_birthday";
            bt_age.Name = "bt_age";

            /*
            bt_id.Text = "ID NO:";
            bt_name.Text = "NAME:";
            bt_sex.Text = "SEX:";
            bt_birthday.Text = "Birthday:";
            bt_age.Text = "Age:";
            */

            x_st = 620;
            y_st = 20;
            w = 64;
            h = 64;
            dx = w + 10;
            dy = h + 10;
            bt_id.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_name.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_sex.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_birthday.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_age.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            this.Controls.Add(bt_id);
            this.Controls.Add(bt_name);
            this.Controls.Add(bt_sex);
            this.Controls.Add(bt_birthday);
            this.Controls.Add(bt_age);

            bt_id.BackgroundImage = Properties.Resources.image_id;
            bt_name.BackgroundImage = Properties.Resources.image_name;
            bt_sex.BackgroundImage = Properties.Resources.image_sex_male;
            bt_birthday.BackgroundImage = Properties.Resources.image_birthday;
            bt_age.BackgroundImage = Properties.Resources.image_age;



            bt_id.BackgroundImageLayout = ImageLayout.Zoom;
            bt_name.BackgroundImageLayout = ImageLayout.Zoom;
            bt_sex.BackgroundImageLayout = ImageLayout.Zoom;
            bt_birthday.BackgroundImageLayout = ImageLayout.Zoom;
            bt_age.BackgroundImageLayout = ImageLayout.Zoom;




            //控件的共通設定

            foreach (Control c in this.Controls)  //撈出所有控件
            {
                //richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Label")   //判斷是否為 Label 控件
                {
                    if (((Label)c).Name[3] == '1')
                    {
                        w = 160;
                        h = 40;

                        ((Label)c).Size = new Size(w, h);  //設定大小
                        //((Label)c).Font = new Font("Courier New", 18, FontStyle.Bold);  //建立字體對象
                        //((Label)c).Font = new Font("Arial", 18, FontStyle.Bold);  //建立字體對象
                        ((Label)c).Font = new Font("Times New Roman", 18, FontStyle.Bold);  //建立字體對象



                        ((Label)c).TextAlign = ContentAlignment.MiddleLeft;
                        ((Label)c).ForeColor = Color.White;
                    }
                    else if (((Label)c).Name[3] == '2')
                    {
                        w = 160;
                        h = 40;

                        ((Label)c).Size = new Size(w, h);  //設定大小
                        ((Label)c).BackColor = background_color;
                        ((Label)c).Font = new Font("Courier New", 18, FontStyle.Bold);  //建立字體對象
                        ((Label)c).TextAlign = ContentAlignment.MiddleLeft;
                    }
                }
                else if (c.GetType().Name == "TextBox")   //判斷是否為 TextBox 控件
                {
                    w = 160;
                    h = 40;

                    ((TextBox)c).Size = new Size(w, h);  //設定大小
                    ((TextBox)c).BackColor = background_color;
                    ((TextBox)c).Font = new Font("Courier New", 18, FontStyle.Bold);  //建立字體對象
                    ((TextBox)c).TextAlign = HorizontalAlignment.Left;
                }
                else if (c.GetType().Name == "Button")   //判斷是否為 Button 控件
                {
                    w = 64;
                    h = 64;

                    ((Button)c).Size = new Size(w, h);  //設定大小
                    ((Button)c).BackColor = background_color;
                    //((Button)c).Font = new Font("Courier New", 18, FontStyle.Bold);  //建立字體對象
                    //((Button)c).TextAlign = ContentAlignment.MiddleLeft;
                }
            }
        }
    }
}

