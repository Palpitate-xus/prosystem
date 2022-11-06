<template>
  <div class="home">
    <el-card>
      <template #header>
        <div class="card-header">
          <el-tag>请选择领域：</el-tag>
          <el-select v-model="value_field" @change="fieldChange">
            <el-option
              v-for="item in fields"
              filterable
              :key="item.id"
              :label="item.field"
              :value="item.id"
            />
          </el-select>

          <el-button @click="handleInfer">推理</el-button>
        </div>
        <el-divider />
        <el-transfer
          style="text-align: left; display: inline-block"
          v-model="value_chosen"
          :data="properties"
          filterable
          :left-default-checked="[]"
          :right-default-checked="[]"
          :titles="['可选属性', '已选属性']"
          :format="{
            noChecked: '${total}',
            hasChecked: '${checked}/${total}'
          }"
          @change="handleChange"
          />
      </template>
          <el-collapse  accordion>
      <el-collapse-item title="如何使用本系统" name="1">
        <div>
          本系统是以知识图谱为基础的产生式系统
        </div>
        <div>
          请在输入框中输入属性的ID，按下推理按钮即可产生结果。
        </div>
      </el-collapse-item>
      <el-collapse-item title="什么是推理规则" name="2">
        <div>推理规则是以事实为基础的，通过属性进行推断的一套方法。其中分为系统内置、用户自定义两种规则。</div>
      </el-collapse-item>
      <el-collapse-item title="如何对推理规则进行修改" name="3">
        <div>用户可以在Settings页面中自定义规则或者修改系统内置的规则。</div>
      </el-collapse-item>
      <el-collapse-item title="什么是类、对象、属性" name="4">
        <div>所谓对象就是真实世界中的实体，对象与实体是一一对应的，也就是说现实世界中每一个实体都是一个对象，它是一种具体的概念。
类是具备某些共同特征的实体的集合，它是一种抽象的概念，用程序设计的语言来说，类是一种抽象的数据类型，它是对所具有相同特征实体的抽象。</div>
        <div>不同对象具有相同特点，称为属性</div>
      </el-collapse-item>
      <el-collapse-item title="如何对类、对象、属性进行修改" name="5">
        <div>用户可以在Settings页面中自定义类、对象、和属性，并对系统内置的类、对象、属性进行修改</div>
      </el-collapse-item>
    </el-collapse>
    </el-card>



  </div>
</template>

  <script>
  import axios from 'axios'
  export default {
    name: 'HomeView',
    data(){
      return {
        fields: [],
        properties: [],
        value_field: '1',
        value_chosen: [],
      }
    },
    mounted(){
      this.fetch_field();
      this.fetch_properties('1');
      this.value_field = 1;
    },
    methods:{
      async fetch_field(){
        let _this = this;
        await axios.get('http://localhost:8000/api/get_fields').then((res) => {
        _this.fields = res.data.data;
        console.log(_this.fields);
        })
      },
      async fetch_properties(id){
        let _this = this;
        _this.properties = [];
        await axios.post('http://localhost:8000/api/get_properties', {'id': id}).then((res) => {
        const dd = res.data
        for (let index = 0; index < dd.data.length; index++) {
          _this.properties.push({
            key: dd.data[index].id,
            label: dd.data[index].property
          })
        }
        console.log(this.properties)
      })
      },
      fieldChange(event, item){
        console.log(event);
        this.fetch_properties(event);
      },
      handleChange(){
        console.log(this.value_chosen);
      },
      async handleInfer(){
        if (this.value_chosen == []) {
          this.$alert("当前未选中任何属性", "Error", {confirmButtonText: '确定'})
        } else {
          if(this.value_chosen.length == 1){
            this.value_chosen.push(this.value_chosen[0])
          }
          await axios.post('http://localhost:8000/api/handle_infer', {'data': this.value_chosen}).then((res) => {
            console.log(res.data.data);
            let result = res.data.data
            this.$alert(result, "推理结果如下：", {
              confirmButtonText: '确定',
            });
          })
        }

      },
    }
  }
  </script>

<style>

</style>
