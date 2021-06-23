using System;

namespace AnimalSpace
{
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

        public override void print()
        {
            Console.WriteLine("名字:" + this.getname() + " 重量:" + this.getweight() + " 身高:" + this.height);
        }
    }
}

