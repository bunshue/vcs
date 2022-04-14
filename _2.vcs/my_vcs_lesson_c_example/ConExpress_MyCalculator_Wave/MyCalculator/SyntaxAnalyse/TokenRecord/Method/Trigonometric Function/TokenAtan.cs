using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenAtan : TokenTrigonometricFunction
    {
        public TokenAtan(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("Atan����������Ԫ���������Ϸ�");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Atan(TokenChild.ChangeTokenToDouble("Atan�����Ĳ�������������")) * 180 / Math.PI, 10);
        }
    }
}
