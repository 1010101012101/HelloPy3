import h5py
f=h5py.File("data/myh5py.hdf5","w")
#deset1是数据集的name，（20,）代表数据集的shape，i代表的是数据集的元素类型
d1=f.create_dataset("dset1", (20,), 'i')
d1[2] = 5
for key in f.keys():
    print("HHHA:0====>")
    print(key)
    print(f[key].name)
    print(f[key].shape)
    print(f[key].value)

print(f.keys)

d2 = f.create_dataset("dset2", (10,), "i")
d2[1]=3
for key in f.keys():
    print("HHHA:1====>")
    print(key)
    print(f[key].name)
    print(f[key].shape)
    print(f[key].value)