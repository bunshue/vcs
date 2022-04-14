using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenRound : TokenArithmeticMethod
    {
        public TokenRound(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("round��������Ԫ���������Ϸ�");

            TokenRecord TokenSouece = this.ChildList[0];
            TokenRecord TokenLength = this.ChildList[1];
            TokenSouece.Execute();
            TokenLength.Execute();

            //check child token type
            double dblSource = TokenSouece.ChangeTokenToDouble("round��������Ԫ�ز�����ֵ");
            int intLength = Convert.ToInt32(TokenLength.ChangeTokenToDouble("round���Ľ�ȡλ��������ֵ"));

            //��Ᵽ��С��λ�����Ƿ�Ϸ�
            intLength = intLength < 0 ? 0 : intLength;
            intLength = intLength > 28 ? 28 : intLength;

            this.TokenValue = Math.Round(dblSource, intLength);
        }
    }
}
