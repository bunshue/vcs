#include "module_ve.h"
#include "module_ve_reg_map.h"
#include "tb_debug_ui.h"

#ifndef max
#define max(a,b)            (((a) > (b)) ? (a) : (b))
#endif

#ifndef min
#define min(a,b)            (((a) < (b)) ? (a) : (b))
#endif


ULONG clamp( ULONG input)
{
  if( input > 255)
    return 255;
  else
    return input;
}

//utility function implemented by right@20040703
inline ULONG ad(int a, int b)
{
	if(a > b)
		return a - b;
	else
		return b - a;
};

inline ULONG getAddress(ULONG base, ULONG horOffset, ULONG index)
{//give it a index, it will translate the proper address point to vmem
	ULONG address;
	ULONG pixelOffset = base & 0x7;
	 if( index >= (8 - pixelOffset))
		address = (base & 0xff8) 
						+ (index + pixelOffset) / 8 * horOffset + (index + pixelOffset) % 8;
	 else
		address = index + base;
	 return address;
};

inline ULONG getFactor(ULONG t1, ULONG t2, ULONG delta, ULONG sad, ULONG k1)
{//factor = f(SAD(in0, in1)) + k1
 // f() is a adapted function.
 // f() = 0 when SAD(in0, in1) <= t1
 // f() = 1 when SAD(in0, in1) > t2
 // f() is linear with (t1-t2) when else SAD(in0, in1)
 // here, sad = SAD(in0, in1) for generalization
 //Be careful with the "fraction" problem.
 //implemented by right@20040707
 if( k1 > 0x100)
 {
#ifndef VE_RELEASE
   cout << "k1 is too big!!\n";
#endif
   return 0x100;
 }
 if( sad <= t1)
	 return k1;
 else if( sad > t2)
	 return 0x100;
  else
  {
    if( (( ( (sad - t1) << 8) >> delta) ) + k1 > 0x100)
      return 0x100;
    else
      return (((sad - t1) << 8 >>  delta) ) + k1;
  }
}

inline int clip( int value, int min, int max)
{
  return (value>max)? max: ((value<min)?min: value);
}

// instruction functions

void module_ve::vsp_verfilt(ve_inst inst)       
{ 
#ifndef VE_RELEASE
  cout << "VE_VERFILT called and issued\n";
#endif
  //implemented by right @20040712
  //modified by right @20040719
  //modified by right @20040721
  //modified by right @20041004 upto VE_Spec0.67
  /***************************************************************************************************
    Vertical filtering.
    1. load data from vmem to inputVectorBlock.
    2. extend data from inputVectorBlock to postInputVectorBlock with rpt_top_line and rpt_bot_line.
    3. filtering.
    4. save data from outputVector to vmem.
  ****************************************************************************************************/
  int mode = GET_IMM_FIELD(inst.inst);
  
  ULONG evenInBase, oddInBase, outBase, inHorOffset, inVerOffset;
  ULONG outHorOffset, outVerOffset, inVerOffset1;
  evenInBase = reg_VE_BASEA[0].basea();
  oddInBase = reg_VE_BASEA[1].basea();
  outBase = reg_VE_BASEA[3].basea();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  outVerOffset = reg_VE_OFFSETA[3].offseta();
  if(mode == 0)
  {
	inHorOffset = reg_VE_OFFSETA[0].offseta();
	outHorOffset = reg_VE_OFFSETA[2].offseta();
	inVerOffset1 = 0;//no use
  }
  else
  {
	inHorOffset = reg_VE_OFFSETA[0].offseta();
	outVerOffset = reg_VE_OFFSETA[0].offseta();
	inVerOffset1 = reg_VE_OFFSETA[2].offseta();
  }
	  ULONG rptTopLine, rptBotLine;
	  rptTopLine = reg_VE_FILTCNTL.rpt_topline();
	  rptBotLine = reg_VE_FILTCNTL.rpt_botline();

	  ULONG tapNum, tapStart;
	  tapNum = reg_VE_FILTCNTL.tapnum() + 1;
	  tapStart = reg_VE_FILTCNTL.start_tap();

	  ULONG inputWidth, outputWidth, inputHeight, outputHeight, postInputHeight, postInputWidth;
	  outputWidth = GET_WIDTH(inst.par[0]) + 1;
	  outputHeight = GET_HEIGHT(inst.par[0]) + 1;
	  inputWidth = outputWidth;
	  inputHeight = outputHeight + tapNum - 1 - rptTopLine - rptBotLine;
	  postInputHeight = outputHeight + tapNum - 1;
	  postInputWidth = inputWidth;

	  ULONG *inputVectorBlock, *postInputVectorBlock, *outputVector;
	  postInputVectorBlock = (ULONG*)malloc(sizeof(ULONG) * postInputWidth * postInputHeight);
	  inputVectorBlock = (ULONG*)malloc(sizeof(ULONG) * inputWidth * inputHeight);
	  outputVector = (ULONG*)malloc(sizeof(ULONG) * outputHeight);

	  //{小數運算需要四捨五入. 利用 initValue 與 filtPrec達到四捨五入的結果.
	  ULONG initValue = reg_VE_FILTINIT.init_value();
	  if( (initValue & 0x80000) != 0)//negative value
	   initValue = (0xFFF00000 | initValue);//sign extension.
	  ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();
	  //}
#ifdef IMGBLK_DEBUG
	  debug_printf("evenInBase: %d, oddInBase: %d\n", evenInBase, oddInBase);
	  debug_printf("inputWidth: %d, inputHeight: %d\n", inputWidth, inputHeight);
	  debug_printf("inVerOffset: %d\n", inVerOffset);
	  debug_printf("outVerOffset: %d\n", outVerOffset);
	  debug_printf("inputHeight: %d\n", inputHeight);
	  debug_printf("outputHeight: %d\n", outputHeight);
	  debug_printf("tapNum: %d\n", tapNum);
#endif
	  /*check illegal parameters}*/

	  int i;
	  int coeff[16];
	  for(i = 0; i < tapNum/2; i++)
	  {//get coefficient tap.
		  coeff[2*i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();
		  coeff[2*i+1] = reg_VE_TAPCOEFF[i + tapStart].coeffnplus1();
	  }
	  if( (tapNum % 2) != 0)
		  coeff[2 * i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();
  
		for(int i = 0; i < inputHeight; i++)
		{//load data from vmem and merge even and odd to a fram picture.
		  for(int j = 0; j < inputWidth; j++)
		  {
			if((i % 2) == 0){
			*(inputVectorBlock + i * inputWidth + j) 
				= get_vmem(inst.tbank, getAddress(evenInBase + (i/2) * inVerOffset, inHorOffset, j));
			#ifdef MEMORY_MONITOR
		  	  if(CDebugUI::memory_r_monitor){
			sc_time st= sc_time_stamp();
			ULONG temp_t = (ULONG)st.to_default_time_units();
			fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",temp_t/SYSTEM_CLOCK_TIME,
			inst.tbank,inst.tbank*4096+getAddress(evenInBase + (i/2) * inVerOffset, inHorOffset, j),*(inputVectorBlock + i * inputWidth + j));
			
			  }
		  	  #endif

			}else{
			*(inputVectorBlock + i * inputWidth + j) 
				= get_vmem(inst.tbank, getAddress(oddInBase + (i/2) * inVerOffset, inHorOffset, j));

			#ifdef MEMORY_MONITOR
		  	  if(CDebugUI::memory_r_monitor){
			sc_time st= sc_time_stamp();
			ULONG temp_t = (ULONG)st.to_default_time_units();
			fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",temp_t/SYSTEM_CLOCK_TIME,
			inst.tbank,inst.tbank*4096+getAddress(oddInBase + (i/2) * inVerOffset, inHorOffset, j),*(inputVectorBlock + i * inputWidth + j));
			
			  }
		  	  #endif
			}
		  }
		}

		for(int i = 0; i < postInputHeight; i++)
		{//extend inputVectorBlock to postInputVectorBlock
		  for(int j = 0; j < postInputWidth; j++)
		  {
			if(i < rptTopLine)
			  *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + 0 * inputWidth + j);
			else if( i >= inputHeight + rptTopLine)
			  *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (inputHeight-1) * inputWidth + j);
			else
			  *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (i - rptTopLine) * inputWidth + j);
		  }
		}
		ULONG result;

		for(int i = 0; i < outputWidth; i++)
		{//filtering
		  for(int j = 0; j < outputHeight; j++)
		  {
			result = 0;
			for(int k = 0; k < tapNum; k++)
			{
	          result += coeff[k] * *(postInputVectorBlock + (j+k) * postInputWidth + i);
			}
		  //四捨五入
			outputVector[j] = result;
			outputVector[j] = (outputVector[j]  + initValue) >> (8 - filtPrec);
  
			//save data to vmem
			get_vmem(inst.tbank, getAddress(outBase + j * outVerOffset, outHorOffset, i)) 
			  = clamp( outputVector[j]);
			#ifdef MEMORY_MONITOR
	  	 	if(CDebugUI::memory_w_monitor){
			sc_time st= sc_time_stamp();
			ULONG temp_t = (ULONG)st.to_default_time_units();
		
			fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",temp_t/SYSTEM_CLOCK_TIME,
			inst.tbank,inst.tbank*4096+ getAddress(outBase + j * outVerOffset, outHorOffset, i) ,get_vmem(inst.tbank, getAddress(outBase + j * outVerOffset, outHorOffset, i)));
		

			}
			#endif
			

		  }
		}
		free(inputVectorBlock);
		free(postInputVectorBlock);
		free(outputVector);
		//for(int w = 0; w < (outputWidth / 8 * tapNum + 1) * outputHeight; w++)
		  ve_wait((outputWidth / 8 * tapNum + 1) * outputHeight); 
#ifndef VE_RELEASE
		debug_printf("verfilt done!\n");  
#endif
};
void module_ve::vsp_horfilt(ve_inst inst)       
{ 
#ifndef VE_RELEASE
  cout << "VE_HORFILT called and issued\n";
#endif
  //implemented by right @20040702
  /***********************************************************************
	  Horizontal filtering.
    1. load the "real" pixels from vmem to inputVector[]
    2. extend inputVector[] to postInputVector[] with rpt pixels
    3. filtering.
    4. store back to vmem.
  ***********************************************************************/
  ULONG oinBase, einBase, outBase, inHorOffset, inVerOffset, outHorOffset, outVerOffset;
  einBase = reg_VE_BASEA[0].basea();
  oinBase = reg_VE_BASEA[1].basea();
  outBase = reg_VE_BASEA[3].basea();
  inHorOffset = reg_VE_OFFSETA[0].offseta();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  outHorOffset = reg_VE_OFFSETA[2].offseta();
  outVerOffset = reg_VE_OFFSETA[3].offseta();
  ULONG outputWidth, outputHeight, inputWidth, inputHeight, rptRight, rptLeft, tapNum, tapStart;
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight =GET_HEIGHT(inst.par[0]) + 1;
  rptRight = reg_VE_FILTCNTL.rpt_rightpel();
  rptLeft = reg_VE_FILTCNTL.rpt_leftpel();
  tapNum = reg_VE_FILTCNTL.tapnum() + 1;
  tapStart = reg_VE_FILTCNTL.start_tap();

  //calculate the inputWidth
  inputWidth = outputWidth + tapNum - 1 - rptRight - rptLeft;
  inputHeight = outputHeight;

  ULONG *inputVector, *postInputVector, *outputVector;
  inputVector = (ULONG*) malloc(sizeof(ULONG) * inputWidth);
  postInputVector = (ULONG*) malloc(sizeof(ULONG) * (inputWidth + rptRight + rptLeft));
  outputVector = (ULONG*) malloc(sizeof(ULONG) * outputWidth);
  int coeff[16];
  //{小數運算需要四捨五入. 利用 initValue 與 filtPrec達到四捨五入的結果.
  ULONG initValue = reg_VE_FILTINIT.init_value();
  if( (initValue & 0x80000) != 0)//negative value
   initValue = (0xFFF00000 | initValue);//sign extension.
  ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();
  //}

  //{get coefficient tap
  int i = 0;
  for(i = 0; i < tapNum/2; i++)
  {
	  coeff[2*i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();
	  coeff[2*i+1] = reg_VE_TAPCOEFF[i + tapStart].coeffnplus1();
  }
  if( (tapNum % 2) != 0)
	  coeff[2 * i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();

#ifndef VE_RELEASE
  debug_printf("outputWidth: %d, inputWidth: %d\n", outputWidth, inputWidth);
#endif

  /*
  {check illegal parameters.
  */
  if( inputHeight <= 0)
  {
#ifndef VE_RELEASE
    debug_printf("illegal inputWidth: inputWidth: %d\n", inputWidth);
    debug_printf("\ttapNum: %d, outputWidth: %d, rptRight: %d, rptLeft: %d", 
                tapNum, outputWidth, rptRight, rptLeft);
#endif
    return;
  }
  /*check illegal parameters}*/


  ULONG addressIn, addressOut;
  for(int j = 0; j < outputHeight; j++)
  {
	  for(int i = 0; i < inputWidth; i++)
	  {//load data from vmem to inputVector
      if( i % 2 == 0)
		  addressIn = getAddress(einBase + j * inVerOffset / 2, inHorOffset, i);
      else
      addressIn = getAddress(oinBase + j * inVerOffset / 2, inHorOffset, i);
		  inputVector[i] = get_vmem(inst.tbank, addressIn);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addressIn,inputVector[i]);
		}
	  	#endif
			
	  }
	  for(int i = 0; i < inputWidth + rptRight + rptLeft; i++)
	  {//move data from inputVector to postInputVector;
		  if(i < rptLeft)//repeat left pels
			  postInputVector[i] = inputVector[0];
		  else if(i >= rptLeft + inputWidth)//repeat right pels
			  postInputVector[i] = inputVector[inputWidth - 1];
		  else
			  postInputVector[i] = inputVector[i - rptLeft];
      //debug_printf("in[%d]: %d\n", i, postInputVector[i]);
	  }
	  for(int i = 0; i < outputWidth; i++)
	  {//filtering
      outputVector[i] = 0;
      for(int k = 0; k < tapNum; k++)
        outputVector[i] += postInputVector[i+k] * coeff[k]  ;
      //四捨五入
      outputVector[i] = (outputVector[i]  + initValue) >> (8 - filtPrec);
      //debug_printf("out[%d]: %d\n", i, outputVector[i]);
    }
	  for(int i = 0; i < outputWidth; i++)
	  {//store data from outputVector to vmem
		  addressOut = getAddress(outBase + j * outVerOffset, outHorOffset, i);
		  get_vmem(inst.tbank, addressOut) = clamp( outputVector[i]);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addressOut,get_vmem(inst.tbank, addressOut));
		}
	  	#endif

	  }
  }
  free(inputVector);
  free(postInputVector);
  free(outputVector);
  //for(int w = 0; w <  ((outputWidth+7)/8*tapNum+1)*outputHeight + 5; w++)
    ve_wait(((outputWidth+7)/8*tapNum+1)*outputHeight + 5);
