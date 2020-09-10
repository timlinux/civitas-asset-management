__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '04/09/20'

from amlit.models.feature.base import FeatureTypeCombination
from amlit.models.feature import (
    FeatureLine, FeaturePolygon, FeaturePoint
)


class _FinancialReportBase(object):
    MODELS = [FeatureLine, FeaturePolygon, FeaturePoint]

    def template(self, name):
        """
        Template report
        :rtype: dict
        """
        raise NotImplementedError

    def add_detail_to_report(
            self, report, model):
        """ Add detail into report based on model data
        """
        raise NotImplementedError

    def base_reports(self):
        """ Return reports format """
        reports = {}
        for _type in FeatureTypeCombination.objects.all():
            _class = _type.the_class
            _sub_class = _type.sub_class
            _type = _type.type

            try:
                reports[_class.id]
            except KeyError:
                reports[_class.id] = self.template(_class.name)
            try:
                reports[_class.id]['details'][_sub_class.id]
            except KeyError:
                reports[_class.id]['details'][_sub_class.id] = self.template(_sub_class.name)
            try:
                reports[_class.id]['details'][_sub_class.id]['details'][_type.id]
            except KeyError:
                reports[_class.id]['details'][_sub_class.id]['details'][_type.id] = self.template(_type.name)
        return reports

    def get(self):
        """
        Return Financial Report Per Class, SubClass and Type

        :return: report
        :rtype:dict
        """
        output = self.template('Grand Total')
        output['details'] = self.base_reports()
        reports = output['details']

        # get report data
        for Model in self.MODELS:
            for model in Model.objects.all():
                try:
                    _class = model.type.the_class
                    _sub_class = model.type.sub_class
                    _type = model.type.type

                    # get class report
                    class_report = reports[_class.id]

                    # get sub class report in class report
                    sub_class_report = class_report['details'][_sub_class.id]

                    # get type report in sub class report
                    type_report = sub_class_report['details'][_type.id]

                    # save data into report
                    self.add_detail_to_report(output, model)
                    self.add_detail_to_report(class_report, model)
                    self.add_detail_to_report(sub_class_report, model)
                    self.add_detail_to_report(type_report, model)
                except KeyError:
                    pass

        return output


class FinancialReport(_FinancialReportBase):
    def template(self, name):
        return {
            'name': name,
            'annual_reserve': 0,
            'replacement': 0,
            'maintenance': 0,
            'total': 0,
            'details': {}
        }

    def add_detail_to_report(
            self, report, model):
        report['annual_reserve'] += model.annual_reserve_cost()
        report['replacement'] += model.replacement_cost()
        report['maintenance'] += model.maintenance_cost()
        report['total'] = report['annual_reserve'] + report['replacement'] + report['maintenance']


class ProjectedReport(_FinancialReportBase):
    def __init__(self, date):
        self.date = date

    def template(self, name):
        return {
            'name': name,
            'replacement': 0,
            'maintenance': 0,
            'total': 0,
            'details': {}
        }

    def add_detail_to_report(
            self, report, model):
        report['maintenance'] += model.maintenance_cost()
        report['replacement'] += model.replacement_cost_year(
            self.date)
        report['total'] = report['replacement'] + report['maintenance']
