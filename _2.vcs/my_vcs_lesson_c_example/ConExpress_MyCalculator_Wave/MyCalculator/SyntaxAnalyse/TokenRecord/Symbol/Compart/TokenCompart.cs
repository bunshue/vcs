using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// �ָ����Ǻ���
    /// </summary>
    public abstract class TokenCompart : TokenSymbol
    {
        public TokenCompart(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 1;
        }

        protected override void SetPriority()
        {
            this.m_Priority = 5;//���ﲢ��ʵ������
        }

        public override void Execute()
        {
            throw new SyntaxException(this.Index, this.Length, "�ָ����޷�ִ������");
        }
    }
}
