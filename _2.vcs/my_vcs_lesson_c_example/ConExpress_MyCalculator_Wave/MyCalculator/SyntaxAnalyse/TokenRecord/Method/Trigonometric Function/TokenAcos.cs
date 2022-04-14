using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenAcos : TokenTrigonometricFunction
    {
        public TokenAcos(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("Acos����������Ԫ���������Ϸ�");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Acos(TokenChild.ChangeTokenToDouble("Acos�����Ĳ�������������")) * 180 / Math.PI, 10);
        }
    }
}
