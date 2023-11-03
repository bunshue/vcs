/*
 * Created on 2005-6-4
 *
 */
package com.lietu.keywords;

import java.io.StringReader;

//import org.apache.lucene.analysis.StopFilter;
import org.apache.lucene.analysis.Token;
import org.apache.lucene.analysis.TokenStream;

//import seg.train.WordContext;
//import seg.train.Bigrams;
//import seg.train.BigramsContextCounts;
//import seg.train.NewWordContext;
//import seg.train.WordContext;
import com.lietu.seg.utility.DicBigram;
import com.lietu.seg.utility.DicCore;
import com.lietu.seg.result.CnTokenizer;

import java.util.ArrayList;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;

/**
 * @author Administrator
 *
 * VSM model of a document
 * 
 * TODO: Koolim是另一個在線即時通訊服務器。它把一些著名的即時通訊服務商放在一起，如：AIM, Yahoo, MSN, Google Talk, ICQ等等。它與其他的一些在線即時通訊網站相同，如：Meebo, Ebuddy,Iloveim。特別適合有些人沒有下載軟件，和使用公用電腦。 
 * 修改 如 的分析規則
 * 發如雪
 */
public class CnTagMaker {

	/** The word list with score. */
	public static DicCore dicCore= DicCore.getInstance();
	public static CnPhraseDic phraseDic = CnPhraseDic.getInstance();
	private static Set stopSet=StopSet.getInstance();
	
