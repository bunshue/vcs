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

    //------------------------------------------------------------  # 60個

    class Human : Animal
    {
        private int height;
        private Animal pet;

        public Human(string n, string t, int w, int h)
        {
            this.setname(n);
            this.settype(t);
            this.setweight(w);
            this.height = h;
        }

        public void setpet(Animal a)
        {
            this.pet = a;
        }
        public Animal getpet()
        {
            return this.pet;
        }

        public override void ShowMsg()
        {
            Console.WriteLine("名字:" + this.getname() + " 重量:" + this.getweight() + " 身高:" + this.height);
        }

        public override string GetMsg()
        {
            return "名字:" + this.getname() + " 重量:" + this.getweight() + " 身高:" + this.height;
        }
    }

    //------------------------------------------------------------  # 60個

    class Cats : Animal
    {
        private int body_length;
        private int tail_length;

        public Cats(string n, string t, int w, int b_length, int t_length)
        {
            this.setname(n);
            this.settype(t);
            this.setweight(w);
            this.body_length = b_length;
            this.tail_length = t_length;
        }

        public void print_length()
        {
            Console.WriteLine("體長:" + this.body_length + " 尾長:" + this.tail_length);
        }

        public string show_length()
        {
            return "體長:" + this.body_length + " 尾長:" + this.tail_length;
        }
    }
}
