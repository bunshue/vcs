--�ж�proc_TransInProc�洢�����Ƿ���ڣ�������ڽ���ɾ��
if exists(select name from sysobjects 
where name='proc_TransInProc'and type='p')
  drop proc proc_TransInProc  --ɾ���洢����
GO
create procedure proc_TransInProc
as
declare @truc int
select @truc=@@trancount
if @truc=0
begin tran p1
else
save tran pl
if (@truc=2)
begin
rollback tran pl
return 25
end
if(@truc=0)
commit tran pl
return 0
