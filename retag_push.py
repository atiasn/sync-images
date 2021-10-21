#!/usr/bin/python3

import os


def get_image_list():
    with open('sync_images.txt', 'r') as f:
        images = f.readlines()
    sync_images = []
    for img in images:
        img = img.strip()
        if 'docker.io/' in img:
            sync_images.append(img.replace('docker.io/', ''))
        else:
            sync_images.append(img)
    return sync_images


def retag_push():
    sync_images = get_image_list()
    ali_registry = 'registry.cn-chengdu.aliyuncs.com'
    ali_namespace = 'atiasn'

    for img in sync_images:
        print(f'基础镜像： {img}')
        base_img = 'docker.io/' + img
        ali_img = f'{ali_registry}/{ali_namespace}/{img}'
        pull_cmd = 'docker pull ' + base_img
        retag_cmd = f'docker tag {base_img} ' + ali_img
        push_cmd = 'docker push ' + ali_img
        print(f'拉取镜像的命令：{pull_cmd}')
        code = os.system(pull_cmd)
        if code != 0:
            raise RuntimeError(f'拉取镜像 {base_img} 失败')

        print(f'retag 镜像的命令：{retag_cmd}')
        code = os.system(retag_cmd)
        if code != 0:
            raise RuntimeError(f'retag 镜像 {base_img} 失败')

        print(f'push 镜像到阿里云的命令：{push_cmd}')
        code = os.system(push_cmd)
        if code != 0:
            raise RuntimeError(f'push 镜像 {ali_img} 到阿里云失败')


if __name__ == '__main__':
    retag_push()
