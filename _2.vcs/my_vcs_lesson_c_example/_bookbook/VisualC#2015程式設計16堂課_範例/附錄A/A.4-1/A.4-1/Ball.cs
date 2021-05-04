using System;
using System.Drawing;

namespace gameItems
{
    class Ball
    {
        private Rectangle position;
        private Color color;
        private int Vx, Vy;

        public Ball(Rectangle r, Color c, int x, int y) {
            this.position = r;
            this.color = c;
            this.Vx = x;
            this.Vy = y;
        }

        public void step(){
            this.position.X += this.Vx;
            this.position.Y += this.Vy;
        }
        public Rectangle getposition(){
            return this.position;
        }

        public Color getcolor(){
            return this.color;
        }
        public void setcolor(Color c){
            this.color = c;
        }

        public void increaseVx(int i){
            this.Vx += i;
        }
        public void increaseVy(int i){
            this.Vy += i;
        }

        public void collisionVx(){
            this.Vx *= -1;
        }
        public void collisionVy(){
            this.Vy *= -1;
        }

    }
}
