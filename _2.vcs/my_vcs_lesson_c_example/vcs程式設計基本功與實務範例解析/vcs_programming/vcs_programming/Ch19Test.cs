using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class Ch19Test : Form
    {
        public Ch19Test()
        {
            InitializeComponent();
        }

        private void btnCircle_Click(object sender, EventArgs e)
        {
            Circle c1 = new Circle(2);
            MessageBox.Show("圓c1的面積 = " + c1.getArea() + "\n" +
                "圓c1的半徑 = " + c1.getRadius(), "Circle物件",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void btnCylinder_Click(object sender, EventArgs e)
        {            
            //Cylinder cy1 = new Cylinder();
            Cylinder cy1 = new Cylinder(5, 10);

            MessageBox.Show("圓柱體cy1的半徑 = " + cy1.getRadius()
                       + "\n" + "圓柱體cy1的高度 = " + cy1.getLength()
                       + "\n" + "圓柱體cy1的表面積 = " + cy1.getArea(), "Cylinder物件",
                       MessageBoxButtons.OK, MessageBoxIcon.Information);

        }

        private void button4_Click(object sender, EventArgs e)
        {

            Base b = new Base();
            Derived d = new Derived();       
            //逐一測試
            b.Method(); //Base.Method
            //b.DMethod();//編譯錯誤
            //d.Method(); //Derived.Method
            //d.DMethod(); //Derived.DMethod
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Derived d = new Derived();
            Base b = d;

            //b.Method(); //--->>Base.Method
            //b.DMethod();//編譯錯誤
            
            //Derived td = b;

            Derived td = (Derived) b;

            td.DMethod(); //Derived.DMethod
            td.Method();  //Derived.Method
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Base b = new Base();
            Derived d = new Derived();

            b.VMethod(); //Base.VMethod
            d.VMethod(); //Derived.VMethod

            b = d;

            b.VMethod(); //Derived.VMethod

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Circle c = new Cylinder();

            // Cylinder cy = new Circle(); // 編譯錯誤

            // Cylinder cy = c; // 編譯錯誤

            Cylinder cy = (Cylinder)c; //OK

            /*
            Circle c1 = new Circle();
            Cylinder cy1 = (Cylinder) c1; // 執行時產生Exception的錯誤
            */

            //int len = c.getLength(); // 編譯錯誤

            int len = ((Cylinder)c).getLength();

            MessageBox.Show("Length = " + len);
        }
      
    }
    
}
