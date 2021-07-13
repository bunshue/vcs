using System;

namespace AnimalSpace
{
    class Animal
    {
        private string name;
        private string type;
        private int weight;

        protected void setname(string n)
        {
            this.name = n;
        }
        public string getname()
        {
            return this.name;
        }

        protected void settype(string t)
        {
            this.type = t;
        }
        public string gettype()
        {
            return this.type;
        }

        protected void setweight(int w)
        {
            this.weight = w;
        }
        public int getweight()
        {
            return this.weight;
        }

        public virtual void ShowMsg()
        {
            Console.WriteLine("名字:" + this.name + " 類型:" + this.type + " 重量:" + this.weight);
        }

        public virtual string GetMsg()
        {
            return "名字:" + this.name + " 類型:" + this.type + " 重量:" + this.weight;
        }

    }
}

