<template>
  <div>
    <el-dialog
      :visible.sync="fieldEditVisible"
      title="编辑"
      style="margin: 0 auto; text-align: center; width: 75%"
    >

      <el-input v-model="input" placeholder="请输入内容" style="width: 200px"></el-input>
      <el-button @click="handleAddField" icon="el-icon-plus">增加领域</el-button>
      <el-table
        :data="form.fields"
        style="width: 67.3%; margin: 0 auto">
        <el-table-column
          prop="id"
          label="id"
          width="100">
        </el-table-column>
        <el-table-column
          prop="field"
          label="领域"
          width="180">
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "editField",
  data(){
    return {
      fieldEditVisible: false,
      fieldsData: [],
      inputVisible: false,
      input: '',
      form:{
        fields: [],
      },
    }
  },
  mounted(){
    this.fetch_field();
  },
  methods: {
    async fetch_field(){
      let _this = this;
      await axios.get('http://localhost:8000/api/get_fields').then((res) => {
        _this.fieldsData = res.data.data;
        _this.form.fields = _this.fieldsData
        console.log(_this.fieldsData);
      })
    },

    async handleAddField() {
      if(this.input != ''){
        this.form.fields.push(this.input);
        await axios.post('http://localhost:8000/api/handle_field', this.form).then((res) => {
          console.log(res.data);
        }).catch((res) => {
          console.log(res)
        })
      }
      await this.fetch_field();
    },


  }
}
</script>

<style scoped>

</style>
