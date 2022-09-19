#include <stdio.h>
#include <GL/glx.h>
#include "rgb.h"

/******************************************************************************/

void rgbCreateFloatImage(RGBImageRec *imageIn, RGBNewImageRec *imageOut)
{
    GLubyte *rawData;
    GLint x, y;
    GLfloat *fltImage, *ptr;
    GLfloat alpha;
    GLint imageWidth, imageHeight;

    imageWidth = imageIn->sizeX;
    imageHeight = imageIn->sizeY;
    rawData = imageIn->data;

    imageOut->imageSize = imageWidth * imageHeight * sizeof(GLfloat) * 4;
    fltImage = (float *)malloc(imageOut->imageSize);
    imageOut->fltImage = fltImage;
    if (NULL == fltImage) {
	fprintf(stderr, "Out of memory!\n");
	exit(1);
    }

    ptr = fltImage;
    for (y = 0; y < imageHeight; y++) {
        for (x = 0; x < imageWidth; x++) {
            *ptr++ = *rawData++ / 255.0;
            alpha = *ptr++ = *rawData++ / 255.0;
            *ptr++ = *rawData++ / 255.0;
            *ptr++ = alpha;
        }
    }
}

/******************************************************************************/

void rgbMakeNewImage(RGBNewImageRec *imageData)
{
    GLint imageWidth = imageData->imageWidth;
    GLint imageHeight = imageData->imageHeight;
    GLboolean swapBytes = imageData->swapBytes;
    GLboolean alignShift = imageData->alignShift; 
    GLenum type = imageData->type;
    GLenum format = imageData->format;
    void *newImage;
    GLfloat *myImage = imageData->fltImage;

    int components;
    int bytesPerComp;
    int i, j, k;
    int index;
    GLfloat indexScale;
    int imageSize;

    imageData->copyFormat = GL_COLOR;
    index = 0;

    switch(type) {
      case GL_BYTE:
        bytesPerComp = 1;
        break;
      case GL_UNSIGNED_BYTE:
        bytesPerComp = 1;
        break;
      case GL_INT:
        bytesPerComp = 4;
        break;
      case GL_UNSIGNED_INT:
        bytesPerComp = 4;
        break;
      case GL_BITMAP:
        break;
      case GL_FLOAT:
        bytesPerComp = 4;
        break;
      case GL_UNSIGNED_SHORT:
        bytesPerComp = 2;
        break;
      case GL_SHORT:
        bytesPerComp = 2;
        break;
      case GL_UNSIGNED_BYTE_3_3_2_EXT:
        bytesPerComp = 1;
        break;
      case GL_UNSIGNED_SHORT_4_4_4_4_EXT:
        bytesPerComp = 2;
        break;
      case GL_UNSIGNED_SHORT_5_5_5_1_EXT:
        bytesPerComp = 2;
        break;
      case GL_UNSIGNED_INT_8_8_8_8_EXT:
        bytesPerComp = 4;
        break;
      case GL_UNSIGNED_INT_10_10_10_2_EXT:
        bytesPerComp = 4;
        break;
    }

    switch(format) {
      case GL_RGB:
        components = 3;
        break;
      case GL_RED:
        components = 1;
        break;
      case GL_GREEN:
        components = 1;
        break;
      case GL_BLUE:
        components = 1;
        break;
      case GL_ALPHA:
        components = 1;
        break;
      case GL_LUMINANCE_ALPHA:
        components = 2;
        break;
      case GL_LUMINANCE:
        components = 1;
        break;
      case GL_RGBA:
        components = 4;
        break;
      case GL_COLOR_INDEX:
        components = 1;
        index = 1;
        break;
      case GL_DEPTH_COMPONENT:
        components = 1;
        imageData->copyFormat = GL_DEPTH;
        break;
      case GL_STENCIL_INDEX:
        components = 1;
        index = 1;
        imageData->copyFormat = GL_STENCIL;
        break;
    }

    switch (type) {
      case GL_UNSIGNED_BYTE_3_3_2_EXT:
      case GL_UNSIGNED_SHORT_4_4_4_4_EXT:
      case GL_UNSIGNED_SHORT_5_5_5_1_EXT:
      case GL_UNSIGNED_INT_8_8_8_8_EXT:
      case GL_UNSIGNED_INT_10_10_10_2_EXT:
        components = 1;
	index = 0;
	break;
    }

    if (index) {
	GLint bufferbits, typebits;
	switch (format) {
	  case GL_COLOR_INDEX:
	    glGetIntegerv(GL_INDEX_BITS, &bufferbits);
	    break;
	  case GL_STENCIL_INDEX:
	    glGetIntegerv(GL_STENCIL_BITS, &bufferbits);
	    break;
	}
	imageData->maxIndex = (bufferbits > 0) ? ~(~1 << bufferbits-1) : 0;
	switch (type) {
	   case GL_BITMAP:
	   case GL_FLOAT:
	     typebits = bufferbits;
	     break;
	   case GL_BYTE:
	     typebits = 8 * sizeof(GLbyte) - 1;
	     break;
	   case GL_UNSIGNED_BYTE:
	     typebits = 8 * sizeof(GLubyte);
	     break;
	   case GL_INT:
	     typebits = 8 * sizeof(GLint) - 1;
	     break;
	   case GL_UNSIGNED_INT:
	     typebits = 8 * sizeof(GLuint);
	     break;
	   case GL_SHORT:
	     typebits = 8 * sizeof(GLshort) - 1;
	     break;
	   case GL_UNSIGNED_SHORT:
	     typebits = 8 * sizeof(GLushort);
	     break;
	   case GL_UNSIGNED_BYTE_3_3_2_EXT:
	     typebits = 8 * sizeof(GLubyte);
	     break;
	   case GL_UNSIGNED_SHORT_4_4_4_4_EXT:
	   case GL_UNSIGNED_SHORT_5_5_5_1_EXT:
	     typebits = 8 * sizeof(GLushort);
	     break;
	   case GL_UNSIGNED_INT_8_8_8_8_EXT:
	   case GL_UNSIGNED_INT_10_10_10_2_EXT:
	     typebits = 8 * sizeof(GLuint);
	     break;
	}
	if (typebits < bufferbits) {
	    indexScale = (GLfloat)pow(2.0, (double)typebits) - 1.0;
	} else {
	    indexScale = (GLfloat)pow(2.0, (double)bufferbits) - 1.0;
	}
    } else {
	imageData->maxIndex = 0;
	indexScale = 0;
    }

    /* Build the new image */
    if (imageData->oldImage) {
	free((void *)((int)(imageData->oldImage)&0xfffffffc));
    }

    if (type != GL_BITMAP) {
        imageSize = imageWidth * imageHeight * components * bytesPerComp;
    } else {
        imageSize = ((imageWidth + 7) / 8) * imageHeight;
    }
    newImage = (void *)malloc(imageSize+3);
    if (NULL == newImage) {
	fprintf(stderr, "Out of memory!\n");
	exit(1);
    }

    if (format == GL_GREEN) {
	myImage += 1;
    } else if (format == GL_BLUE ||
	       format == GL_LUMINANCE ||
               format == GL_LUMINANCE_ALPHA) {
	myImage += 2;
    } else if (format == GL_ALPHA) {
	myImage += 3;
    }

    switch (type) {
	case GL_BITMAP:
	    {
		GLubyte *data;
		GLint bit;
		GLubyte byte;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    bit = 0;
		    byte = 0;
		    for (j = 0; j < imageWidth; j++) {
			if (*myImage++ > 0.5) {
			    if (swapBytes) {
				byte |= 1 << (7 - bit);
			    } else {
				byte |= 1 << bit;
			    }
			}
			bit++;
			if (bit == 8) {
			    bit = 0;
			    *data++ = byte;
			    byte = 0;
			}
			myImage += 3;
		    }
		    if (bit) {
			*data++ = byte;
		    }
		}
	    } 
	    break;
	case GL_UNSIGNED_BYTE:
	    {
		GLubyte *data;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {
			for (k = 0; k < components; k++) {
			    if (index) {
				*data++ = *myImage++ * indexScale;
			    } else {
				*data++ = *myImage++ * 255.0;
			    }
			}
			myImage += (4 - components);
		    }
		}
	    }
	    break;
	case GL_BYTE:
	    {
		GLbyte *data;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {
			for (k = 0; k < components; k++) {
			    if (index) {
				*data++ = *myImage++ * indexScale;
			    } else {
				*data++ = *myImage++ * 127.0;
			    }
			}
			myImage+=(4 - components);
		    }
		}
	    }
	    break;
	case GL_UNSIGNED_SHORT:
	    {
		GLushort *data;
		GLubyte *temp1, *temp2;
		GLushort answer;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {
			for (k = 0; k < components; k++) {
			    if (index) {
				answer = *myImage++ * indexScale;
			    } else {
				answer = *myImage++ * (GLfloat)65535.0;
			    }
			    if (swapBytes) {
				temp2 = (GLubyte *)&answer;
				temp1 = (GLubyte *)data;
				temp1[0] = temp2[1];
				temp1[1] = temp2[0];
			    } else {
				data[0] = answer;
			    }
			    data++;
			}
			myImage += (4 - components);
		    }
		}
	    } 
	    break;
	case GL_SHORT:
	    {
		GLshort *data;
		GLubyte *temp1, *temp2;
		GLshort answer;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {
			for (k = 0; k < components; k++) {
			    if (index) {
				answer = *myImage++ * indexScale;
			    } else {
				answer = *myImage++ * (GLfloat)32767.0;
			    }
			    if (swapBytes) {
				temp2 = (GLubyte *)&answer;
				temp1 = (GLubyte *)data;
				temp1[0] = temp2[1];
				temp1[1] = temp2[0];
			    } else {
				data[0] = answer;
			    }
			    data++;
			}
			myImage += (4 - components);
		    }
		}
	    }
	    break;
	case GL_INT:
	    {
		GLint *data;
		GLubyte *temp1, *temp2;
		GLint answer;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {
			for (k = 0; k < components; k++) {
			    if (index) {
				answer = *myImage++ * indexScale;
			    } else {
				answer = *myImage++ * (GLfloat)2147482500.0;
			    }
			    if (swapBytes) {
				temp2 = (GLubyte *)&answer;
				temp1 = (GLubyte *)data;
				temp1[0] = temp2[3];
				temp1[1] = temp2[2];
				temp1[2] = temp2[1];
				temp1[3] = temp2[0];
			    } else {
				data[0] = answer;
			    }
			    data++;
			}
			myImage += (4 - components);
		    }
		}
	    }
	    break;
	case GL_UNSIGNED_INT:
	    {
		GLuint *data;
		GLubyte *temp1, *temp2;
		GLuint answer;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {
			for (k = 0; k < components; k++) {
			    if (index) {
				answer = *myImage++ * indexScale;
			    } else {
				answer = *myImage++ * (GLfloat)4294965000.0;
			    }
			    if (swapBytes) {
				temp2 = (GLubyte *)&answer;
				temp1 = (GLubyte *)data;
				temp1[0] = temp2[3];
				temp1[1] = temp2[2];
				temp1[2] = temp2[1];
				temp1[3] = temp2[0];
			    } else {
				data[0] = answer;
			    }
			    data++;
			}
			myImage += (4 - components);
		    }
		}
	    }
	    break;
	case GL_FLOAT:
	    {
		GLfloat *data;
		GLubyte *temp1, *temp2;
		GLfloat answer;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {
			for (k = 0; k < components; k++) {
			    if (index) {
				answer = *myImage++ * indexScale;
			    } else {
				answer = *myImage++;
			    }
			    if (swapBytes) {
				temp2 = (GLubyte *)&answer;
				temp1 = (GLubyte *)data;
				temp1[0] = temp2[3];
				temp1[1] = temp2[2];
				temp1[2] = temp2[1];
				temp1[3] = temp2[0];
			    } else {
				data[0] = answer;
			    }
			    data++;
			}
			myImage += (4 - components);
		    }
		}
	    }
	    break;
	case GL_UNSIGNED_BYTE_3_3_2_EXT:
	    {
		GLubyte *data;
		GLubyte *answer, swapped_answer[4];
		GLfloat *invalue;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {

			/* first bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data = ((GLubyte)(*invalue * 7) << 5) & 0xE0;

			/* second bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLubyte)(*invalue * 7) << 2) & 0x1C;

			/* third bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= (GLubyte)(*invalue * 3) & 0x03;

			data++;
			myImage += 1; /* skip the final component */
		    }
		}
	    }
	    break;
	case GL_UNSIGNED_SHORT_4_4_4_4_EXT:
	    {
		GLushort *data;
		GLubyte *answer, swapped_answer[4];
		GLfloat *invalue;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {

			/* first bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data = ((GLushort)(*invalue * 15) << 12) & 0xF000;

			/* second bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLushort)(*invalue * 15) << 8) & 0x0F00;

			/* third bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLushort)(*invalue * 15) << 4) & 0x00F0;

			/* fourth bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= (GLushort)(*invalue * 15) & 0x000F;

			data++;
		    }
		}
	    }
	    break;
	case GL_UNSIGNED_SHORT_5_5_5_1_EXT:
	    {
		GLushort *data;
		GLubyte *answer, swapped_answer[4];
		GLfloat *invalue;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {

			/* first bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data = ((GLushort)(*invalue * 31) << 11) & 0xF800;

			/* second bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLushort)(*invalue * 31) << 6) & 0x07C0;

			/* third bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLushort)(*invalue * 31) << 1) & 0x003E;

			/* fourth bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= (GLushort)(*invalue) & 0x0001;

			data++;
		    }
		}
	    }
	    break;
	case GL_UNSIGNED_INT_8_8_8_8_EXT:
	    {
		GLuint *data;
		GLubyte *answer, swapped_answer[4];
		GLfloat *invalue;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {

			/* first bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data = ((GLuint)(*invalue * 255) << 24) & 0xFF000000;

			/* second bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLushort)(*invalue * 255) << 16) &
				 0x00FF0000;

			/* third bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLuint)(*invalue * 255) << 8) & 0x0000FF00;

			/* fourth bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= (GLuint)(*invalue * 255) & 0x000000FF;

			data++;
		    }
		}
	    }
	    break;
	case GL_UNSIGNED_INT_10_10_10_2_EXT:
	    {
		GLuint *data;
		GLubyte *answer, swapped_answer[4];
		GLfloat *invalue;

		data = newImage;
		for (i = 0; i < imageHeight; i++) {
		    for (j = 0; j < imageWidth; j++) {

			/* first bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data = ((GLuint)(*invalue * 1023) << 22) & 0xFFC00000;

			/* second bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLuint)(*invalue * 1023) << 12) & 0x003FF000;

			/* third bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= ((GLuint)(*invalue * 1023) << 2) & 0x00000FFC;

			/* fourth bitfield */
			invalue = myImage++;
			if (swapBytes) {
			    answer = (GLubyte *)invalue;
			    swapped_answer[0] = answer[3];
			    swapped_answer[1] = answer[2];
			    swapped_answer[2] = answer[1];
			    swapped_answer[3] = answer[0];
			    invalue = (GLfloat *)swapped_answer;
			}
			*data |= (GLuint)(*invalue * 3) & 0x00000003;

			data++;
		    }
		}
	    }
	    break;
    } 

    if (alignShift) {
        memcpy((void *)(((int)newImage)+alignShift), newImage, imageSize);
        newImage = (void *)(((int)newImage)+alignShift);
    }
    imageData->newImage = newImage;
}

/******************************************************************************/
