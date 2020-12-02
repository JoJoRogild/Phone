#include <stdio.h>

char flags[4][10] = {"-A", "-main", "-header", "--help"};
int whichOne = -1;

int cfileexists(const char * filename){
    FILE *file;
    if (file = fopen(filename, "r")){
        fclose(file);
        return 1;
    }
    return 0;
}

int main(int argc, char *argv[]){
 printf("this program can check which programming language and stuff all the simple information in a program an put it out in a very readable format\nSyntax: getInfoRev \"flag\" \"file\"\n");
 if (argc == 1){printf("you need to specify a program. DICKHEAD\n");}
 else if (argc == 2){
  if(cfileexists(argv[1]) == 1){
   printf("starting the basic scann on: %s\n", argv[1]); 
  }
  else{
   printf("the file you specified does not exists\n");
  }
 }
 else if (argc == 3){
  if(cfileexists(argv[2]) == 0){
   printf("the file you specified does not exists\n");
  }
  else{
   for (int i = 0; i < 5; i++){
    if(i > 3){printf("the flag you have specified does not exists. use --help for getting imformation\n");return 0;}
    else if(strncmp(argv[1], flags[i], 2) == 0){whichOne == i;}
   }
   printf("the file you have specified is: %s  the flag you have specified is: %d\n", argv[2], whichOne);
  }
 }
}
