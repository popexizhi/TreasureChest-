[build] 
 gcc bind_one.c -o bind_one -lpthread -lm

[readme]
 bind_one 运行当前绑定0号CPU 100% 使用，测试使用,如果要指定其他号CPU 修改 int use_num 和 i的定义即可.
