using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class7
{
    class Class1
    {
    }

    abstract class Shape
    {
        private string type;
        public Shape(string type)
        {
            this.type = type;
        }
        public string getType()
        {
            return type;
        }
        public virtual string show() { return type; }
        abstract public double area();
    }

    interface Comparable
    {
        int compareTo(Object obj);
    }

    class Triangle : Shape, Comparable
    {
        private double tbase;
        private double height;
        public Triangle(double tbase, double height)
            : base("Triangle")
        {
            this.tbase = tbase;
            this.height = height;
        }
        public override string show()
        {
            return base.show() +
                   ": 底 = " + tbase +
                   ", 高 = " + height;
        }
        public override double area()
        {
            return 0.5 * tbase * height;
        }

        public int compareTo(Object obj)
        {
            double myArea = area();
            double sArea = ((Shape)obj).area();

            if (myArea == sArea) return 0;
            else if (myArea < sArea) return -1;
            else return 1;
        }
    }

    class Rectangle : Shape, Comparable
    {
        private double width;
        private double height;
        public Rectangle(double width, double height)
            : base("Rectangle")
        {
            this.width = width;
            this.height = height;
        }
        public override string show()
        {
            return base.show() +
                   ": 寬 = " + width +
                   ", 高 = " + height;
        }
        public override double area()
        {
            return width * height;
        }

        public int compareTo(Object obj)
        {
            double myArea = area();
            double sArea = ((Shape)obj).area();

            if (myArea == sArea) return 0;
            else if (myArea < sArea) return -1;
            else return 1;
        }

    }

    class ShapeCollection
    {
        private int count = 0;

        private Shape[] shapeArray = new Shape[100];

        public ShapeCollection() { }

        public int getCount() { return count; }

        public void add(Shape s)
        {
            if (s != null && count < 100) shapeArray[count++] = s;
        }

        public string listing()
        {
            string res = "";

            for (int i = 0; i < count; i++)
            {   // polymorphism
                Shape s = shapeArray[i];
                res += s.show() + ", 面積 = " + s.area() + "\r\n";
            }

            return res;
        }
        /*
         * 使用interface Comparable的compareTo(Object obj)方法取得比較的結果
         */
        public string maxShape()
        {
            if (count == 0) return "尚未有圖形";

            string res = "";

            Shape max = shapeArray[0];

            for (int i = 1; i < count; i++)
            {
                Shape cObj = shapeArray[i];
                if (((Comparable)cObj).compareTo(max) > 0)
                    max = cObj;
            }

            res = max.show();

            return res;
        }

        public string rankShape()
        {
            string res = "[ ";

            if (count == 0) return res + "]";

            int[] rank = new int[count];

            for (int i = 0; i < count; i++)
            {
                rank[i] = 1;
                Shape iShape = shapeArray[i];

                for (int j = 0; j < count; j++)
                {
                    Shape jShape = shapeArray[j];
                    if (((Comparable)jShape).compareTo(iShape) > 0)
                        rank[i]++;
                }
            }

            for (int i = 0; i < count; i++)
                res += rank[i] + " ";

            return res + "]";
        }

        /*
         * 直接使用area()方法來進行比較
        */
        /*
        public string maxShape()
        {
            if (count == 0) return "尚未有圖形";

            string res = "";

            Shape max = shapeArray[0];

            for (int i = 1; i < count; i++)
            {
                Shape cObj = shapeArray[i];

                if (cObj.area() > max.area())
                    max = cObj;
            }

            res = max.show();

            return res;
        }

        public string rankShape()
        {
            string res = "[ ";

            if (count == 0) return res + "]";

            int[] rank = new int[count];

            for (int i = 0; i < count; i++)
            {
                rank[i] = 1;
                Shape iShape = shapeArray[i];

                for (int j = 0; j < count; j++)
                {
                    Shape jShape = shapeArray[j];
                    if (jShape.area() > iShape.area())
                        rank[i]++;
                }
            }

            for (int i = 0; i < count; i++)
                res += rank[i] + " ";

            return res + "]";
        }
        */

    }

}
