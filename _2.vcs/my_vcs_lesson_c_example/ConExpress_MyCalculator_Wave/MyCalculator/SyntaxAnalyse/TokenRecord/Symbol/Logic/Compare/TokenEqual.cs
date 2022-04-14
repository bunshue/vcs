using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenEqual : TokenCompare
    {
        public TokenEqual(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "���������Ԫ���������Ϸ�";
        }

        public override void Execute()
        {
            base.Execute();
            this.TokenValue = (base.Compare() == 0);
        }
    }

    /// <summary>
    /// ��ֵ�����
    /// </summary>
    /// <remarks>��Ӧ=��</remarks>
    public class TokenEvaluate : TokenCompare
    {
        public TokenEvaluate(int Index, int Length)
            : base(Index, Length)
        { 
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "��ֵ�����Ԫ���������Ϸ�";
        }

        public override void Execute()
        {
            //base.Execute();
            this.CheckChildCount(this.m_ChildCountErrorInformation);

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenSecond.Execute();

            if (TokenFirst is TokenValue && SyntaxAnalyse.DicVariable.ContainsValue(TokenFirst as TokenValue))
            {
                TokenFirst.TokenValueType = TokenSecond.TokenValueType;
                TokenFirst.TokenValue = TokenSecond.TokenValue;
                this.TokenValue = TokenSecond.TokenValue;
                this.TokenValueType = TokenSecond.TokenValueType;
            }
            else
            {
                //����
                throw new SyntaxException(this.Index, this.Length, "��ֵ����ĸ�ֵ�����Ǳ���");
            }
        }
    }
}