	public static WordWeight[] GetTag(String name,
									String content,
									int retNum)
	{
		HashMap<KeyWord,Double> wordTable = new HashMap<KeyWord,Double>();
		java.lang.Double scoreNormalized;
		
		double weight;
		double count;
		int n=0;//words count
		ArrayList wordList= new ArrayList();
		String	word;
		WordContext item;
		Hashtable oneFreq = new Hashtable();
		String token1 = "始??始";
		String token2 = null;
		Hashtable biTable = new Hashtable();
		
    	StringReader input;
    	
    	input = new java.io.StringReader(content);
    	
    	CnTokenizer.segSZ=false;
    	CnTokenizer.segName=false;
    	
    	TokenStream tokenizer = new CnTokenizer(input);
    	//tokenizer = new StopFilter(tokenizer, stopSet);
    	
    	int offset =0;

    	try
    	{
    	for (Token t = tokenizer.next(); t != null; t = tokenizer.next())
    	{
    		n++;
			word = t.termText();
			wordList.add(word);
			if ("w".equals(t.type()) )
			{
				//System.out.println("t"+t.termText);
				if ("「".equals(t.termText()))
				{
					Token t1 = tokenizer.next();
					if ( t1 == null )
						continue;
					if( "」".equals(t1.termText()) )
					{
						continue;
					}
					else
					{
						 Token t2 = tokenizer.next();
						 if ( t2 == null )
							continue;
						 if ("」".equals(t2.termText()))
						 {
							//System.out.println("t1"+t1.termText());
							if( stopSet.contains(t1.termText()) )
							{
								continue;
							}
						 	java.lang.Double tempDouble = null;
						 	//System.out.println("t1 type:"+t1.termText());
						 	if(t1.type().startsWith("n")|| t1.type().startsWith("v"))
						 	{
						 		//System.out.println("t1"+t1.termText());
						 		tempDouble = new Double(100000000.0);
						 	}
						 	else
						 	{
						 		tempDouble = new Double(1);
						 	}
						 	wordTable.put(new KeyWord(t1.termText()), tempDouble);
						 }
						 else
						 {
							 Token t3 = tokenizer.next();
							 if ( t3 == null )
								continue;
							 //System.out.println("t3"+t3.termText);
							 if ("」".equals(t3.termText()))
							 {
								//System.out.println("t3:"+t3.termText());
							 	java.lang.Double tempDouble = new Double(100000000.0);
							 	wordTable.put(new KeyWord(t1.termText(),t2.termText()), tempDouble);
							 }
							 else
							 {
								 Token t4 = tokenizer.next();
								 if ( t4 == null )
									continue;
								 if ("」".equals(t4.termText()))
								 {
								 	java.lang.Double tempDouble = new Double(100000000.0);
								 	wordTable.put(new KeyWord(t1.termText(),t2.termText(),t3.termText()), tempDouble);
								 }
							 }
						 }
					}
					continue;
				}
				else
					continue;
			}
			else if( "m".equals(t.type()) || "t".equals(t.type()) )
			{
				continue;
			}
			else if( stopSet.contains(t.termText()) )
			{
				continue;
			}
			
			scoreNormalized = wordTable.get(new KeyWord(word));
			if("nx".equals(t.type()))
			{
				count = Math.log(dicCore.getAllFreq("未??專")+2);
				//System.out.println("專有名詞:"+word+":"+dicCore.getAllFreq("未??專"));
			}
			else if("nz".equals(t.type()))
			{
				int freq = dicCore.getAllFreq(word);
				if(freq<=0)
				{
					count = Math.log(dicCore.getAllFreq("未??專")+2);
				}
				else
				{
					count = Math.log(freq+2);
				}
				//System.out.println("專有名詞:"+word+":"+dicCore.getAllFreq("未??專"));
			}
			else if("nr".equals(t.type()))
			{
				int freq = dicCore.getAllFreq(word);
				if(freq<=0)
				{
					count = Math.log(dicCore.getAllFreq("未??人")+2);
				}
				else
				{
					count = Math.log(freq+2);
				}
				//System.out.println("專有名詞:"+word+":"+dicCore.getAllFreq("未??專"));
			}
			else
			{
				count = Math.log(dicCore.getAllFreq(word)+2);
			}
			double position = t.startOffset() / content.length();
			position = position * position - position +2;
			
			weight= position * 60000/(double)((count+1)*content.length());
			if ( scoreNormalized == null )
			{
				//normalize the data
				scoreNormalized = new java.lang.Double(weight);
				//System.out.println("not find:"+word);
			}
			else
			{
				scoreNormalized = new java.lang.Double(scoreNormalized.doubleValue() + weight);
			}
			//System.out.println("score "+word +" "+scoreNormalized+" "+t.type());
			wordTable.put(new KeyWord(word), scoreNormalized);
			
			//count freq
			item = (WordContext)oneFreq.get(t.termText());
			if (item != null)
			{
				item.freq++;
			}
			else
			{
				item = new WordContext();
				oneFreq.put(t.termText(),item);
			}
			token2 = t.termText();

			if (token2!= null && (! "始??始".equals(token1)) )
			{
				if (t.startOffset() == offset)
				{
					Bigrams bigram = new Bigrams(token1,token2);
					Object biItem = biTable.get(bigram);
					if (biItem != null)
					{
						((int[])biItem)[0]++;
					}
					else
					{
						int[] countArray = {1};
						biTable.put(bigram,countArray);
					}
					//System.out.println("add bigram");
				}
				/*else{
					System.out.println("t.startOffset()"+t.startOffset());
					System.out.println("offset "+offset);
				}*/
			}
			
			offset = t.endOffset();

			token1 = token2; // step forward
    	}
    	}catch(Exception e)
    	{
    		return null;
    	}
    	
		int start=0;
		int end=1;
		while(end<= wordList.size())
		{
			//System.out.println("start:"+start+" end"+end);
			
			String phrase2 = "";
			for(int i =start ;i<end ;++i)
			{
				phrase2 +=wordList.get(i);
			}
			//System.out.println("phrase2:"+phrase2);

			CnPhraseDic.Prefix phraseMatch = phraseDic.checkPrefix(wordList,start,end);
			if (phraseMatch == CnPhraseDic.Prefix.MisMatch)
			{
				++start;
				if (end<=start)
					++end;
			}
			else if (phraseMatch == CnPhraseDic.Prefix.Match)
			{
				String phrase = "";
				for(int i =start ;i<end ;++i)
				{
					phrase +=wordList.get(i);
				}
				//System.out.println("phrase:"+phrase);
				double freq = (Math.log(phraseDic.getFreq(wordList,start,end)));
				KeyWord phraseKey = new KeyWord(phrase);
				if ( wordTable.containsKey(phraseKey) )
				{
					Double oweight = (Double)wordTable.get(phraseKey);
					//System.out.println("phrase "+phrase +" oweight " + oweight);
					wordTable.remove(phrase);
					freq += oweight.doubleValue();
				}

				wordTable.put(phraseKey, new Double( freq));
				++end;
			}
			else if (phraseMatch == CnPhraseDic.Prefix.MatchPrefix)
			{
				//System.Console.WriteLine("match prefix");
				//System.Console.WriteLine("start:"+start+" end"+end);
				++end;
			}
		}
		
		//***********************************************/

	 	Enumeration elements, keys;
	 	
		keys = biTable.keys();
		elements = biTable.elements();
		int index = 0;
		BigramsContextCounts[] bigramsResults = new BigramsContextCounts[biTable.size()];
		Bigrams key;
		int freq1,freq2;
		double logn = Math.log((double)n);
		long temp;
		double entropy;
		int bigramCount;
		WordContext item1,item2;
		
		while(keys.hasMoreElements()){
			key = ((Bigrams)keys.nextElement());
			//System.out.println("key :"+key.toString()+" ");
			
			item1 = (WordContext)(oneFreq.get(key.one));
			item2 = (WordContext)(oneFreq.get(key.two));
			
			freq1 = item1.freq;
			freq2 = item2.freq;
			
			temp = (freq1*freq2);
			bigramCount = ((int[])elements.nextElement())[0];
			entropy = logn+Math.log((double)bigramCount/(double)temp);
			
			//System.out.println("temp :"+temp+" entropy:"+entropy);
			bigramsResults[index] = 
					new BigramsContextCounts(
							bigramCount,
							entropy,
							key.one,
							key.two);
			index++;
		}
		
		ArrayList<WordWeight> ngram= countBigram(bigramsResults,content,n,retNum);

		PairingHeap h = new PairingHeap();
		
		Set mappings = wordTable.entrySet();
		
		for (Iterator it = mappings.iterator(); it.hasNext();)
		{
			Map.Entry me = (Map.Entry)it.next();
			KeyWord keyWord = (KeyWord)me.getKey();
			java.lang.Double tempDouble;
			word = keyWord.toString();
			if( word.length() ==1)
			{
				tempDouble = new Double(0.0);
			}
			else
			{
				tempDouble = (java.lang.Double)me.getValue();
			}
			h.insert( new WordWeight(keyWord,tempDouble.doubleValue()) );
			//System.out.println("word:"+word+" weight:"+tempDouble.doubleValue());
		}
		
		for (int i=0; i<ngram.size();i++)
		{
			h.insert( ngram.get(i) );
		}
		
		retNum = Math.min(retNum,h.size());
		HashSet<String> means = new HashSet<String>();
		//WordWeight[] fullResults = new WordWeight[retNum];
		ArrayList<WordWeight> fullResults = new ArrayList<WordWeight>(retNum);
		int i=0;
	    
		while(fullResults.size()<retNum && !h.isEmpty())
		{
			WordWeight wordWeight = (WordWeight)h.deleteMin();
			
			if(means.contains(wordWeight.word.one))
			{
				continue;
			}
			if(wordWeight.word.two!=null && means.contains(wordWeight.word.two))
			{
				continue;
			}
			if(wordWeight.word.three!=null && means.contains(wordWeight.word.three))
			{
				continue;
			}
			fullResults.add(wordWeight);
			
			if(wordWeight.word.one!=null )
			{
				means.add(wordWeight.word.one);
			}
			if(wordWeight.word.two!=null )
			{
				means.add(wordWeight.word.two);
			}
			if(wordWeight.word.three!=null )
			{
				means.add(wordWeight.word.three);
			}
		}

		return fullResults.toArray(new WordWeight[fullResults.size()]);
		
		//WordWeight[] results = filter(fullResults);
		//return results;
	}
		
