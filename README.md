# 旧版本同步镜像
1. 首先通过Travis CI每天定时更新代码
2. 然后在阿里云镜像服务中使用代码变化时自动构建镜像，把docker hub上的镜像自动同步到阿里云镜像服务仓库中

# 新版本同步镜像
1. 使用 github action 来同步镜像到阿里云镜像仓库
