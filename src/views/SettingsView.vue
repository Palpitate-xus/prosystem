<template>
  <div>
    <el-button @click="handleDelete" type="danger" icon="el-icon-delete">批量删除</el-button>
    <el-button @click="handleAdd" icon="el-icon-plus">新增对象</el-button>
    <el-button @click="get_list" icon="el-icon-setting">领域管理</el-button>
    <el-button @click="get_list" type="primary">刷新</el-button>
    <el-table
      v-loading="loading"
      ref="filterTable"
      :data="tableData"
      style="width: 100%"
      stripe
      @selection-change="handleSelectionChange">
      <el-table-column
      type="selection"
      />
      <el-table-column
       label="id"
       prop="id"
       sortable
       />

       <el-table-column
        label="Object"
        prop="object"
        sortable
        />

        <el-table-column
        label="Field"
        prop="field"
        sortable
        :filters="filterDataField"
        :filter-method="filterHandlerField"
        />

      <el-table-column
        prop="properties"
        label="Property"
        :filters="filterDataProperty"
        :filter-method="filterTag"
        filter-placement="bottom-end">
        <template slot-scope="scope">
          <el-tag
            v-for="i in scope.row.properties"
            :key="i.id"
            size="small"
            style="margin-left:4px; margin-top: 4px;"
            >{{i}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作">
      <template slot-scope="scope">
          <el-button
            size="mini"
            type="primary"
            icon="el-icon-edit"
            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button
            size="mini"
            type="danger"
            icon="el-icon-delete"
            @click="handleDeleteItem(scope.$index, scope.row)">删除</el-button>

      </template>
    </el-table-column>
    </el-table>
    <edit-dialog ref="update"></edit-dialog>
  </div>
  </template>

  <script>
  import axios from 'axios'
  import editDialog from '../components/editObject.vue'
  export default {
    name: 'SettingsView',
    components:{
      editDialog,
    },
    data(){
      return {
        filterDataField:[],
        filterDataProperty:[],
        tableData: [],
        muSelection: [],
        form:{
          id: '',
          object: '',
          field: '',
          properties: [],
        },
        loading: true,
      }
    },
    mounted(){
      this.get_list();
      this.get_filter_list();
    },
    methods: {
      async fetch_field(){
        await axios.get('http://localhost:8000/api/get_fields').then((res) => {
          return  res.data.data;
        })
      },
      async get_list(){
        let _this = this;
        await axios.get('http://localhost:8000/api/get_objectsList').then((res) => {
        _this.tableData = res.data.data;
        })
      },
      async get_filter_list(){
        let _this = this;
        await axios.get('http://localhost:8000/api/get_filterList').then((res) => {
        _this.filterDataField = res.data.data_field;
        _this.filterDataProperty = res.data.data_property;
        console.log(_this.filterDataField);
        console.log(_this.filterDataProperty);
        })
        this.loading = false;
      },
      handleEdit(index, row){
        this.$refs['update'].dialogFormVisible = true;
        this.$refs['update'].form = row;
        this.$refs['update'].fetch_field();
      },
      handleAdd(){
        this.$refs['update'].dialogFormVisible = true;
        this.$refs['update'].form = this.form;
      },
      async handleDelete(){
        await axios.post('http://localhost:8000/api/handle_delete', this.muSelection).then((res) => {
        })
        await this.get_list();
      },
      async handleDeleteItem(index, row){
        await axios.post('http://localhost:8000/api/handle_delete', [row]).then((res) => {
        })
        await this.get_list();
      },
      handleSelectionChange(val) {
        this.muSelection = val;
      },
      filterTag(value, row) {
        return row.properties.indexOf(value) >= 0;
      },
      filterHandlerField(value, row) {
        return value === row.field;
      },
    }
  }
  </script>
