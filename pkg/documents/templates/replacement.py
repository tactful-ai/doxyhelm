from typing import Any

from chart import *
from requirements import *
from values import *


def replace_template_parts(template_content, chart_data, requirements_data, chart_folder):
    """
    Replaces template parts in the given template content with corresponding values.

    Args:
        template_content (str): Original template content.
        chart_data (dict): Data containing information about the chart.
        requirements_data (dict): Combined requirements data from 'requirements.yaml' and chart data.
        chart_folder (str): Path to the chart folder.

    Returns:
        str: Template content with replaced parts.
    """
    # Dictionary to hold template patterns and their corresponding replacement values
    replacement_dict: dict[str | Any, str | Any] = {
        # List of template patterns and their corresponding replacement functions
        '{{ template "chart.header" . }}': get_chart_header(chart_data),
        '{{ template "chart.description" . }}': get_chart_description(chart_data),
        '{{ template "chart.versionBadge" . }}': get_chart_version_badge(chart_data),
        '{{ template "chart.typeBadge" . }}': get_chart_type_badge(chart_data),
        '{{ template "chart.appVersionBadge" . }}': get_chart_app_version_badge(chart_data),
        '{{ template "chart.deprecationWarning" . }}': get_chart_deprecation_warning(chart_data),
        '{{ template "chart.badgesSection" . }}': get_chart_badges_section(chart_data),
        '{{ template "chart.homepageLine" . }}': get_chart_homepage_line(chart_data),
        '{{ template "chart.maintainersSection" . }}': get_chart_maintainers_section(chart_data),
        '{{ template "chart.sourcesSection" . }}': get_chart_sources_section(chart_data),
        '{{ template "chart.requirementsSection" . }}': get_chart_requirements_section(requirements_data),
        '{{ template "chart.name" . }}': get_chart_name(chart_data),
        '{{ template "chart.version" . }}': get_chart_version(chart_data),
        '{{ template "chart.type" . }}': get_chart_type(chart_data),
        '{{ template "chart.appVersion" . }}': get_chart_app_version(chart_data),
        '{{ template "chart.maintainersHeader" . }}': get_chart_maintainers_header(chart_data),
        '{{ template "chart.maintainersTable" . }}': get_chart_maintainers_table(chart_data),
        '{{ template "chart.sourcesHeader" . }}': get_chart_sources_header(chart_data),
        '{{ template "chart.sourcesList" . }}': get_chart_sources_list(chart_data),
        '{{ template "chart.homepage" . }}': get_chart_homepage(chart_data),
        '{{ template "chart.kubeVersion" . }}': get_chart_kube_version(chart_data),
        '{{ template "chart.kubeVersionLine" . }}': get_chart_kube_version_line(chart_data),
        '{{ template "chart.requirementsHeader" . }}': get_chart_requirements_header(),
        '{{ template "chart.requirementsTable" . }}': get_chart_requirements_table(requirements_data),

        '{{ template "chart.valuesHeader" . }}': get_chart_values_header(),
        '{{ template "chart.valuesTable" . }}': get_chart_values_table(chart_folder),
        '{{ template "chart.valuesSection" . }}': get_chart_values_section(chart_folder),

        '{{ template "doxy-helm.versionFooter" . }}': get_doxy_helm_version_footer('v1.0.1'),
        '{{ template "extra.flower" . }}': 'Extra Flower Replacement',
    }

    # Iterate through the replacement dictionary and replace each pattern with its corresponding value
    for pattern, replacement in replacement_dict.items():
        template_content = template_content.replace(pattern, replacement)

    return template_content
