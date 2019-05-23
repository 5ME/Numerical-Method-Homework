% 程序7.3（递归梯形公式）利用梯形公式和连续增加的[a,b]子区间数
function T = rctrap( f,a,b,n )
% Input - f is the integrand input as a string 'f'. 
%         f是作为字符串'f'的被积函数输入
%       - a and b are upper and lower limits of integration.
%         a和b是积分的上限和下限
%       - n is the number of times for recursion. n是递归的次数
%Output - T is the recursive trapezoidal rule list. T是递归梯形公式序列
    M = 1;
    h = b - a;
    T = zeros(1, n+1);
    T(1) = h * (feval(f,a) + feval(f,b)) / 2;
    for j = 1:n
        M = 2 * M;
        h = h / 2;
        s = 0;
        for k = 1:M/2
            x = a + h*(2*k-1);
            s = s + feval(f,x);
        end
        T(j+1) = T(j)/2 + h*s;
    end
end

% % % % % % % % % % % % % % % % % % % % % % 
% 输入：
% f = @myfun;
% a = 1;
% b = 5;
% n = 3;
% T = rctrap(f, a, b, n)
% 
% 输出：
% T =
% 
%     2.4000    1.8667    1.6833    1.6290
% 
% 
% 
% 
% 
% 