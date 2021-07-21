
from flask import Blueprint, request, json, url_for, redirect, make_response, render_template, flash

from portfolio.internal.biz.services.children import ChildrenService
from portfolio.internal.biz.services.employee import EmployeeService
from portfolio.internal.biz.services.events import EventsService
from portfolio.internal.biz.services.organisation import OrganisationService
from portfolio.internal.http.wrappers.parents import get_parent_id_and_acc_id_with_confirmed_email
from portfolio.models.account_main import AccountMain
from portfolio.models.children import Children
from portfolio.models.events import Events
from portfolio.models.parents import Parents

main = Blueprint('main', __name__, template_folder='templates/main', static_folder='static/main')


@main.route('/organisations', methods=['GET'])
@get_parent_id_and_acc_id_with_confirmed_email
def list_organisation(auth_account_main_id: int, parent_id: int):
    if request.method == 'GET':

        organisations, err = OrganisationService.get_all_organisations()

        if err:
            return json.dumps(err)
        response = make_response(render_template(
            'main/list_organisations.html',
            organisations=organisations
        ))
        return response


@main.route('/organisations/<int:organisation_id>', methods=['GET'])
@get_parent_id_and_acc_id_with_confirmed_email
def detail_organisation(auth_account_main_id: int, parent_id: int, organisation_id: int):
    if request.method == 'GET':
        organisation, err = OrganisationService.get_by_id(organisation_id)
        list_employee, err = EmployeeService.get_list_employee_by_org_id(organisation.id)
        list_active_events, err = EventsService.get_active_events_by_organisation_id(organisation.id)
        if err:
            return json.dumps(err)
        resp = make_response(
            render_template(
                'main/detail_organisation.html',
                organisation=organisation,
                list_employee=list_employee,
                count_employee=len(list_employee) if list_employee else 0,
                list_active_events=list_active_events,
                count_events=len(list_active_events) if list_active_events else 0,
            )
        )
        return resp


@main.route('/organisations/<int:organisation_id>/events/<int:events_id>', methods=['GET'])
@get_parent_id_and_acc_id_with_confirmed_email
def detail_event(auth_account_main_id: int, parent_id: int, organisation_id: int, events_id: int):
    if request.method == 'GET':
        events = Events(id=events_id)
        event, err = EventsService.get_by_events_id(events)
        if err:
            return json.dumps(err)
        children = Children(
            parents=Parents(
                id=parent_id,
            )
        )
        list_children, err = ChildrenService.get_children_by_parents_id(children)
        if err:
            return json.dumps(err)
        resp = make_response(
            render_template(
                'main/detail_event.html',
                event=event,
                list_children=list_children,
                organisation_id=organisation_id
            )
        )
        return resp
