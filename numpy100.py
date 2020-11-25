#1,导入numpy库并取别名为np
import numpy as np
#2,打印输出numpy的版本和配置信息 
print(np.__version__)
np.show_config()
#3,创建长度为10的零向量 
Z = np.zeros(10)
print(Z)
#4,获取数组所占内存大小
Z = np.zeros((10,10))
print(Z.itemsize)
print(Z.size*Z.itemsize)
#5. 怎么用命令行获取numpy add函数的文档说明？ 
np.info(np.add)
Z = np.ones((10, 10))
Z[1:-1, 1:-1] = 0
print (Z)
Z = np.ones((10, 10))
Z = np.pad(Z, (1,1), mode='constant', constant_values=0)
print (Z)
print(abs(3-3 * 1)<=10e-6)

