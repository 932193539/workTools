--lua弱表，主要是删除key或者value是table的一种元方法
--元表里的__mode字段包含k或者v；k表示key为弱引用；v表示value为弱引用
 
local testa = {}
tbl_key = {1}
testa[tbl_key] = 1
tbl_key = {2}
testa[tbl_key] = 2
 
--垃圾回收
collectgarbage()
 
local function PrintInfo()
 
	for k, v in pairs(testa) do
		print(k, "===", v)
		print("k[1]="..k[1])
	end
 
end
 
 
 local test = {1}
 local test = {2}
PrintInfo()