#ifndef VE_RELEASE
  debug_printf("VE_HORFILT done!\n");
#endif
};
void module_ve::vsp_hordec(ve_inst inst)        
{ 
#ifndef VE_RELEASE
  cout << "VE_HORDEC called and issued\n";
#endif
  // implemented by right@20040629
  // modified by right@20040803
  /*******************************************
  Decimate by 2 pixel in horizontal direction
  ********************************************/
 ULONG outputWidth, outputHeight, inputWidth, inputHeight;
 outputWidth = (GET_WIDTH(inst.par[0]) + 1);
 outputHeight = (GET_HEIGHT(inst.par[0]) + 1);
 inputWidth = 2 * outputWidth;
 inputHeight = outputHeight;

 ULONG inBase, outBase;
 ULONG pixelOffsetIn, pixelOffsetOut;
 inBase = reg_VE_BASEA[0].basea();
 pixelOffsetIn = inBase & 0x7;
 outBase = reg_VE_BASEA[3].basea();
 pixelOffsetOut = outBase & 0x7;

 ULONG inHorOffset, inVerOffset, outHorOffset, outVerOffset;
 inHorOffset = reg_VE_OFFSETA[0].offseta();
 inVerOffset = reg_VE_OFFSETA[1].offseta();
 outHorOffset = reg_VE_OFFSETA[2].offseta();
 outVerOffset = reg_VE_OFFSETA[3].offseta();
//{test
#ifndef VE_RELEASE
 debug_printf("inBase: %d\n", inBase);
 debug_printf("inHorOffset: %d\n", inHorOffset);
 debug_printf("inVerOffset: %d\n", inVerOffset);
 debug_printf("outBase: %d\n", outBase);
 debug_printf("outHorOffset: %d\n", outHorOffset);
 debug_printf("outVerOffset: %d\n", outVerOffset);
 debug_printf("Width: %d, Height: %d\n", outputWidth, outputHeight);
#endif
//}

  /*
  {check illegal parameters.
  */
  /*check illegal parameters}*/

 ULONG initValue = reg_VE_FILTINIT.init_value();
 if( (initValue & 0x80000) != 0)//negative value
	 initValue = (0xFFF00000 | initValue);
 ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

 ULONG addressIn, addressOut;
 ULONG i, j;
 ULONG *inputVector, *outputVector;
 inputVector = (ULONG*) malloc(sizeof(ULONG) * inputWidth);
 outputVector = (ULONG*) malloc(sizeof(ULONG) * outputWidth);
 for(j = 0; j < outputHeight; j++)
 {

	 for(i = 0; i < inputWidth; i++)
	 {//load data from vmem to local inputVector[]
     addressIn = getAddress(inBase + j * inVerOffset, inHorOffset, i);
		 inputVector[i] = get_vmem(inst.tbank, addressIn);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addressIn,inputVector[i]);
		}
	  	#endif

	 }
	 for(i = 0; i < outputWidth; i++)
	 {//decimation
		// (8 - filtprec) 表示小數點的位數. 所以先把pixel左移. 加上initValue, 再右移回來.再除二(right shift 1)
		 outputVector[i] = (((inputVector[i * 2] + inputVector[i * 2 + 1] ) << (8 - filtPrec)) 
							+ initValue) >> (1 + (8 - filtPrec));
	 }
	 for(i = 0; i < outputWidth; i++)
	 {//store data to vmem to local outputVector[]
     addressOut = getAddress(outBase + j * outVerOffset, outHorOffset, i);
     get_vmem(inst.tbank, addressOut) = clamp(outputVector[i]);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addressOut,get_vmem(inst.tbank, addressOut));
		}
	  	#endif
	 }
 }
 free(inputVector);
 free(outputVector);
 
 //for(int i = 0; i < (outputWidth+7)/8*outputHeight*3 ; i++)
   ve_wait( (outputWidth+7)/8*outputHeight*3 );
#ifndef VE_RELEASE
 debug_printf("Hordec done!\n");
#endif
};
void module_ve::vsp_decimate(ve_inst inst)      
{ 
#ifndef VE_RELEASE
  cout << "VE_DECIMATE called and issued\n";
#endif
// implemented by right@20040701
/***********************************************************
Decimate by 4 pixels
***********************************************************/
	ULONG evenInBase, oddInBase, outputBase;
	ULONG inHorOffset, inVerOffset, outHorOffset, outVerOffset;
	evenInBase = reg_VE_BASEA[0].basea();
	oddInBase = reg_VE_BASEA[1].basea();
	outputBase = reg_VE_BASEA[3].basea();
	inHorOffset = reg_VE_OFFSETA[0].offseta();
	inVerOffset = reg_VE_OFFSETA[1].offseta();
	outHorOffset = reg_VE_OFFSETA[2].offseta();
	outVerOffset = reg_VE_OFFSETA[3].offseta();

	ULONG inputWidth, inputHeight, outputWidth, outputHeight;
	outputWidth = GET_WIDTH(inst.par[0]) + 1;
	outputHeight = GET_HEIGHT(inst.par[0]) + 1;
	inputWidth = 2 * outputWidth;
	inputHeight = 2 * outputHeight;
	ULONG *inputVectorEven, *inputVectorOdd, *outputVector;
	inputVectorEven = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
	inputVectorOdd = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
	outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth);
	ULONG addressInEven, addressInOdd, addressOut;

	ULONG initValue = reg_VE_FILTINIT.init_value();
	if( (initValue & 0x80000) != 0)//negative value
	 initValue = (0xFFF00000 | initValue);
	ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();
//{test
#ifndef VE_RELEASE
 debug_printf("evenInBase: %d\n", evenInBase);
 debug_printf("oddInBase: %d\n", oddInBase);
 debug_printf("inHorOffset: %d\n", inHorOffset);
 debug_printf("inVerOffset: %d\n", inVerOffset);
 debug_printf("outBase: %d\n", outputBase);
 debug_printf("outHorOffset: %d\n", outHorOffset);
 debug_printf("outVerOffset: %d\n", outVerOffset);
 debug_printf("Width: %d, Height: %d\na", outputWidth, outputHeight);
#endif
//}
	
	for(int j = 0; j < outputHeight; j++)
	{
		for(int i = 0; i < inputWidth; i++)
		{//load data from vmem to local inputVectorEven[] and inputVectorOdd[]
     addressInEven = getAddress(evenInBase + j * inVerOffset, inHorOffset, i);
		 inputVectorEven[i] = get_vmem(inst.tbank, addressInEven);

     addressInOdd = getAddress(oddInBase + j * inVerOffset, inHorOffset, i);
		 inputVectorOdd[i] = get_vmem(inst.tbank, addressInOdd);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addressInEven,inputVectorEven[i]);
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addressInOdd,inputVectorOdd[i]);
		}
	  	#endif

     //debug_printf("even: %x, odd: %x\n", inputVectorEven[i], inputVectorOdd[i]);
		}
		for(int i = 0; i < outputWidth; i++)
		{//decimation
			outputVector[i] = (	((inputVectorEven[2*i] + inputVectorEven[2*i + 1] 
								+ inputVectorOdd[2*i] + inputVectorOdd[2*i +1]) << (8 - filtPrec)) + initValue
							) >> (2 + (8 - filtPrec));
		}
		for(int i = 0; i < outputWidth; i++)
		{//store data from local outputVector[] to vmem
     addressOut = getAddress(outputBase + j * outVerOffset, outHorOffset, i);
		 get_vmem(inst.tbank, addressOut) = clamp( outputVector[i]);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addressOut,get_vmem(inst.tbank, addressOut));
		
		}
	  	#endif
		 //debug_printf("output[i]: %x\n", outputVector[i]);	
		}
	}
	free(inputVectorEven);
	free(inputVectorOdd);
	free(outputVector);
  //for(int w = 0; w < (outputWidth+7)/8*outputHeight*5 + 5; w++)
    ve_wait((outputWidth+7)/8*outputHeight*5 + 5);
};
void module_ve::vsp_horint(ve_inst inst)        
{ 
#ifndef VE_RELEASE
  cout << "VE_HORINT called and issued\n";
#endif
  // implemented by right@20040705
  /******************************************************************************
	  Horizontal interpoation.
  *******************************************************************************/
  ULONG inBase, outBase, inputWidth, outputWidth, inputHeight, outputHeight;
  inBase = reg_VE_BASEA[0].basea();
  outBase = reg_VE_BASEA[3].basea();
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight = GET_HEIGHT(inst.par[0]) + 1;
  inputWidth = outputWidth / 2;
  inputHeight = outputHeight;

  ULONG inHorOffset, inVerOffset, outHorOffset, outVerOffset;
  inHorOffset = reg_VE_OFFSETA[0].offseta();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  outHorOffset = reg_VE_OFFSETA[2].offseta();
  outVerOffset = reg_VE_OFFSETA[3].offseta();

  ULONG *inputVector, *outputVector;
  inputVector = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
  outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth);

  ULONG initValue = reg_VE_FILTINIT.init_value();
  if( (initValue & 0x80000) != 0)//negative value
   initValue = (0xFFF00000 | initValue);
  ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

#ifndef VE_RELEASE
  debug_printf("inputWidth: %d, outputWidth: %d\n", inputWidth, outputWidth);
#endif

  for(int i = 0; i < outputHeight; i++)
  {
	  for(int j = 0; j < inputWidth; j++)
	  {//load data from vmem to inputVector[]
		  inputVector[j] = get_vmem( inst.tbank, getAddress(inBase, inHorOffset, j));
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(inBase, inHorOffset, j),inputVector[j]);
		
		}
	  	#endif
	  }
	  for(int j = 0; j < outputWidth; j++)
	  {//interpolation
		  if( j == outputWidth - 1)
			  outputVector[j] = inputVector[j / 2]; //duplicate the last one.
		  else if( (j % 2) == 0)
			  outputVector[j] = inputVector[j/2];
		  else
			  outputVector[j] = (((inputVector[j/2] + inputVector[j/2 + 1]) << (8 - filtPrec)) + initValue)
								  >> ( 1 + (8 - filtPrec));
	  }
	  for(int j = 0; j < outputWidth; j++)
	  {//store data from outputVector to vmem
      get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = 0xff & outputVector[j];
	#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)));
		
		}
	  	#endif
	  }
	  inBase += inVerOffset;
	  outBase += outVerOffset;
  }
  free(inputVector);
  free(outputVector);  
  //for(int w = 0; w < (outputWidth+7)/8*outputHeight*1.5 + 5; w++)
    ve_wait((outputWidth+7)/8*outputHeight*3/2 + 5);
};

void module_ve::vsp_horint2(ve_inst inst)       
{ 
#ifndef VE_RELEASE
  cout << "VE_HORINT2 called and issued\n";
#endif
// implemented by right@20040703
/**************************************************************************************
	Duplicate pixels
***************************************************************************************/
ULONG inBase, outBase, inputWidth, outputWidth, inputHeight, outputHeight;
inBase = reg_VE_BASEA[0].basea();
outBase = reg_VE_BASEA[3].basea();
outputWidth = GET_WIDTH(inst.par[0]) + 1;
outputHeight = GET_HEIGHT(inst.par[0]) + 1;
inputWidth = outputWidth / 2;
inputHeight = outputHeight;

ULONG inHorOffset, inVerOffset, outHorOffset, outVerOffset;
inHorOffset = reg_VE_OFFSETA[0].offseta();
inVerOffset = reg_VE_OFFSETA[1].offseta();
outHorOffset = reg_VE_OFFSETA[2].offseta();
outVerOffset = reg_VE_OFFSETA[3].offseta();

ULONG *inputVector, *outputVector;
inputVector = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth);