	/**
	 * collect the new words to database
	 * because the mount of candidate words 
	 * @return
	 */
	public static ArrayList<WordWeight> countBigram(BigramsContextCounts[] fullResults,
										String content,
										int n,
										int topK) {
		ArrayList<WordWeight> ret = new ArrayList<WordWeight>();
		BigramsContextCounts[] tempResults = new BigramsContextCounts[topK];
		int count =0;
		PairingHeap pq = new PairingHeap();
		
		for(int i=0; i < fullResults.length && count<topK; i++)
		{
			pq.insert(fullResults[i]);
		}
		
		//System.out.println("Results sorted by bigram count total words:"+n);
		int countFilter = (n/50);
		if (countFilter<2 )
			countFilter = 2;
		//System.out.println("min count:"+countFilter);
		for(int i=0; i < fullResults.length && count<topK; i++)
		{
			//System.out.println("all bi"+fullResults[i].toString());
			BigramsContextCounts bigger = (BigramsContextCounts)pq.deleteMin();
			if (bigger.count>=countFilter && bigger.entropy>2 )
			{
				tempResults[count++] = bigger;
				//System.out.println(bigger.toString());
			}
		}
		
		boolean add = true;
		//find trigram
		if (count>1)
		{
			if (tempResults[0].one.equals(tempResults[1].two))
			{
				//combine into one
				KeyWord trigram = new KeyWord( tempResults[1].one,tempResults[1].two,tempResults[0].two);
				if ( content.indexOf(trigram.toString())>=0 )
				{
					ret.add(new WordWeight(trigram,(tempResults[1].entropy+tempResults[0].entropy)*10000));
					//System.out.println("will add trigram "+trigram);
				
					add = false;
				}
			}
			else if (tempResults[1].one.equals(tempResults[0].two))
			{
				KeyWord trigram = new KeyWord(tempResults[0].one,tempResults[0].two,tempResults[1].two);
				
				if ( content.indexOf(trigram.toString())>=0 )
				{
					//should add to database
					ret.add(new WordWeight(trigram,(tempResults[1].entropy+tempResults[0].entropy)*100000));
					//System.out.println("will add trigram "+trigram);
					//System.out.println(newWord.toString());
					add = false;
				}
			}
		}
		
		if (add)
			{
				DicBigram dicBigram = DicBigram.getInstance();
				
				for(int i=0; i < count; i++)
				{
					//if is normal bigram
					if (dicBigram.isExist(tempResults[i].one,tempResults[i].two))
						continue;
					KeyWord bigram = new KeyWord(tempResults[i].one,tempResults[i].two);
					
					ret.add(new WordWeight(bigram,tempResults[i].entropy*100000));
					//System.out.println("will add bigram "+bigram);
					//System.out.println(newWord.toString());
				}
			}
		
		return ret;
	}
}

class WordContext {
	public int freq=1;
}
