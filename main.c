#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int current_sum=0,best_start_ind=0, best_end_ind=0,current_ind=0, best_sum=0;
/*
long long find_max(int* A, int i){
	if (i==0){	
		return A[i];
	}
	else if(find_max(A, i-1)
}
*/
int main() {
    	int i,j,k,l,n,t,A[100000],val=0, min;
	long long ans,ans2;
    	scanf("%d", &t);
    	for(i=0; i<t; i++){
        current_sum=best_start_ind=best_end_ind=current_ind=best_sum=0;
		ans=0, ans2=0;
        min=-10000000;
        int count=0;    
		scanf("%d", &n);
		for(k=0; k<n; k++){
			scanf("%d", &A[k]);
            if(A[k]<0){
                  count++;
                if (A[k]>min)
                    min = A[k];
            }
			if(A[k]>0){
				ans2+=A[k];
			}
			val=current_sum+A[k];
			if(val>0){
				if(current_sum==0){
					current_ind=k;
				}
				current_sum=val;
			}
			else
				current_sum=0;
			if(current_sum>best_sum){
				best_sum=current_sum;
				best_start_ind=current_ind;
				best_end_ind=k;
			}
		}
        if(count!=n){
		  for(j=best_start_ind; j<best_end_ind+1; j++){
			 ans+=A[j];
		  }
        }
            else ans=ans2=min;
		printf("%lld %lld\n", ans,ans2);	
	}	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