ULONG initValue = reg_VE_FILTINIT.init_value();
if( (initValue & 0x80000) != 0)//negative value
 initValue = (0xFFF00000 | initValue);
ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

for(int i = 0; i < outputHeight; i++)
{
	for(int j = 0; j < inputWidth; j++)
	{//load data from vmem to inputVector[]
		inputVector[j] = vmem[inst.tbank][getAddress(inBase, inHorOffset, j)];
	}
	for(int j = 0; j < outputWidth; j++)
	{//duplication
		outputVector[j] = inputVector[j / 2];
	}
	for(int j = 0; j < outputWidth; j++)
	{//store data from outputVector to vmem
    get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = 0xff & outputVector[j];
	#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)));
		
		}
	  	#endif


//		vmem[inst.tbank][getAddress(outBase, outHorOffset, j)] = outputVector[j];
	}
	inBase +=  inVerOffset;
	outBase += outVerOffset;
}
free(inputVector);
free(outputVector);
//for(int w = 0; w <(outputWidth+7)/8*outputHeight*1.5 + 5; w++)
  ve_wait((outputWidth+7)/8*outputHeight*3/2 + 5);
}
void module_ve::vsp_alpha(ve_inst inst)         
{ 
#ifndef VE_RELEASE
  cout << "VE_ALPHA called and issued\n";
#endif
  //implemented by right@20040703
  /********************************************************************************
	  Alpha mixing of two block with a constant alpha specified in the VE_ALPHA.
	  Out = alpha * In0 + (1 - alpha) * In1
  *********************************************************************************/
  ULONG inBase0, inBase1, outBase, in0HorOffset, in1HorOffset, in0VerOffset, in1VerOffset, outHorOffset, outVerOffset;
  inBase0 = reg_VE_BASEA[0].basea();
  inBase1 = reg_VE_BASEA[1].basea();
  outBase = reg_VE_BASEA[3].basea();
  in0HorOffset = reg_VE_OFFSETA[0].offseta();
  in0VerOffset = reg_VE_OFFSETA[1].offseta();
  in1HorOffset = in0HorOffset;
  in1VerOffset = in0VerOffset;
  outHorOffset = reg_VE_OFFSETA[2].offseta();
  outVerOffset = reg_VE_OFFSETA[3].offseta();

  ULONG inputWidth, inputHeight, outputWidth, outputHeight;
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight = GET_HEIGHT(inst.par[0]) + 1;
  inputWidth = outputWidth;
  inputHeight = outputHeight;

  ULONG initValue = reg_VE_FILTINIT.init_value();
  initValue = (initValue << 12) >> 12;
/*
  if( (initValue & 0x80000) != 0)//negative value
   initValue = (0xFFF00000 | initValue);
*/
  ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

  ULONG alpha;
  alpha = reg_VE_ALPHA.alpha();

  for(int j = 0; j < outputHeight; j++)
  {
	  for(int i = 0; i < outputWidth; i++)
	  {// alpha < 1; so, we need shift them all for accumulation.
      get_vmem(inst.tbank, getAddress(outBase, outHorOffset, i))
        = ((get_vmem(inst.tbank, getAddress(inBase0, in0HorOffset, i)) * alpha
          + get_vmem(inst.tbank, getAddress(inBase1, in1HorOffset, i)) * ((1 << 8) - alpha))
          + (initValue << filtPrec)) >> 8;
		
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(inBase0, in0HorOffset, i),get_vmem(inst.tbank, getAddress(inBase0, in0HorOffset, i)));
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(inBase1, in1HorOffset, i),get_vmem(inst.tbank, getAddress(inBase1, in1HorOffset, i)));
		

		}
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, i),get_vmem(inst.tbank, getAddress(outBase, outHorOffset, i)));
		
		}
	  	#endif

	  }
	  inBase0 += in0VerOffset;
	  inBase1 += in1VerOffset;
	  outBase += outVerOffset;
  }
  //for(int w = 0; w < outputWidth/8*outputHeight*3 + 5; w++)
    ve_wait(outputWidth/8*outputHeight*3 + 5);
};
void module_ve::vsp_adapfilt(ve_inst inst)      
{ 
#ifndef VE_RELEASE
  cout << "VE_ADAPFILT called and issued\n";
#endif
// implemented by right@20040705
/***************************************************************************************
	adaption filtering.
****************************************************************************************/
ULONG in0Base, in1Base, in0HorOffset, in1HorOffset, in0VerOffset, in1VerOffset;
ULONG outBase, outHorOffset, outVerOffset;
in0Base = reg_VE_BASEA[0].basea();
in1Base = reg_VE_BASEA[1].basea();
outBase = reg_VE_BASEA[3].basea();
in0HorOffset = reg_VE_OFFSETA[0].offseta();
in1HorOffset = in0HorOffset;
in0VerOffset = reg_VE_OFFSETA[1].offseta();
in1VerOffset = in0VerOffset;
outHorOffset = reg_VE_OFFSETA[2].offseta();
outVerOffset = reg_VE_OFFSETA[3].offseta();

ULONG inputWidth, outputWidth, inputHeight, outputHeight;
outputWidth = GET_WIDTH(inst.par[0]) + 1;
outputHeight = GET_HEIGHT(inst.par[0]) + 1;
inputWidth = outputWidth;
inputHeight = outputHeight;

ULONG *input0Vector, *input1Vector, *outputVector;
input0Vector = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
input1Vector = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth);

ULONG initValue = reg_VE_FILTINIT.init_value();
if( (initValue & 0x80000) != 0)//negative value
 initValue = (0xFFF00000 | initValue);
ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

ULONG k1, t1, rshift_size, t2;
k1 = reg_VE_ADAPCNTL.k1();
t1 = reg_VE_ADAPCNTL.t1();
t2 = reg_VE_ADAPCNTL.t2();//modified by VE_Spec0.65
rshift_size = reg_VE_ADAPCNTL.rshift_size();

ULONG iDiff = 0;
for(int i = 0; i < outputHeight; i++)
{
	for(int j = 0; j < inputWidth; j++)
	{//load data from vmem to inputVector
		input0Vector[j] = get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j));
 		input1Vector[j] = get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j));
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in0Base, in0HorOffset, j),input0Vector[j]);
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in1Base, in1HorOffset, j),input1Vector[j]);
		

		}
	  	#endif

	}
	for(int j = 0; j < outputWidth; j++)
	{//adapted filtering
//		debug_printf("width: %d, height: %d\n", j, i);
		if( input0Vector[j] > input1Vector[j])
		{
			iDiff = input0Vector[j] - input1Vector[j];
			outputVector[j] = 
				(
				( 
				(input1Vector[j] << 8) + 
				getFactor(t1, t2, t2 - t1, iDiff, k1) * iDiff + 
				(initValue << filtPrec)
				) >> 8
				) & 0xff;
#ifndef VE_RELEASE
		debug_printf("iDiff: %d, factor: %d, outputVector[%d]: %d\n", 
			iDiff, getFactor(t1, t2, t2 - t1, iDiff, k1), j, outputVector[j]);
#endif
		}
		else
		{
			iDiff = input1Vector[j] - input0Vector[j];
			outputVector[j] = (((input1Vector[j] << 8) - 
				getFactor(t1, t2, t2 - t1, iDiff, k1) * (input1Vector[j] - input0Vector[j])
        + (initValue << filtPrec)) >> 8) & 0xff;
#ifndef VE_RELEASE
		debug_printf("iDiff: %d, factor: %d, outputVector[%d]: %d\n", 
			iDiff, getFactor(t1, t2, t2 - t1, iDiff, k1), j, outputVector[j]);
#endif
		}
		get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = outputVector[j];
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),outputVector[j]);
		
		

		}
	  	#endif
	}
/*
	for(int j = 0; j < outputWidth; j++)
	{//store data from outputWidth to vmeme
		get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = outputVector[j];
	}

*/
	in0Base += in0VerOffset;
	in1Base += in1VerOffset;
	outBase += outVerOffset;
}

	//for(int w = 0; w < outputWidth/8*outputHeight*3 + 5; w++)
    ve_wait(outputWidth/8*outputHeight*3 + 5);
};

void module_ve::vsp_adapfilt1x3(ve_inst inst)   
{ 
#ifndef VE_RELEASE
  cout << "VE_ADAPFILT1X3 called and issued\n";
#endif
// implemented by right@20040707
/***********************************************************************************************
	1x3 nonlinear adapted filtering
************************************************************************************************/
ULONG in0Base, in1Base, outBase, in0HorOffset, in0VerOffset, in1HorOffset, in1VerOffset,outHorOffset, outVerOffset;
in0Base = reg_VE_BASEA[0].basea();
in1Base = reg_VE_BASEA[1].basea();
outBase = reg_VE_BASEA[3].basea();
in0HorOffset = reg_VE_OFFSETA[0].offseta();
in1HorOffset = in0HorOffset;
in0VerOffset = reg_VE_OFFSETA[1].offseta();
in1VerOffset = in0VerOffset;
outHorOffset = reg_VE_OFFSETA[2].offseta();
outVerOffset = reg_VE_OFFSETA[3].offseta();

ULONG outputWidth, outputHeight, inputWidth, inputHeight;
outputWidth = GET_WIDTH(inst.par[0]) + 1;
outputHeight = GET_HEIGHT(inst.par[0]) + 1;
inputWidth = outputWidth;
inputHeight = outputHeight;

ULONG *input0Vector, *input1Vector, *outputVector;
input0Vector = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
input1Vector = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth);
ULONG sad, t1, t2, k1;
t1 = reg_VE_ADAPCNTL.t1();
k1 = reg_VE_ADAPCNTL.k1();
t2 = reg_VE_ADAPCNTL.t2();


