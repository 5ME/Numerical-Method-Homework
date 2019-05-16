% ����7.1���������ɭ��ʽ��ͨ��f(x)��2M+1���Ȳ���������ƽ�����
function s = simprl(f,a,b,M)
% Input - f is the integrand input as a string 'f'. 
%         f����Ϊ�ַ���'f'�ı�����������
%       - a and b are upper and lower limits of integration.
%         a��b�ǻ��ֵ����޺�����
%       - M is the number of subintervals. M�ǵȾ������������
%Output - s is the simpson rule sum. s���������ɭ��ʽ���
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
% ���룺
% a = 1;
% b = 6;
% M = 5;
% f = @myfun;
% s = simprl(f,a,b,M)
% 
% �����
% s =
% 
%     8.1830
% 
% 
