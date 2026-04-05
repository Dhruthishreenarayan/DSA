int lengthOfLastWord(char* s) {
    int a=0;
    int i=strlen(s)-1;
    while(i>=0 && s[i]==' ')
    { i--; }
    while(i>=0 && s[i]!=' '){
        a++;
        i--;
    }return a;
   
}