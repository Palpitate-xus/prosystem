# prosystem

> A Vue.js project

基于知识图谱的产生式系统前端（Based on Vue2.x）

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

If you want to know more, check it in [Palpitate-xus's blog](https://palpitate-xus.github.io/blog_dev/blogs/code/2022/2210312.html)

## API文档：
| url                 | method | payload | response | mark    |
|---------------------|--------|---------|----------|---------|
| api/get_fields      | GET    | /       |          | 获取领域    |
| api/get_properties  | POST   | 领域id    |          | 获取属性    |
| api/handle_infer    | POST   | 属性id列表  |          | 进行推理    |
| api/get_objectsList | GET    | /       |          | 获取所有对象  |
| api/handle_delete   | POST   | 对象id列表  |          | 删除对象    |
| api/get_filterList  | GET    | /       |          | 获取过滤器数据 |
| api/handle_update   | POST   | 对象json  |          | 更新对象    |
| api/get_classList   | GET    | /       |          | 获取类列表   |
