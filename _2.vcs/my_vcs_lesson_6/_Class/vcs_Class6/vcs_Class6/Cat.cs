using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CatTest
{
    class Cat
    {
        public string name;
        private string type;
        private int weight;

        public Cat()
        {
            this.name = "未知";
            this.type = "未知";
            this.weight = -1;
        }

        public Cat(string n, string t)
        {
            this.name = n;
            this.type = t;
            this.weight = -1;
        }

        public void settype(string t)
        {
            this.type = t;
        }
        public string gettype()
        {
            return this.type;
        }

        public void setweight(int w)
        {
            this.weight = w;
        }
        public int getweight()
        {
            return this.weight;
        }

        public void feed()
        {
            Console.WriteLine("餵食" + this.name);
            this.weight += 1;
        }
        public void play()
        {
            Console.WriteLine("與" + this.name + "遊戲");
            this.weight -= 1;
        }

        public void print()
        {
            Console.WriteLine("名稱:" + this.name + " 品種:" + this.type + " 體重:" + this.weight);
        }
    }
}
