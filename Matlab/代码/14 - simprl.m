% 程序7.1（组合辛普森公式）通过f(x)的2M+1个等步长采样点逼近积分
function s = simprl(f,a,b,M)
% Input - f is the integrand input as a string 'f'. 
%         f是作为字符串'f'的被积函数输入
%       - a and b are upper and lower limits of integration.
%         a和b是积分的上限和下限
%       - M is the number of subintervals. M是等距子区间的数量
%Output - s is the simpson rule sum. s是组合辛普森公式结果
h = (b-a) / (2*M);
s1 = 0;
s2 = 0;
for k = 1:M
    x = a + h*(2*k-1);
    s1 = s1 + feval(f, x);
end
for k = 1:(M-1)
    x = a + h*2*k;
    s2 = s2 + feval(f, x);
end
s = h * (feval(f,a) + feval(f,b) + 4*s1 + 2*s2)/3;

end

% % % % % % % % % % % % % % % % % % % % % % % 
% 输入：
% a = 1;
% b = 6;
% M = 5;
% f = @myfun;
% s = simprl(f,a,b,M)
% 
% 输出：
% s =
% 
%     8.1830
% 
% 
