
"""

task makeJar(type: Copy) {
    //删除旧的jar包
    delete 'build/libs/ireadygo_keyadapter.jar'
    //原地址
    //from('build/intermediates/bundles/release/')
    from('build/intermediates/packaged-classes/release/')
    //导出jar包的地址
    into('build/libs/')
    //包含的jar包
    include('classes.jar')
    //重命名jar包为mysdk
    rename ('classes.jar', 'ireadygo_keyadapter.jar')
}
makeJar.dependsOn(build)

"""