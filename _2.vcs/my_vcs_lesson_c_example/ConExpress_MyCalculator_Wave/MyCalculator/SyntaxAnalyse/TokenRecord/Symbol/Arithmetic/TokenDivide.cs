using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenDivide : TokenArithmeticSymbol 
    {
        public TokenDivide(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 3;
        }

        public override void Execute()
        {
            this.CheckChildCount("����������Ԫ���������Ϸ�");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            //����������Ϊ0
            if (TokenSecond.ChangeTokenToDouble("����������Ԫ�ز�����ֵ") == 0)
            {
                //throw new DivideByZeroException(string.Format("�������������{0}����������Ϊ�㡣",this.Index.ToString()));
                throw new SyntaxException(this.Index, this.Length, "����������󣬳�������Ϊ��");
            }

            this.TokenValue = TokenFirst.ChangeTokenToDouble("����������Ԫ�ز�����ֵ") / TokenSecond.ChangeTokenToDouble("����������Ԫ�ز�����ֵ");
        }
    }
}
