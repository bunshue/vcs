using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// �����żǺ��࣬��Ӧ�ַ�(
    /// </summary>
    public class TokenLeftBracket : TokenCompart
    {
        public TokenLeftBracket(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 10;//���ŵ����ȼ���ߣ�������������������
        }

        public override void Execute()
        {
            this.CheckChildCount("��������������Ψһ");

            TokenRecord TokenInner = this.ChildList[0];
            TokenInner.Execute();
            this.TokenValueType = TokenInner.TokenValueType;
            this.TokenValue = TokenInner.TokenValue;
            //if (TokenInner.TokenValueType == TokenValueTypeEnum.String)
            //{
            //    this.TokenString = TokenInner.TokenString;
            //}
            //else
            //{
            //    this.TokenNumber = TokenInner.TokenNumber;
            //}
        }
    }
}