<template>
  <div>
    <el-button @click="handleDelete">批量删除</el-button>
    <el-button @click="handleAdd">新增对象</el-button>
    <el-table
      ref="filterTable"
      :data="tableData"
      style="width: 100%"
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
        label="Class"
        sortable
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
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
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
      },
      handleEdit(index, row){
        this.$refs['update'].dialogFormVisible = true;
        this.$refs['update'].form = row;
        this.$refs['update'].fetch_field();
        this.$refs['update'].fetch_class();
      },
      handleAdd(){
        this.$refs['update'].dialogFormVisible = true;
      },
      async handleDelete(){
        await axios.post('http://localhost:8000/api/handle_delete', this.muSelection).then((res) => {
        })
        this.get_list();
      },
      async handleDeleteItem(index, row){
        await axios.post('http://localhost:8000/api/handle_delete', [row]).then((res) => {
        })
        this.get_list();
      },
      handleSelectionChange(val) {
        this.muSelection = val;
      },
      filterTag(value, row) {
        return row.properties.indexOf(value) > 0;
      },
      filterHandlerField(value, row) {
        return value === row.field;
      },
    }
  }
  </script>
