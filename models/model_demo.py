# -*- encoding:utf-8 -*-
__author__ = 'cysnake4713'

# coding=utf-8
from openerp import tools
from openerp import models, fields, api
from openerp.tools.translate import _
# A use B


class DemoA(models.Model):
    # Examples:
    #    _inherits = {
    #       'tiny.object_a': 'object_a_id'(the column name used in this model stored foreign key),
    #       'tiny.object_b': 'object_b_id',
    #       ... ,
    #       'tiny.object_n': 'object_n_id'
    #    }
    # The object 'tiny.object' inherits from all the columns and all the methods from
    # the n objects 'tiny.object_a', ..., 'tiny.object_n'.
    # _inherits = {}
    # The name of the osv object which the current object inherits from.
    # _name == _inherit means override old model
    # _name != _inherit means inherit in new new model
    # _inherit = ''
    # Name of the field in which the name of every resource is stored.
    # Default value: 'name'. Note: by default, the name_get method simply returns the content of this field.
    _name = 'tr.demo.a'
    # Name of the field in which the name of every resource is stored. Default value: 'name'.
    # Note: by default, the name_get method simply returns the content of this field.
    _rec_name = 'char_field'
    #  TODO
    _constraints = ''
    #  TODO
    _sql_constraints = ''
    # Determines whether or not the write access to the resource must be logged.
    # If true, four fields will be created in the SQL table: create_uid, create_date, write_uid, write_date.
    # Those fields represent respectively the id of the user who created the record,
    # the creation date of record, the id of the user who last modified the record,
    # and the date of that last modification. This data may be obtained by using the perm_read method.
    _log_access = True
    # Name of the fields used to sort the results of the search and read methods.
    # Default value: 'id'.
    # Examples:
    #   _order = "name"
    #   _order = "date_order desc"
    _order = 'id'
    #Name of the SQL sequence that manages the ids for this object. Default value: None.
    _sequence = None
    #Determines whether a corresponding PostgreSQL table must be generated automatically from the object.
    #Setting _auto to False can be useful in case of OpenERP objects generated from PostgreSQL views.
    #See the "Reporting From PostgreSQL Views" section for more details.
    _auto = True
    # SQL code executed upon creation of the object (only if _auto is True).
    # It means this code gets executed after the table is created.
    _sql = ''
    # Name of the SQL table. Default value:
    # the value of the _name field above with the dots ( . ) replaced by underscores ( _ ).
    _table = 'tr_demo_a'

    # noinspection PyUnusedLocal
    @api.model
    def _get_selection(self):
        return (
            ('choice1', 'This is the choice 1'),
            ('choice2', 'This is the choice 2'))

    char_field = fields.Char(
        # The field name as it should appear in a label or column header.
        # Strings containing non-ASCII characters must use python unicode objects.
        # For example: 'tested': fields.boolean(u'Testé')
        string='Name',
        # The size of the field in the database: number characters or digits.
        size=50,
        # True if this field must have a value before the object can be saved, otherwise False.
        required=True,
        # True if the user cannot edit this field, otherwise False.
        readonly=False,
        # Lets you override other parameters for specific states of this object.
        # Accepts a dictionary with the state names as keys and a list of name/value tuples as the values.
        # For example: states={'posted':[('readonly',True)]}
        states=None,
        # True if the content of this field should be translated, otherwise False.
        translate=False,
        # TODO: Whether or not the user can define default values on other fields depending on the value of this field.
        # Those default values need to be defined in the ir.values table.
        change_default=False,
        # A description of how the field should be used: longer and more descriptive than string.
        # It will appear in a tooltip when the mouse hovers over the field.
        help="",
        # Hide the field's value in forms. For example, a password.
        # TODO
        invisible=False,
        # Default value for the select attribute in the view. 1 means basic search, and 2 means advanced search.
        select=1,
    )
    boolean_field = fields.Boolean(string='Boolean')
    integer_field = fields.Integer(string='Integer')
    float_field = fields.Float(
        string='Float',
        # The optional parameter digits defines the precision and scale of the number.
        # The scale being the number of digits after the decimal point whereas the precision is
        # the total number of significant digits in the number (before and after the decimal point).
        # If the parameter digits is not present, the number will be a double precision floating point number.
        # Warning: these floating-point numbers are inexact (not any value can be converted to its binary representation)
        # and this can lead to rounding errors. You should always use the digits parameter for monetary amounts.
        digits=(10, 2),
        # synopsis: digits_compute(cr) ->  (precision, scale)
        digits_compute=None,
        required=False,
    )
    text_field = fields.Text('Text')
    date_field = fields.Date('Date')
    datetime_field = fields.Datetime('Datetime')
    binary_field = fields.Binary('Binary')
    selection_simple_field = fields.Selection(selection=[('yes', 'Yes'), ('no', 'No')], string='Selection Simple')
    selection_complex_field = fields.Selection(_get_selection, 'Selection Complex')
    many2one_field = fields.Many2one(
        comodel_name='tr.demo.b',
        # What should happen when the resource this field points to is deleted.
        # Predefined value: "cascade", "set null", "restrict", "no action", "set default"
        # Default value: "set null"
        string='Many2one Field',
        # TODO
        auto_join=False,
        ondelete='set null',
        # Using relation fields many2one with selection.
        # TODO:selection=_sel_func,
        # Domain restriction on a relational field.
        # Example: domain=[('field','=',value)])
        domain=[],
        # Default value for the on_change attribute in the view.
        # This will launch a function on the server when the field changes in the client.
        # For example, on_change="onchange_shop_id(shop_id)".
        on_change=None,
    )
    #
    # Values: (0, 0,  { fields })    create
    #         (1, ID, { fields })    update (write fields to ID)
    #         (2, ID)                remove (calls unlink on ID, that will also delete the relationship because of the ondelete)
    #         (3, ID)                unlink (delete the relationship between the two objects but does not delete ID)
    #         (4, ID)                link (add a relationship)
    #         (5, ID)                unlink all
    #         (6, ?, ids)            set a list of links
    one2many_field = fields.One2many(
        obj='tr.demo.b',
        fields_id='a_id',
        string='one2many Field',
        # TODO
        limit=None,
        # TODO
        auto_join=False,
        # TODO:
        # Define a variable's value visible in the view's context or an on-change function.
        # Used when searching child table of one2many relationship?
        context={},
        domain=[],
        #one2many can't be used as condition for defaults
        change_default=False,
    )
    many2many_field = fields.Many2many(
        # destination model
        obj='tr.demo.b',
        # optional name of the intermediary relationship table. If not specified,
        # a canonical name will be derived based on the alphabetically-ordered
        # model names of the source and destination (in the form: ``amodel_bmodel_rel``).
        # Automatic naming is not possible when the source and destination are
        # the same, for obvious ambiguity reasons.
        rel='rel_tr_demo_a_b',
        # optional name for the column holding the foreign key to the current
        # model in the relationship table. If not specified, a canonical name
        # will be derived based on the model name (in the form: `src_model_id`).
        id1='a_id',
        # optional name for the column holding the foreign key to the destination
        # model in the relationship table. If not specified, a canonical name
        # will be derived based on the model name (in the form: `dest_model_id`)
        id2='b_id',
        string='Many2many Field B',
        # TODO
        limit=None,
    )
    function_field = fields.Char(string='Function', compute='_function_compute')

    @api.one
    @api.depends('char_field')
    def _function_compute(self):
        self.function_field = self.char_field


class DemoB(models.Model):
    _name = 'tr.demo.b'

    many2many_field = fields.Many2many('tr.demo.a', 'tr_demo_a_b', 'b_id', 'a_id', 'Many2Many A demos')
    a_id = fields.Many2one('tr.demo.a', 'Demo A')