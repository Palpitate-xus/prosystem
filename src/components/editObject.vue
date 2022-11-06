<template>
    <div>
      <el-dialog
        :visible="dialogFormVisible"
        title="编辑">
        <el-form :model="form" label-width="85px">
          <el-form-item label="id:">
            <div>{{form.id}}</div>
          </el-form-item>
          <el-form-item label="Object:">
            <el-input v-model="form.object" ></el-input>
          </el-form-item>
          <el-form-item label="Field:">
            <el-select v-model="form.field" placeholder="请选择领域">
              <el-option
                v-for="item in fields"
                filterable
                :key="item.id"
                :label="item.field"
                :value="item.id"
              />
            </el-select>
          </el-form-item>

          <el-form-item label="Properties:">
            <el-tag
              :key="tag"
              v-for="tag in form.properties"
              closable
              :disable-transitions="false"
              @close="handleClose(tag)">
              {{tag}}
            </el-tag>
            <el-input
              class="input-new-tag"
              v-if="inputVisible"
              v-model="inputValue"
              ref="saveTagInput"
              size="small"
              @keyup.enter.native="handleInputConfirm"
              @blur="handleInputConfirm"
            >
            </el-input>
            <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="handle_save">确 定</el-button>
        </div>
      </el-dialog>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'editDialog',
    data(){
      return {
        tableData: [],
        dialogFormVisible: false,
        fieldsData: [],
        inputVisible: false,
        inputValue: '',
        form:{
          id: '',
          object: '',
          field: '',
          properties: [],
        },
        fields: [],
        classes:[],
      }
    },
    mounted(){
      this.fetch_field();
      this.fetch_class();
    },
    methods: {
      handleClose(tag) {
        this.form.properties.splice(this.form.properties.indexOf(tag), 1);
      },
      async fetch_field(){
        let _this = this;
        await axios.get('http://localhost:8000/api/get_fields').then((res) => {
          _this.fields = res.data.data;
          console.log(_this.fields);
        })
      },

      showInput() {
        this.inputVisible = true;
        this.$nextTick(_ => {
          this.$refs.saveTagInput.$refs.input.focus();
        });
      },

      handleInputConfirm() {
        let inputValue = this.inputValue;
        if (inputValue) {
          this.form.properties.push(inputValue);
        }
        this.inputVisible = false;
        this.inputValue = '';
      },

      async handle_save() {
        this.dialogFormVisible = false;
        console.log(this.form);
        await axios.post('http://localhost:8000/api/handle_update', this.form).then((res) => {
          console.log(res.data);
        })
      },
    }
  }
  </script>

<style>
.el-tag{
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>
