﻿using System;

namespace AnimalSpace
{
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

