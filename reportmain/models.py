# coding=utf-8
from django.db import models


# Create your models here.


class Base(models.Model):
    """
    作业地点
    """
    name = models.CharField(max_length=30, verbose_name='地点')
    province = models.CharField(max_length=30, null=True, blank=True, verbose_name='省份')
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='市/区')
    county = models.CharField(max_length=30, null=True, blank=True, verbose_name='区/县')
    other = models.CharField(max_length=128, null=True, blank=True, verbose_name='其他')
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    GMT_CREATE = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    GMT_MODIFY = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = '作业地点'
        verbose_name_plural = '作业地点'


class Person(models.Model):
    """
    人员
    """
    JOBS = (('1', '农机队长'), ('2', '销售'), ('3', '机手'))

    name = models.CharField(max_length=30, verbose_name='姓名')
    uName = models.CharField(max_length=30, verbose_name='userName')
    pwd = models.CharField(max_length=64, verbose_name='密码')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='电话')
    weChat = models.CharField(max_length=30, null=True, blank=True, verbose_name='微信')
    email = models.CharField(max_length=64, null=True, blank=True, verbose_name='Email')
    job = models.CharField(max_length=30, verbose_name='职位', choices=JOBS)
    GMT_CREATE = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    GMT_MODIFY = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = '人员'
        verbose_name_plural = '人员'


class Machine(models.Model):
    """
    机械
    """
    rackNumber = models.CharField(max_length=50, null=True, blank=True, verbose_name='机架编号')
    engineNumber = models.CharField(max_length=50, null=True, blank=True, verbose_name='引擎编号')
    propertyNumber = models.CharField(max_length=50, null=True, blank=True, verbose_name='资产编号')
    brand = models.CharField(max_length=50, null=True, blank=True, verbose_name='品牌')
    model = models.CharField(max_length=255, null=True, blank=True, verbose_name='型号')
    GMT_CREATE = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    GMT_MODIFY = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        return u'%s' % (self.propertyNumber)

    class Meta:
        verbose_name = '机械'
        verbose_name_plural = '机械'


class DailyReport(models.Model):
    """
    日报
    """
    STATES = (('0', '未审核'), ('1', '通过'), ('2', '打回'), ('99', '其他'))

    reportDate = models.DateField(verbose_name='上报日期')
    base = models.ForeignKey(Base, verbose_name='作业地点')
    reportUser = models.ForeignKey(Person, related_name='dailyReports', verbose_name='上报员')
    operator = models.ForeignKey(Person, related_name='workingByOperator', verbose_name='操作员')
    machine = models.ForeignKey(Machine, verbose_name='机器编号')
    oil = models.CharField(max_length=20, null=True, blank=True, verbose_name='耗油量')
    startTime = models.CharField(max_length=30, null=True, blank=True, verbose_name='开始时间')
    endTime = models.CharField(max_length=30, null=True, blank=True, verbose_name='结束时间')
    workTime = models.CharField(max_length=30, null=True, blank=True, verbose_name='作业时长')
    workTotal = models.CharField(max_length=30, null=True, blank=True, verbose_name='作业总量')
    waterCar = models.CharField(max_length=30, null=True, blank=True, verbose_name='加水车数')
    waterSize = models.CharField(max_length=30, null=True, blank=True, verbose_name='加水车容量')
    tag = models.CharField(max_length=1024, null=True, blank=True, verbose_name='备注')
    position = models.CharField(max_length=10, null=True, blank=True, verbose_name='经纬度')
    state = models.CharField(max_length=2, null=True, blank=True, default='0', verbose_name='审核状态')
    GMT_CREATE = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    GMT_MODIFY = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        return u'%s %s %s' % (self.reportDate, self.base, self.machine)

    class Meta:
        verbose_name = '日报'
        verbose_name_plural = '日报'
        ordering = ['-reportDate']
