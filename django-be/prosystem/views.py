from msilib.schema import Class
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from prosystem.models import *
# Create your views here.


def test(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode())
        temp = received_data.get('data')
        input_fea = temp.split()

        data = Classes.objects.get(id = temp)[1]
        response = {"code": 200, "data": data}
        return HttpResponse(json.dumps(response))
    else:
        temp = Classes.objects.all()
        print(temp[0].id)
        response = {'code': 200, 'msg': 'success', 'id':str(temp[0].id)}
        return HttpResponse(json.dumps(response))


def get_field(request):
    temp = Fields.objects.all()
    data = []
    for i in temp:
        data.append({'id': i.id, 'field': i.field})
    print(data)
    response = {'code': 200, 'msg': 'success', 'data':data}
    return HttpResponse(json.dumps(response))


def get_properties(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode())
        temp = Properties.objects.filter(field_id=received_data.get('id'))
        data = []
        for i in temp:
            data.append({'id': i.id, 'property':i.info})
        print(data)
        response = {"code": 200, "data": data}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 200, 'msg': 'success'}
        return HttpResponse(json.dumps(response))


def handle_infer(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode())
        temp = received_data.get('data')
        print(temp)
        if len(temp) == 1:
            temp_data = ObjectsQuery.objects.filter(property_id = temp[0])
            data = []
            for i in temp_data:
                data.append(Objects.objects.get(id = i.object_id))
            response = {"code": 200, "data": data}
            return HttpResponse(json.dumps(response))
        temp_data = ObjectsQuery.objects.filter(property_id = temp[0])
        data = []
        for i in temp_data:
            data.append(i.object_id)
        print(data)
        for i in temp:
            temp_res = ObjectsQuery.objects.filter(property_id = i)
            print(temp_res)
            temp_data = []
            for i in temp_res:
                temp_data.append(i.object_id)
            data = list(set(data) & set(temp_data))
        result = ''
        for i in data:
            result += Objects.objects.get(id = i).object + "  "
        if len(data) == 0:
            result = "根据目前的条件无法找到"
        elif len(data) == 1:
            result = "您要找的是：" + result
        else:
            result = "您要找的可能是：" + result
        response = {"code": 200, 'msg': 'success', "data": result}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 200, 'msg': 'success'}
        return HttpResponse(json.dumps(response))


def get_objectsList(request):
    temp_all_obj = Objects.objects.all()
    all_obj = []
    for i in temp_all_obj:
        all_obj.append([i.id, i.object])  # 获取全部object
    data = []
    objfield_id = 0
    for i in all_obj:
        temp_obj_properties_id = ObjectsQuery.objects.filter(object_id = i[0])  # 获取对应object的property_id
        objfield_id = Objects.objects.get(id=i[0]).field_id
        obj_field = Fields.objects.get(id = objfield_id).field

        obj_properties = []
        for j in temp_obj_properties_id:
            if Properties.objects.filter(id = j.property_id).count != 0:
                for k in Properties.objects.filter(id = j.property_id):
                    obj_properties.append(k.info)

        
        data.append({'id':i[0], 'object':i[1],'field': obj_field, 'properties': obj_properties})
    for i in data:
        print(i)
    response = {"code": 200, 'msg': 'success', "data": data}
    return HttpResponse(json.dumps(response))


def handle_delete(request):
    received_data = json.loads(request.body.decode())
    print(received_data)
    data = []
    for i in received_data:
        object_item = Objects.objects.get(id = i['id'])
        object_item.delete()
        data.append(i['id'])
    response = {"code": 200, 'msg': 'success', "data": data}
    return HttpResponse(json.dumps(response))


def get_filterList(request):
    temp_data_property = Properties.objects.all()
    temp_data_field = Fields.objects.all()
    data_property = []
    data_field = []
    for i in temp_data_property:
        data_property.append({'text': i.info, 'value': i.info})
    for i in temp_data_field:
        data_field.append({'text': i.field, 'value': i.field})
    response = {"code": 200, 'msg': 'success', "data_property": data_property, "data_field": data_field}
    return HttpResponse(json.dumps(response))


def handle_field(request):
    received_data = json.loads(request.body.decode())
    print(received_data)
    data = []
    for i in received_data['fields']:
        if isinstance(i, str):
            Fields.objects.create(field = i)
            data.append({"id": Fields.objects.get(field=i).id, "field": i})
    response = {"code": 200, 'msg': 'success', "data": data}
    return HttpResponse(json.dumps(response))


def get_classList(request):
    received_data = request.body.decode()
    temp_field_id = Fields.objects.get(field = received_data).id
    print(temp_field_id)
    temp_data_class = Classes.objects.all()
    data_class = []
    for i in temp_data_class:
        if i.field_id == temp_field_id:
            data_class.append({'text': i.class_field, 'value': i.id})
    print(data_class)
    response = {"code": 200, 'msg': 'success', "data": data_class}
    return HttpResponse(json.dumps(response))


def handle_update(request):
    received_data = json.loads(request.body.decode())
    if received_data['id'] == "":
        fieldid = Fields.objects.get(field=received_data['field']).id
        Objects.objects.create(field_id=fieldid, object=received_data['object'])
        data = Objects.objects.get(object=received_data['object']).id
        for i in received_data['properties']:
            if Properties.objects.filter(info=i).exists():
                ObjectsQuery.objects.create(object_id=int(data), field_id = fieldid, property_id = Properties.objects.get(info=i).id)
            else:
                Properties.objects.create(info=i, field_id=received_data['field'])
                property_id = Properties.objects.get(info=i).id
                ObjectsQuery.objects.create(object_id=int(data), field_id = fieldid, property_id = property_id)
    else:
        obj_id = Objects.objects.get(object=received_data['object']).id
        temp_obj = Objects.objects.get(id=received_data['id'])
        temp_obj.object = received_data['object']
        temp_obj.save()
        ObjectsQuery.objects.filter(object_id=received_data['id']).delete()
        fieldid1 = Fields.objects.get(field=received_data['field']).id
        for i in received_data['properties']:
            if Properties.objects.filter(info=i).exists():
                ObjectsQuery.objects.create(object_id=int(obj_id), field_id = fieldid1, property_id = Properties.objects.get(info=i).id)
            else:
                Properties.objects.create(info=i, field_id=fieldid1)
                property_id = Properties.objects.get(info=i).id
                ObjectsQuery.objects.create(object_id=int(obj_id), field_id = fieldid1, property_id = property_id)
    data = obj_id
    response = {"code": 200, 'msg': 'success', "data": data}
    return HttpResponse(json.dumps(response))