for( int i = 0; i < outputHeight; i++)
{
	for(int j = 0; j < inputWidth; j++)
	{//load data from vmem to inputVector[]
		input0Vector[j] = get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j));
		input1Vector[j] = get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j));
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in0Base, in0HorOffset, j),input0Vector[j]);
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in1Base, in1HorOffset, j),input1Vector[j]);
		

		}
	  	#endif

	}
	for(int j = 0; j < outputWidth; j++)
	{
		if( j == 0)
		{//duplicate current pixel for left
			sad = ( (ad(input0Vector[j], input1Vector[j]) << 1) + 
					ad(input0Vector[j+1], input0Vector[j+1])) >> 2;
		}
		else if( j == outputWidth - 1)
		{//duplicate current pixel for right
			sad = (ad(input0Vector[j-1], input1Vector[j-1]) + 
					(ad(input0Vector[j], input0Vector[j]) << 1)) >> 2;
		}
		else
		{
			sad = (ad(input0Vector[j-1], input1Vector[j-1]) + 
					ad(input0Vector[j], input1Vector[j]) + 
					ad(input0Vector[j+1], input0Vector[j+1])) >> 2;
		}
		if( input0Vector[j] > input1Vector[j])
			outputVector[j] = input1Vector[j] + 
				(( getFactor(t1, t2, t2 - t1, sad, k1) * (input0Vector[j] - input1Vector[j]) ) >> 8);
		else
			outputVector[j] = input1Vector[j] -
				(( getFactor(t1, t2, t2 - t1, sad, k1) * (input1Vector[j] - input0Vector[j]) ) >> 8);
	}
	for(int j = 0; j < outputWidth; j++)
	{//store data to vmem
		get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = outputVector[j];
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),outputVector[j]);
				

		}
	  	#endif
		
	}
	in0Base += in0VerOffset;
	in1Base += in1VerOffset;
	outBase += outVerOffset;
}
  //for(int w = 0; w < outputWidth/8*outputHeight*3 + 5; w++)
    ve_wait(outputWidth/8*outputHeight*3 + 5);
};
void module_ve::vsp_verfiltm(ve_inst inst)      
{ 
#ifndef VE_RELEASE
  cout << "VE_VERFILTM called and issued\n";
#endif
// implemented by right@ 20040716
// modified by right @20040721
/***************************************************************************************************
  Vertical filtering in mirror mode.
  1. load data from vmem to inputVectorBlock.
  2. extend data from inputVectorBlock to postInputVectorBlock with rpt_top_line and rpt_bot_line.
  3. filtering.
  4. save data from outputVector to vmem.
****************************************************************************************************/
  ULONG evenInBase, oddInBase, outBase, inHorOffset, inVerOffset;
  ULONG outHorOffset, outVerOffset;
  evenInBase = reg_VE_BASEA[0].basea();
  oddInBase = reg_VE_BASEA[1].basea();
  outBase = reg_VE_BASEA[3].basea();
  inHorOffset = reg_VE_OFFSETA[0].offseta();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  outHorOffset = inHorOffset;
  outVerOffset = reg_VE_OFFSETA[3].offseta();

  ULONG rptTopLine, rptBotLine;
  rptTopLine = reg_VE_FILTCNTL.rpt_topline();
  rptBotLine = reg_VE_FILTCNTL.rpt_botline();

  ULONG tapNum, tapStart;
  tapNum = reg_VE_FILTCNTL.tapnum() + 1;
  tapStart = reg_VE_FILTCNTL.start_tap();

  ULONG inputWidth, outputWidth, inputHeight, outputHeight, postInputHeight, postInputWidth;
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight = GET_HEIGHT(inst.par[0]) + 1;
  inputWidth = outputWidth;
  inputHeight = outputHeight + tapNum - 1 - rptTopLine - rptBotLine;
  postInputHeight = outputHeight + tapNum - 1;
  postInputWidth = inputWidth;

  ULONG *inputVectorBlock, *postInputVectorBlock, *outputVector;
  postInputVectorBlock = (ULONG*)malloc(sizeof(ULONG) * postInputWidth * postInputHeight);
  inputVectorBlock = (ULONG*)malloc(sizeof(ULONG) * inputWidth * inputHeight);
  outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth);

  //{小數運算需要四捨五入. 利用 initValue 與 filtPrec達到四捨五入的結果.
  ULONG initValue = reg_VE_FILTINIT.init_value();
  if( (initValue & 0x80000) != 0)//negative value
   initValue = (0xFFF00000 | initValue);//sign extension.
  ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();
  //}
  
  int i;
  ULONG coeff[16];
  for(i = 0; i < tapNum/2; i++)
  {//get coefficient tap.
	  coeff[2*i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();
	  coeff[2*i+1] = reg_VE_TAPCOEFF[i + tapStart].coeffnplus1();
  }
  if( (tapNum % 2) != 0)
	  coeff[2 * i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();

    for(int i = 0; i < (inputHeight/2); i++)
    {//load data from vmem and merge even and odd to a fram picture.
      for(int j = 0; j < inputWidth; j++)
      {
        *(inputVectorBlock + 2 * i * inputWidth + j) 
            = get_vmem(inst.tbank, getAddress(evenInBase + i * inVerOffset, inHorOffset, j));

        *(inputVectorBlock + (2 * i + 1) * inputWidth + j) 
            = get_vmem(inst.tbank, getAddress(oddInBase + i * inVerOffset, inHorOffset, j));
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(evenInBase + i * inVerOffset, inHorOffset, j),get_vmem(inst.tbank, getAddress(evenInBase + i * inVerOffset, inHorOffset, j)));

		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(oddInBase + i * inVerOffset, inHorOffset, j),get_vmem(inst.tbank, getAddress(oddInBase + i * inVerOffset, inHorOffset, j)));
				

		}
	  	#endif

      }
    }
    for(int i = 0; i < postInputHeight; i++)
    {//extend inputVectorBlock to postInputVectorBlock
      for(int j = 0; j < postInputWidth; j++)
      {
        if(i < rptTopLine)//top lines
          *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (rptTopLine - 1 - i) * inputWidth + j);
        else if( i >= inputHeight + rptTopLine)//bottom lines
          *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (inputHeight - 1 - (i - inputHeight - rptTopLine)) * inputWidth + j);
        else//normol case
          *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (i - rptTopLine) * inputWidth + j);
      }
    }
    ULONG result;
    for(int i = 0; i < outputWidth; i++)
    {//filtering
      for(int j = 0; j < outputHeight; j++)
      {
//        debug_printf("(width: %d, height: %d\n", i, j);
        result = 0;
        for(int k = 0; k < tapNum; k++)
          result += coeff[k] * *(postInputVectorBlock + (j+k) * postInputWidth + i);
      //四捨五入
        outputVector[j] = result;
        outputVector[j] = (outputVector[j]  + initValue) >> (8 - filtPrec);
    
        //save data to vmem
        get_vmem(inst.tbank, getAddress(outBase + j * outVerOffset, outHorOffset, i)) 
          = 0xff & outputVector[j];
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase + j * outVerOffset, outHorOffset, i),get_vmem(inst.tbank, getAddress(outBase + j * outVerOffset, outHorOffset, i)));

		

		}
	  	#endif
      if(j == 7)
      {
        printf("\n result: %d\n", outputVector[j] & 0xff);
        printf("postInputVector[%d:%d]: %d, %d, %d, %d\n", 7, 10, 
          postInputVectorBlock[7*postInputWidth + i]
          , postInputVectorBlock[8*postInputWidth + i]
          , postInputVectorBlock[9*postInputWidth + i]
          , postInputVectorBlock[10*postInputWidth + i]);
      }
      }
    }
    free(inputVectorBlock);
    free(postInputVectorBlock);
    free(outputVector);
    //for(int w = 0; w < ((outputWidth/8)*tapNum+1)*outputHeight + 10; w++)
      ve_wait(((outputWidth/8)*tapNum+1)*outputHeight + 10);
};

void module_ve::vsp_horfiltm(ve_inst inst)      
{ 
#ifndef VE_RELEASE
  cout << "VE_HORFILTM called and issued\n";
#endif
//implemented by right@ 20040716
ULONG inBase, outBase, inHorOffset, inVerOffset, outHorOffset, outVerOffset;
inBase = reg_VE_BASEA[0].basea();
outBase = reg_VE_BASEA[3].basea();
inHorOffset = reg_VE_OFFSETA[0].offseta();
inVerOffset = reg_VE_OFFSETA[1].offseta();
outHorOffset = reg_VE_OFFSETA[2].offseta();
outVerOffset = reg_VE_OFFSETA[3].offseta();

int rptRightPel, rptLeftPel, tapNum, tapStart;
rptRightPel = reg_VE_FILTCNTL.rpt_rightpel();
rptLeftPel = reg_VE_FILTCNTL.rpt_leftpel();
tapNum = reg_VE_FILTCNTL.tapnum() + 1;
tapStart = reg_VE_FILTCNTL.start_tap();

int inputWidth, inputHeight, outputWidth, outputHeight, mode, postInputWidth;
mode = GET_IMM_FIELD(inst.inst);
if(mode == 0)
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
else if(mode == 1 || mode == 2)
  outputWidth = (GET_WIDTH(inst.par[0]) + 1) * 2;
inputWidth = GET_WIDTH(inst.par[0]) + 2 ;
postInputWidth = inputWidth + rptRightPel + rptLeftPel;
outputHeight = GET_HEIGHT(inst.par[0]) + 1;
inputHeight = outputHeight;

//get initial value and filt_prec
ULONG initValue = reg_VE_FILTINIT.init_value();
if( (initValue & 0x80000) != 0)//negative value
 initValue = (0xFFF00000 | initValue);
ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

//get coefficient tap
ULONG coeff[16];
int i = 0;
for(i = 0; i < tapNum/2; i++)
{
	coeff[2*i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();
	coeff[2*i+1] = reg_VE_TAPCOEFF[i + tapStart].coeffnplus1();
}
if( (tapNum % 2) != 0)
	coeff[2 * i] = reg_VE_TAPCOEFF[i + tapStart].coeffn();

ULONG *postInputVector, *outputVector, *inputVector;
inputVector = (ULONG*)malloc(sizeof(ULONG) * inputWidth);
postInputVector = (ULONG*)malloc(sizeof(ULONG) * postInputWidth);
outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth);
for(int i = 0; i < outputHeight; i++)
{
  for(int j = 0; j < inputWidth; j++)
  {//load real pixel from vmem to inputVector
    inputVector[j] = get_vmem(inst.tbank, getAddress(inBase, inHorOffset, j));
   		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(inBase, inHorOffset, j),inputVector[j]);

		

		}
	  	#endif

  }
  for(int j = 0; j < postInputWidth; j++)
  {//extending
    if(j < rptLeftPel)
      postInputVector[j] = inputVector[rptLeftPel - 1 - j];
    else if( j >= inputWidth + rptLeftPel)
      postInputVector[j] = inputVector[inputWidth + rptLeftPel - 1 - (j - (inputWidth + rptLeftPel) )];
    else
      postInputVector[j] = inputVector[j - rptLeftPel];
  }
  for(int j = 0; j < GET_WIDTH(inst.par[0]) + 1; j++)//the width always be "M".
  {//filtering
    outputVector[j] = 0;
    for(int k = 0; k < tapNum; k++)
        outputVector[j] += postInputVector[j+k] * coeff[j];
    outputVector[j] = ((outputVector[j] << (8 - filtPrec)) + initValue) >> (8 - filtPrec);
  }
  if( mode == 0)
    for(int j = 0;j < outputWidth; j++)
    {//store data from outputVector to vmem
        get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = outputVector[j];
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),outputVector[j]);

		

		}
	  	#endif
    
    }
  else if( mode == 1)
    for(int j = 0; j < outputWidth; j++)
    {//store data from outputVector to vmem
        if(j % 2 == 0){
          get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = inputVector[j/2];
	  	#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),inputVector[j/2]);

		}
	  	#endif
        }else{
          get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = outputVector[j/2];
	  #ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),outputVector[j/2]);

		}
	  	#endif
	}
    }
  else if( mode == 2)
    for(int j = 0; j < outputWidth; j++)
    {//store data from outputVector to vmem
      if(j % 2 == 0){
        get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = outputVector[j/2];
	#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),outputVector[j/2]);

		}
	  	#endif
      }else{
        get_vmem(inst.tbank, getAddress(outBase, outHorOffset, j)) = inputVector[j/2 + 1];
	#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_w_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase, outHorOffset, j),inputVector[j/2 + 1]);

		}
	  	#endif
      }
    }
  inBase += inVerOffset;
  outBase += outHorOffset;
}
  //for(int w = 0; w < ((outputWidth+7)/8*tapNum+1)*outputHeight + 10; w++)
    ve_wait(((outputWidth+7)/8*tapNum+1)*outputHeight + 10);
};
int filterModeDecision(int th1, int th2, ULONG v[])
{
	enum filterMode_e
	{
		DEFAULT_MODE = 0,
		DC_MODE
	};
	filterMode_e filterMode = DEFAULT_MODE;
	int eq_cnt = 0;
	for( int i = 0; i < 9; i++)
	{
		if( ad(v[i], v[i+1]) <= th1)
			eq_cnt +=1;
	}
	if( eq_cnt >= th2)
		filterMode = DC_MODE;
	return filterMode;
};
void deblock_filter(ULONG output[], ULONG v[], int filter_mode, ULONG qp)
{
	for(int i = 0; i < 8; i++)
		output[i] = 0;

	enum filterMode_e
	{
		DEFAULT_MODE = 0,
		DC_MODE
	};
	if( filter_mode == DEFAULT_MODE)
	{ // DEFAULT MODE
		int d, aa30, a30, a31, a32;
		a30 = 2 * v[3] + (-5) * v[4] + 5 * v[5] + (-2) * v[6];
		//rounding
		a30 = (a30 + 4) >> 3;

		a31 = 2 * v[1] - 5 * v[2] + 5 * v[3] - 2 * v[4];
		//rounding
		a31 = (a31 + 4) >> 3;

		a32 = 2 * v[5] - 5 * v[6] + 5 * v[7] - 2 * v[8];
		//rounding
		a32 = (a32 + 4) >> 3;

		aa30 = (0x80000000 & a30) | min( min( abs(a30), abs(a31)), abs(a32));
		int delta = 0;
		if( abs(a30) < qp)
			delta = 1;
		else
			delta = 0;

		int tmp = 0;
		tmp = 5 * (aa30 - a30);
		tmp = (tmp + 4) >> 3;

		d = clip(tmp, 0, (v[4] - v[5]) / 2 * delta);
		
		output[4] = v[4] - d;
		output[5] = v[5] + d;
		
	}
	else
	{// DC OFFSET MODE
		int max = max( max( max( max( max( max( max(v[1], v[2]), v[3]), v[4]), v[5]), v[6]), v[7]), v[8]);
		int min = min( min( min( min( min( min( min(v[1], v[2]), v[3]), v[4]), v[5]), v[6]), v[7]), v[8]);
		if( abs(max - min) < 2 * qp)
		{
			ULONG p[10];
			p[0] = (abs(v[1] - v[0]) < qp) ? v[0] : v[1];
			p[9] = (abs(v[8] - v[9]) < qp) ? v[9] : v[8];
			for(int i = 0; i < 8; i++)
				p[i + 1] = v[i + 1];
			int b[9] = {1, 1, 2, 2, 4, 2, 2, 1, 1};
			for(int n = 1; n < 8; n++)
			{
				for(int k = -4; k <=4; k++)
				{
					if( n + k < 1)
						output[n - 1] += b[k + 4] * p[0];
					else if( (n + k) > 8 )
						output[n - 1] += b[k + 4] * p[9];
					else
						output[n - 1] += b[k + 4] * p[n + k];
				}
				output[n - 1] = (output[n - 1] + 8) >> 4;
			}
			
		}
		else
		{
			for(int i = 0; i < 8; i++)
			output[i] = v[i + 1];
		}
	}
};

