using System;

namespace RunnerSpace
{
    class Rabbit : AnimalRunner
    {
        private int break_time;

        public Rabbit(int bs, int es){
            this.base_speed = bs;
            this.extra_speed = es;
            this.rnd = new Random();
            this.break_time = 0;
        }

        public override int step(){
            if (this.break_time == 0){
                this.break_time = rnd.Next(1, 5);
                return base_speed + rnd.Next(0, extra_speed);
            }
            else {
                --this.break_time;
                return 0;
            }
        }
    }
}
