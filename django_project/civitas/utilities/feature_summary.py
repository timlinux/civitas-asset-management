__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '04/09/20'

from civitas.models.feature.feature_base import FeatureBase
from civitas.models.feature.identifier import FeatureTypeCombination
from civitas.models.feature.identifier import (
    FeatureClass, FeatureSubClass, FeatureType
)
from civitas.models.view.feature_calculations import FeatureCalculation


class _FeatureSummaryBase(object):
    def template(self, name: str):
        """
        Template report
        :rtype: dict
        """
        raise NotImplementedError

    def add_detail_to_report(
            self, report: dict, model: FeatureCalculation()):
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
                reports[_class.id] = self.template(_class.description)
            try:
                reports[_class.id]['details'][_sub_class.id]
            except KeyError:
                reports[_class.id]['details'][_sub_class.id] = self.template(_sub_class.name)
            try:
                reports[_class.id]['details'][_sub_class.id]['details'][_type.id]
            except KeyError:
                reports[_class.id]['details'][_sub_class.id]['details'][_type.id] = self.template(_type.name)
        return reports

    def summary_all(self):
        """
        Return Financial Report Per Class, SubClass and Type

        :return: report
        :rtype:dict
        """
        output = self.base_reports()

        # get report data
        for model in FeatureCalculation.objects.all():
            try:
                # class report
                _class = model.feature.the_class
                class_report = output[_class.id]
                self.add_detail_to_report(class_report, model)

                # sub class report
                _sub_class = model.feature.sub_class
                sub_class_report = class_report['details'][_sub_class.id]
                self.add_detail_to_report(sub_class_report, model)

                # type report
                _type = model.feature.type
                type_report = sub_class_report['details'][_type.id]
                self.add_detail_to_report(type_report, model)
            except (
                    KeyError,
                    AttributeError,
                    FeatureClass.DoesNotExist,
                    FeatureSubClass.DoesNotExist,
                    FeatureType.DoesNotExist):
                pass

        return output

    def summary(self, systems=None):
        """
        Return Financial Report Per Class, SubClass and Type that is just has data

        :return: report
        :rtype:dict
        """
        output = {}

        # get report data
        for model in FeatureCalculation.objects.all():
            try:
                if systems is not None and str(model.feature.system.id) not in systems:
                    continue

                # class report
                _class = model.feature.the_class
                if _class.id not in output:
                    output[_class.id] = self.template(_class.description)

                class_report = output[_class.id]
                self.add_detail_to_report(class_report, model)

                # sub class report
                _sub_class = model.feature.sub_class
                if _sub_class.id not in class_report['details']:
                    class_report['details'][_sub_class.id] = self.template(_sub_class.name)

                sub_class_report = class_report['details'][_sub_class.id]
                self.add_detail_to_report(sub_class_report, model)

                # type report
                _type = model.feature.type
                if _type.id not in sub_class_report['details']:
                    sub_class_report['details'][_type.id] = self.template(_type.name)

                type_report = sub_class_report['details'][_type.id]
                self.add_detail_to_report(type_report, model)
            except (
                    KeyError,
                    AttributeError,
                    FeatureBase.DoesNotExist,
                    FeatureClass.DoesNotExist,
                    FeatureSubClass.DoesNotExist,
                    FeatureType.DoesNotExist):
                pass

        return output


class SummaryReport(_FeatureSummaryBase):
    def template(self, name: str):
        return {
            'name': name,
            'renewal': 0,
            'maintenance': 0,
            'annual_reserve': 0,
            'quantity': 0,
            'unit': None,
            'details': {}
        }

    def add_detail_to_report(
            self, report: dict, model: FeatureCalculation()):
        """ Add detail to report
        """
        report['renewal'] += model.renewal_cost()
        report['maintenance'] += model.maintenance_cost()
        report['annual_reserve'] += model.annual_reserve_cost()
        report['quantity'] += model.feature.quantity if model.feature.quantity else 0
        if model.feature.sub_class.unit and not report['unit']:
            report['unit'] = model.feature.sub_class.unit.name


class FinancialReport(_FeatureSummaryBase):
    def template(self, name: str):
        return {
            'name': name,
            'renewal': 0,
            'maintenance': 0,
            'annual_reserve': 0,
            'total': 0,
            'details': {}
        }

    def add_detail_to_report(
            self, report: dict, model: FeatureCalculation()):
        """ Add detail to report
        """
        report['annual_reserve'] += model.annual_reserve_cost()
        report['renewal'] += model.renewal_cost()
        report['maintenance'] += model.maintenance_cost()
        report['total'] = report['renewal'] + report['maintenance']


class ProjectedReport(_FeatureSummaryBase):
    def __init__(self, date):
        self.date = date

    def template(self, name):
        return {
            'name': name,
            'renewal': 0,
            'maintenance': 0,
            'total': 0,
            'details': {}
        }

    def add_detail_to_report(
            self, report: dict, model: FeatureCalculation()):
        """ Add detail to report
        :type report: dict
        :type model: FeatureBase()
        """
        if model.age():
            report['maintenance'] += model.maintenance_cost()
            report['renewal'] += model.renewal_cost_year(
                self.date)
            report['total'] = report['renewal'] + report['maintenance']