void module_ve::vsp_deblock(ve_inst inst)       
{ 
#ifndef VE_RELEASE
  cout << "VE_DEBLOCK called and issued\n";
#endif
  ULONG currentBlockBase, upperLeftBlockBase, upperBlockBase, leftBlockBase;
  currentBlockBase = reg_VE_BASEA[0].basea();
  upperLeftBlockBase = currentBlockBase + reg_VE_OFFSETA[1].offseta();
  upperBlockBase = currentBlockBase + reg_VE_OFFSETA[2].offseta();
  leftBlockBase = currentBlockBase + reg_VE_OFFSETA[3].offseta();

  ULONG qp, qp0, qp1, blkMode;
  int th1, th2;
  qp0 = inst.par[0] & 0x1F;
  qp1 = (inst.par[0] >> 8) & 0x1F;
  blkMode = GET_IMM_FIELD(inst.inst);
  th1 = reg_VE_DEBLKCNTL.thr_1();
  th2 = reg_VE_DEBLKCNTL.thr_2();
#ifndef VE_RELEASE
  debug_printf("par[0]: %d, par[1]: %d\n", inst.par[0], inst.par[1]);
#endif
	ULONG cBlkBase, uBlkBase, ulBlkBase, lBlkBase, verOffset;
	cBlkBase = reg_VE_BASEA[0].basea();
	uBlkBase = reg_VE_BASEA[0].basea() + reg_VE_OFFSETA[1].offseta();
	ulBlkBase = reg_VE_BASEA[0].basea() + reg_VE_OFFSETA[2].offseta();
	lBlkBase = reg_VE_BASEA[0].basea() + reg_VE_OFFSETA[3].offseta();
	verOffset = reg_VE_OFFSETA[0].offseta();
  enum
  {
	  BASE_BLK = 0,
	  TOP_BLK,
	  BOT_BLK,
	  LEFT_EDGE_BLK
  } ;
  if( blkMode == BASE_BLK /**　base block mode*/)
  {/**
   do HE-deblock
   do VE-deblock
   */

	/** HE-deblock */
	ULONG inputVector[10], outputVector[8];
	for( int j = 0; j < 8; j++)
	{
		for(int i = 0; i < 10; i++)//get input
		{
			if( i < 5){
				inputVector[i] = 
					get_vmem( inst.tbank, 
						getAddress(uBlkBase + (3 + i ) * verOffset, 8, j));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(uBlkBase + (3 + i ) * verOffset, 8, j),inputVector[i]);

				}
			  	#endif
			}else{
				inputVector[i] = 
					get_vmem( inst.tbank,
						getAddress(cBlkBase + (i - 5) * verOffset, 8, j));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBlkBase + (i - 5) * verOffset, 8, j),inputVector[i]);

				}
			  	#endif
			}
		}
		int filter_mode = filterModeDecision(th1, th2, inputVector);
		qp = qp1;
		deblock_filter(outputVector, inputVector, filter_mode, qp);//deblock filtering
		for(int i = 0; i < 8; i++)//store output
		{
			if( i < 4){
				get_vmem(inst.tbank, getAddress( uBlkBase + (4 + i) * verOffset, 8, j )) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( uBlkBase + (4 + i) * verOffset, 8, j ),outputVector[i]);

				}
			  	#endif
			}else{
				get_vmem(inst.tbank, getAddress( cBlkBase + (i - 4) * verOffset, 8, j )) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( cBlkBase + (i - 4) * verOffset, 8, j ),outputVector[i]);

				}
			  	#endif
			}
		}
	}
	/** VE-deblock */
	for( int j = 0; j < 8; j++)
	{
		for(int i = 0; i < 10; i++)
		{
			if( j < 5)
			{// get Upper-Left Block or Upper Block
				if( i < 5)
				{// Upper-Left Block
					inputVector[i] = 
						get_vmem(inst.tbank, getAddress(ulBlkBase + ((j + 3) * verOffset), 8, i + 3));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(ulBlkBase + ((j + 3) * verOffset), 8, i + 3),inputVector[i]);

				}
			  	#endif

				}
				else
				{// Upper Block
					inputVector[i] =
						get_vmem(inst.tbank, getAddress(uBlkBase + ((j + 3) * verOffset), 8, i - 5));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(uBlkBase + ((j + 3) * verOffset), 8, i - 5),inputVector[i]);

				}
			  	#endif
				}
			}
			else
			{// get Left Block or current Block
				if( i < 5)
				{// Left Block
					inputVector[i] = 
						get_vmem(inst.tbank, getAddress(lBlkBase + ((j - 5) * verOffset), 8, i + 3));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(lBlkBase + ((j - 5) * verOffset), 8, i + 3),inputVector[i]);

				}
			  	#endif

				}
				else
				{// Current Block
					inputVector[i] =
						get_vmem(inst.tbank, getAddress(cBlkBase + ((j - 5) * verOffset), 8, i - 5));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBlkBase + ((j - 5) * verOffset), 8, i - 5),inputVector[i]);

				}
			  	#endif
				}
			}
		}
		int filter_mode = filterModeDecision(th1, th2, inputVector);
		if( j < 5)
			qp = qp0;
		else
			qp = qp1;
		deblock_filter(outputVector, inputVector, filter_mode, qp);//deblock filtering
	// Store output to vmem
		for(int i = 0; i < 10; i++)
		{
			if( j < 5)
			{// get Upper-Left Block or Upper Block
				if( i < 5)
				{// Upper-Left Block
					get_vmem(inst.tbank, getAddress(ulBlkBase + ((j + 3) * verOffset), 8, i + 3))
						= outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(ulBlkBase + ((j + 3) * verOffset), 8, i + 3),outputVector[i]);

				}
			  	#endif

				}
				else
				{// Upper Block
					get_vmem(inst.tbank, getAddress(uBlkBase + ((j + 3) * verOffset), 8, i - 5))
						= outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(ulBlkBase + ((j + 3) * verOffset), 8, i - 5),outputVector[i]);

				}
			  	#endif
				}
			}
			else
			{// get Left Block or current Block
				if( i < 5)
				{// Left Block
					get_vmem(inst.tbank, getAddress(lBlkBase + (j - 5) * verOffset, 8, i + 3))
						= outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(lBlkBase + (j - 5) * verOffset, 8, i + 3),outputVector[i]);

				}
			  	#endif
				}
				else
				{// Current Block
					get_vmem(inst.tbank, getAddress(cBlkBase + (j - 5) * verOffset, 8, i - 5))
						= outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBlkBase + (j - 5) * verOffset, 8, i - 5),outputVector[i]);

				}
			  	#endif
				}
			}
		}
	}

  }
  else if( blkMode == TOP_BLK /** top block mode*/)
  {/**
   do VE-deblock
   */
	ULONG inputVector[10], outputVector[8];
	for(int j = 0; j < 3; j++)
	{
		for(int i = 0; i < 10; i++)
		{
			if( i < 5){
				inputVector[i] = get_vmem( inst.tbank, getAddress(lBlkBase + j * verOffset, 8, i + 3));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(lBlkBase + j * verOffset, 8, i + 3),inputVector[i]);

				}
			  	#endif
			}else{
				inputVector[i] = get_vmem( inst.tbank, getAddress(cBlkBase + j * verOffset, 8, i -5));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBlkBase + j * verOffset, 8, i -5),inputVector[i]);

				}
			  	#endif
			}
		}
		int filter_mode = filterModeDecision(th1, th2, inputVector);
		qp = qp1;
		deblock_filter(outputVector, inputVector, filter_mode, qp);//deblock filtering
		for( int i = 0; i < 8; i++)
		{
			if( i < 5){
				get_vmem(inst.tbank, getAddress(lBlkBase + j * verOffset, 8, i + 3)) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(lBlkBase + j * verOffset, 8, i + 3),get_vmem(inst.tbank, getAddress(lBlkBase + j * verOffset, 8, i + 3)));

				}
			  	#endif
				
			}else{
				get_vmem(inst.tbank, getAddress(cBlkBase + j * verOffset, 8, i - 5)) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBlkBase + j * verOffset, 8, i -5),get_vmem(inst.tbank, getAddress(cBlkBase + j * verOffset, 8, i - 5)));

				}
			  	#endif
			}
		}
	}
  }
  else if( blkMode == BOT_BLK /** bottom block mode*/)
  {/**
   do HE-deblock
   do VE-deblock
   */
	ULONG inputVector[10], outputVector[8];
	/** HE deblock as base block*/
	for( int j = 0; j < 8; j++)
	{
		for(int i = 0; i < 10; i++)//get input
		{
			if( i < 5){
				inputVector[i] = 
					get_vmem( inst.tbank, 
						getAddress(uBlkBase + (3 + i ) * verOffset, 8, j));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(uBlkBase + (3 + i ) * verOffset, 8, j),inputVector[i]);

				}
			  	#endif
				
			}else{
				inputVector[i] = 
					get_vmem( inst.tbank,
						getAddress(cBlkBase + (i - 5) * verOffset, 8, j));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBlkBase + (i - 5) * verOffset, 8, j),inputVector[i]);

				}
			  	#endif
			}
		}
		int filter_mode = filterModeDecision(th1, th2, inputVector);
		qp = qp1;
		deblock_filter(outputVector, inputVector, filter_mode, qp);//deblock filtering
		for(int i = 0; i < 8; i++)//store output
		{
			if( i < 4){
				get_vmem(inst.tbank, getAddress( uBlkBase + (4 + i) * verOffset, 8, j )) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( uBlkBase + (4 + i) * verOffset, 8, j ),outputVector[i]);

				}
			  	#endif
		
			}else{
				get_vmem(inst.tbank, getAddress( cBlkBase + (i - 4) * verOffset, 8, j )) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%01d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( cBlkBase + (i - 4) * verOffset, 8, j ),outputVector[i]);

				}
			  	#endif
			}
		}
	}
	/** VE deblock */
	for( int j = 0; j < 13; j++) // total 13 rows
	{
		for(int i = 0; i < 10; i++)
		{
			if( i < 5 && j < 5){ // Upper and Left Block
				inputVector[i] =
					get_vmem( inst.tbank,
						getAddress(ulBlkBase + (j+3) * verOffset, 8, i + 3));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(ulBlkBase + (j+3) * verOffset, 8, i + 3),inputVector[i]);

				}
			  	#endif
			}else if( i >= 5 && j < 5){ // Upper Block
				inputVector[i] =
					get_vmem( inst.tbank,
						getAddress(uBlkBase + (j + 3) * verOffset, 8, i - 5));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(uBlkBase + (j + 3) * verOffset, 8, i - 5),inputVector[i]);

				}
			  	#endif
			}else if( i < 5 && j >= 5){ // Left Block
				inputVector[i] =
					get_vmem( inst.tbank,
						getAddress(lBlkBase + (j-5) * verOffset, 8, i + 3));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(lBlkBase + (j-5) * verOffset, 8, i + 3),inputVector[i]);

				}
			  	#endif
			}else if( i >= 5 && j >= 5){ // Base Block
				inputVector[i] =
					get_vmem( inst.tbank,
						getAddress(ulBlkBase + (j-3) * verOffset, 8, i - 5));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(ulBlkBase + (j-3) * verOffset, 8, i - 5),inputVector[i]);

				}
			  	#endif
			}
		}
		qp = qp1;
		int filterMode = filterModeDecision( th1, th2, inputVector);
		deblock_filter( outputVector, inputVector, filterMode, qp);
		for(int i = 1; i < 9; i++)
		{ // Save output to VMEM
			if( i < 5 && j < 5){ // Upper and Left Block
				get_vmem( inst.tbank, getAddress(ulBlkBase + (j+3) * verOffset, 8, i + 3)) = outputVector[i - 1];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(ulBlkBase + (j+3) * verOffset, 8, i + 3),outputVector[i - 1]);

				}
			  	#endif
			}else if( i >= 5 && j < 5){ // Upper Block
				get_vmem( inst.tbank, getAddress(uBlkBase + (j + 3) * verOffset, 8, i - 5)) = outputVector[i - 1];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(uBlkBase + (j + 3) * verOffset, 8, i - 5),outputVector[i - 1]);

				}
			  	#endif
			}else if( i < 5 && j >= 5){ // Left Block
				get_vmem( inst.tbank, getAddress(lBlkBase + (j-5) * verOffset, 8, i + 3)) = outputVector[i - 1];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(lBlkBase + (j-5) * verOffset, 8, i + 3),outputVector[i - 1]);

				}
			  	#endif
			}else if( i >= 5 && j >= 5){ // Base Block
				get_vmem( inst.tbank, getAddress(cBlkBase + (j-3) * verOffset, 8, i - 5)) = outputVector[i - 1];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBlkBase + (j-3) * verOffset, 8, i - 5),outputVector[i - 1]);

				}
			  	#endif
			}
		}
	}
  }
  else if( blkMode == LEFT_EDGE_BLK /** left-edge block mode*/)
  {/**
   do HE-deblock
   */
	ULONG inputVector[10], outputVector[8];
	for( int j = 0; j < 8; j++)
	{
		for(int i = 0; i < 10; i++)
		{
			if( i < 5){
				inputVector[i] = 
					get_vmem( inst.tbank, 
						getAddress( lBlkBase + (i + 3) * verOffset, 8, j));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( lBlkBase + (i + 3) * verOffset, 8, j),inputVector[i]);

				}
			  	#endif
			}else{
				inputVector[i] = 
					get_vmem( inst.tbank, getAddress( cBlkBase + (i - 5) * verOffset, 8, j));
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_r_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( cBlkBase + (i - 5) * verOffset, 8, j),inputVector[i]);

				}
			  	#endif
			}
		}
		qp = qp1;
		int filter_mode = filterModeDecision( th1, th2, inputVector);
		deblock_filter( outputVector, inputVector, filter_mode, qp);
		for(int i = 0; i < 8; i++)//store output
		{
			if( i < 4){
				get_vmem(inst.tbank, getAddress( uBlkBase + (4 + i) * verOffset, 8, j )) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( uBlkBase + (4 + i) * verOffset, 8, j ),outputVector[i]);

				}
			  	#endif
				
			}else{
				get_vmem(inst.tbank, getAddress( cBlkBase + (i - 4) * verOffset, 8, j )) = outputVector[i];
				#ifdef MEMORY_MONITOR
				if(CDebugUI::memory_w_monitor){
				sc_time st= sc_time_stamp();
				ULONG temp_t = (ULONG)st.to_default_time_units();
				fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
				temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress( cBlkBase + (i - 4) * verOffset, 8, j ),outputVector[i]);

				}
			  	#endif
			}
		}
	}
  }


  ve_wait(138);
};

