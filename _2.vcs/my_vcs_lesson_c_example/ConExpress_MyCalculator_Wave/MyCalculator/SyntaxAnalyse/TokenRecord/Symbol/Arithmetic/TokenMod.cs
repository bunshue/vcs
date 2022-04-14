using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenMod : TokenArithmeticSymbol
    {
        public TokenMod(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 3;
        }

        public override void Execute()
        {
            this.CheckChildCount("ģ����Ĳ������������Ϸ�");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValue = TokenFirst.ChangeTokenToDouble("ģ���������Ԫ�ز�����ֵ") % TokenSecond.ChangeTokenToDouble("ģ���������Ԫ�ز�����ֵ");
        }
    }
}
