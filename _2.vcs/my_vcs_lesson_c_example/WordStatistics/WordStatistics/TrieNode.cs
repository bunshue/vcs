using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication62
{

    public class Trie
    {
        
        private TrieNode root;//字典树的根

        HashSet<string> hashSet = new HashSet<string>();

        public Trie()
        {//初始化字典树
            root = new TrieNode();
        }

        public void insert(String str)
        {//在字典树中插入一个单词
            if (str == null || str.Length == 0)
            {
                return;
            }
            TrieNode node = root;
            char[] letters = str.ToArray();
            for (int i = 0, len = str.Length; i < len; i++)
            {
                int pos = letters[i] - 'a';
                if (node.son[pos] == null)
                {
                    node.son[pos] = new TrieNode();
                    node.son[pos].val = letters[i];
                }
                else
                {
                    node.son[pos].num++;
                }
                node = node.son[pos];
            }
            node.isEnd = true;
        }
        //在字典树中查找一个完全匹配的单词.
        public Boolean has(String str)
        {
            if (str == null || str.Length == 0)
            {
                return false;
            }
            TrieNode node = root;
            char[] letters = str.ToArray();
            for (int i = 0, len = str.Length; i < len; i++)
            {
                int pos = letters[i] - 'a';
                if (node.son[pos] != null)
                {
                    node = node.son[pos];
                }
                else
                {
                    return false;
                }
            }
            return node.isEnd;
        }
    }

    public class TrieNode
    {//字典树节点
        public int num;//有多少单词通过这个节点,即节点字符出现的次数
        public TrieNode[] son;//所有的儿子节点
        public Boolean isEnd;//是不是最后一个节点
        public char val;//节点的值

        public TrieNode()
        {
            num = 1;
            son = new TrieNode[26];
            isEnd = false;
        }
    }


    //public class TrieNode
    //{
    //    private string Prefix { get; set; }
    //    private IDictionary<string, TrieNode> ChildNodes { get; set; }
    //    private IEqualityComparer<string> Comparer { get; set; }
    //    public int Count = 1;
    //    public string nodeName { get; set; }

    //    public TrieNode() : this(StringComparer.CurrentCulture) { }
    //    public TrieNode(IEqualityComparer<string> comparer) : this(comparer, string.Empty) { }

    //    private TrieNode(IEqualityComparer<string> comparer, string prefix)
    //    {
    //        if (prefix == null)
    //            throw new ArgumentNullException("Invalid prefix");

    //        this.Prefix = prefix;
    //        this.ChildNodes = new Dictionary<string, TrieNode>(comparer);
    //        this.Comparer = comparer;
    //    }

    //    public void Add(string word)
    //    {
    //        if (word == null)
    //            throw new InvalidOperationException("Cannot add null to list");

    //        if (word.Length < this.Prefix.Length
    //            || !this.Comparer.Equals(word.Substring(0, this.Prefix.Length), this.Prefix))
    //        {
    //            throw new ArgumentException("Parameter does not match prefix.");
    //        }

    //        if (word.Length > this.Prefix.Length)
    //        {
    //            string childKey = word.Substring(0, this.Prefix.Length + 1);
    //            if (!this.ChildNodes.ContainsKey(childKey))
    //            {
    //                this.ChildNodes.Add(childKey, new TrieNode(this.Comparer, childKey));
    //            }

    //            this.ChildNodes[childKey].Add(word);
    //        }
    //        else
    //        {
    //            this.nodeName = this.Prefix;
    //        }
    //    }

    //    public TrieNode FindMatche(string searchPrefix)
    //    {
    //        if (searchPrefix == null)
    //            throw new InvalidOperationException("Cannot search on null strings");

    //        if (this.Comparer.Equals(searchPrefix, this.Prefix))
    //        {
    //            Count++;
    //            return this;
    //        }
    //        else
    //        {
    //            string childKey = searchPrefix.Substring(0, this.Prefix.Length + 1);
    //            if (this.ChildNodes.ContainsKey(childKey))
    //                return this.ChildNodes[childKey].FindMatche(searchPrefix);
    //            else
    //                return null; // empty list for no matches 
    //        }
    //    }
    //}
}
