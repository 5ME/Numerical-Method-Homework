% ����7.3���ݹ����ι�ʽ���������ι�ʽ���������ӵ�[a,b]��������
function T = rctrap( f,a,b,n )
% Input - f is the integrand input as a string 'f'. 
%         f����Ϊ�ַ���'f'�ı�����������
%       - a and b are upper and lower limits of integration.
%         a��b�ǻ��ֵ����޺�����
%       - n is the number of times for recursion. n�ǵݹ�Ĵ���
%Output - T is the recursive trapezoidal rule list. T�ǵݹ����ι�ʽ����
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
% ���룺
% f = @myfun;
% a = 1;
% b = 5;
% n = 3;
% T = rctrap(f, a, b, n)
% 
% �����
% T =
% 
%     2.4000    1.8667    1.6833    1.6290
% 
% 
% 
% 
% 
% 