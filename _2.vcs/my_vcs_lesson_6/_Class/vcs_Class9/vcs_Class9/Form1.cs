using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using CharacterSpace;

namespace vcs_Class9
{
    public partial class Form1 : Form
    {
        private Monster monster;
        private Hero hero;
        private bool attack_mode;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            reset();
        }

        private void reset()
        {
            this.hero = new Hero("勇者", 100, 20, 12, 20);
            this.monster = new Monster("怪物", 200, 25, 10, 10);
            this.attack_mode = false;
            logList.Items.Clear();
            refresh();
        }

        private void refresh()
        {
            if (this.hero.gethealth() <= 0)
            {
                MessageBox.Show("勇者輸了 請重新來過");
                reset();
            }
            else if (this.monster.gethealth() <= 0)
            {
                MessageBox.Show("勇者成功打敗了怪物!");
                reset();
            }

            this.attack_mode = !this.attack_mode;
            heroLabel.Text = "勇者狀態:\n" + this.hero.print();
            monsterLabel.Text = "怪物狀態:\n" + this.monster.print();
            attackButton.Enabled = this.attack_mode;
            powerButton.Enabled = this.attack_mode;
            defenseButton.Enabled = !this.attack_mode;
            dodgeButton.Enabled = !this.attack_mode;
        }

        private void attackButton_Click(object sender, EventArgs e)
        {
            logList.Items.Add(this.hero.attack(this.monster));
            refresh();
        }
        private void powerButton_Click(object sender, EventArgs e)
        {
            logList.Items.Add(this.hero.power_attack(this.monster));
            refresh();
        }

        private void defenseButton_Click(object sender, EventArgs e)
        {
            logList.Items.Add(this.monster.attack(this.hero));
            refresh();
        }

        private void dodgeButton_Click(object sender, EventArgs e)
        {
            this.hero.double_dodge();
            logList.Items.Add(this.monster.attack(this.hero));
            this.hero.half_dodge();
            refresh();
        }
    }
}
