using System;

namespace RunnerSpace
{
    class AnimalRunner
    {
        protected int base_speed;
        protected int extra_speed;
        protected Random rnd;

        public virtual int step(){
            return base_speed + rnd.Next(0, extra_speed);
        }

    }
}
