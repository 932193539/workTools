--lua������Ҫ��ɾ��key����value��table��һ��Ԫ����
--Ԫ�����__mode�ֶΰ���k����v��k��ʾkeyΪ�����ã�v��ʾvalueΪ������
 
local testa = {}
tbl_key = {1}
testa[tbl_key] = 1
tbl_key = {2}
testa[tbl_key] = 2
 
--��������
collectgarbage()
 
local function PrintInfo()
 
	for k, v in pairs(testa) do
		print(k, "===", v)
		print("k[1]="..k[1])
	end
 
end
 
PrintInfo()
