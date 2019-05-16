% 程序7.1（组合梯形公式）通过f(x)的M+1个等步长采样点逼近积分
function s = traprl(f,a,b,M)
% Input - f is the integrand input as a string 'f'. 
%         f是作为字符串'f'的被积函数输入
%       - a and b are upper and lower limits of integration.
%         a和b是积分的上限和下限
%       - M is the number of subintervals. M是等距子区间的数量
%Output - s is the trapezoidal rule sum. s是组合梯形公式结果
h = (b-a) / M;
s = 0;
for k = 1:(M-1)
    x = a + h*k;
    s = s + feval(f, x);
end
s = h * (feval(f,a) + feval(f,b))/2 + h*s;

end

% % % % % % % % % % % % % % % % % % % % % % % 
% 输入：
% a = 1;
% b = 6;
% M = 10;
% f = @myfun;
% s = traprl(f,a,b,M)
% 
% 输出：
% s =
% 
%     8.1939
% 
% 