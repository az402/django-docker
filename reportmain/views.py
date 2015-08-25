# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import models


# Create your views here.
def dailyReportAdd(request):
    reportDate = request.POST['reportDate']
    base = models.Base(id=request.POST['base'])
    reportUser = models.Person.objects.get(id=request.POST['reportUser'])
    pwd = request.POST['pwd']
    if pwd != reportUser.pwd:
        return HttpResponse("密码错误")
    operator = models.Person(id=request.POST['operator'])
    machine = models.Machine(id=request.POST['machine'])
    oil = request.POST['oil']
    startTime = request.POST['startTime']
    endTime = request.POST['endTime']
    workTime = request.POST['workTime']
    workTotal = request.POST['workTotal']
    waterCar = request.POST['waterCar']
    waterSize = request.POST['waterSize']
    tag = request.POST['tag']
    dailyReport = models.DailyReport(reportDate=reportDate, base=base, reportUser=reportUser, operator=operator,
                                     machine=machine, oil=oil
                                     , startTime=startTime, endTime=endTime, workTime=workTime, workTotal=workTotal,
                                     waterCar=waterCar,
                                     waterSize=waterSize, tag=tag)
    html = dailyReport.save()
    return HttpResponse(html)


def dailyReportEdit(request, reportId):
    dailyReport = models.DailyReport.objects.get(id=reportId)

    dailyReport.base = models.Base(id=request.POST['base'])
    dailyReport.reportUser = models.Person.objects.get(id=request.POST['reportUser'])
    pwd = request.POST['pwd']
    if pwd != dailyReport.operator.pwd:
        return HttpResponse("密码错误")
    dailyReport.operator = models.Person(id=request.POST['operator'])
    dailyReport.machine = models.Machine(id=request.POST['machine'])
    dailyReport.oil = request.POST['oil']
    dailyReport.startTime = request.POST['startTime']
    dailyReport.endTime = request.POST['endTime']
    dailyReport.workTime = request.POST['workTime']
    dailyReport.workTotal = request.POST['workTotal']
    dailyReport.waterCar = request.POST['waterCar']
    dailyReport.waterSize = request.POST['waterSize']
    dailyReport.tag = request.POST['tag']

    html = dailyReport.save()
    return HttpResponse(html)


def reportForm(request, reportId):
    base_list = models.Base.objects.all()
    reportUser_list = models.Person.objects.filter(job='1')
    operator_list = models.Person.objects.filter(job='3')
    machine_list = models.Machine.objects.all()

    if reportId:
        dailyReport = models.DailyReport.objects.get(id=reportId)
    else:
        dailyReport = None

    return render_to_response('reportForm.html',
                              {'dailyReport': dailyReport, 'base_list': base_list, 'reportUser_list': reportUser_list,
                               'operator_list': operator_list, 'machine_list': machine_list})


def reportList(request):
    reportUser_list = models.Person.objects.filter(job='1')

    return render_to_response('reportList.html', {'reportUser_list': reportUser_list})
