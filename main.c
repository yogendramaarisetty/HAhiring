#include<stdio.h>
int opp(int n){
    int l=((n/12)+1)*12;
    if(n%12==0){
        return n-(6-(n%12))*2+1;
    }
    else if(n%12<=6){
        return n+(6-(n%12))*2+1;
    }
    
    else if(n%12>6){
        return n-((((n%12)-6)-1)*2+1);
    }
}

void main(){
    int n,t;
   char *strs[6]  = {"WS","MS","AS","AS","MS","WS"};
    scanf("%d",&t);
    for(int i=0;i<t;i++){
    scanf("%d",&n);
    int seat_count = n%6;
    if(seat_count==0){
        printf("%d %s\n",opp(n),"WS");
    }
    else{
        printf("%d %s\n",opp(n),strs[seat_count-1]);
      }
    }
}
