# coding=utf-8
__author__ = 'az402'
from django.contrib import admin


class DailyReportAdmin(admin.ModelAdmin):
    list_display = (
        'reportDate', 'base', 'reportUser', 'operator', 'machine', 'oil', 'startTime', 'endTime', 'workTime',
        'workTotal',
        'waterCar', 'waterSize', 'tag', 'position', 'state', 'GMT_CREATE', 'GMT_MODIFY')


class BaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'city', 'county', 'other', 'note', 'GMT_CREATE', 'GMT_MODIFY')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'uName', 'pwd', 'phone', 'weChat', 'email', 'job', 'GMT_CREATE', 'GMT_MODIFY')


class MachineAdmin(admin.ModelAdmin):
    list_display = ('rackNumber', 'engineNumber', 'propertyNumber', 'brand', 'model', 'GMT_CREATE', 'GMT_MODIFY')
