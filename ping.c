//make two empty file with name upo.txt and s.txt
/*This is the program in c to check which of the systems are up right now
 * in the series od 10.104.X.X in the current N/W
 *The systems which are up will be stored in upips.txt
 * */
#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include<stdlib.h>

int main(){
long total=0;
int x=1,y=1;
char strmain[30];
char upip[20];
char str1[10],str2[10],ch;
FILE *pt,*ft;
for(;x<256;x++)
for(;y<256;y++)
{

strcpy(str1,"");

strcpy(str2,"");
strcpy(strmain,"ping -c 1 10.104.");
snprintf(str1, sizeof(str1), "%d", x);
snprintf(str2, sizeof(str2), "%d", y);


strcat(str1,".");
strcat(str1,str2);
//printf("%s\n",str1);
strcat(strmain,str1);
strcpy(upip,strmain);
strcat(strmain," | grep -c from >> upo.txt");
//printf("%s\n",strmain);
system(strmain);

pt=fopen("upo.txt","r+");
ft=fopen("upips.txt","a");

fseek(pt,-2,SEEK_END);


ch=fgetc(pt);
printf("%c\n",ch);
if(ch=='1')
{
printf("%s\n",upip);
fputs(upip,ft);
total++;

}

fclose(pt);

fclose(ft);


}






return 0;}

