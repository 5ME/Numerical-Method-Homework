% ����7.1��������ι�ʽ��ͨ��f(x)��M+1���Ȳ���������ƽ�����
function s = traprl(f,a,b,M)
% Input - f is the integrand input as a string 'f'. 
%         f����Ϊ�ַ���'f'�ı�����������
%       - a and b are upper and lower limits of integration.
%         a��b�ǻ��ֵ����޺�����
%       - M is the number of subintervals. M�ǵȾ������������
%Output - s is the trapezoidal rule sum. s��������ι�ʽ���
h = (b-a) / M;
s = 0;
for k = 1:(M-1)
    x = a + h*k;
    s = s + feval(f, x);
end
s = h * (feval(f,a) + feval(f,b))/2 + h*s;

end

% % % % % % % % % % % % % % % % % % % % % % % 
% ���룺
% a = 1;
% b = 6;
% M = 10;
% f = @myfun;
% s = traprl(f,a,b,M)
% 
% �����
% s =
% 
%     8.1939
% 
% 