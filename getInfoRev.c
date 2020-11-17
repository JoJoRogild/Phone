#include <stdio.h>

int cfileexists(const char * filename){
    FILE *file;
    if (file = fopen(filename, "r")){
        fclose(file);
        return 1;
    }
    return 0;
}

int main(int argc, char *argv[]){
 printf("this program can check which programming language and if it stripped all the simple information in a program an put it out in a very readable format\n");
 if (argc == 1){printf("you need to specify a program. DICKHEAD\n");}
 else if (argc == 2){
  if(cfileexists(argv[1]) == 1){
   printf("starting the scanning on: %s\n", argv[1]); 
  }
  else{
   printf("the file u have specified does not exitst. plz specifi a real file: idk: %s\n", argv[1]);
   return 1;
  }
 }
}
