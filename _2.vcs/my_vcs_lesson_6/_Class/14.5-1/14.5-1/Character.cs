using System;

namespace CharacterSpace
{
    class Character
    {
        protected string name;
        protected int health, attack_ability, defense_ability, dodge_rate;
        protected Random rnd;

        public string getname(){
            return this.name;
        }
        public int gethealth() {
            return this.health;
        }

        public string attack(Character c) {
            int accuracy = this.rnd.Next(80, 121);
            string result = c.defense(this.attack_ability*accuracy / 100, 1);
            return this.name + "嘗試攻擊" + c.name + " " + result;
        }

        public string defense(int a, int d) {
            int dodge = this.rnd.Next(1, 101);
            if (dodge < this.dodge_rate*d) {
                return this.name + "閃避了攻擊";
            }
            else {
                this.health -= a-this.defense_ability;
                return this.name + "受到" + (a-this.defense_ability) + "點傷害";
            }
        }

        public string print(){
            return "攻擊力:" + this.attack_ability + "\n防禦力:" + this.defense_ability + "\n生命值:" + this.health;
        }

    }
}