void module_ve::vsp_ivpd(ve_inst inst)          
{ 
#ifndef VE_RELEASE
  cout << "VE_IPVD called and issued\n";
#endif
  // implemented by right@20040713
  ULONG evenInBase, oddInBase, inVerOffset;
  evenInBase = reg_VE_BASEA[0].basea();
  oddInBase = reg_VE_BASEA[1].basea();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  
  ULONG d01, dd, d0, d1;

  ULONG evenBlock[8*16], oddBlock[8*16];
  for(int i = 0; i < 8; i++)
  {//load data from vmem to local
    for(int j = 0; j < 16; j++)
    {
      evenBlock[i*16+j] = get_vmem(inst.tbank, getAddress(evenInBase, 8, j));
      oddBlock[i*16+j] = get_vmem(inst.tbank, getAddress(oddInBase, 8, j));
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(evenInBase, 8, j),evenBlock[i*16+j]);
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(oddInBase, 8, j), oddBlock[i*16+j]);

	}
	#endif
    }
	evenInBase += inVerOffset;
	oddInBase += inVerOffset;
  }
  //vertical pixel diff between different field
  d01 = 0;
  for(int i = 0; i < 128; i++)
  {//even - odd difference
    d01 += ad(evenBlock[i], oddBlock[i]);
  }
  for( int i = 0; i < (64 - 16); i++)
  {//odd - even difference
    d01 += ad(oddBlock[i], evenBlock[i + 16]);
  }
  for( int i = 64; i < (128-16); i++)
  {
    d01 += ad(oddBlock[i], evenBlock[i + 16]);
  }
  //vertical pixel diff between the samd field
  d0 = 0;
  d1 = 0;
  for(int i = 0; i < (128 -16); i++)
  {
    d0 += ad(evenBlock[i], evenBlock[i + 16]);
    d1 += ad(oddBlock[i], oddBlock[i + 16]);
  }
  dd = d0 + d1;
  ULONG result = (dd & 0xFFFF) | ((d01 & 0xFFFF) << 16);
  ve_wait(75);
  while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, result) == 0)
    ve_wait(1);

};
void module_ve::vsp_pvpd(ve_inst inst)          
{ 
#ifndef VE_RELEASE
  cout << "VE_PVPD called and issued\n";
#endif
//implemented by right@20040714
  ULONG cBase, pBase;
  int cBlock[256], pBlock[256], evenBlock[8 * 16], oddBlock[8 * 16];
  ULONG cVerOffset, pVerOffset;

  cBase = reg_VE_BASEA[0].basea();
  pBase = reg_VE_BASEA[1].basea();
  //cVerOffset = reg_VE_OFFSETA[1].offseta();
  //pVerOffset = reg_VE_OFFSETA[1].offseta();
  cVerOffset = 16;
  pVerOffset = 16;
  
  for(int i = 0;i < 16; i++)
  {//load data from vmem and calculate cBlock[] - pBlock[]
    for(int j = 0; j < 16; j++)
    {
      cBlock[i * 16 + j] = (int)get_vmem(inst.tbank, getAddress(cBase, 8, j));
      pBlock[i * 16 + j] = (int)get_vmem(inst.tbank, getAddress(pBase, 8, j));
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBase, 8, j),cBlock[i * 16 + j]);
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(pBase, 8, j), pBlock[i * 16 + j]);

	}
	#endif
      cBlock[i * 16 + j] = cBlock[i * 16 + j] - pBlock[i * 16 + j];
    }
    cBase += cVerOffset;
    pBase += pVerOffset;
  }
  for(int i = 0; i < 8; i++)
  {//split even/odd block
    for(int j = 0; j < 16; j++)
    {
      evenBlock[i * 16 + j] = cBlock[i * 2 * 16 + j];
      oddBlock[i * 16 + j] = cBlock[(i * 2 + 1) * 16 + j];
    }


  }
  //calculate VPD as IVPD
  int d01 = 0, d0 = 0, d1 = 0, dd = 0;
  for(int i = 0; i < 128; i++)
  {//even - odd difference
    d01 += ad(evenBlock[i], oddBlock[i]);
  }
  for( int i = 0; i < (64 - 16); i++)
  {//odd - even difference
    d01 += ad(oddBlock[i], evenBlock[i + 16]);
  }
  for( int i = 64; i < (128-16); i++)
  {
    d01 += ad(oddBlock[i], evenBlock[i + 16]);
  }
  //vertical pixel diff between the samd field
  for(int i = 0; i < (128 -16); i++)
  {
    d0 += ad(evenBlock[i], evenBlock[i + 16]);
    d1 += ad(oddBlock[i], oddBlock[i + 16]);
  }
  dd = d0 + d1;
  ULONG result = (dd & 0xFFFF) | ((d01 & 0xFFFF) << 16);

  ve_wait(85);
  while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, result) == 0)
    ve_wait(1);

};
void module_ve::vsp_avgvpd(ve_inst inst)        
{ 
#ifndef VE_RELEASE
  cout << "VE_AVGVPD called and issued\n";
#endif
  //implemented by right @20040719
  ULONG cBase, fBase, bBase;
  ULONG cBlock[256], fBlock[256], bBlock[256], evenBlock[8 * 16], oddBlock[8 * 16];
  ULONG cVerOffset, fVerOffset, bVerOffset;

  cBase = reg_VE_BASEA[0].basea();
  fBase = reg_VE_BASEA[1].basea();
  bBase = reg_VE_BASEA[2].basea();
  
  cVerOffset = 16;
  fVerOffset = 16;
  bVerOffset = 16;
	//{小數運算需要四捨五入. 利用 initValue 與 filtPrec達到四捨五入的結果.
	ULONG initValue = reg_VE_FILTINIT.init_value();
	if( (initValue & 0x80000) != 0)//negative value
	 initValue = (0xFFF00000 | initValue);//sign extension.
	ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

  for(int i = 0;i < 16; i++)
  {//load data from vmem and calculate cBlock[] - pBlock[]
    for(int j = 0; j < 16; j++)
    {
      cBlock[i * 16 + j] = get_vmem(inst.tbank, getAddress(cBase, 8, j));
      fBlock[i * 16 + j] = get_vmem(inst.tbank, getAddress(fBase, 8, j));
      bBlock[i * 16 + j] = get_vmem(inst.tbank, getAddress(bBase, 8, j));
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(cBase, 8, j),cBlock[i * 16 + j]);
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(fBase, 8, j), fBlock[i * 16 + j]);
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(bBase, 8, j), bBlock[i * 16 + j]);

	}
	#endif
      cBlock[i * 16 + j] = cBlock[i * 16 + j] - ((fBlock[i * 16 + j] + bBlock[i * 16 + j] + initValue) >> (8 - filtPrec));
    }
    cBase += cVerOffset;
    fBase += fVerOffset;
    bBase += bVerOffset;
  }
  for(int i = 0; i < 8; i++)
  {//split even/odd block
    for(int j = 0; j < 16; j++)
    {
      evenBlock[i * 16 + j] = cBlock[i * 2 * 16 + j];
      oddBlock[i * 16 + j] = cBlock[(i * 2 + 1) * 16 + j];
    }
  }
  //calculate VPD as IVPD
  int d01, d0, d1, dd;
  d01 = 0;
  for(int i = 0; i < 128; i++)
  {//even - odd difference
    d01 += ad(evenBlock[i], oddBlock[i]);
  }
  for( int i = 0; i < 64 - 16; i++)
  {//odd - even difference
    d01 += ad(oddBlock[i], evenBlock[i + 16]);
  }
  for( int i = 64; i < 128-16; i++)
  {
    d01 += ad(oddBlock[i], evenBlock[i + 16]);
  }
  //vertical pixel diff between the samd field
  d0 = 0;
  d1 = 0;
  for(int i = 0; i < 128 -16; i++)
  {
    d0 += ad(evenBlock[i], evenBlock[i + 16]);
    d1 += ad(oddBlock[i], oddBlock[i + 16]);
  }
  dd = d0 + d1;
  ULONG result = (dd & 0xFFFF) | ((d01 & 0xFFFF) << 16);
  ve_wait(115);
  while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, result) == 0)
    ve_wait(1);

};
void module_ve::vsp_sad(ve_inst inst)           
{ 
#ifndef VE_RELEASE
  cout << "VE_SAD called and issued\n";
#endif
//implemented by right@20040707
ULONG in0Base, in1Base, in0HorOffset, in1HorOffset, in0VerOffset, in1VerOffset;
in0Base = reg_VE_BASEA[0].basea();
in1Base = reg_VE_BASEA[1].basea();
in0HorOffset = reg_VE_OFFSETA[0].offseta();
in1HorOffset = in0HorOffset;
in0VerOffset = reg_VE_OFFSETA[1].offseta();
in1VerOffset = in0VerOffset;

ULONG Width, Height;
Width = GET_WIDTH(inst.par[0]) + 1;
Height = GET_HEIGHT(inst.par[0]) + 1;
ULONG result= 0;
for(int i = 0; i < Height; i++)
{
	for(int j = 0; j < Width; j++)
	{
		result += ad(get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j)),
			get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j)));
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in0Base, in0HorOffset, j),get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j)));
	
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in1Base, in1HorOffset, j),get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j)));

		}
		#endif
	}
	in0Base += in0VerOffset;
	in1Base += in1VerOffset;
}
  ve_wait( Width/8*Height/2 + 10);
	while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, result) == 0)
		ve_wait(1);
};
void module_ve::vsp_blkdc(ve_inst inst)         
{ 
#ifndef VE_RELEASE
  cout << "VE_BLKDC called and issued\n";
#endif
// implemented by right@20040708
  ULONG inBase, inHorOffset, inVerOffset;
  inBase = reg_VE_BASEA[0].basea();
  inHorOffset = reg_VE_OFFSETA[0].offseta();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  ULONG Width, Height;
  Width = GET_WIDTH(inst.par[0]) + 1;
  Height = GET_HEIGHT(inst.par[0]) + 1;
  ULONG dcValue = 0;
  for(int i = 0; i < Height; i++)
  {
	  for(int j = 0; j < Width; j++)
	  {
		  dcValue += get_vmem(inst.tbank, getAddress(inBase, inHorOffset, j));
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(inBase, inHorOffset, j),get_vmem(inst.tbank, getAddress(inBase, inHorOffset, j)));
	
		}
		#endif

	  }
	  inBase += inVerOffset;
  }
  dcValue = dcValue /(Width * Height);
  reg_VE_DCVAL.dc_value() = dcValue;

  ve_wait( Width/8*Height + 10);
  while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, dcValue) == 0)
    ve_wait(1);
};
void module_ve::vsp_saddc(ve_inst inst)         
{ 
#ifndef VE_RELEASE
  cout << "VE_SADDC called and issued\n";
#endif
// implemented by right@20040708
  ULONG inBase, inHorOffset, inVerOffset;
  inBase = reg_VE_BASEA[0].basea();
  inHorOffset = reg_VE_OFFSETA[0].offseta();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  ULONG Width, Height;
  Width = GET_WIDTH(inst.par[0]) + 1;
  Height = GET_HEIGHT(inst.par[0]) + 1;

  ULONG dcValue;
  ULONG result = 0;
  dcValue = reg_VE_DCVAL.dc_value();
  for(int i = 0; i < Height; i++)
  {
	  for(int j = 0; j < Width; j++)
	  {
		  result += ad(get_vmem(inst.tbank, getAddress(inBase, inHorOffset, j)), dcValue);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(inBase, inHorOffset, j),get_vmem(inst.tbank, getAddress(inBase, inHorOffset, j)));
	
		}
		#endif
	  }
	  inBase += inVerOffset;
  }
  ve_wait(Width/8*Height + 10);
  while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, result) == 0)
    ve_wait(1);
};
void module_ve::vsp_sadavg(ve_inst inst)        
{ 
#ifndef VE_RELEASE
  cout << "VE_SADAVG called and issued\n";
#endif
// implemented by right@20040708
  ULONG in0Base, in1Base, in2Base, horOffset, in0VerOffset, in1VerOffset, in2VerOffset;
  in0Base = reg_VE_BASEA[0].basea();
  in1Base = reg_VE_BASEA[1].basea();
  in2Base = reg_VE_BASEA[2].basea();
  horOffset = reg_VE_OFFSETA[0].offseta();
  in0VerOffset = reg_VE_OFFSETA[1].offseta();
  in1VerOffset = in0VerOffset;
  in2VerOffset = reg_VE_OFFSETA[2].offseta();
  ULONG Width, Height;
  Width = GET_WIDTH(inst.par[0]) + 1;
  Height = GET_HEIGHT(inst.par[0]) + 1;
  ULONG result = 0;
  for(int i = 0; i < Height; i++)
  {
	  for(int j = 0; j < Width; j++)
	  {
		  result += ad(get_vmem(inst.tbank, getAddress(in0Base, horOffset, j)), 
			  ( 1 + get_vmem(inst.tbank, getAddress(in1Base, horOffset, j)) 
        + get_vmem(inst.tbank, getAddress(in2Base, horOffset, j)))>>1);
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in0Base, horOffset, j),get_vmem(inst.tbank, getAddress(in0Base, horOffset, j)));

		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in1Base, horOffset, j),get_vmem(inst.tbank, getAddress(in1Base, horOffset, j)));
		
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in2Base, horOffset, j),get_vmem(inst.tbank, getAddress(in2Base, horOffset, j)));
		

		}
		#endif
	  }
    in0Base += in0VerOffset;
    in1Base += in1VerOffset;
    in2Base += in2VerOffset;
  }
  ve_wait(Width/8*Height*3 + 10);
  while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, result) == 0)
    ve_wait(1);
};
void module_ve::vsp_blkdiff(ve_inst inst)       
{ 
#ifndef VE_RELEASE
  cout << "VE_BLKDIFF called and issued\n";
#endif
// implemented by right@20040708
  ULONG TR1, TR2, TR3, TR4;
  TR1 = reg_VE_BLKD_THR.thr_1();
  TR2 = reg_VE_BLKD_THR.thr_2();
  TR3 = reg_VE_BLKD_THR.thr_3();
  TR4 = reg_VE_BLKD_THR.thr_4();
  ULONG in0Base, in0HorOffset, in0VerOffset, in1Base, in1HorOffset, in1VerOffset;
  in0Base = reg_VE_BASEA[0].basea();
  in0HorOffset = reg_VE_OFFSETA[0].offseta();
  in0VerOffset = reg_VE_OFFSETA[1].offseta();
  in1Base = reg_VE_BASEA[1].basea();
  in1HorOffset = reg_VE_OFFSETA[0].offseta();
  in1VerOffset = reg_VE_OFFSETA[1].offseta();

  ULONG Width, Height;
  Width = GET_WIDTH(inst.par[0]) + 1;
  Height = GET_HEIGHT(inst.par[0]) + 1;
  ULONG Weight2, Weight3, Weight4, Weight5, result = 0;
  Weight2 = reg_VE_BLKD_WEIGHT.weight_2();
  Weight3 = reg_VE_BLKD_WEIGHT.weight_3();
  Weight4 = reg_VE_BLKD_WEIGHT.weight_4();
  Weight5 = reg_VE_BLKD_WEIGHT.weight_5();

  int bucket5 = 0, bucket4 = 0, bucket3 = 0, bucket2 = 0;
//  Weight1 = reg_VM_BLKD_WEIGHT
  for(int i = 0; i < Height; i++)
  {
    for(int j = 0; j < Width; j++)
    {
      if( ad( get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j)),
			get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j))) >= TR4)
        bucket5++;
      else if(ad( get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j)),
			get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j))) >= TR3)
        bucket4++;
      else if(ad( get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j)),
			get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j))) >= TR2)
        bucket3++;
      else if(ad( get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j)),
			get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j))) >= TR1)
        bucket2++;
		#ifdef MEMORY_MONITOR
		if(CDebugUI::memory_r_monitor){
		sc_time st= sc_time_stamp();
		ULONG temp_t = (ULONG)st.to_default_time_units();
		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in0Base, in0HorOffset, j),get_vmem(inst.tbank, getAddress(in0Base, in0HorOffset, j)));

		fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
		temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(in1Base, in1HorOffset, j),get_vmem(inst.tbank, getAddress(in1Base, in1HorOffset, j)));
		
		}
		#endif
    }
    in0Base += in0VerOffset;
	in1Base += in1VerOffset;
  }
  result = bucket2 * Weight2 + bucket3 * Weight3 + bucket4 * Weight4 + bucket5 * Weight5;

  ve_wait(Width/8*Height*2 + 10);
  while( store_result_fifo(RSLT_ID_IMGBLOCK, inst, result) == 0)
    ve_wait(1);
};

