using System;
using System.Drawing;

namespace gameItems
{
    class Block
    {
        private Rectangle position;
        private Color color;

        public Block(Rectangle r, Color c) {
            this.position = r;
            this.color = c;
        }

        public Rectangle getposition(){
            return this.position;
        }
        public Color getcolor(){
            return this.color;
        }
    }
}
