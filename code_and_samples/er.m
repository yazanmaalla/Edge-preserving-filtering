function [r] = er(a,b)
tt=b;
th=0.150;
b=b(b>th);
m1=mean(mean(b));
[n m ]=size(b);

bb=(b-m1).^2;
v1=mean(mean(bb));
s1=v1^0.5;

sn1=20*log10(m1/s1);
ms1=mean(mean( (a-tt).^2));

c1= tt(tt>th);
c2= tt(tt<=th);
mc1=mean(mean(c1));
mc2=mean(mean(c2 ));

bb=(c1-mc1).^2;
vc1=mean(mean(bb));
sc1=vc1^0.5;
bb=(c2-mc2).^2;
vc2=mean(mean(bb));
sc2=vc2^0.5;

cnr=abs(mc1-mc2)/(( sc1*sc1+sc2*sc2)^0.5);
r=zeros(1,5);
r(1)=m1;
r(2)=v1;
r(3)=s1;
r(4)=sn1;
r(5)=ms1;
r(6)=cnr;
    

end

