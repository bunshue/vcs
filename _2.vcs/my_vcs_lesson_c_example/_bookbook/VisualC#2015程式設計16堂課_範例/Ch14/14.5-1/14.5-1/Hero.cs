using System;

namespace CharacterSpace
{
    class Hero : Character
    {
        public Hero(string n, int h, int a, int d, int dr) {
            this.name = n;
            this.health = h;
            this.attack_ability = a;
            this.defense_ability = d;
            this.dodge_rate = dr;
            this.rnd = new Random();
        }

        public string power_attack(Character c) {
            int accuracy = this.rnd.Next(80, 121);
            string result = c.defense(this.attack_ability*2* accuracy / 100, 3);
            return this.name + "強力攻擊" + c.getname() + " " + result;
        }

        public void double_dodge() {
            this.dodge_rate *= 2;
            this.defense_ability /= 2;
        }
        public void half_dodge(){
            this.dodge_rate /= 2;
            this.defense_ability *= 2;
        }
    }
}
