using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// ����ֵ�Ǻ��࣬��Ӧ�ؼ���abs�������ִ�Сд��
    /// </summary>
    /// <example>�÷�abs(-12)����������š�</example>
    public class TokenAbs : TokenArithmeticMethod
    {
        public TokenAbs(int Index, int Length)
            : base(Index, Length)
        { }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 1;
        }

        public override void Execute()
        {
            this.CheckChildCount("Abs����������Ԫ���������Ϸ�");

            TokenRecord Token = this.ChildList[0];
            Token.Execute();

            this.TokenValue = Math.Abs(Token.ChangeTokenToDouble("Abs�����Ĳ�������������"));
        }
    }
}