--�ж��Ƿ������Ϊ��tri_delete_laborage���Ĵ�����
if exists(
select name from sysobjects where name='tri_delete_laborage' 
and type='TR')
drop trigger tri_delete_laborage--ɾ���Ѿ����ڵĴ�����
go
create trigger tri_delete_laborage--����������
on Ա���� for delete
as 
begin
if @@rowcount>1
  begin
    rollback transaction
    raiserror('ÿ��ֻ��ɾ��һ����¼',16,1)
  end
end
--��������
declare @id varchar(50)
select @id = Ա����� from deleted
delete нˮ�� where Ա����� = @id
go