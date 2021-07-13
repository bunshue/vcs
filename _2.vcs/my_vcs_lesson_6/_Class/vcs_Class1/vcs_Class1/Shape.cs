using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class1
{

    class Circle
    {
        //protected int radius; // 子類別可以直接存取 
        private int radius;
        public Circle() { radius = 2; }
        public Circle(int r) { radius = r; }
        public int getRadius() { return radius; }
        public double getArea()
        {
            return Math.PI * radius * radius;
        }
    }

    class Cylinder : Circle
    {
        int length; // private

        public Cylinder() { length = 3; }
        /*
        public Cylinder(int r, int l)
        {
            radius = r; // 此radius是繼承Circle而來 
            length = l;           
        }
        */

        public Cylinder(int r, int l)
            : base(r)
        {
            length = l;
        }

        public int getLength() { return length; }
        /*
        public new double getArea()
        {
            double ca = base.getArea();
            double cl = 2 * Math.PI * radius;
            return 2 * ca + cl * length;
        }
        */

        public new double getArea()
        {
            double ca = base.getArea();
            double cl = 2 * Math.PI * getRadius(); // base.getRadius();亦可
            return 2 * ca + cl * length;
        }
    }

}
