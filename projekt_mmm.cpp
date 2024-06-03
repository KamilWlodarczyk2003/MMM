#include <iostream>
#include <fstream>
#include <cmath>
#define PI 3.141592
using namespace std;

int main(){
	//setup**************************************
ifstream wejscie("dane.txt");
ofstream wyjscie("wyjscie.txt");
double m1,m2,k1,k2,b1,b2,X1,u,X2,dT=0.1,V1,V2,A1,A2,a,T;
bool czy_sinusoida;
wejscie>>czy_sinusoida;
if(czy_sinusoida){
	wejscie>>a>>m1>>m2>>k1>>k2>>b1>>b2>>T;
}else{
	wejscie>>a>>m1>>m2>>k1>>k2>>b1>>b2;
}

V1=0;
V2=0;
A1=0;
A2=0;
X1=0;
X2=0;
u=a;
	//matma**************************************
	
for(int i=0;i<1000;i++){
	if(czy_sinusoida){
		u=a*sin((1/T)*2*PI*dT*i)+a;
	}
	A2=u/m2-(X2-X1)*k2/m2-(V2-V1)*b2/m2;
	A1=-k1*X1/m1+k2*(X2-X1)/m1-b1*V1/m1+b2*(V2-V1)/m1;
	V2=V2+(A2/2)*dT;
	V1=V1+(A1/2)*dT;
	X2=X2+(V2/2)*dT;
	X1=X1+(V1/2)*dT;
	wyjscie<<i*dT<<";";
	wyjscie<<X1<<";";
	wyjscie<<X2<<";";
	wyjscie<<u<<endl;
}


wyjscie.close();
wejscie.close();

return 0;
}