void module_ve::vsp_vmcopy(ve_inst inst)		
{ 
#ifndef VE_RELEASE
  cout << "VE_VMCOPY called and issued\n";
#endif
  int         fromBank, toBank;
  fromBank    = GET_IMM_FIELD(inst.inst) & 0x1;
  toBank      = 1 - fromBank;
#ifndef VE_RELEASE
	debug_printf("fromBank: %d, toBank: %d\n", fromBank, toBank);
#endif

  ULONG       fromAddr, toAddr, fromOffset, toOffset, width, height;
  fromAddr    = reg_VE_BASEA[0].basea();
  toAddr      = reg_VE_BASEA[3].basea();
  fromOffset  = reg_VE_OFFSETA[0].offseta();
  toOffset    = reg_VE_OFFSETA[3].offseta();
  width       = GET_WIDTH(inst.par[0]) + 1;
  height      = GET_HEIGHT(inst.par[0]) + 1;

  ULONG       i, j;

  for( j=0; j<height; j++)
    for( i=0; i<width; i++)
    {
      get_vmem(toBank, (toAddr + i) + toOffset * j) = get_vmem(fromBank, (fromAddr + i) + fromOffset * j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, fromBank, fromBank*4096+(fromAddr + i) + fromOffset * j,get_vmem(fromBank, (fromAddr + i) + fromOffset * j));
	}
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, toBank, toBank*4096+(toAddr + i) + toOffset * j,get_vmem(toBank, (toAddr + i) + toOffset * j));
	}
	#endif

#ifndef VE_RELEASE
			debug_printf("src: %x, target: %x\n", get_vmem(fromBank, (fromAddr + i) + fromOffset * j),
				get_vmem(toBank, (toAddr + i) + toOffset * j));
#endif
    }

    ve_wait(width * height/8 * 2);
};
void module_ve::vsp_rotate(ve_inst inst)        
{ 
#ifndef VE_RELEASE
  cout << "VE_ROTATE called and issued\n";
#endif
  //implemented by right @20040720
  ULONG inBase, inOffset, outBase, outOffset;
  inBase = reg_VE_BASEA[0].basea();
  inOffset = reg_VE_OFFSETA[0].offseta();
  outBase = reg_VE_BASEA[3].basea();
  outOffset = reg_VE_OFFSETA[3].offseta();

  int degree;
  int size;
  degree = (inst.par[0] & 0x3);
  
  if( (inst.par[0] >> 2) & 0x1 == 1)
  {// rotate 16x16
      size = 16;
  }
  else
  {// rotate 8x8
    size = 8;
  }
  ULONG *src, *dest;
  src = (ULONG*)malloc(sizeof(ULONG) * size * size);
  dest = (ULONG*)malloc(sizeof(ULONG) * size * size);
  for(int i = 0; i < size; i++)
  {
    for(int j = 0; j < size; j++)
    {//load data from vmem
      *(src + i * size + j) = get_vmem(inst.tbank, inBase + i * inOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+inBase + i * inOffset + j,get_vmem(inst.tbank, inBase + i * inOffset + j));
	}
	#endif
    }
  }
  switch(degree)
  {
  case '0':
    {//90'
      for(int i = 0; i < size; i++)
        for(int j = 0; j < size; j++)
          *(dest + i * size + j) = *(src + (size - 1 - j)*size + i);
    }
	break;
  case '1':
    {//180'
      for(int i = 0; i < 8; i++)
        for(int j = 0; j < 8; j++)
          *(dest + i * size + j) = *(src + ((size-1) - i)*size + ((size-1) - j));
    }
	break;
  case '2':
    {//270'
      for(int i = 0; i < 8; i++)
        for(int j = 0; j < 8; j++)
          *(dest + i * size + j) = *(src + j * size + (size -1 - i));
    }
	break;
  }

  for(int i = 0; i < size; i++)
    for(int j = 0; j < size; j++){//store data to vmem
      get_vmem(inst.tbank, outBase + i * outOffset) = *(dest + i * size + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset,*(dest + i * size + j));
	}
	#endif
    }
  
    ve_wait(size * size/8*2);
};

void module_ve::vsp_vernr(ve_inst inst)
{
#ifndef VE_RELEASE
  cout << "VE_VERNR called and issued\n";
#endif
  ULONG evenInBase, oddInBase, outBase, inHorOffset, inVerOffset;
  ULONG outHorOffset, outVerOffset;
  evenInBase = reg_VE_BASEA[0].basea();
  oddInBase = reg_VE_BASEA[1].basea();
  outBase = reg_VE_BASEA[3].basea();
  inHorOffset = reg_VE_OFFSETA[0].offseta();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
//  outHorOffset = inHorOffset;
  outHorOffset = reg_VE_OFFSETA[2].offseta();           // modified by gcc: according to VE spec 0.74
  outVerOffset = reg_VE_OFFSETA[3].offseta();

  ULONG rptTopLine, rptBotLine;
  rptTopLine = reg_VE_FILTCNTL.rpt_topline();
  rptBotLine = reg_VE_FILTCNTL.rpt_botline();

  ULONG tapNum, tapStart;
  tapNum = reg_VE_FILTCNTL.tapnum() + 1;
  tapStart = reg_VE_FILTCNTL.start_tap();

  ULONG inputWidth, outputWidth, inputHeight, outputHeight, postInputHeight, postInputWidth;
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight = GET_HEIGHT(inst.par[0]) + 1;
  inputWidth = outputWidth;
  inputHeight = outputHeight + tapNum - 1 - rptTopLine - rptBotLine;
  postInputHeight = outputHeight + tapNum - 1;
  postInputWidth = inputWidth;

  ULONG *inputVectorBlock, *postInputVectorBlock, *outputVector;
  postInputVectorBlock = (ULONG*)malloc(sizeof(ULONG) * postInputWidth * postInputHeight);
  inputVectorBlock = (ULONG*)malloc(sizeof(ULONG) * inputWidth * inputHeight);
  outputVector = (ULONG*)malloc(sizeof(ULONG) * outputWidth * outputHeight);            // modified by gcc: correct buffer overflow

  ULONG thr1, thr2, coeff[7], rshift_size;
  int   i, j, k;
  int   addr;

  thr1 = reg_VE_ADAPCNTL.t1();
  thr2 = reg_VE_ADAPCNTL.t2();
  rshift_size = reg_VE_ADAPCNTL.rshift_size();
  
  ULONG delta = 1 << (rshift_size + 2);

  for(i = 0; i < inputHeight; i++)
  {//load data from vmem
    for(j = 0; j < inputWidth; j++)
    {
      if (i % 2 == 0)
        addr = getAddress(evenInBase + (i/2) * inVerOffset, inHorOffset, j);
      else
        addr = getAddress(oddInBase + (i/2) * inVerOffset, inHorOffset, j);

      *(inputVectorBlock + i * inputWidth + j) = get_vmem(inst.tbank, addr);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addr,get_vmem(inst.tbank, addr));
	}
	#endif
    }
  }

  for(i = 0; i < postInputHeight; i++)
  {//extend inputVectorBlock to postInputVectorBlock
    for(j = 0; j < postInputWidth; j++)
    {
      if(i < rptTopLine)//top lines
        *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (rptTopLine - 1 - i) * inputWidth + j);
      else if( i >= inputHeight + rptTopLine)//bottom lines
        *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (inputHeight - 1 - (i - inputHeight - rptTopLine)) * inputWidth + j);
      else//normol case
        *(postInputVectorBlock + i * postInputWidth + j) = *(inputVectorBlock + (i - rptTopLine) * inputWidth + j);
    }
  }

  printf("vernr post input:\n");
  for(i = 0;i < postInputHeight;i++)
  {//extend inputVectorBlock to postInputVectorBlock
    for(j = 0; j < postInputWidth; j++)
      printf("%3d ", *(postInputVectorBlock + i * postInputWidth + j));
    printf("\n");
  }

  
  ULONG result, pixelDiff;
  int   coeff_sum;

  for(i = 0; i < outputHeight; i++)
  {
    for(j = 0; j < outputWidth; j++)
    {
      if (i == 8 && j == 8)
        i = i;
      
    //decide coeff
      for(coeff_sum = k = 0; k < 7; k++)
      {
        pixelDiff = ad(postInputVectorBlock[(i + k) * postInputWidth + j], 
                          postInputVectorBlock[(i + 3) * postInputWidth + j]);
        if(  pixelDiff < thr1 || k == 3) // diff is too small as identical pixel
          coeff[k] = 8;					// 8 is the biggest weight coeff.
        else if( pixelDiff >= thr2)		// diff is too large
          coeff[k] = 0;					// 0 is the smallest weight coeff.
        else if( pixelDiff < (thr1 + (delta >> 2)) && pixelDiff >= thr1) 
            coeff[k] = 4;
        else if( pixelDiff < (thr1 + (delta >> 1)) && pixelDiff >= (thr1 + (delta >> 2)) ) 
            coeff[k] = 2;
        else
            coeff[k] = 1;
      }

      coeff_sum = 0;
      coeff_sum += coeff[0] = coeff[6] = min(coeff[0], coeff[6]);
      coeff_sum += coeff[1] = coeff[5] = min(coeff[1], coeff[5]);
      coeff_sum += coeff[2] = coeff[4] = min(coeff[2], coeff[4]);
      coeff_sum = (coeff_sum << 1) + coeff[3];

    //filtering
      result = 0;
      
      for(k = 0; k < tapNum; k++)
        result += coeff[k] * *(postInputVectorBlock + (i+k) * postInputWidth + j);
      *(outputVector + i * outputWidth + j) = (result + (coeff_sum >> 1)) / coeff_sum;

      //save data to vmem
      addr = getAddress(outBase + i * outVerOffset, outHorOffset, j);

      get_vmem(inst.tbank, addr) 
        = *(outputVector + i * outputWidth + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addr,get_vmem(inst.tbank, addr));
	}
	#endif
    }
  } 

  //for(int w = 0; w < (outputWidth/8)*outputHeight*10; w++)
  // the three lines are added by gcc: free buffers
  free(inputVectorBlock);                                           
  free(postInputVectorBlock);
	free(outputVector);
  // end of modification by gcc
  ve_wait((outputWidth/8)*outputHeight*10);
