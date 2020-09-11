using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_使用自适应类的窗体
{
    public partial class Form1 : Form
    {

        //1.声明自适应类实例
        //AutoSizeFormClass asc = new AutoSizeFormClass();

        public Form1()
        {
            InitializeComponent();

            //如果加入"皮肤"，则不能在Form1_Load中记录控件的大小和位置，因为有些控件如dataGridView的子控件还未完成
            //而要在在Form1_SizeChanged中，第一次改变时，记录控件的大小和位置
            //this.skinEngine1.SkinFile = "EmeraldColor1.ssk";
        }

        //2. 为窗体添加Load事件，并在其方法Form1_Load中，调用类的初始化方法，记录窗体和其控件的初始位置和大小
        private void Form1_Load(object sender, EventArgs e)
        {
            //asc.controllInitializeSize(this);
        }

        //3.为窗体添加SizeChanged事件，并在其方法Form1_SizeChanged中，调用类的自适应方法，完成自适应
        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            //asc.controlAutoSize(this);
            //this.WindowState =(System.Windows.Forms.FormWindowState)(2);//记录完控件的初始位置和大小后，再最大化
        }



        MyRecordControlClass mdc = new MyRecordControlClass();

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += button1.Text + "\n";
            mdc.recordAllControls(this);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += button2.Text + "\n";
            mdc.controlSizeChange(this);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += button3.Text + "\n";
            int count = mdc.control_data.Count;
            richTextBox1.Text += "共有 " + count.ToString() + " 個控件\n";
            int i;
            for (i = 0; i < count; i++)
            {
                richTextBox1.Text += (i + 1).ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].name + "\t\t";
                //richTextBox1.Text += mdc.control_data[i].text + "\t\t";
                richTextBox1.Text += mdc.control_data[i].x_st.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].y_st.ToString() + "\t";
                //richTextBox1.Text += mdc.control_data[i].index.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Left.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Top.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Width.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Height.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].enable.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].visible.ToString() + "\n";



            }
        }

    }

    /*
    class AutoSizeFormClass
    {
        //(1).声明结构,只记录窗体和其控件的初始位置和大小。
        public struct controlRect
        {
            public int Left;
            public int Top;
            public int Width;
            public int Height;
        }
        //(2).声明 1个对象
        //注意这里不能使用控件列表记录 List nCtrl;，因为控件的关联性，记录的始终是当前的大小。
        //      public List oldCtrl= new List();//这里将西文的大于小于号都过滤掉了，只能改为中文的，使用中要改回西文
        public List<controlRect> oldCtrl = new List<controlRect>();
        int ctrlNo = 0;//1;
        //(3). 创建两个函数
        //(3.1)记录窗体和其控件的初始位置和大小,
        public void controllInitializeSize(Control mForm)
        {
            controlRect cR;
            cR.Left = mForm.Left; cR.Top = mForm.Top; cR.Width = mForm.Width; cR.Height = mForm.Height;
            oldCtrl.Add(cR);//第一个为"窗体本身",只加入一次即可

            AddControl(mForm);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用

            //this.WindowState = (System.Windows.Forms.FormWindowState)(2);//记录完控件的初始位置和大小后，再最大化
            //0 - Normalize , 1 - Minimize,2- Maximize
        }

        private void AddControl(Control ctl)
        {
            foreach (Control c in ctl.Controls)
            {  //**放在这里，是先记录控件的子控件，后记录控件本身
                //if (c.Controls.Count > 0)
                //    AddControl(c);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
                controlRect objCtrl;
                objCtrl.Left = c.Left; objCtrl.Top = c.Top; objCtrl.Width = c.Width; objCtrl.Height = c.Height;
                oldCtrl.Add(objCtrl);
                //**放在这里，是先记录控件本身，后记录控件的子控件
                if (c.Controls.Count > 0)
                    AddControl(c);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
            }
        }

        //(3.2)控件自适应大小,
        public void controlAutoSize(Control mForm)
        {
            if (ctrlNo == 0)
            { //*如果在窗体的Form1_Load中，记录控件原始的大小和位置，正常没有问题，但要加入皮肤就会出现问题，因为有些控件如dataGridView的的子控件还没有完成，个数少
                //*要在窗体的Form1_SizeChanged中，第一次改变大小时，记录控件原始的大小和位置,这里所有控件的子控件都已经形成
                controlRect cR;
                //  cR.Left = mForm.Left; cR.Top = mForm.Top; cR.Width = mForm.Width; cR.Height = mForm.Height;
                cR.Left = 0; cR.Top = 0; cR.Width = mForm.PreferredSize.Width; cR.Height = mForm.PreferredSize.Height;
                oldCtrl.Add(cR);//第一个为"窗体本身",只加入一次即可
                AddControl(mForm);//窗体内其余控件可能嵌套其它控件(比如panel),故单独抽出以便递归调用
            }
            float wScale = (float)mForm.Width / (float)oldCtrl[0].Width;//新旧窗体之间的比例，与最早的旧窗体
            float hScale = (float)mForm.Height / (float)oldCtrl[0].Height;//.Height;
            ctrlNo = 1;//进入=1，第0个为窗体本身,窗体内的控件,从序号1开始

            AutoScaleControl(mForm, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
        }

        private void AutoScaleControl(Control ctl, float wScale, float hScale)
        {
            int ctrLeft0, ctrTop0, ctrWidth0, ctrHeight0;
            //int ctrlNo = 1;//第1个是窗体自身的 Left,Top,Width,Height，所以窗体控件从ctrlNo=1开始
            foreach (Control c in ctl.Controls)
            { //**放在这里，是先缩放控件的子控件，后缩放控件本身
                //if (c.Controls.Count > 0)
                //   AutoScaleControl(c, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
                ctrLeft0 = oldCtrl[ctrlNo].Left;
                ctrTop0 = oldCtrl[ctrlNo].Top;
                ctrWidth0 = oldCtrl[ctrlNo].Width;
                ctrHeight0 = oldCtrl[ctrlNo].Height;
                //c.Left = (int)((ctrLeft0 - wLeft0) * wScale) + wLeft1;//新旧控件之间的线性比例
                //c.Top = (int)((ctrTop0 - wTop0) * h) + wTop1;
                c.Left = (int)((ctrLeft0) * wScale);//新旧控件之间的线性比例。控件位置只相对于窗体，所以不能加 + wLeft1
                c.Top = (int)((ctrTop0) * hScale);//
                c.Width = (int)(ctrWidth0 * wScale);//只与最初的大小相关，所以不能与现在的宽度相乘 (int)(c.Width * w);
                c.Height = (int)(ctrHeight0 * hScale);//
                ctrlNo++;//累加序号
                //**放在这里，是先缩放控件本身，后缩放控件的子控件
                if (c.Controls.Count > 0)
                    AutoScaleControl(c, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
            }
        }
    }
    */




    class MyRecordControlClass
    {
        //(1).声明结构,只记录窗体和其控件的初始位置和大小。
        public struct controlInfo
        {
            public string name;
            public string text;

            public int index;
            public int x_st;
            public int y_st;
            /*
            public int cx;
            public int cy;
            public int r;
            public int width;
            */
            public int Left;
            public int Top;
            public int Width;
            public int Height;
            public bool enable;
            public bool visible;

        }

        public List<controlInfo> control_data = new List<controlInfo>();

        int ctrlNo = 0;//1;
        //(3). 创建两个函数
        //(3.1)记录窗体和其控件的初始位置和大小,
        int index = 0;
        public void recordAllControls(Control mForm)
        {
            controlInfo ctrl_info;
            //mForm.
            ctrl_info.name = mForm.Name;
            ctrl_info.text = mForm.Text;
            ctrl_info.x_st = mForm.Location.X;
            ctrl_info.y_st = mForm.Location.Y;
            ctrl_info.index = index;
            index++;
            ctrl_info.Left = mForm.Left;
            ctrl_info.Top = mForm.Top;
            ctrl_info.Width = mForm.Width;
            ctrl_info.Height = mForm.Height;
            ctrl_info.enable = mForm.Enabled;
            ctrl_info.visible = mForm.Visible;
            control_data.Add(ctrl_info);   //第一个为"窗体本身",只加入一次即可

            AddControl(mForm);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
        }

        private void AddControl(Control ctl)
        {
            foreach (Control c in ctl.Controls)
            {  //**放在这里，是先记录控件的子控件，后记录控件本身
                //if (c.Controls.Count > 0)
                //    AddControl(c);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
                controlInfo ctrl_info;
                ctrl_info.name = c.Name;
                ctrl_info.text = c.Text;
                ctrl_info.x_st = c.Location.X;
                ctrl_info.y_st = c.Location.Y;
                ctrl_info.index = index;
                index++;
                ctrl_info.Left = c.Left;
                ctrl_info.Top = c.Top;
                ctrl_info.Width = c.Width;
                ctrl_info.Height = c.Height;
                ctrl_info.enable = c.Enabled;
                ctrl_info.visible = c.Visible;

                control_data.Add(ctrl_info);

                //**放在这里，是先记录控件本身，后记录控件的子控件
                if (c.Controls.Count > 0)
                    AddControl(c);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
            }
        }

        //(3.2)控件自适应大小,
        public void controlSizeChange(Control mForm)
        {
            //if (ctrlNo == 0)
            { //*如果在窗体的Form1_Load中，记录控件原始的大小和位置，正常没有问题，但要加入皮肤就会出现问题，因为有些控件如dataGridView的的子控件还没有完成，个数少
                //*要在窗体的Form1_SizeChanged中，第一次改变大小时，记录控件原始的大小和位置,这里所有控件的子控件都已经形成
                controlInfo ctrl_info;
                //cR.Left = mForm.Left; cR.Top = mForm.Top; cR.Width = mForm.Width; cR.Height = mForm.Height;
                ctrl_info.name = mForm.Name;
                ctrl_info.text = mForm.Text;
                ctrl_info.x_st = mForm.Location.X;
                ctrl_info.y_st = mForm.Location.Y;
                ctrl_info.index = index;
                index++;
                ctrl_info.Left = 0;
                ctrl_info.Top = 0;
                ctrl_info.Width = mForm.PreferredSize.Width;
                ctrl_info.Height = mForm.PreferredSize.Height;
                ctrl_info.enable = mForm.Enabled;
                ctrl_info.visible = mForm.Visible;

                control_data.Add(ctrl_info);   //第一个为"窗体本身",只加入一次即可
                AddControl(mForm);//窗体内其余控件可能嵌套其它控件(比如panel),故单独抽出以便递归调用
            }
            float wScale = (float)mForm.Width / (float)control_data[0].Width;//新旧窗体之间的比例，与最早的旧窗体
            float hScale = (float)mForm.Height / (float)control_data[0].Height;//.Height;

            AutoScaleControl(mForm, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
        }

        private void AutoScaleControl(Control ctl, float wScale, float hScale)
        {
            int ctrLeft0, ctrTop0, ctrWidth0, ctrHeight0;
            //int ctrlNo = 1;//第1个是窗体自身的 Left,Top,Width,Height，所以窗体控件从ctrlNo=1开始
            foreach (Control c in ctl.Controls)
            { //**放在这里，是先缩放控件的子控件，后缩放控件本身

                //if (c.Name != "button2")
                  //  continue;

                c.Size = new Size(c.Size.Width / 2, c.Size.Height / 2);
                //c.Size.Width = c.Size.Width / 2;
                //c.Size.Height = c.Size.Height / 2;


                /*

                //if (c.Controls.Count > 0)
                //   AutoScaleControl(c, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
                ctrLeft0 = control_data[ctrlNo].Left;
                ctrTop0 = control_data[ctrlNo].Top;
                ctrWidth0 = control_data[ctrlNo].Width;
                ctrHeight0 = control_data[ctrlNo].Height;
                //c.Left = (int)((ctrLeft0 - wLeft0) * wScale) + wLeft1;//新旧控件之间的线性比例
                //c.Top = (int)((ctrTop0 - wTop0) * h) + wTop1;

                //c.Left = (int)((ctrLeft0) * wScale);//新旧控件之间的线性比例。控件位置只相对于窗体，所以不能加 + wLeft1
                //c.Top = (int)((ctrTop0) * hScale);//
                //c.Width = (int)(ctrWidth0 * wScale);//只与最初的大小相关，所以不能与现在的宽度相乘 (int)(c.Width * w);
                //c.Height = (int)(ctrHeight0 * hScale);//
                c.Width = (int)(ctrWidth0/2);//只与最初的大小相关，所以不能与现在的宽度相乘 (int)(c.Width * w);
                c.Height = (int)(ctrHeight0/2);//

                ctrlNo++;//累加序号
                //**放在这里，是先缩放控件本身，后缩放控件的子控件
                //if (c.Controls.Count > 0)
                    //AutoScaleControl(c, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
               */
            }
        }
    }







}
