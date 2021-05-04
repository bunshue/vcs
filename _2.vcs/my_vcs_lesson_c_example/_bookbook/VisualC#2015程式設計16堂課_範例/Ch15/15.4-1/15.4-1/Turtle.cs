using System;

namespace RunnerSpace
{
    class Turtle : AnimalRunner
    {
        public Turtle(int bs, int es) {
            this.base_speed = bs;
            this.extra_speed = es;
            this.rnd = new Random();
        }
    }
}
