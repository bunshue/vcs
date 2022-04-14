using System;
using System.Collections.Generic;
using System.Text;

//Author: Alex Leo
//Email: alexleo321@hotmail.com
//Blog: http://www.cnblogs.com/conexpress/
namespace ConExpress.Calculator
{
    /// <summary>
    /// �﷨������
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    internal class SyntaxTreeAnalyse
    {
        /// <summary>
        /// �ǺŶ���ȡ����ȡ���������Ǻ�
        /// </summary>
        /// <param name="TokenList">�Ǻ��б�</param>
        /// <param name="VariableDic">�����ֵ�</param>
        /// <param name="IndexStart">��ʼ���</param>
        /// <param name="IndexEnd">�������</param>
        /// <returns>����ǺŶεĶ��������Ǻż�¼����</returns>
        /// <remarks>Author:Alex Leo</remarks>
        internal static TokenRecord SyntaxTreeGetTopTokenAnalyse(List<TokenRecord> TokenList, int IndexStart, int IndexEnd)
        {
            int intIndexCurrent = IndexStart;//��ǰ�������
            int intIndexSubStart = IndexStart;//�ӼǺŶε���ʼ���
            TokenRecord Token;//��ȡ��ǰToken
            Stack<TokenRecord> StackCompart = new Stack<TokenRecord>();//���Ŷ�ջ
            Stack<TokenRecord> StackOperate = new Stack<TokenRecord>();//�����ǺŶ�ջ

            for (int intIndex = IndexStart; intIndex <= IndexEnd; intIndex++)
            {
                Token = TokenList[intIndex];
                intIndexCurrent = intIndex;
                if (Token is TokenLeftBracket)
                {
                    StackCompart.Push(TokenList[intIndexCurrent]);//��������ѹջ
                    //��ȡ�����Ŷ��а����ļǺŶ�
                    intIndexSubStart = intIndexCurrent + 1;//�����ӼǺŶε���ʼ���
                    //��ȡ�ǺŶ�
                    //����﷨���󣬱����ڼǺŶε�ĩβû����Ե������żǺţ��������������Ϊ�﷨��ȷ
                    while (StackCompart.Count > 0)
                    {
                        intIndexCurrent += 1;
                        if (intIndexCurrent >= TokenList.Count)
                        {
                            //Error or auto add lossed bracket
                            throw new SyntaxException(Token.Index, Token.Length, "ȱ����Ե�����");
                        }

                        if (TokenList[intIndexCurrent] is TokenLeftBracket)
                        {
                            StackCompart.Push(TokenList[intIndexCurrent]);
                        }
                        else if (TokenList[intIndexCurrent] is TokenRightBracket)
                        {
                            StackCompart.Pop();
                        }
                    }

                    TokenRecord TokenInnerTop = SyntaxTreeGetTopTokenAnalyse(TokenList, intIndexSubStart, intIndexCurrent - 1);
                    if (TokenInnerTop != null)//ֻ����ȡ�������еĶ����ڵ�����
                    {
                        Token.ChildList.Add(TokenInnerTop);
                    }
                    else
                    {
                        //�޷���ȡ�����ڵĶ����ڵ�
                        throw new SyntaxException(Token.Index, Token.Length, "�����ڲ�����������ʽ");
                    }

                    intIndex = intIndexCurrent;//�ƶ���ŵ���ǰ���
                    SyntaxTreeStackAnalyse(StackOperate, Token);
                }//if token is TokenLeftBracket
                else if (Token is TokenMethod)//��������
                {
                    //��鷽�����Ƿ����������
                    if (intIndexCurrent >= IndexEnd || !(TokenList[intIndexCurrent + 1] is TokenLeftBracket))
                    {
                        throw new SyntaxException(Token.Index, Token.Length, "������ȱ������");
                    }

                    intIndexSubStart = intIndexCurrent;//�����ӼǺŶε���ʼ���
                    intIndexCurrent += 1;//ָ�����
                    StackCompart.Push(TokenList[intIndexCurrent]);//��������ѹջ
                    //��ȡ�ǺŶ�
                    //����﷨���󣬱����ڼǺŶε�ĩβû����Ե������żǺţ��������������Ϊ�﷨��ȷ
                    while (StackCompart.Count > 0)
                    {
                        intIndexCurrent += 1;
                        if (intIndexCurrent >= TokenList.Count)
                        {
                            //Error or auto add lossed bracket
                            throw new SyntaxException(Token.Index, Token.Length, "ȱ����Ե�����");
                        }
                        if (TokenList[intIndexCurrent] is TokenLeftBracket)
                        {
                            StackCompart.Push(TokenList[intIndexCurrent]);
                        }
                        else if (TokenList[intIndexCurrent] is TokenRightBracket)
                        {
                            StackCompart.Pop();
                        }
                    }

                    if ((intIndexCurrent - intIndexSubStart) == 2)//��������ŵ���źͷ��������֮����2��˵���м�ֻ��һ��������
                    {
                        throw new SyntaxException(TokenList[intIndexCurrent - 1].Index, 1, "�����ڲ�����������ʽ");
                    }

                    //���������ǺŶΣ���Ϊ�������Ŷ��п����ж��������������if��max�ȣ������û�ȡ�����ڵ�ķ���SyntaxTreeGetTopTokenAnalyse
                    SyntaxTreeMethodAnalyse(TokenList, intIndexSubStart, intIndexCurrent);

                    intIndex = intIndexCurrent;//�ƶ���ŵ���ǰ���
                    SyntaxTreeStackAnalyse(StackOperate, Token);
                }//if token is TokenKeyword
                else if (Token is TokenSymbol || Token is TokenValue)
                {
                    SyntaxTreeStackAnalyse(StackOperate, Token);
                }
                else
                {
                    //��������
                    throw new SyntaxException(Token.Index, Token.Length, "�����λ�ô���");
                }
            }
            return SyntaxTreeStackGetTopToken(StackOperate);//���ض����Ǻ�
        }


        /// <summary>
        /// �����ǺŶη��������������м�Ĵ���Σ�
        /// </summary>
        /// <param name="ListToken">�Ǻ��б�</param>
        /// <param name="IndexStart">���ſ�ʼ�����</param>
        /// <param name="IndexEnd">���Ž��������</param>
        /// <remarks>ֻ���������ķ����Σ�����if(...), round(...)</remarks>
        /// <remarks>Author:Alex Leo</remarks>
        private static void SyntaxTreeMethodAnalyse(List<TokenRecord> ListToken, int IndexStart, int IndexEnd)
        {
            int intIndexSubStart = IndexStart;//�ӼǺŶε���ʼ���
            intIndexSubStart = IndexStart + 2;//�ƶ��ӼǺŶεĿ�ʼ��ŵ����ź���
            int intIndexSubEnd = IndexEnd;//�ӼǺŶεĽ������
            TokenRecord TokenMethod = ListToken[IndexStart];//�����ǺŶ���
            TokenRecord TokenCurrent;//��ȡ��ǰToken
            Stack<TokenRecord> StackCompart = new Stack<TokenRecord>();//�ָ�����ջ

            for (int intIndex = IndexStart; intIndex <= IndexEnd; intIndex++)
            {
                TokenCurrent = ListToken[intIndex];
                if (TokenCurrent is TokenLeftBracket)
                {
                    StackCompart.Push(TokenCurrent);
                }
                else if (TokenCurrent is TokenRightBracket)
                {
                    StackCompart.Pop();
                    if (StackCompart.Count == 0)//��������һ��������
                    {
                        intIndexSubEnd = intIndex - 1;//���öν������
                        TokenMethod.ChildList.Add(SyntaxTreeGetTopTokenAnalyse(ListToken, intIndexSubStart, intIndexSubEnd));//�ݹ�
                    }
                }
                else if (TokenCurrent is TokenComma)
                {
                    if (StackCompart.Count == 1)//����Ƿ������Ӷ�
                    {
                        intIndexSubEnd = intIndex - 1;//���öν������
                        TokenMethod.ChildList.Add(SyntaxTreeGetTopTokenAnalyse(ListToken, intIndexSubStart, intIndexSubEnd));//�ݹ�
                        intIndexSubStart = intIndex + 1;//���ӼǺŶ���ź���
                    }
                }
                else
                {
                    //��������
                }
            }

            //TokenMethod.GetType().GetMethod("CheckChildCount").Invoke(TokenMethod, new object[] { "����Ԫ���������Ϸ�" });
        }


        /// <summary>
        /// �﷨����ջ���������ڼǺŵ����ȼ�
        /// </summary>
        /// <param name="SyntaxTreeStack">�﷨����ջ</param>
        /// <param name="NewToken">�¼Ǻ�</param>
        /// <remarks>Author:Alex Leo</remarks>
        private static void SyntaxTreeStackAnalyse(Stack<TokenRecord> SyntaxTreeStack, TokenRecord NewToken)
        {
            if (SyntaxTreeStack.Count == 0)//����﷨����ջ�в����ڼǺţ���ֱ��ѹջ
            {
                SyntaxTreeStack.Push(NewToken);
            }
            else//���򣬱Ƚ����ȼ�����ջ����
            {
                //�Ƚ����ȼ��������Token���ȼ��ߣ���ѹջ��
                //�����Token���ȼ��ͣ���ջ���ѵ�����Token����Ϊ��Token���¼���������Tokenѹջ��
                //��ͬ���ȼ�Ҳ��ջ��������Tokenѹջ
                //if (this.m_DicTokenTypePriority[SyntaxTreeStack.Peek().TokenType] < this.m_DicTokenTypePriority[NewToken.TokenType])//�ͽ�
                if (SyntaxTreeStack.Peek().Priority < NewToken.Priority)//�ͽ�
                {
                    SyntaxTreeStack.Push(NewToken);//�ͽ�
                }
                else
                {
                    TokenRecord TempToken = null;
                    //�����ջ���мǺţ�����ջ���ļǺ����ȼ����ڵ����¼Ǻŵ����ȼ����������ջ
                    while (SyntaxTreeStack.Count > 0 && (SyntaxTreeStack.Peek().Priority >= NewToken.Priority))
                    {
                        TempToken = SyntaxTreeStack.Pop();
                        if (SyntaxTreeStack.Count > 0)//���ջ���Ƿ����Ϊ�գ����Ϊ�����˳�
                        {
                            if (SyntaxTreeStack.Peek().Priority >= NewToken.Priority)
                            {
                                SyntaxTreeStack.Peek().ChildList.Add(TempToken);
                            }
                            else
                            {
                                NewToken.ChildList.Add(TempToken);
                            }
                        }
                        else
                        {
                            NewToken.ChildList.Add(TempToken);
                        }
                    }
                    SyntaxTreeStack.Push(NewToken);//ѹջ
                }
            }
        }


        /// <summary>
        /// ��ȡ�﷨����ջ�Ķ����Ǻ�
        /// </summary>
        /// <param name="SyntaxTreeStack">�﷨����ջ</param>
        /// <returns>�����Ǻ�</returns>
        /// <remarks>Author:Alex Leo</remarks>
        private static TokenRecord SyntaxTreeStackGetTopToken(Stack<TokenRecord> SyntaxTreeStack)
        {
            TokenRecord TempToken = null;
            if (SyntaxTreeStack.Count > 0)
            { 
                TempToken = SyntaxTreeStack.Pop();
                while (SyntaxTreeStack.Count > 0)
                {
                    SyntaxTreeStack.Peek().ChildList.Add(TempToken);
                    TempToken = SyntaxTreeStack.Pop();
                }
            }
            return TempToken;
        }
    }//class SyntaxTreeAnalyse
}//namespace