#ifndef VE_RELEASE
  debug_printf("VE_VERNR done.\n");
#endif
};

void module_ve::vsp_hornr(ve_inst inst)
{
#ifndef VE_RELEASE
  cout << "VE_HORNR called and issued\n";
#endif
//implemented by right @20040721
/**********************************************************************************
  1. Load data from vmem and extend it as HORFILTM do.
  2. calculate Omega.
  3. filtering it.
  4. store data to vmem.
***********************************************************************************/
  ULONG evenInBase, oddInBase, outBase, inHorOffset, inVerOffset, outHorOffset, outVerOffset;
  int   i, j, k;

  evenInBase  = reg_VE_BASEA[0].basea();
  oddInBase   = reg_VE_BASEA[1].basea();
  outBase     = reg_VE_BASEA[3].basea();
  inHorOffset = reg_VE_OFFSETA[0].offseta();
  inVerOffset = reg_VE_OFFSETA[1].offseta();
  outHorOffset = reg_VE_OFFSETA[2].offseta();
  outVerOffset = reg_VE_OFFSETA[3].offseta();
  ULONG outputWidth, outputHeight, inputWidth, inputHeight, rptRight, rptLeft, tapNum, tapStart, postInputWidth;
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight =GET_HEIGHT(inst.par[0]) + 1;
  rptRight = reg_VE_FILTCNTL.rpt_rightpel();
  rptLeft = reg_VE_FILTCNTL.rpt_leftpel();
  tapNum = reg_VE_FILTCNTL.tapnum() + 1;
  tapStart = reg_VE_FILTCNTL.start_tap();
  inputWidth = outputWidth + tapNum - 1 - rptRight - rptLeft;
  inputHeight = outputHeight;
  postInputWidth = inputWidth + rptRight + rptLeft;

  ULONG *inputVector, *postInputVector, *outputVector;
  inputVector = (ULONG*) malloc(sizeof(ULONG) * inputWidth);
  postInputVector = (ULONG*) malloc(sizeof(ULONG) * (inputWidth + rptRight + rptLeft));
  outputVector = (ULONG*) malloc(sizeof(ULONG) * outputWidth);

  ULONG initValue = reg_VE_FILTINIT.init_value();
  if( (initValue & 0x80000) != 0)//negative value
   initValue = (0xFFF00000 | initValue);
  ULONG filtPrec = reg_VE_FILTCNTL.filt_prec();

  ULONG thr1, thr2, rshift_size;
//  delta = reg_VE_ADAPCNTL.delta_thresh();
  thr1 = reg_VE_ADAPCNTL.t1();
  thr2 = reg_VE_ADAPCNTL.t2();
  rshift_size = reg_VE_ADAPCNTL.rshift_size();
  ULONG delta = 1 << (rshift_size + 2);
  ULONG coeff[7];
  int   coeff_sum;

  ULONG result, pixelDiff;
  int   addr;

  for(i = 0; i < outputHeight; i++)
  {
    for(int m = 0; m < inputWidth; m++)
    {//load data from vmem to inputVector
      if (i & 1)          // i is odd
        addr = getAddress(oddInBase + (i >> 1) * inVerOffset, inHorOffset, m);
      else
        addr = getAddress(evenInBase + (i >> 1) * inVerOffset, inHorOffset, m);
      
      inputVector[m] = get_vmem(inst.tbank, addr);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+addr,get_vmem(inst.tbank, addr));
	}
	#endif
    }

    for(j = 0; j < postInputWidth; j++)
    {//extend inputVector to postInputVector
      if(j < rptLeft)//mirror left
        postInputVector[j] = inputVector[rptLeft - 1 - j];
      else if(j >= inputWidth + rptLeft) //mirror right
        postInputVector[j] = inputVector[inputWidth - 1 - (j - rptLeft - inputWidth)];
      else
        postInputVector[j] = inputVector[j - rptLeft];
    }

    for(j = 0; j < outputWidth; j++)
    { // 1st, decide the Omega.
      if (j == 14)
        j = j;
      
      for(k = 0; k < 7; k++)
      {
        pixelDiff = ad(postInputVector[j + k], postInputVector[j + 3]);
        if(  pixelDiff < thr1 || k == 3) // diff is too small as identical pixel
          coeff[k] = 8;					// 8 is the biggest weight coeff.
        else if( pixelDiff >= thr2)		// diff is too large
          coeff[k] = 0;					// 0 is the smallest weight coeff.
        else if( pixelDiff < (thr1 + (delta >> 2)) && pixelDiff >= thr1) 
            coeff[k] = 4;
        else if( pixelDiff < (thr1 + (delta >> 1)) && pixelDiff >= (thr1 + (delta >> 2)) ) 
            coeff[k] = 2;
        else
            coeff[k] = 1;
      }
      coeff_sum = 0;
      coeff_sum += coeff[0] = coeff[6] = min(coeff[0], coeff[6]);
      coeff_sum += coeff[1] = coeff[5] = min(coeff[1], coeff[5]);
      coeff_sum += coeff[2] = coeff[4] = min(coeff[2], coeff[4]);
      coeff_sum = (coeff_sum << 1) + coeff[3];
        
      //filtering
      result = 0;
      for(int k = 0; k < 7; k++)
        result += coeff[k] * postInputVector[j + k];
      
      outputVector[j] = (result + (coeff_sum >> 1)) / coeff_sum;

      //store data to vmem
      get_vmem(inst.tbank, getAddress(outBase + i * outVerOffset, outHorOffset, j)) = outputVector[j];
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+getAddress(outBase + i * outVerOffset, outHorOffset, j),outputVector[j]);
	}
	#endif
    }
  }
  //for(int w = 0; w < ((outputWidth+7)/8)*outputHeight*12; w++)

  free(inputVector);
  free(postInputVector);
  free(outputVector);

  ve_wait(((outputWidth+7)/8)*outputHeight*12);
  
#ifndef VE_RELEASE
  debug_printf("VE_HORNR done.\n");
#endif
};

void module_ve::vsp_packclr(ve_inst inst)
{
#ifndef VE_RELEASE
  cout << "VE_PACKCLR called and issued\n";
#endif
  ULONG outputWidth, outputHeight, inputWidth, inputHeight;
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight = GET_HEIGHT(inst.par[0]) + 1;
  inputWidth = outputWidth / 4;
  inputHeight = outputHeight;
  ULONG redBase, greenBase, blueBase, alphaBase, outBase, inOffset, outOffset;
  redBase = reg_VE_BASEA[0].basea();
  greenBase = reg_VE_BASEA[1].basea();
  blueBase = reg_VE_BASEA[2].basea();
  alphaBase = reg_VE_BASEA[1].basea();
  outBase = reg_VE_BASEA[3].basea();
  inOffset = reg_VE_OFFSETA[0].offseta();
  outOffset = reg_VE_OFFSETA[3].offseta();


  for(int i = 0; i < outputHeight; i++)
  {
    for(int j = 0; j < outputWidth; j++)
    {
      if(j % 4 == 0){//red
        get_vmem(inst.tbank, outBase + i * outOffset + j) = get_vmem(inst.tbank, redBase + i * inOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+redBase + i * inOffset + j,get_vmem(inst.tbank, redBase + i * inOffset + j));
	}
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	}
	#endif
      }else if(j % 4 == 1){
        get_vmem(inst.tbank, outBase + i * outOffset + j) = get_vmem(inst.tbank, greenBase + i * inOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+greenBase + i * inOffset + j,get_vmem(inst.tbank, greenBase + i * inOffset + j));
	}
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	}
	#endif
      }else if(j % 4 == 2){
        get_vmem(inst.tbank, outBase + i * outOffset + j) = get_vmem(inst.tbank, blueBase + i * inOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+blueBase + i * inOffset + j,get_vmem(inst.tbank, blueBase + i * inOffset + j));
	}
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	}
	#endif
      }else if(j % 4 == 3){
        get_vmem(inst.tbank, outBase + i * outOffset + j) = get_vmem(inst.tbank, alphaBase + i * inOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+alphaBase + i * inOffset + j,get_vmem(inst.tbank, alphaBase + i * inOffset + j));
	}
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	}
	#endif
      }
    }
  }
  //for(int w = 0; w < ((outputWidth+7)/8)*outputHeight*2; w++)
    ve_wait(((outputWidth+7)/8)*outputHeight*2);
};

void module_ve::vsp_unpackclr(ve_inst inst)
{
#ifndef VE_RELEASE
  cout << "VE_PACKCLR called and issued\n";
#endif
  ULONG outputWidth, outputHeight, inputWidth, inputHeight;
  outputWidth = GET_WIDTH(inst.par[0]) + 1;
  outputHeight = GET_HEIGHT(inst.par[0]) + 1;
  inputWidth = outputWidth / 4;
  inputHeight = outputHeight;
  ULONG redBase, greenBase, blueBase, alphaBase, outBase, inOffset, outOffset;
  redBase = reg_VE_BASEA[0].basea();
  greenBase = reg_VE_OFFSETA[1].offseta();
  blueBase = reg_VE_OFFSETA[2].offseta();
  alphaBase = reg_VE_BASEA[1].basea();
  outBase = reg_VE_BASEA[3].basea();
  inOffset = reg_VE_OFFSETA[0].offseta();
  outOffset = reg_VE_OFFSETA[3].offseta();


  for(int i = 0; i < outputHeight; i++)
  {
    for(int j = 0; j < outputWidth; j++)
    {
      if(j % 4 == 0){//red
        get_vmem(inst.tbank, redBase + i * inOffset + j) = get_vmem(inst.tbank, outBase + i * outOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+redBase + i * inOffset + j,get_vmem(inst.tbank, redBase + i * inOffset + j));
	}
	}
	#endif
      }else if(j % 4 == 1){
        get_vmem(inst.tbank, greenBase + i * inOffset + j) = get_vmem(inst.tbank, outBase + i * outOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+greenBase + i * inOffset + j,get_vmem(inst.tbank, greenBase + i * inOffset + j));
	}
	}
	#endif
      }else if(j % 4 == 2){
        get_vmem(inst.tbank, blueBase + i * inOffset + j) = get_vmem(inst.tbank, outBase + i * outOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+blueBase + i * inOffset + j,get_vmem(inst.tbank, blueBase + i * inOffset + j));
	}
	}
	#endif
      }else if(j % 4 == 3){
        get_vmem(inst.tbank, alphaBase + i * inOffset + j) = get_vmem(inst.tbank, outBase + i * outOffset + j);
	#ifdef MEMORY_MONITOR
	if(CDebugUI::memory_r_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] R [%04d]=>%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+outBase + i * outOffset + j,get_vmem(inst.tbank, outBase + i * outOffset + j));
	if(CDebugUI::memory_w_monitor){
	sc_time st= sc_time_stamp();
	ULONG temp_t = (ULONG)st.to_default_time_units();
	fprintf(CDebugUI::MemMonitor,"%d [ve][vmem][%d] W [%04d]<=%02x [ve]<-[ve]\n",
	temp_t/SYSTEM_CLOCK_TIME, inst.tbank, inst.tbank*4096+alphaBase + i * inOffset + j,get_vmem(inst.tbank, alphaBase + i * inOffset + j));
	}
	}
	#endif
      }
    }
  }
  //for(int w = 0; w < ((outputWidth+7)/8)*outputHeight*2; w++)
    ve_wait(((outputWidth+7)/8)*outputHeight*2);
}



void module_ve::vsp_verfiltk(ve_inst inst) 
{
#ifndef VE_RELEASE
	cout << "VE_VERFILTK called and issued\n";
#endif

};
