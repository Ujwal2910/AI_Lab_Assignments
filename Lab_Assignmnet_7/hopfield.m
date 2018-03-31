clear all;
close all;

%--------------------------------------------
% Patterns to store
% D, J, C, M
%--------------------------------------------
X = [1 1 1 1 -1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 1 -1;
1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 1 -1 -1;
-1 1 1 1 1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 1 1 1;
1 -1 -1 -1 1 1 1 -1 1 1 1 -1 1 -1 1 1 -1 -1 -1 1 1 -1 -1 -1 1]';

%figure;
%imshow(reshape(-X(:,1),5,5)');

%--------------------------------------------
% Learn the weights according to Hebb's rule 
%--------------------------------------------
[m,n] = size(X);
W = zeros(m,m);
for i = 1:n
	W = W + X(:,i)*X(:,i)';
endfor
W(logical(eye(size(W)))) = 0;
W = W/n;

%-------------------------------------------
% Dynamical (Linear) System and fixed points
%-------------------------------------------
x = X(:,1);
x(5)=-1*x(5);

figure(1);
subplot(1,2,1);
imshow(reshape(-X(:,1),5,5)');
subplot(1,2,2);
imshow(reshape(-x,5,5)');

y = x;
erry = 10;
while erry > 1
	yp = sign(W*y);	
	erry = norm(yp-y);
	y = yp;
	figure(2);
	imshow(reshape(-y, 5, 5)');
	pause();
endwhile

%--------------------------------------------
% Damaging 50 neurons!
%--------------------------------------------









