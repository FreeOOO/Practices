#include <mirdef.h>
#include <miracl.h>
#include <malloc.h>
#include <sys/time.h>
#include <stdio.h>
#include <string.h>

#define NUM 2
#define MODE MR_CFB2
#define _NK 16

void encrypt_(aes *_aes,char *szAesKey,char *iv,char *szStr,long int sizetemp,int size){
	//加密
	struct timeval start,end;
	aes_init(_aes,MODE,_NK,szAesKey,iv);
	int len;
	gettimeofday(&start,NULL);
	for(long int i = 0;i < size;i++){
		len = aes_encrypt(_aes,&szStr[i * NUM]);
	}
	gettimeofday(&end,NULL);
	int timeuse = 1000000 * (end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;
	aes_end(_aes);
	printf("encrypt time:%d us\n",timeuse);			//输出微秒
}

void decrypt_(aes *_aes,char *szAesKey,char *iv,char *szStr,int sizearr,int size){
	//解密
	struct timeval start,end;
	aes_init(_aes,MODE,_NK,szAesKey,iv);
	gettimeofday(&start,NULL);
	int len;
	for(long int i = 0;i < size;i++){
		len = aes_decrypt(_aes,&szStr[i * NUM]);
	}
	gettimeofday(&end,NULL);
	int timeuse = 1000000 * (end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;
	aes_end(_aes);
	printf("decrypt time:%d us\n",timeuse);			//输出微秒
}

void AesTest(char *szStr1,char *miwen,char *mingwen)
{
	aes _aes;
	char szAesKey[] = "1234567890abcdef";		//加密密钥
	char iv[17] = "1213112342321432";			//用于生产密钥流
	long int size = strlen(szStr1);
	printf("%ld\n",size);
	long int sizearr = size;		//数组实际长度
	long int sizetemp = (sizearr % NUM == 0 ? sizearr : (sizearr / NUM + 1 ) * NUM);		//加密后数组长度
	char *szStr = (char *)malloc((sizetemp + 1) * sizeof(char));
	strcpy(szStr,szStr1);		//拷贝到新数组
	size = size % NUM != 0 ? size / NUM + 1 : size / NUM;		//密文分组长度
	encrypt_(&_aes,szAesKey,iv,szStr,sizetemp,size);
	strcpy(miwen,szStr);
	decrypt_(&_aes,szAesKey,iv,szStr,sizearr,size);
	strcpy(mingwen,szStr);
	free(szStr);
}

char *textFileRead(char *filename,long *lsize){
	char *text;
	long size;
	FILE *pf = fopen(filename,"rb");
	if(pf == NULL){
		printf("文件不存在");
		return NULL;
	}
	fseek(pf,0,SEEK_END);
	size = ftell(pf);
	text = (char*)malloc(size * sizeof(char));
	rewind(pf);
	fread(text,1,size,pf);
	*lsize = size;
	fclose(pf);
	return text;
}

int main(){
	FILE *outfpencrypt,*outfpdecrypt;
	outfpencrypt = fopen("./a.encrypt","wb");
	outfpdecrypt = fopen("./a.decrypt","wb");
	long a = 0;
	long *lSize=&a;
	char *buff,*miwen,*mingwen;
	char *file = "./a.txt";
	buff = textFileRead(file,lSize);
	miwen = (char *)malloc(sizeof(char) * (*lSize) + 100);
	mingwen = (char *)malloc(sizeof(char) * (*lSize));
	AesTest(buff,miwen,mingwen);
	fwrite(miwen,1,(*lSize),outfpencrypt);
	fwrite(mingwen,1,(*lSize),outfpdecrypt);
	free(buff);
	free(miwen);
	free(mingwen);
	fclose(outfpdecrypt);
	fclose(outfpencrypt);
}
