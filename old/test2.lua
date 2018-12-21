local testa = {}
local mt = {__mode = 'k'}
setmetatable(testa,mt)
 
tbl_key = {1}
testa[tbl_key] = 1
tbl_key = {2}
testa[tbl_key] = 2

tbl_key3 = {1}
 
--À¬»ø»ØÊÕ
collectgarbage()
 
local function PrintInfo()
 
	for k, v in pairs(testa) do
		print(k, "===", v)
		print("k[1]="..k[1])
	end
 
end
 
PrintInfo()


 print("tbl_key3",tbl_key3)
 print("tbl_key",tbl_key[1])