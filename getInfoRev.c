#include <stdio.h>

char* help = "-all to get all information\n-main to get a answer of were the program thinks the main functions is\n-header analyze the header for information\n--help to show tags\n";
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
  for (int i = 0; i < 4; i++){
   if(argv[1][1] - flags[i][1] + argv[1][0] - flags[i][0] == 0){whichOne = i;}
  }
  if (whichOne == 3){
   printf("\n\n%s", help);
  }
  else if (whichOne == 2){
   printf("analysing the header\n");
  }
  else if (whichOne == 1){
   printf("finding the main function\n");
  }
  else if(whichOne == 0){
   printf("analysing everything\n");
  }
  else{
   printf("the flag you have specified does not exists");
  }
 }
}
