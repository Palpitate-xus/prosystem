# prosystem

基于知识图谱的产生式系统

### Build Setup of BackEnd

```bash
# install dependencies
pip install -r requirement.txt

# serve with hot reload at localhost:8080
python manage.py runserver
```

## Build Setup of FrontEnd

```bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```



## API文档：

| url                 | method | payload | response | mark    |
| ------------------- | ------ | ------- | -------- | ------- |
| api/get_fields      | GET    | /       | 领域列表     | 获取领域    |
| api/get_properties  | POST   | 领域id    | 属性列表     | 获取属性    |
| api/handle_infer    | POST   | 属性id列表  | 对象列表     | 进行推理    |
| api/get_objectsList | GET    | /       | 对象列表     | 获取所有对象  |
| api/handle_delete   | POST   | 对象id列表  | success  | 删除对象    |
| api/get_filterList  | GET    | /       | 领域/属性列表  | 获取过滤器数据 |
| api/handle_update   | POST   | 对象json  | success  | 更新对象    |
| api/handle_field    | POST   | 领域列表    | success  | 增加领域    |

If you want to know more, check it in [Palpitate-xus's blog](https://palpitate-xus.github.io/blog_dev/blogs/code/2022/2210312.html)
