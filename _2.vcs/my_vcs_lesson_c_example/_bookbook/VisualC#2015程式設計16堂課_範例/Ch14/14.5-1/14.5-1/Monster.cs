using System;

namespace CharacterSpace
{
    class Monster : Character
    {
        public Monster(string n, int h, int a, int d, int dr) {
            this.name = n;
            this.health = h;
            this.attack_ability = a;
            this.defense_ability = d;
            this.dodge_rate = dr;
            this.rnd = new Random();
        }
    }
}
