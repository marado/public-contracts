from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = patterns('',
                       url(r'^%s/%s$' % (_('law'), _('home')), views.home, name='law_home'),
                       url(r'^%s/%s$' % (_('law'), _('analysis')), views.analysis_list, name='law_analysis'),

                       url(r'^%s/%s/(\d+)/(\w+)' % (_('law'), _('analysis')),
                           views.law_analysis, name='law_analysis_selector'),
                       url(r'^%s/%s/(\d+)' % (_('law'), _('analysis')),
                           views.law_analysis, name='law_analysis_internal_selector',
                        ),

                       url(r'^%s$' % _('law'), views.law_list, name='law_law_list'),
                       url(r'^%s$' % _('types'), views.types_list, name='law_types_list'),
                       url(r'^%s/(\d+)$' % _('type'), views.type_view, name='law_type'),

                       url(r'^%s/(\d+)$' % _('document'), views.law_view, name='law_view'),
                       url(r'^%s/(\d+)/(.*)' % _('document'), views.law_view, name='law_view'),
                       )
