

/******************************************************************************/
/**
*
* This function copies a memory region to another memory region
*
* @param 	s1 is starting address for destination
* @param 	s2 is starting address for the source
* @param 	n is the number of bytes to copy
*
* @return	Starting address for destination
*
****************************************************************************/
void *(memcpy_rom)(void * s1, const void * s2, u32 n)
{
	char *dst = (char *)s1;
	const char *src = (char *)s2;

	/*
	 * Loop and copy
	 */
	while (n-- != 0)
		*dst++ = *src++;
	return s1;
}


/******************************************************************************/
/**
*
* This function copies a string to another, the source string must be null-
* terminated.
*
* @param 	Dest is starting address for the destination string
* @param 	Src is starting address for the source string
*
* @return	Starting address for the destination string
*
****************************************************************************/
char *strcpy_rom(char *Dest, const char *Src)
{
	unsigned i;
	for (i=0; Src[i] != '\0'; ++i)
		Dest[i] = Src[i];
	Dest[i] = '\0';
	return Dest;
}

/******************************************************************************
*
* This function Measures the execution time
*
* @param	Current time , End time
*
* @return
*			None
*
* @note		None
*
*******************************************************************************/
void FsblMeasurePerfTime (XTime tCur, XTime tEnd)
{
	double tDiff = 0.0;
	double tPerfSeconds;
	XTime_GetTime(&tEnd);
	tDiff  = (double)tEnd - (double)tCur;

	/*
	 * Convert tPerf into Seconds
	 */
	tPerfSeconds = tDiff/COUNTS_PER_SECOND;

#if defined(STDOUT_BASEADDRESS)
	printf("%f seconds \r\n",tPerfSeconds);
#endif

}
#endif





