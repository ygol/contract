# © 2019 Ygol InternetWork (Yves Goldberg <yves@ygol.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields
from odoo.exceptions import ValidationError
from odoo.tests import common


class TestAgreement(common.SavepointCase):
    """
    Test name_get
    """
