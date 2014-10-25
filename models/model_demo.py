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
    # Name of the fields used to sort the results of the search and read methods.
    # Default value: 'id'.
    # Examples:
    #   _order = "name"
    #   _order = "date_order desc"
    _order = 'id'

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