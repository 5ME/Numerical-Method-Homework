% 程序7.4（龙贝格积分）生成J≥K的逼近表R(J,K)，并以R(J+1,J+1)为最终解来逼近积分
function [R, quad, err, h] = romber(f, a, b, n, tol)
% Input - f is the integrand input as a string 'f'. 
%         f是作为字符串'f'的被积函数输入
%       - a and b are upper and lower limits of integration.
%         a和b是积分的上限和下限
%       - n is the maximum number of rows in the table. 
%         n是表中的最大行数
%       - tol is the tolerance. tol是容差
%Output - R is the Romberg table. R是Romberg表
%       - quad is the quadrature value. quad是正交值
%       - err is the error estimate. err是误差
%       - h is the smallest step size used. h是使用的最小步长
    M = 1;
    h = b - a;
    err = 1;
    J = 0;
    R = zeros(4,4);
    R(1,1) = h * (feval(f,a) + feval(f,b)) / 2;
    while ((err>tol)&&(J<n)) || (J<4)
        J = J + 1;
        h = h / 2;
        s = 0;
        for p = 1:M
            x = a + h*(2*p-1);
            s = s + feval(f,x);
        end
        R(J+1,1) = R(J,1) / 2 + h*s;
        M = 2 * M;
        for K = 1:J
            R(J+1, K+1) = R(J+1, K) + (R(J+1, K) - R(J,K)) / (4^K - 1);
        end
        err = abs(R(J,J) - R(J+1,K+1));
    end
    quad = R(J+1, J+1);

end

