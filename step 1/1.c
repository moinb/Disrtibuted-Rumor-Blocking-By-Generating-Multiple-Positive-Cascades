#include<stdio.h>
#include<stdlib.h>
int main(){
	int a, b;
	FILE *fp, *fw;
	fp = fopen("facebook_combined.txt", "r");
	fw = fopen("out.txt", "w");
	while(fscanf(fp, "%d %d", &a, &b) != EOF){
		if((a <= 50) && (b <= 50))
			fprintf(fw, "%d %d\n", a, b);
	}
	fclose(fp);
	fclose(fw);
}
