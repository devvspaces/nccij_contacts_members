import json
import logging
from werkzeug.exceptions import BadRequest

# Odoo imports
import odoo.http as http
from odoo.http import request
from werkzeug.wrappers import Response


_logger = logging.getLogger(__name__)


class ContactExtended(http.Controller):
    def check_auth(self, access_token):
        if not access_token:
            raise BadRequest('Access token missing')

        if access_token.startswith('Bearer '):
            access_token = access_token[7:]

        user_id = request.env["res.users.apikeys"]._check_credentials(
            scope='browser', key=access_token)
        if not user_id:
            raise BadRequest('Access token invalid')

        request.update_env(user=user_id)

    @http.route(
        "/contacts/add/", type="http",
        methods=['POST'], auth="public",
        csrf=False, cors="*"
    )
    def add_contacts(self):
        # Access token verification
        access_token = request.httprequest.headers.get('Authorization')
        self.check_auth(access_token)

        # Get data from post request
        data = request.httprequest.data
        body = json.loads(data.decode('utf-8'))

        _logger.info(f"Data to add to contacts {body}")

        # Add data to contacts module
        try:
            request.env['contact.member'].sudo().create(body)
            res_body = json.dumps({
                "message": "Member signup successful"
            })
            return Response(
                res_body,
                status=200,
                headers={'Content-Type': 'application/json'}
            )
        except Exception:
            res_body = json.dumps({
                "error": "Contact member creation failed \
please verify parameters",
            })
            return Response(
                res_body,
                status=400,
                headers={'Content-Type': 'application/json'}
            )
